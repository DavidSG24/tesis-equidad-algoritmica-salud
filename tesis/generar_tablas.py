"""Genera las tablas y macros LaTeX de la tesis a partir de los resultados reales.

El capítulo de resultados no transcribe cifras a mano: las toma de los artefactos
JSON que producen los notebooks 03 y 04. Así el documento no puede desincronizarse
de los experimentos, que es la forma más común de introducir inconsistencias entre
el texto y el análisis.

Uso:
    python3 generar_tablas.py

Entradas:  auditoria_equidad.json, resultados_tesis.json,
           dge_covid2021_limpio.manifest.json
Salidas:   tesis/tablas/*.tex y tesis/macros_resultados.tex
"""

from __future__ import annotations

import json
import os

DIR_TABLAS = os.path.join("tesis", "tablas")
RUTA_MACROS = os.path.join("tesis", "macros_resultados.tex")


def leer(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def escribir(nombre: str, contenido: str) -> None:
    os.makedirs(DIR_TABLAS, exist_ok=True)
    ruta = os.path.join(DIR_TABLAS, nombre)
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write("% Generado por generar_tablas.py -- NO editar a mano.\n")
        fh.write(contenido.rstrip() + "\n")
    print("  ", ruta)


def num(x, d=3):
    """Formatea un número para LaTeX, o `--` si es nulo."""
    if x is None:
        return "--"
    return f"{x:.{d}f}"


def miles(n: int) -> str:
    """Separador de miles con espacio fino, seguro en modo texto de LaTeX."""
    return f"{n:,}".replace(",", "\\,")


#: El catálogo de la DGE guarda los nombres sin acentos y en mayúsculas; en el
#: documento deben aparecer con su ortografía correcta.
ACENTOS = {
    "MICHOACAN": "Michoacán", "YUCATAN": "Yucatán", "NUEVO LEON": "Nuevo León",
    "SAN LUIS POTOSI": "San Luis Potosí", "QUERETARO": "Querétaro",
    "CIUDAD DE MEXICO": "Ciudad de México", "MEXICO": "México",
}


def entidad(nombre: str) -> str:
    """Nombre de entidad en su ortografía de presentación."""
    if nombre in ACENTOS:
        return ACENTOS[nombre]
    return nombre.title().replace("De ", "de ")


# --------------------------------------------------------------------------- #
# Tablas
# --------------------------------------------------------------------------- #

def tabla_entidad(aud: dict) -> None:
    filas = sorted(aud["por_entidad"], key=lambda r: r["AUROC"])
    cuerpo = "\n".join(
        f"{entidad(r['grupo'])} & {miles(int(r['n']))} & {num(r['tasa'], 4)} & "
        f"{num(r['AUROC'], 4)} & {num(r['TPR'])} & {num(r['FPR'])} & {num(r['cal_pred'], 4)} \\\\"
        for r in filas)
    # longtable no crea grupo propio: sin \begingroup, el \small se filtraría al
    # resto del capítulo.
    escribir("tab_entidad.tex", f"""
\\begingroup
\\small\\setlength{{\\tabcolsep}}{{4pt}}
\\begin{{longtable}}{{l r r r r r r}}
\\caption{{Desempeño y equidad por entidad federativa en el conjunto de prueba
($n={miles(aud['n_test'])}$), al umbral de sensibilidad objetivo
$\\tau={aud['umbral']:.4f}$. Ordenadas por AUROC ascendente.}}
\\label{{tab:entidad}}\\\\
\\toprule
Entidad & $n$ & Mort. & AUROC & TPR & FPR & Riesgo \\\\
\\midrule
\\endfirsthead
\\toprule
Entidad & $n$ & Mort. & AUROC & TPR & FPR & Riesgo \\\\
\\midrule
\\endhead
\\midrule
\\multicolumn{{7}}{{r}}{{\\footnotesize Continúa en la página siguiente}} \\\\
\\endfoot
\\bottomrule
\\endlastfoot
{cuerpo}
\\end{{longtable}}
\\endgroup
""")


def tabla_simple(nombre, filas, caption, label, etiqueta_col):
    cuerpo = "\n".join(
        f"{r['grupo']} & {miles(int(r['n']))} & {num(r['tasa'], 4)} & {num(r['AUROC'], 4)} & "
        f"{num(r['TPR'])} & {num(r['FPR'])} & {num(r['seleccion'])} & {num(r['cal_pred'], 4)} \\\\"
        for r in filas)
    escribir(nombre, f"""
\\begin{{table}}[htbp]
\\centering
\\small\\setlength{{\\tabcolsep}}{{4pt}}
\\caption{{{caption}}}
\\label{{{label}}}
\\begin{{tabular}}{{l r r r r r r r}}
\\toprule
{etiqueta_col} & $n$ & Mort. & AUROC & TPR & FPR & Selec. & Riesgo \\\\
\\midrule
{cuerpo}
\\bottomrule
\\end{{tabular}}
\\end{{table}}
""")


def tabla_disparidad(aud: dict) -> None:
    ejes = [("Entidad federativa", "disparidad_entidad"),
            ("Sexo", "disparidad_sexo"),
            ("Grupo etario", "disparidad_edad")]
    claves = ["gap_TPR (equalized odds)", "gap_FPR", "gap_AUROC",
              "gap_seleccion (paridad demogr.)", "max_error_calibracion"]
    cuerpo = "\n".join(
        f"{nom} & " + " & ".join(num(aud[k][c], 4) for c in claves) + " \\\\"
        for nom, k in ejes)
    escribir("tab_disparidad.tex", f"""
\\begin{{table}}[htbp]
\\centering
\\caption{{Brechas máximas entre grupos por eje de auditoría, al umbral
$\\tau={aud['umbral']:.4f}$. La brecha de TPR corresponde a la violación de
\\emph{{equalized odds}}; el error de calibración se mide sobre el riesgo calibrado.}}
\\label{{tab:disparidad}}
\\small\\setlength{{\\tabcolsep}}{{5pt}}
\\begin{{tabular}}{{l r r r r r}}
\\toprule
Eje & $\\Delta$TPR & $\\Delta$FPR & $\\Delta$AUROC & $\\Delta$Selec. & Err.\\ calib. \\\\
\\midrule
{cuerpo}
\\bottomrule
\\end{{tabular}}
\\end{{table}}
""")


def tabla_interseccional(aud: dict) -> None:
    filas = sorted(aud["mayores_60_por_entidad"], key=lambda r: r["AUROC"])
    sel = filas[:5] + filas[-5:]
    cuerpo = "\n".join(
        f"{entidad(r['grupo'])} & {miles(int(r['n']))} & {num(r['tasa'], 3)} & "
        f"{num(r['AUROC'], 3)} & {num(r['TPR'])} \\\\" for r in sel[:5])
    cuerpo += "\n\\midrule\n" + "\n".join(
        f"{entidad(r['grupo'])} & {miles(int(r['n']))} & {num(r['tasa'], 3)} & "
        f"{num(r['AUROC'], 3)} & {num(r['TPR'])} \\\\" for r in sel[5:])
    escribir("tab_interseccional.tex", f"""
\\begin{{table}}[htbp]
\\centering
\\caption{{Subgrupo interseccional: adultos de 60 años o más, por entidad
(cinco peores y cinco mejores de {len(filas)} evaluadas). El deterioro persiste
tras controlar por edad avanzada.}}
\\label{{tab:interseccional}}
\\begin{{tabular}}{{l r r r r}}
\\toprule
Entidad & $n$ & Mortalidad & AUROC & TPR \\\\
\\midrule
{cuerpo}
\\bottomrule
\\end{{tabular}}
\\end{{table}}
""")


def tabla_mitigacion(res: dict) -> None:
    nombres = {
        "Baseline (umbral global)": "Línea de base (umbral global)",
        "PRE (reponderacion entidad)": "Pre: reponderación por entidad",
        "IN (Fairlearn EqOdds)*": "In: \\emph{equalized odds} (Fairlearn)\\textsuperscript{a}",
        "POST (umbral/entidad)": "Post: umbral por entidad\\textsuperscript{b}",
        "POST (umbral/entidad, en test)": "Post: umbral por entidad (en muestra)\\textsuperscript{c}",
    }
    cuerpo = "\n".join(
        f"{nombres.get(r['metodo'], r['metodo'])} & {num(r['gap_TPR'])} & "
        f"{num(r['gap_FPR'])} & {num(r['seleccion'])} & {num(r['bal_acc'])} \\\\"
        for r in res["mitigacion"])
    escribir("tab_mitigacion.tex", f"""
\\begin{{table}}[htbp]
\\centering
\\caption{{Comparación de las tres familias de mitigación sobre el conjunto de
prueba. Menor $\\Delta$TPR indica mayor equidad entre entidades.}}
\\label{{tab:mitigacion}}
\\small\\setlength{{\\tabcolsep}}{{5pt}}
\\begin{{tabular}}{{l r r r r}}
\\toprule
Intervención & $\\Delta$TPR & $\\Delta$FPR & Selec. & Exact.\\ bal. \\\\
\\midrule
{cuerpo}
\\bottomrule
\\end{{tabular}}

\\vspace{{0.4em}}
\\begin{{minipage}}{{0.95\\linewidth}}\\footnotesize
\\textsuperscript{{a}} Evaluado en una submuestra del bloque de entrenamiento
($n=\\numprint{{120000}}$) y con un clasificador lineal; no es comparable uno a uno
con las demás filas. La reducción devuelve una distribución sobre clasificadores:
sobre {res["in_estabilidad"]["n_realizaciones"]} realizaciones del mismo modelo
ajustado, la brecha tiene mediana {res["in_estabilidad"]["mediana"]:.3f} y rango
[{res["in_estabilidad"]["min"]:.3f}, {res["in_estabilidad"]["max"]:.3f}], intervalo
que contiene a la línea de base.\\\\
\\textsuperscript{{b}} Umbrales estimados en el bloque de calibración y evaluados
en el de prueba: es la cifra desplegable.\\\\
\\textsuperscript{{c}} Umbrales estimados sobre el propio conjunto de prueba:
cota optimista, reportada solo para dimensionar el sesgo de ajuste en muestra.
\\end{{minipage}}
\\end{{table}}
""")


def tabla_pareto(res: dict) -> None:
    cuerpo = "\n".join(
        f"{r['alpha']:.1f} & {num(r['gap_TPR'], 4)} & {num(r['bal_acc'], 4)} & "
        f"{num(r['seleccion'], 4)} \\\\" for r in res["frontera_pareto"])
    escribir("tab_pareto.tex", f"""
\\begin{{table}}[htbp]
\\centering
\\caption{{Frontera de Pareto equidad--desempeño. El parámetro $\\alpha$ interpola
entre el umbral global ($\\alpha=0$) y el umbral por entidad estimado fuera de
muestra ($\\alpha=1$). Cada fila es una política de despliegue posible.}}
\\label{{tab:pareto}}
\\begin{{tabular}}{{r r r r}}
\\toprule
$\\alpha$ & $\\Delta$TPR & Exactitud balanceada & Selección \\\\
\\midrule
{cuerpo}
\\bottomrule
\\end{{tabular}}
\\end{{table}}
""")


def tabla_importancia(mod: dict) -> None:
    """Importancia por permutación sobre el AUROC, ordenada de mayor a menor."""
    filas = mod["importancia_permutacion"]
    cuerpo = "\n".join(
        f"{r['variable'].replace('_bin','').replace('_', chr(92)+'_')} & {r['importancia']:.4f} \\\\"
        for r in filas)
    escribir("tab_importancia.tex", f"""
\\begin{{table}}[htbp]
\\centering
\\small
\\caption{{Importancia por permutación sobre el AUROC en el conjunto de prueba
(3 repeticiones, submuestra de \\numprint{{50000}} observaciones).}}
\\label{{tab:importancia}}
\\begin{{tabular}}{{l r}}
\\toprule
Variable & Caída de AUROC \\\\
\\midrule
{cuerpo}
\\bottomrule
\\end{{tabular}}
\\end{{table}}
""")


def tabla_marginacion(res: dict) -> None:
    """Desempeño medio por grado de marginación de CONAPO."""
    filas = res["marginacion_por_grado"]
    cuerpo = "\n".join(
        f"{r['grado']} & {int(r['n_entidades'])} & {r['AUROC_medio']:.4f} & "
        f"{r['TPR_medio']:.3f} \\\\" for r in filas)
    kw = res["kruskal_auroc_grado"]
    escribir("tab_marginacion.tex", f"""
\\begin{{table}}[htbp]
\\centering
\\small
\\caption{{Desempeño medio por grado de marginación (CONAPO 2020), de mayor a
menor carencia. Kruskal--Wallis sobre el AUROC entre grados:
$H={kw['H']:.3f}$, $p={kw['p']:.3f}$.}}
\\label{{tab:marginacion}}
\\begin{{tabular}}{{l r r r}}
\\toprule
Grado de marginación & Entidades & AUROC medio & TPR medio \\\\
\\midrule
{cuerpo}
\\bottomrule
\\end{{tabular}}
\\end{{table}}
""")


def tabla_sensibilidad(sen: dict) -> None:
    """Cohorte completa frente al subconjunto donde el desenlace es posible."""
    c, h = sen["completa"], sen["hospitalizados"]
    escribir("tab_sensibilidad.tex", f"""
\\begin{{table}}[htbp]
\\centering
\\small
\\caption{{Análisis de sensibilidad: cohorte completa frente al subconjunto
hospitalizado, que es donde el desenlace es posible. El AUPRC se acompaña de su
razón respecto de la prevalencia, que es su línea base.}}
\\label{{tab:sensibilidad}}
\\begin{{tabular}}{{l r r}}
\\toprule
& Cohorte completa & Solo hospitalizados \\\\
\\midrule
$n$ & {miles(c['n'])} & {miles(h['n'])} \\\\
Prevalencia del desenlace & {c['prevalencia']:.3f} & {h['prevalencia']:.3f} \\\\
\\midrule
AUROC & {c['auroc']:.4f} & {h['auroc']:.4f} \\\\
AUPRC & {c['auprc']:.4f} & {h['auprc']:.4f} \\\\
AUPRC / prevalencia & {c['auprc_sobre_prevalencia']:.2f}$\\times$ & {h['auprc_sobre_prevalencia']:.2f}$\\times$ \\\\
Brier & {c['brier']:.4f} & {h['brier']:.4f} \\\\
\\midrule
$\\Delta$TPR entre entidades & {c['gap_TPR']:.4f} & {h['gap_TPR']:.4f} \\\\
$\\Delta$AUROC entre entidades & {c['gap_AUROC']:.4f} & {h['gap_AUROC']:.4f} \\\\
\\bottomrule
\\end{{tabular}}
\\end{{table}}
""")


def tabla_loeo(tr: dict) -> None:
    """Desempeño por entidad con y sin haberla visto en el entrenamiento."""
    filas = sorted(tr["por_entidad"], key=lambda r: r["delta_AUROC"])
    sel = filas[:6] + filas[-4:]
    def linea(r):
        return (f"{entidad(r['entidad'])} & {miles(int(r['n']))} & "
                f"{r['AUROC_interno']:.4f} & {r['AUROC_loeo']:.4f} & "
                f"{r['delta_AUROC']:+.4f} \\\\")
    cuerpo = "\n".join(linea(r) for r in sel[:6])
    cuerpo += "\n\\midrule\n" + "\n".join(linea(r) for r in sel[6:])
    escribir("tab_loeo.tex", f"""
\\begin{{table}}[htbp]
\\centering
\\small
\\caption{{Transportabilidad geográfica interna: AUROC de cada entidad cuando
participó en el entrenamiento frente a cuando fue excluida por completo (seis
mayores pérdidas y cuatro mayores ganancias de {tr['n_entidades']} entidades).}}
\\label{{tab:loeo}}
\\begin{{tabular}}{{l r r r r}}
\\toprule
Entidad & $n$ & AUROC interno & AUROC no vista & $\\Delta$ \\\\
\\midrule
{cuerpo}
\\bottomrule
\\end{{tabular}}
\\end{{table}}
""")


def tabla_incertidumbre(inc: dict) -> None:
    """AUROC y sensibilidad por entidad con intervalos de confianza."""
    filas = sorted(inc["por_entidad"], key=lambda r: r["AUROC"])
    sel = filas[:5] + filas[-5:]
    def linea(r):
        return (f"{entidad(r['entidad'])} & {miles(int(r['n']))} & "
                f"{r['AUROC']:.4f} & [{r['AUROC_lo']:.4f},\\,{r['AUROC_hi']:.4f}] & "
                f"{r['TPR']:.3f} & [{r['TPR_lo']:.3f},\\,{r['TPR_hi']:.3f}] \\\\")
    cuerpo = "\n".join(linea(r) for r in sel[:5])
    cuerpo += "\n\\midrule\n" + "\n".join(linea(r) for r in sel[5:])
    escribir("tab_incertidumbre.tex", f"""
\\begin{{table}}[htbp]
\\centering
\\small\\setlength{{\\tabcolsep}}{{4pt}}
\\caption{{Desempeño por entidad con intervalos de confianza al 95\\,\\% obtenidos
por remuestreo estratificado ({inc['B_bootstrap']} réplicas); cinco peores y cinco
mejores por AUROC.}}
\\label{{tab:incertidumbre}}
\\begin{{tabular}}{{l r r c r c}}
\\toprule
Entidad & $n$ & AUROC & IC 95\\,\\% & TPR & IC 95\\,\\% \\\\
\\midrule
{cuerpo}
\\bottomrule
\\end{{tabular}}
\\end{{table}}
""")


def tabla_permutacion(inc: dict) -> None:
    """Brecha observada frente a su distribución bajo la hipótesis nula."""
    escribir("tab_permutacion.tex", f"""
\\begin{{table}}[htbp]
\\centering
\\small
\\caption{{Prueba de permutación sobre las brechas entre entidades
({inc['P_permutaciones']} permutaciones de las etiquetas de entidad, conservando
los tamaños de grupo). La brecha bajo la nula no es cero: con 32 grupos, máximo y
mínimo se separan por azar.}}
\\label{{tab:permutacion}}
\\begin{{tabular}}{{l r r r r}}
\\toprule
Brecha & Observada & IC 95\\,\\% & Nula (mediana) & $p$ \\\\
\\midrule
AUROC & {inc['gap_auroc_obs']:.4f} & [{inc['gap_auroc_ic'][0]:.4f},\\,{inc['gap_auroc_ic'][1]:.4f}] & {inc['nula_auroc_mediana']:.4f} & {inc['p_auroc']:.3f} \\\\
Sensibilidad & {inc['gap_tpr_obs']:.4f} & [{inc['gap_tpr_ic'][0]:.4f},\\,{inc['gap_tpr_ic'][1]:.4f}] & {inc['nula_tpr_mediana']:.4f} & {inc['p_tpr']:.3f} \\\\
\\bottomrule
\\end{{tabular}}
\\end{{table}}
""")


# --------------------------------------------------------------------------- #
# Macros con las cifras que cita la prosa
# --------------------------------------------------------------------------- #

def macros(aud: dict, res: dict, man: dict, cal: dict, mod: dict,
           sen: dict, tr: dict, inc: dict) -> None:
    ent = sorted(aud["por_entidad"], key=lambda r: r["AUROC"])
    e60 = sorted(aud["mayores_60_por_entidad"], key=lambda r: r["AUROC"])
    mit = {r["metodo"]: r for r in res["mitigacion"]}
    cor = aud["correlatos"]
    marg = res["corr_marginacion"]
    d_ent, d_sex, d_eda = (aud["disparidad_entidad"], aud["disparidad_sexo"],
                           aud["disparidad_edad"])

    defs = {
        # Calidad de datos y contraste base completa / cohorte
        "nBaseCompleta": miles(cal["n_base_completa"]),
        "tasaDefBase": f"{cal['tasa_def_base_completa']*100:.2f}",
        "tasaHospCohorte": f"{cal['tasa_hosp_cohorte']*100:.2f}",
        "faltEdad": f"{cal['faltantes']['EDAD']*100:.4f}",
        "naComorbMin": f"{cal['na_comorb_min']*100:.2f}",
        "naComorbMax": f"{cal['na_comorb_max']*100:.2f}",
        "naComorbMaxVar": cal["na_comorb_max_var"].replace("_", "\\_"),
        "entNmin": miles(cal["entidad_n_min"]),
        "entNmax": miles(cal["entidad_n_max"]),
        "entFactorN": f"{cal['entidad_n_max']/cal['entidad_n_min']:.0f}",
        "entFactorTasa": f"{cal['entidad_tasa_max']/cal['entidad_tasa_min']:.1f}",
        # Bloques y desempeño comparado
        "nTrain": miles(mod["n_train"]),
        "nCalib": miles(mod["n_calib"]),
        "desbalance": f"{mod['desbalance']:.1f}",
        "logitAUROC": f"{mod['logit']['auroc']:.4f}",
        "crudoAUROC": f"{mod['hgb_crudo']['auroc']:.4f}",
        "crudoRiesgo": f"{mod['hgb_crudo']['riesgo_medio']:.3f}",
        "calibRiesgo": f"{mod['hgb_calibrado']['riesgo_medio']:.3f}",
        "mortObsTest": f"{mod['mortalidad_observada_test']:.3f}",
        "tprObjetivo": f"{mod['tpr_objetivo']:.3f}",
        "fprObjetivo": f"{mod['fpr_objetivo']:.3f}",
        # Importancia por permutación
        "impPrimeraVar": mod["importancia_permutacion"][0]["variable"].replace("_bin", "").replace("_", "\\_"),
        "impPrimera": f"{mod['importancia_permutacion'][0]['importancia']:.3f}",
        "impSegunda": f"{mod['importancia_permutacion'][1]['importancia']:.3f}",
        "impTercera": f"{mod['importancia_permutacion'][2]['importancia']:.3f}",
        # Error de calibración por entidad: crudo frente a calibrado
        "errCalCrudo": f"{aud['max_error_calibracion_crudo']:.4f}",
        # Traducciones a lenguaje clínico y cifras derivadas que cita la prosa
        "entPeorPct": f"{ent[0]['TPR']*100:.0f}",
        "entMejorPct": f"{ent[-1]['TPR']*100:.0f}",
        "entDifPct": f"{(ent[-1]['TPR']-ent[0]['TPR'])*100:.0f}",
        "edadMenorTasa": f"{min(aud['por_grupo_edad'], key=lambda r: r['tasa'])['tasa']*100:.2f}",
        "edadMayorTasa": f"{max(aud['por_grupo_edad'], key=lambda r: r['tasa'])['tasa']*100:.1f}",
        "edadMenorTPR": f"{min(aud['por_grupo_edad'], key=lambda r: r['tasa'])['TPR']:.3f}",
        "edadMenorSel": f"{min(aud['por_grupo_edad'], key=lambda r: r['tasa'])['seleccion']*100:.1f}",
        "paretoAccMin": f"{min(r['bal_acc'] for r in res['frontera_pareto']):.3f}",
        "paretoAccMax": f"{max(r['bal_acc'] for r in res['frontera_pareto']):.3f}",
        "paretoGapMin": f"{min(r['gap_TPR'] for r in res['frontera_pareto']):.3f}",
        "paretoGapMax": f"{max(r['gap_TPR'] for r in res['frontera_pareto']):.3f}",
        "selGlobal": f"{mit['Baseline (umbral global)']['seleccion']:.3f}",
        "factorOptimismo": f"{mit['POST (umbral/entidad)']['gap_TPR']/mit['POST (umbral/entidad, en test)']['gap_TPR']:.1f}",
        # Correlatos: r, p y rho exportados desde los cuadernos 03 y 04
        "corrAurocNr": f"{cor['auroc_vs_n']['r']:+.3f}",
        "corrAurocNp": f"{cor['auroc_vs_n']['p_r']:.3f}",
        "corrAurocNrho": f"{cor['auroc_vs_n']['rho']:+.3f}",
        "corrAurocNprho": f"{cor['auroc_vs_n']['p_rho']:.3f}",
        "corrAurocTasar": f"{cor['auroc_vs_tasa']['r']:+.3f}",
        "corrAurocTasap": f"{cor['auroc_vs_tasa']['p_r']:.3f}",
        "corrAurocTasarho": f"{cor['auroc_vs_tasa']['rho']:+.3f}",
        "corrAurocTasaprho": f"{cor['auroc_vs_tasa']['p_rho']:.3f}",
        "corrMargAurocr": f"{marg['auroc']['r']:+.3f}",
        "corrMargAurocp": f"{marg['auroc']['p_r']:.3f}",
        "corrMargAurocrho": f"{marg['auroc']['rho']:+.3f}",
        "corrMargAurocprho": f"{marg['auroc']['p_rho']:.3f}",
        "corrMargTprr": f"{marg['tpr']['r']:+.3f}",
        "corrMargTprp": f"{marg['tpr']['p_r']:.3f}",
        "paretoMesetaMin": f"{min(r['gap_TPR'] for r in res['frontera_pareto'] if 0.45 <= r['alpha'] <= 0.85):.3f}",
        "paretoMesetaMax": f"{max(r['gap_TPR'] for r in res['frontera_pareto'] if 0.45 <= r['alpha'] <= 0.85):.3f}",
        # Marginación (CONAPO 2020) y estabilidad del método in-procesamiento
        "gradoAurocMin": f"{min(r['AUROC_medio'] for r in res['marginacion_por_grado']):.3f}",
        "gradoAurocMax": f"{max(r['AUROC_medio'] for r in res['marginacion_por_grado']):.3f}",
        "gradoPeor": min(res["marginacion_por_grado"], key=lambda r: r["AUROC_medio"])["grado"].lower(),
        "kruskalH": f"{res['kruskal_auroc_grado']['H']:.3f}",
        "kruskalP": f"{res['kruskal_auroc_grado']['p']:.3f}",
        "inMediana": f"{res['in_estabilidad']['mediana']:.3f}",
        "inMin": f"{res['in_estabilidad']['min']:.3f}",
        "inMax": f"{res['in_estabilidad']['max']:.3f}",
        "inRealizaciones": str(res["in_estabilidad"]["n_realizaciones"]),
        # Cifras que la prosa comparaba "a ojo" y resultaron inexactas
        "razonBrechas": f"{d_ent['gap_TPR (equalized odds)']/d_ent['gap_AUROC']:.1f}",
        "corrTprTasar": f"{cor['tpr_vs_tasa']['r']:+.3f}",
        "corrTprTasap": f"{cor['tpr_vs_tasa']['p_r']:.3f}",
        "corrTprNr": f"{cor['tpr_vs_n']['r']:+.3f}",
        "corrTprNp": f"{cor['tpr_vs_n']['p_r']:.3f}",
        "sesentaRango": f"{e60[-1]['AUROC'] - e60[0]['AUROC']:.3f}",
        "sesentaPeorN": miles(int(e60[0]["n"])),
        "sesentaPeorTasa": f"{e60[0]['tasa']:.3f}",
        "sesentaMasLetal": entidad(max(e60, key=lambda r: r["tasa"])["grupo"]),
        "sesentaMasLetalTasa": f"{max(e60, key=lambda r: r['tasa'])['tasa']:.3f}",
        "sesentaMasLetalAUROC": f"{max(e60, key=lambda r: r['tasa'])['AUROC']:.3f}",
        "entFactorTasaTexto": f"{cal['entidad_tasa_max']/cal['entidad_tasa_min']:.1f}",
        "factorSobreestimacion": f"{mod['hgb_crudo']['riesgo_medio']/mod['mortalidad_observada_test']:.1f}",
        # Estructura del desenlace y análisis de sensibilidad
        "defTotales": miles(cal["defunciones_totales"]),
        "hospAUPRC": f"{sen['hospitalizados']['auprc']:.4f}",
        "fracHosp": f"{cal['frac_hospitalizados']*100:.1f}",
        "nHosp": miles(cal["n_hospitalizados"]),
        "defAmbulatorias": miles(cal["defunciones_ambulatorias"]),
        "hospPrev": f"{sen['hospitalizados']['prevalencia']:.3f}",
        "hospAUROC": f"{sen['hospitalizados']['auroc']:.4f}",
        "hospBrier": f"{sen['hospitalizados']['brier']:.4f}",
        "hospLift": f"{sen['hospitalizados']['auprc_sobre_prevalencia']:.2f}",
        "completaLift": f"{sen['completa']['auprc_sobre_prevalencia']:.2f}",
        "hospGapTPR": f"{sen['hospitalizados']['gap_TPR']:.4f}",
        "hospGapAUROC": f"{sen['hospitalizados']['gap_AUROC']:.4f}",
        "hospPeor": entidad(sen["hospitalizados"]["peor_entidad"]),
        "hospPeorAUROC": f"{sen['hospitalizados']['peor_auroc']:.4f}",
        "hospMejor": entidad(sen["hospitalizados"]["mejor_entidad"]),
        "hospMejorAUROC": f"{sen['hospitalizados']['mejor_auroc']:.4f}",
        # Transportabilidad geográfica interna
        "loeoMediana": f"{tr['delta_auroc_mediana']:+.4f}",
        "loeoMin": f"{tr['delta_auroc_min']:+.4f}",
        "loeoMax": f"{tr['delta_auroc_max']:+.4f}",
        "loeoEmpeoran": str(tr["n_empeoran"]),
        "loeoNent": str(tr["n_entidades"]),
        "loeoGapAurocInterno": f"{tr['gap_auroc_interno']:.4f}",
        "loeoGapAurocFuera": f"{tr['gap_auroc_loeo']:.4f}",
        "loeoGapTprInterno": f"{tr['gap_tpr_interno']:.4f}",
        "loeoGapTprFuera": f"{tr['gap_tpr_loeo']:.4f}",
        "loeoCorrTamr": f"{tr['corr_perdida_tamano']['r']:+.3f}",
        "loeoCorrTamp": f"{tr['corr_perdida_tamano']['p']:.3f}",
        "loeoCorrTasar": f"{tr['corr_perdida_tasa']['r']:+.3f}",
        "loeoCorrTasap": f"{tr['corr_perdida_tasa']['p']:.3f}",
        "loeoPeor": entidad(min(tr["por_entidad"], key=lambda r: r["delta_AUROC"])["entidad"]),
        "loeoPeorDelta": f"{min(r['delta_AUROC'] for r in tr['por_entidad']):+.4f}",
        # Informatividad del dato faltante y criterio del análisis interseccional
        "naRazonMax": f"{cal['na_informativo']['razon_max']:.1f}",
        "naVarMax": cal["na_informativo"]["var_razon_max"].replace("_", "\\_"),
        "naMortConNa": f"{cal['na_informativo']['mort_con_na_max']*100:.1f}",
        "naMortSinNa": f"{max(cal['na_informativo']['por_variable'], key=lambda r: r['mort_con_na'])['mort_sin_na']*100:.1f}",
        "naRazonMin": f"{cal['na_informativo']['razon_min']:.3f}",
        "naVarMin": cal["na_informativo"]["var_razon_min"].replace("_", "\\_"),
        "naEntMin": f"{cal['na_entidad_min']*100:.2f}",
        "naEntMax": f"{cal['na_entidad_max']*100:.2f}",
        "naEntMinEnt": entidad(cal["na_entidad_min_ent"]),
        "naEntMaxEnt": entidad(cal["na_entidad_max_ent"]),
        "interMinN": str(aud["interseccional_criterio"]["min_n_usado"]),
        "interNestandar": str(aud["interseccional_criterio"]["n_entidades_estandar"]),
        "interRangoEstandar": f"{aud['interseccional_criterio']['rango_estandar']:.3f}",
        "interPeorEstandar": entidad(aud["interseccional_criterio"]["peor_estandar"]),
        "interPeorEstandarAUROC": f"{aud['interseccional_criterio']['peor_estandar_auroc']:.4f}",
        "postGapFPRbase": f"{mit['Baseline (umbral global)']['gap_FPR']:.3f}",
        "postGapFPR": f"{mit['POST (umbral/entidad)']['gap_FPR']:.3f}",
        "loeoMayoresUnPct": str(sum(1 for x in tr["por_entidad"] if abs(x["delta_AUROC"]) > 0.01)),
        # Incertidumbre: remuestreo y prueba de permutación
        "boB": str(inc["B_bootstrap"]), "boP": str(inc["P_permutaciones"]),
        "gapAurocICa": f"{inc['gap_auroc_ic'][0]:.4f}",
        "gapAurocICb": f"{inc['gap_auroc_ic'][1]:.4f}",
        "gapTprICa": f"{inc['gap_tpr_ic'][0]:.4f}",
        "gapTprICb": f"{inc['gap_tpr_ic'][1]:.4f}",
        "nulaAuroc": f"{inc['nula_auroc_mediana']:.4f}",
        "nulaAurocPsup": f"{inc['nula_auroc_p95']:.4f}",
        "nulaTpr": f"{inc['nula_tpr_mediana']:.4f}",
        "nulaTprPsup": f"{inc['nula_tpr_p95']:.4f}",
        "pAuroc": f"{inc['p_auroc']:.3f}", "pTpr": f"{inc['p_tpr']:.3f}",
        "paresDisjuntos": str(inc["pares_disjuntos"]),
        "paresTotal": str(inc["pares_total"]),
        "paresPct": f"{inc['frac_pares_disjuntos']*100:.0f}",
        "icAncho": entidad(inc["ic_mas_ancho"]),
        "icAnchoAmp": f"{inc['ic_mas_ancho_amplitud']:.3f}",
        "icAnchoN": miles(inc["ic_mas_ancho_n"]),
        "excesoTpr": f"{inc['gap_tpr_obs'] - inc['nula_tpr_mediana']:.4f}",
        # Sensibilidad sin NEUMONIA
        "sinNeuAUROC": f"{sen['sin_neumonia']['auroc']:.4f}",
        "sinNeuCaida": f"{sen['sin_neumonia']['caida_auroc']:.4f}",
        "sinNeuAUPRC": f"{sen['sin_neumonia']['auprc']:.4f}",
        "sinNeuGapTPR": f"{sen['sin_neumonia']['gap_TPR']:.4f}",
        "sinNeuGapAUROC": f"{sen['sin_neumonia']['gap_AUROC']:.4f}",
        "sinNeuNpred": str(sen["sin_neumonia"]["n_predictores"]),
        # Cohorte
        "cohorteN": miles(man["n_filas"]),
        "cohorteTasaDef": f"{man['tasa_defuncion']*100:.2f}",
        "cohorteFuente": man["fuente"].replace("_", "\\_"),
        "testN": miles(aud["n_test"]),
        # Desempeño
        "aurocGlobal": f"{res['modelo']['auroc_global']:.4f}",
        "auprcGlobal": f"{res['modelo']['auprc_global']:.4f}",
        "brierCrudo": f"{res['modelo']['brier_crudo']:.4f}",
        "brierCalibrado": f"{res['modelo']['brier_calibrado']:.4f}",
        "umbralOperacion": f"{res['modelo']['umbral']:.4f}",
        "sensObjetivo": f"{res['modelo']['sensibilidad_objetivo']*100:.0f}",
        # Auditoría por entidad
        "gapTPRentidad": f"{d_ent['gap_TPR (equalized odds)']:.4f}",
        "gapFPRentidad": f"{d_ent['gap_FPR']:.4f}",
        "gapAUROCentidad": f"{d_ent['gap_AUROC']:.4f}",
        "gapSelEntidad": f"{d_ent['gap_seleccion (paridad demogr.)']:.4f}",
        "errCalEntidad": f"{d_ent['max_error_calibracion']:.4f}",
        "entPeor": entidad(ent[0]["grupo"]),
        "entPeorAUROC": f"{ent[0]['AUROC']:.4f}",
        "entPeorTPR": f"{ent[0]['TPR']:.3f}",
        "entMejor": entidad(ent[-1]["grupo"]),
        "entMejorAUROC": f"{ent[-1]['AUROC']:.4f}",
        "entMejorTPR": f"{ent[-1]['TPR']:.3f}",
        "nEntidades": str(len(ent)),
        # Sexo y edad
        "gapTPRsexo": f"{d_sex['gap_TPR (equalized odds)']:.4f}",
        "gapAUROCsexo": f"{d_sex['gap_AUROC']:.4f}",
        "gapTPRedad": f"{d_eda['gap_TPR (equalized odds)']:.4f}",
        "gapAUROCedad": f"{d_eda['gap_AUROC']:.4f}",
        # Interseccional
        "sesentaPeor": entidad(e60[0]["grupo"]),
        "sesentaPeorAUROC": f"{e60[0]['AUROC']:.3f}",
        "sesentaMejor": entidad(e60[-1]["grupo"]),
        "sesentaMejorAUROC": f"{e60[-1]['AUROC']:.3f}",
        # Mitigación
        "gapBase": f"{mit['Baseline (umbral global)']['gap_TPR']:.3f}",
        "accBase": f"{mit['Baseline (umbral global)']['bal_acc']:.3f}",
        "gapPre": f"{mit['PRE (reponderacion entidad)']['gap_TPR']:.3f}",
        "gapIn": f"{mit['IN (Fairlearn EqOdds)*']['gap_TPR']:.3f}",
        "gapPost": f"{mit['POST (umbral/entidad)']['gap_TPR']:.3f}",
        "accPost": f"{mit['POST (umbral/entidad)']['bal_acc']:.3f}",
        "gapPostOpt": f"{mit['POST (umbral/entidad, en test)']['gap_TPR']:.3f}",
        "reduccionPost": f"{(1 - mit['POST (umbral/entidad)']['gap_TPR'] / mit['Baseline (umbral global)']['gap_TPR'])*100:.0f}",
    }
    lineas = ["% Generado por generar_tablas.py -- NO editar a mano.",
              "% Cifras extraidas de auditoria_equidad.json y resultados_tesis.json.",
              ""]
    lineas += [f"\\newcommand{{\\{k}}}{{{v}}}" for k, v in defs.items()]
    with open(RUTA_MACROS, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lineas) + "\n")
    print("  ", RUTA_MACROS, f"({len(defs)} macros)")


