"""Contrato compartido de la cadena de notebooks de la tesis (01 -> 04).

Única fuente de verdad para rutas de artefactos, definición de cohorte,
hiperparámetros del modelo, partición de datos, punto de operación clínico y
métricas de equidad.

Los notebooks importan de aquí en lugar de redefinir constantes: así un cambio en
una etapa no puede desalinear las demás en silencio. Antes de este módulo, el
notebook 04 entrenaba un modelo con hiperparámetros distintos de los que el 02
guardaba y el 03 auditaba, de modo que las tres etapas hablaban de "el modelo"
refiriéndose a objetos diferentes.

Uso típico:

    import tesis_common as tc
    df, manifiesto = tc.cargar_cohorte()
    idx_tr, idx_cal, idx_te = tc.particionar(df[tc.TARGET])
"""

from __future__ import annotations

import json
import os

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# --------------------------------------------------------------------------- #
# Artefactos
# --------------------------------------------------------------------------- #

CSV_CRUDO = os.environ.get("DGE_DATA_PATH", "COVID19MEXICO2021.csv")
PARQUET = "dge_covid2021_limpio.parquet"
MANIFIESTO = PARQUET.replace(".parquet", ".manifest.json")
MODELO_PATH = "modelo_hgb_mortalidad.joblib"

# --------------------------------------------------------------------------- #
# Definición de la cohorte
# --------------------------------------------------------------------------- #

#: Cohorte canónica: casos COVID confirmados (CLASIFICACION_FINAL in {1,2,3}).
#: Un modelo de mortalidad por COVID debe estimarse sobre enfermos de COVID;
#: incluir negativos y sospechosos mezcla poblaciones y diluye la señal.
SOLO_CONFIRMADOS = True
CLASIF_CONFIRMADO = [1, 2, 3]

TARGET = "defuncion"

ENTIDADES = {
    1: "AGUASCALIENTES", 2: "BAJA CALIFORNIA", 3: "BAJA CALIFORNIA SUR", 4: "CAMPECHE",
    5: "COAHUILA", 6: "COLIMA", 7: "CHIAPAS", 8: "CHIHUAHUA", 9: "CIUDAD DE MEXICO",
    10: "DURANGO", 11: "GUANAJUATO", 12: "GUERRERO", 13: "HIDALGO", 14: "JALISCO",
    15: "MEXICO", 16: "MICHOACAN", 17: "MORELOS", 18: "NAYARIT", 19: "NUEVO LEON",
    20: "OAXACA", 21: "PUEBLA", 22: "QUERETARO", 23: "QUINTANA ROO",
    24: "SAN LUIS POTOSI", 25: "SINALOA", 26: "SONORA", 27: "TABASCO",
    28: "TAMAULIPAS", 29: "TLAXCALA", 30: "VERACRUZ", 31: "YUCATAN", 32: "ZACATECAS",
}

#: Comorbilidades y síntomas codificados 1=Sí, 2=No, 97/98/99=ausente.
COMORBILIDADES = [
    "DIABETES", "EPOC", "ASMA", "INMUSUPR", "HIPERTENSION", "OTRA_COM",
    "CARDIOVASCULAR", "OBESIDAD", "RENAL_CRONICA", "TABAQUISMO", "NEUMONIA",
]

#: Variables POSTERIORES al punto de predicción (ingreso). Nunca son predictores.
VARS_FUGA = ["UCI", "INTUBADO", "FECHA_DEF"]

#: Cortes de edad. Definidos una sola vez: el notebook 03 los recalculaba con
#: bordes distintos ([-1, ..., 200]) que los del notebook 01 ([-0.1, ..., 120]).
BINS_EDAD = [-0.1, 17, 39, 59, 120]
ETIQUETAS_EDAD = ["0-17", "18-39", "40-59", "60+"]

PREDICTORES = ["EDAD", "sexo_mujer"] + [c + "_bin" for c in COMORBILIDADES]
ATRIBUTOS_SENSIBLES = ["entidad_nombre", "sexo_mujer", "grupo_edad"]

