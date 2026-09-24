# Tesis — Estratificación de riesgo clínico consciente de la equidad

Auditoría y mitigación del sesgo geográfico entre entidades federativas en modelos
predictivos con datos abiertos de salud de México (DGE / Secretaría de Salud).

Maestría en Ciencia de Datos — David Segundo.

## Qué hay aquí

| Ruta | Contenido |
|---|---|
| `tesis_common.py` | Contrato compartido de los cuadernos: rutas, cohorte, hiperparámetros, partición, punto de operación y métricas de equidad. **Única definición** de cada uno. |
| `01_exploracion_datos_dge.ipynb` | Ingesta, recodificación, control de fuga de información, EDA. |
| `02_modelo_referencia.ipynb` | Entrenamiento, calibración isotónica, punto de operación, importancia. |
| `03_auditoria_equidad.ipynb` | Auditoría por entidad, sexo, grupo etario e interseccional. |
| `04_mitigacion_pareto.ipynb` | Correlatos, mitigación pre/in/post, frontera de Pareto. |
| `05_transportabilidad_loeo.ipynb` | Dejar-una-entidad-fuera: 32 modelos, cada uno excluyendo una entidad. Validación **interna**. |
| `06_incertidumbre.ipynb` | Remuestreo (1000 réplicas) y prueba de permutación (1000) sobre las brechas. |
| `generar_tablas.py` | Traduce los JSON de resultados a tablas y macros de LaTeX. |
| `tesis/` | Documento LaTeX de la tesis (`tesis.tex`), capítulos, tablas generadas y bibliografía. |
| `protocolo/` | Protocolo de tesis (`protocolo.tex`), documento **prospectivo** e independiente. |
| `presentacion/` | Presentación del protocolo en Beamer (`presentacion.tex`), 25 diapositivas. |
| `plan_trabajo/` | Entregable 1A del seminario: plan de trabajo con Gantt. Dos versiones: `.tex`/`.pdf` y `.docx` (para Google Docs). |
| `requirements.txt` | Dependencias de Python. |

## Requisitos

- Python 3.14 (probado en 3.14.5) — `python3 -m pip install -r requirements.txt`
- TeX Live 2026 o equivalente con `latexmk` y `biber` (MacTeX completo sirve)
- El corte anual `COVID19MEXICO2021.csv` de la DGE en el directorio raíz
  (~1.4 GB, no versionado)

### Variables de entorno

| Variable | Obligatoria | Descripción |
|---|---|---|
| `DGE_DATA_PATH` | No | Ruta al CSV crudo de la DGE. Por omisión, `COVID19MEXICO2021.csv` en el directorio raíz. |

## Runbook

Los cuadernos deben ejecutarse **en orden**. Cada uno verifica la procedencia de
lo que consume y falla de inmediato si el artefacto previo no corresponde a la
corrida vigente.

```bash
# 1. Dependencias (una vez; se recomienda entorno virtual)
python3 -m venv .venv && source .venv/bin/activate
python -m pip install -r requirements.txt

# 2. Cadena analítica, en orden
jupyter lab   # ejecutar 01 -> 02 -> 03 -> 04 -> 05 -> 06

# 3. Tablas y macros de LaTeX a partir de los resultados
python3 generar_tablas.py

# 4. Documentos
cd tesis && latexmk -pdf tesis.tex          # tesis
cd ../protocolo && latexmk -pdf protocolo.tex  # protocolo
cd ../presentacion && latexmk -pdf presentacion.tex  # presentación
cd ../plan_trabajo && latexmk -pdf plan_trabajo.tex   # plan de trabajo (1A)
```

El **plan de trabajo** existe en dos formatos, con el mismo contenido:

- `plan_trabajo.tex` → PDF. Tiene un interruptor al inicio: `\portadatrue` produce
  portada + 2 cuartillas (3 páginas); `\portadafalse` produce exactamente 2 páginas
  con los datos en un encabezado compacto, por si la evaluación cuenta la portada
  dentro del límite.