def main() -> None:
    aud = leer("auditoria_equidad.json")
    res = leer("resultados_tesis.json")
    man = leer("dge_covid2021_limpio.manifest.json")
    cal = leer("calidad_datos.json")
    mod = leer("modelo_referencia.json")
    sen = leer("sensibilidad_hospitalizados.json")
    tr = leer("transportabilidad_loeo.json")
    inc = leer("incertidumbre_brechas.json")

    print("Generando tablas y macros:")
    tabla_entidad(aud)
    tabla_simple("tab_sexo.tex", aud["por_sexo"],
                 "Desempeño y equidad por sexo en el conjunto de prueba.",
                 "tab:sexo", "Sexo")
    tabla_simple("tab_edad.tex",
                 sorted(aud["por_grupo_edad"], key=lambda r: r["grupo"]),
                 "Desempeño y equidad por grupo etario en el conjunto de prueba.",
                 "tab:edad", "Grupo etario")
    tabla_disparidad(aud)
    tabla_interseccional(aud)
    tabla_mitigacion(res)
    tabla_pareto(res)
    tabla_importancia(mod)
    tabla_marginacion(res)
    tabla_sensibilidad(sen)
    tabla_loeo(tr)
    tabla_incertidumbre(inc)
    tabla_permutacion(inc)
    macros(aud, res, man, cal, mod, sen, tr, inc)

    if res.get("conapo_verificado", False):
        print("\nIndice de marginacion VERIFICADO:", res.get("conapo_fuente", ""))
    else:
        print("\n!! AVISO: el indice de marginacion sigue SIN VERIFICAR contra CONAPO.")
        print("   La seccion de correlatos de la tesis queda marcada como provisional.")


if __name__ == "__main__":
    main()