COLUMNAS_PARQUET = (
    ["ID_REGISTRO", "hospitalizado", "defuncion", "EDAD", "grupo_edad",
     "sexo_mujer", "entidad_nombre", "MUNICIPIO_RES", "CLASIFICACION_FINAL"]
    + [c + "_bin" for c in COMORBILIDADES]
    + [c + "_na" for c in COMORBILIDADES]
)

#: Columnas sin las que los notebooks 02-04 no pueden operar.
COLUMNAS_REQUERIDAS = {
    "ID_REGISTRO", "hospitalizado", "defuncion", "EDAD", "grupo_edad",
    "sexo_mujer", "entidad_nombre", "CLASIFICACION_FINAL",
}

# --------------------------------------------------------------------------- #
# Modelo y partición
# --------------------------------------------------------------------------- #

SEMILLA = 42

#: Fracción de test. El bloque de test se separa PRIMERO, con la misma semilla
#: que usaban los notebooks originales, de modo que la población auditada no
#: cambia respecto de los resultados ya reportados.
FRACCION_TEST = 0.25

#: Fracción del bloque de ajuste reservada para calibrar. Calibrar sobre datos
#: de test (como hacía el notebook 04) contamina la evaluación.
FRACCION_CALIB = 0.20

#: Hiperparámetros canónicos del modelo principal. El notebook 04 usaba
#: max_iter=250 / learning_rate=0.06, distintos de los del 02 y 03.
HPARAMS_HGB = {
    "max_iter": 300,
    "learning_rate": 0.05,
    "max_depth": 6,
    "class_weight": "balanced",
    "random_state": SEMILLA,
}

#: Punto de operación clínico: sensibilidad global objetivo para triage.
#: El notebook 02 evaluaba en 0.5, un umbral sin significado en un modelo con
#: class_weight="balanced", mientras 03 y 04 auditaban al 80%.
SENSIBILIDAD_OBJETIVO = 0.80

# --------------------------------------------------------------------------- #
# Índice de marginación
# --------------------------------------------------------------------------- #

#: Índice de marginación por entidad federativa, 2020.
#:
#: Fuente: CONAPO, "Índices de marginación 2020", archivo por entidad
#: `IME_2020.xls`, con base en el Censo de Población y Vivienda 2020 (INEGI).
#: https://www.gob.mx/conapo/documentos/indices-de-marginacion-2020-284372
#:
#: DIRECCIÓN DEL ÍNDICE: un valor MÁS ALTO indica MENOR marginación
#: (Guerrero 10.99 = grado "Muy alto"; Nuevo León 23.44 = "Muy bajo"). La
#: edición 2020 se calcula por Distancias Ponderadas al cuadrado (DP2) y su
#: escala no está acotada a [0,1]: el "índice normalizado" pertenece a las
#: ediciones anteriores, basadas en componentes principales, y su dirección es
#: la CONTRARIA. Confundirlos invierte la lectura de la hipótesis H2.
#:
#: Los valores anteriores de este catálogo eran un reescalamiento no documentado
#: de estas mismas cifras (r = 1.000 con el oficial); se sustituyen por el índice
#: publicado para que sea citable y para conservar el grado de marginación.
CONAPO_VERIFICADO = True
CONAPO_FUENTE = ("CONAPO, Índices de marginación 2020 (IME_2020.xls), "
                 "Censo de Población y Vivienda 2020, INEGI")

CONAPO_IM_2020 = {
    "AGUASCALIENTES": 22.2057, "BAJA CALIFORNIA": 21.3803,
    "BAJA CALIFORNIA SUR": 21.4734, "CAMPECHE": 17.8051, "CHIAPAS": 11.9987,
    "CHIHUAHUA": 20.0153, "CIUDAD DE MEXICO": 23.1431, "COAHUILA": 22.5457,
    "COLIMA": 21.5323, "DURANGO": 18.4727, "GUANAJUATO": 19.4195,
    "GUERRERO": 10.9892, "HIDALGO": 18.0532, "JALISCO": 21.8151,
    "MEXICO": 20.8036, "MICHOACAN": 18.2808, "MORELOS": 19.8139,
    "NAYARIT": 17.5160, "NUEVO LEON": 23.4443, "OAXACA": 13.2164,
    "PUEBLA": 17.7216, "QUERETARO": 20.8382, "QUINTANA ROO": 20.6289,
    "SAN LUIS POTOSI": 18.6880, "SINALOA": 20.5099, "SONORA": 21.4056,
    "TABASCO": 18.3325, "TAMAULIPAS": 20.9966, "TLAXCALA": 19.8707,
    "VERACRUZ": 16.4142, "YUCATAN": 17.5122, "ZACATECAS": 19.4972,
}