- `generar_docx.py` → `plan_trabajo.docx`, para editar en Google Docs. Usa **Arial**
  (Google Docs no tiene Calibri y lo sustituiría, desplazando el texto) y anchos de
  columna fijados celda por celda, porque Google Docs recalcula los automáticos y
  descuadraría el Gantt. Regenerar con `python3 generar_docx.py`.

El **protocolo** no depende de la cadena analítica: es prospectivo y no contiene
resultados, por lo que no carga `macros_resultados.tex`. Sí reutiliza
`tesis/referencias.bib`, de modo que la bibliografía cotejada es la misma en ambos
documentos.

La **presentación** también es prospectiva y autocontenida (no lee `.bib` ni macros);
está pensada para 12–15 minutos.

Para ejecutar la cadena sin interfaz:

```bash
python3 - <<'PY'
import nbformat
from nbclient import NotebookClient
for f in ["01_exploracion_datos_dge.ipynb", "02_modelo_referencia.ipynb",
          "03_auditoria_equidad.ipynb", "04_mitigacion_pareto.ipynb",
          "05_transportabilidad_loeo.ipynb", "06_incertidumbre.ipynb"]:
    nb = nbformat.read(f, as_version=4)
    NotebookClient(nb, timeout=5400, kernel_name="python3",
                   resources={"metadata": {"path": "."}}).execute()
    nbformat.write(nb, f)
PY
```

Tiempo aproximado de la cadena completa: 45–60 minutos (el 05 ajusta 32 modelos; el 06 hace 2000 remuestreos) (el cuaderno 01 lee 1.4 GB
de CSV; el 02 y el 04 entrenan sobre ~1.5 M de registros).

## Artefactos generados

No versionados; se reproducen ejecutando la cadena.

- `dge_covid2021_limpio.parquet` — cohorte limpia (única entrada de 02–04)
- `dge_covid2021_limpio.manifest.json` — procedencia de la cohorte
- `modelo_hgb_mortalidad.joblib` — paquete: modelo + calibrador + huella de cohorte
- `calidad_datos.json`, `modelo_referencia.json`, `auditoria_equidad.json`,
  `resultados_tesis.json`, `sensibilidad_hospitalizados.json`,
  `transportabilidad_loeo.json`, `incertidumbre_brechas.json` — cifras que cita
  el documento
- `eda_por_entidad.png`, `equidad_por_entidad.png`, `pareto_mitigacion.png`,
  `transportabilidad_loeo.png`, `incertidumbre_brechas.png`
- `tesis/tablas/*.tex`, `tesis/macros_resultados.tex`

## Contrato de datos

El riesgo de un canal por cuadernos es que una etapa consuma un artefacto de una
versión anterior de la etapa previa sin que nada lo señale. Las salvaguardas son:

1. El cuaderno 01 emite un **manifiesto** con cohorte, filas, columnas y tasas.
2. `tc.cargar_cohorte()` exige el manifiesto y verifica columnas, filas y cohorte.
3. El modelo se persiste como **paquete**; `tc.cargar_modelo()` rechaza uno
   entrenado sobre otra cohorte o con otros predictores.
4. La escritura del parquet **falla de inmediato**: nunca degrada a otro formato
   dejando en disco el artefacto anterior.
5. El documento LaTeX no contiene cifras de resultados escritas a mano; todas
   provienen de `macros_resultados.tex`.

Si una cifra del documento no coincide con los cuadernos, es que falta ejecutar
`generar_tablas.py`.

## Índice de marginación