#: Grado de marginación publicado por CONAPO para el mismo corte.
CONAPO_GRADO = {
    "AGUASCALIENTES": "Muy bajo", "BAJA CALIFORNIA": "Bajo",
    "BAJA CALIFORNIA SUR": "Bajo", "CAMPECHE": "Alto", "CHIAPAS": "Muy alto",
    "CHIHUAHUA": "Medio", "CIUDAD DE MEXICO": "Muy bajo", "COAHUILA": "Muy bajo",
    "COLIMA": "Bajo", "DURANGO": "Alto", "GUANAJUATO": "Medio",
    "GUERRERO": "Muy alto", "HIDALGO": "Alto", "JALISCO": "Bajo",
    "MEXICO": "Bajo", "MICHOACAN": "Alto", "MORELOS": "Medio",
    "NAYARIT": "Alto", "NUEVO LEON": "Muy bajo", "OAXACA": "Muy alto",
    "PUEBLA": "Alto", "QUERETARO": "Bajo", "QUINTANA ROO": "Medio",
    "SAN LUIS POTOSI": "Medio", "SINALOA": "Medio", "SONORA": "Bajo",
    "TABASCO": "Alto", "TAMAULIPAS": "Bajo", "TLAXCALA": "Medio",
    "VERACRUZ": "Alto", "YUCATAN": "Alto", "ZACATECAS": "Medio",
}

#: Orden de severidad para agrupar entidades por grado, de mayor a menor carencia.
GRADOS_ORDEN = ["Muy alto", "Alto", "Medio", "Bajo", "Muy bajo"]

# Umbrales mínimos para que un grupo sea evaluable sin ruido dominante.
MIN_N_GRUPO = 500
MIN_POS_GRUPO = 20


# --------------------------------------------------------------------------- #
# Carga con contrato
# --------------------------------------------------------------------------- #

def cargar_cohorte(parquet: str = PARQUET, manifiesto: str = MANIFIESTO):
    """Carga la cohorte limpia validando su procedencia.

    Falla rápido si el parquet no corresponde a la corrida vigente del notebook
    01. Sin esta verificación un artefacto obsoleto se consume en silencio y
    todo lo reportado aguas abajo queda invalidado.

    Returns:
        (DataFrame, dict): la cohorte y su manifiesto.

    Raises:
        FileNotFoundError: si falta el manifiesto.
        KeyError: si faltan columnas requeridas.
        ValueError: si el conteo de filas no coincide con el manifiesto.
    """
    if not os.path.exists(manifiesto):
        raise FileNotFoundError(
            f"No existe {manifiesto}: el parquet en disco no tiene procedencia "
            "verificable. Ejecuta 01_exploracion_datos_dge.ipynb completo."
        )
    with open(manifiesto, encoding="utf-8") as fh:
        meta = json.load(fh)

    df = pd.read_parquet(parquet)

    faltan = COLUMNAS_REQUERIDAS - set(df.columns)
    if faltan:
        raise KeyError(
            f"{parquet} está desactualizado; faltan columnas {sorted(faltan)}. "
            "Re-ejecuta el notebook 01."
        )
    if len(df) != meta["n_filas"]:
        raise ValueError(
            f"El parquet tiene {len(df):,} filas pero el manifiesto declara "
            f"{meta['n_filas']:,}. Artefactos desincronizados: re-ejecuta el 01."
        )
    if meta["solo_confirmados"] != SOLO_CONFIRMADOS:
        raise ValueError(
            f"Cohorte inconsistente: el manifiesto dice solo_confirmados="
            f"{meta['solo_confirmados']} y el contrato exige {SOLO_CONFIRMADOS}. "
            "Re-ejecuta el notebook 01."
        )
    return df, meta


def particionar(y):
    """Parte en entrenamiento / calibración / test de forma reproducible.

    El bloque de test se separa primero para que sea idéntico en los notebooks
    02, 03 y 04 y comparable con los resultados previos; la calibración se talla
    después sobre el bloque de ajuste, nunca sobre test.

    Args:
        y: vector del desenlace, usado para estratificar.

    Returns:
        (ndarray, ndarray, ndarray): índices posicionales de train, calib y test.
    """
    y = np.asarray(y)
    idx = np.arange(len(y))
    idx_fit, idx_test = train_test_split(
        idx, test_size=FRACCION_TEST, stratify=y, random_state=SEMILLA)
    idx_train, idx_calib = train_test_split(
        idx_fit, test_size=FRACCION_CALIB, stratify=y[idx_fit], random_state=SEMILLA)
    return idx_train, idx_calib, idx_test


# --------------------------------------------------------------------------- #
# Modelo: persistencia y puntuación
# --------------------------------------------------------------------------- #

def guardar_modelo(modelo, calibrador, n_filas_cohorte, path: str = MODELO_PATH):
    """Persiste el modelo junto con su calibrador y la huella de su cohorte.

    Se guarda un paquete y no el estimador desnudo para que los notebooks 03 y
    04 no puedan auditar un modelo entrenado sobre otra cohorte ni olvidar
    aplicar la calibración.
    """
    import joblib

    joblib.dump({
        "modelo": modelo,
        "calibrador": calibrador,
        "predictores": PREDICTORES,
        "hparams": HPARAMS_HGB,
        "n_filas_cohorte": int(n_filas_cohorte),
        "sensibilidad_objetivo": SENSIBILIDAD_OBJETIVO,
    }, path)
    return path


def cargar_modelo(n_filas_cohorte=None, path: str = MODELO_PATH) -> dict:
    """Carga el paquete del modelo entrenado por el notebook 02.

    Raises:
        FileNotFoundError: si el notebook 02 no se ha ejecutado.
        ValueError: si el modelo se entrenó sobre otra cohorte o con otros
            predictores que los del contrato vigente.
    """
    import joblib

    if not os.path.exists(path):
        raise FileNotFoundError(
            f"No existe {path}. Ejecuta 02_modelo_referencia.ipynb antes de este "
            "notebook: la auditoría debe correr sobre el modelo de referencia, "
            "no sobre uno reentrenado aquí."
        )
    paquete = joblib.load(path)
    if not isinstance(paquete, dict) or "modelo" not in paquete:
        raise ValueError(
            f"{path} tiene formato antiguo (estimador desnudo). Re-ejecuta el 02."
        )
    if paquete["predictores"] != PREDICTORES:
        raise ValueError(
            "El modelo guardado usa otros predictores que el contrato vigente. "
            "Re-ejecuta el notebook 02."
        )
    if n_filas_cohorte is not None and paquete["n_filas_cohorte"] != int(n_filas_cohorte):
        raise ValueError(
            f"El modelo se entrenó sobre una cohorte de "
            f"{paquete['n_filas_cohorte']:,} filas y la actual tiene "
            f"{int(n_filas_cohorte):,}. Re-ejecuta el notebook 02."
        )
    return paquete


def puntuar(paquete: dict, X) -> np.ndarray:
    """Devuelve el riesgo calibrado. Punto de entrada único para predecir.

    Aplicar el calibrador es obligatorio: el modelo crudo usa
    class_weight="balanced" y sobreestima el riesgo por un factor ~4, así que
    sus probabilidades no son interpretables ni auditables en calibración.
    """
    p = paquete["modelo"].predict_proba(X)[:, 1]
    cal = paquete.get("calibrador")
    return p if cal is None else cal.predict(p)


# --------------------------------------------------------------------------- #
# Punto de operación
# --------------------------------------------------------------------------- #