`tesis_common.CONAPO_IM_2020` y `CONAPO_GRADO` contienen el índice y el grado de
marginación por entidad de los **Índices de marginación 2020** de CONAPO
([fuente](https://www.gob.mx/conapo/documentos/indices-de-marginacion-2020-284372),
archivo por entidad `IME_2020.xls`, con base en el Censo INEGI 2020).

⚠️ **Dirección del índice.** La edición 2020 se calcula por Distancias Ponderadas
al cuadrado (DP2) y va de 10.99 (Guerrero, «Muy alto») a 23.44 (Nuevo León, «Muy
bajo»): **mayor valor = menor marginación**. El «índice normalizado» acotado a
0–1 pertenece a las ediciones anteriores, basadas en componentes principales, y su
dirección es **la contraria**. Confundirlos invierte la lectura de H2.

Un catálogo previo de este proyecto guardaba un reescalamiento no documentado de
estas mismas cifras a 0–1 (r = 1.000 con el oficial), etiquetado con el nombre de
la edición anterior. Se sustituyó por el índice publicado; las conclusiones no
cambiaron.

## Estructura del desenlace (importante)

En la cohorte de confirmados **fallecer implica estar registrado como
hospitalizado**: hay 0 defunciones ambulatorias, frente a 2,520 en la base
completa. El desenlace solo es posible en el 11.8 % hospitalizado.

Consecuencia: el AUROC de 0.9503 de la cohorte completa incluye separar
ambulatorios de hospitalizados. Restringido a la población en riesgo es **0.7001**
(cuaderno 02, sección de sensibilidad). Esa es la cifra comparable con modelos
clínicos de mortalidad hospitalaria.

⚠️ **Prerrequisito para la validación externa en DGIS.** SAEH es una base de
egresos: población hospitalizada, prevalencia ≈ 47.5 %. Validar contra ella el
modelo de la cohorte completa (prevalencia 5.6 %) haría pasar un cambio de
espectro por un fallo de transportabilidad. Debe usarse el modelo restringido.

## Pendientes conocidos

- **Validación externa (DGIS) no ejecutada.** La hipótesis H4 queda sin poner a
  prueba; así se declara en el documento. La generalización geográfica *interna*
  sí se evaluó (cuaderno 05) y resultó buena: pérdida mediana de AUROC −0.0006 al
  excluir una entidad del entrenamiento, sin que las brechas se acentúen.
- **Incertidumbre solo en el eje geográfico.** El cuaderno 06 da intervalos de
  confianza y prueba de permutación para las brechas por entidad; los subgrupos
  interseccionales siguen siendo estimaciones puntuales.
- **Indicadores de infraestructura de salud.** H2 quedó refutada con el índice de
  marginación estatal; el paso siguiente es probarla con camas y personal por
  habitante, idealmente por unidad médica y no por entidad.

## Referencias

Formato **APA 7** (`biblatex-apa` + `biber`). Citas: `\parencite` para
parentéticas y `\textcite` para narrativas — no usar `\cite`.

Todas las entradas se cotejaron el 30 de julio de 2026. Las que tienen DOI se
generaron desde la **API de Crossref**, de modo que autoría, revista, volumen,
número, páginas y año provienen del registro del editor y no de una
transcripción. Las de conferencia (NIPS, ITCS) y JMLR, que Crossref no indexa, se
cotejaron contra **DBLP**. El encabezado de `tesis/referencias.bib` documenta las
correcciones encontradas. **Sin pendientes bibliográficos**: el rango de páginas
de `geograficos2024`, que no figura en Crossref ni en el portal OJS, se tomó del
pie del PDF del propio artículo (pp. 5–18).

## Nota de reproducibilidad: Fairlearn

`ExponentiatedGradient` devuelve una **distribución sobre clasificadores**, y
`predict()` muestrea de ella. Sin `random_state` en la llamada a `predict` —no
basta con fijarlo al ajustar— el resultado cambia entre ejecuciones: se midieron
brechas de 0.245 a 0.628 sobre el mismo modelo ajustado. El cuaderno 04 fija la
semilla y además reporta el rango sobre 20 realizaciones, porque la dispersión es
el resultado relevante.