def umbral_para_sensibilidad(y_true, p_score, objetivo: float = SENSIBILIDAD_OBJETIVO):
    """Umbral que alcanza la sensibilidad global objetivo.

    Returns:
        (float, float, float): umbral, TPR y FPR logrados.
    """
    from sklearn.metrics import roc_curve

    fpr, tpr, thr = roc_curve(y_true, p_score)
    i = int(np.argmin(np.abs(tpr - objetivo)))
    return float(thr[i]), float(tpr[i]), float(fpr[i])


# --------------------------------------------------------------------------- #
# Métricas de equidad (implementación transparente y auditable)
# --------------------------------------------------------------------------- #

def tasas(y_true, p_score, umbral):
    """Devuelve (TPR, FPR) a un umbral dado."""
    pred = (np.asarray(p_score) >= umbral).astype(int)
    yt = np.asarray(y_true)
    tp = int(((pred == 1) & (yt == 1)).sum())
    fn = int(((pred == 0) & (yt == 1)).sum())
    fp = int(((pred == 1) & (yt == 0)).sum())
    tn = int(((pred == 0) & (yt == 0)).sum())
    tpr = tp / (tp + fn) if (tp + fn) else np.nan
    fpr = fp / (fp + tn) if (fp + tn) else np.nan
    return tpr, fpr


def grupos_evaluables(grupos, y_true, min_n=MIN_N_GRUPO, min_pos=MIN_POS_GRUPO):
    """Grupos con soporte suficiente, y los descartados con su motivo.

    Devolver los descartados es deliberado: recortar en silencio hace que una
    cobertura parcial se lea como completa.
    """
    g = pd.Series(np.asarray(grupos))
    yt = np.asarray(y_true)
    ok, fuera = [], []
    for v in sorted(g.dropna().unique()):
        m = (g == v).to_numpy()
        n, pos = int(m.sum()), int(yt[m].sum())
        if n >= min_n and pos >= min_pos and len(np.unique(yt[m])) == 2:
            ok.append(v)
        else:
            fuera.append({"grupo": v, "n": n, "positivos": pos})
    return ok, pd.DataFrame(fuera)


def metricas_por_grupo(y_true, p_score, grupos, umbral,
                       min_n=MIN_N_GRUPO, min_pos=MIN_POS_GRUPO):
    """Métricas de desempeño y equidad por grupo, a un umbral común.

    Args:
        y_true: desenlace observado.
        p_score: riesgo calibrado.
        grupos: etiqueta de grupo por observación (mismo orden que y_true).
        umbral: punto de operación.

    Returns:
        DataFrame con una fila por grupo evaluable.
    """
    from sklearn.metrics import roc_auc_score

    yt = np.asarray(y_true)
    ps = np.asarray(p_score)
    g = pd.Series(np.asarray(grupos))
    ok, _ = grupos_evaluables(g, yt, min_n, min_pos)

    filas = []
    for v in ok:
        m = (g == v).to_numpy()
        tpr, fpr = tasas(yt[m], ps[m], umbral)
        filas.append(dict(
            grupo=v, n=int(m.sum()), tasa=float(yt[m].mean()),
            AUROC=roc_auc_score(yt[m], ps[m]), TPR=tpr, FPR=fpr,
            seleccion=float((ps[m] >= umbral).mean()),
            cal_pred=float(ps[m].mean()), cal_obs=float(yt[m].mean()),
        ))
    return pd.DataFrame(filas)


def resumen_disparidad(tabla: pd.DataFrame) -> pd.Series:
    """Brechas máximas entre grupos: equalized odds, paridad y calibración."""
    return pd.Series({
        "gap_TPR (equalized odds)": tabla["TPR"].max() - tabla["TPR"].min(),
        "gap_FPR": tabla["FPR"].max() - tabla["FPR"].min(),
        "gap_AUROC": tabla["AUROC"].max() - tabla["AUROC"].min(),
        "gap_seleccion (paridad demogr.)": tabla["seleccion"].max() - tabla["seleccion"].min(),
        "max_error_calibracion": (tabla["cal_pred"] - tabla["cal_obs"]).abs().max(),
    }).round(4)
