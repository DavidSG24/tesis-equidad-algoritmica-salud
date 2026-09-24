# Estratificación de riesgo clínico consciente de la equidad

Auditoría y mitigación del sesgo geográfico entre entidades federativas en modelos
predictivos de mortalidad por COVID-19, sobre datos abiertos de salud de México
(DGE / Secretaría de Salud).

Proyecto terminal de la Maestría en Ciencia de Datos e Información (INFOTEC).
Autor: David Segundo García. Asesor: Dr. Daniel Alejandro Cervantes Cabrera.

## Propósito

La predicción de desenlaces por COVID-19 con datos mexicanos ha sido ampliamente
estudiada. Este trabajo desplaza la pregunta: no si un modelo acierta, sino **si
acierta por igual** entre entidades federativas, sexos y grupos etarios, y qué
puede hacerse cuando no lo hace. El entregable central es una frontera de Pareto
equidad–desempeño utilizable como instrumento de decisión antes del despliegue.

## Organización del repositorio

| Ruta | Contenido |
|---|---|
| `tesis/` | Núcleo del proyecto: cuadernos de análisis, código compartido y documento LaTeX. Tiene su propio [README](tesis/README.md) con el detalle de cada archivo. |
| `tesis/tesis/` | Documento de la tesis en LaTeX: capítulos, tablas generadas y bibliografía. |
| `entregas/` | Entregas al asesor en formato Word y PDF. |
| `entregas/generador/` | Generador de las entregas: `contenido.py` (texto, fuente único de verdad) y `armar_entrega.py` (lo vuelca sobre la plantilla institucional). |

> `tesis/README.md` describe además las carpetas `protocolo/`, `presentacion/` y
> `plan_trabajo/`, que no forman parte de este repositorio.

## Datos

Los microdatos **no están en el repositorio** por su tamaño (2.2 GB). Son públicos
y se descargan de la fuente:

| Archivo | Tamaño | Origen |
|---|---|---|
| `tesis/COVID19MEXICO2021.csv` | 1.3 GB | [Datos abiertos de COVID-19, DGE](https://www.gob.mx/salud/documentos/datos-abiertos-152127) — corte anual 2021 |
| `tesis/dge_covid2021_limpio.parquet` | 28 MB | Derivado; lo produce el cuaderno `01_exploracion_datos_dge.ipynb` |
| `tesis/IME_2020.xls` | — | [Índices de marginación 2020, CONAPO](https://www.gob.mx/conapo/documentos/indices-de-marginacion-2020-284372) |

Sí se versionan los JSON de resultados y las figuras, de modo que las tablas del
documento pueden regenerarse sin volver a ejecutar el análisis completo.

## Puesta en marcha

```bash
# 1. Dependencias de Python (probado en 3.14.5)
python3 -m pip install -r tesis/requirements.txt

# 2. Colocar COVID19MEXICO2021.csv en tesis/
#    (descarga desde el enlace de la tabla anterior)

# 3. Ejecutar los cuadernos en orden, del 01 al 06
```

Para compilar el documento se necesita TeX Live 2026 o equivalente, con `latexmk`
y `biber` (MacTeX completo sirve).

No se requieren variables de entorno ni credenciales: todas las fuentes son
públicas y de libre uso.

## Operaciones frecuentes

```bash
# Regenerar las tablas y macros de LaTeX a partir de los JSON de resultados
cd tesis && python3 generar_tablas.py

# Compilar la tesis
cd tesis/tesis && latexmk -pdf tesis.tex

# Regenerar la entrega en Word a partir de contenido.py
cd entregas/generador && python3 armar_entrega.py
```

> El generador de entregas necesita la plantilla institucional
> `plantilla infotec/Plantilla Tesis MCDI_ProyectoTerminal.docx`. Es material de
> INFOTEC y no se redistribuye aquí, de modo que `armar_entrega.py` solo funciona
> en un entorno que ya la tenga.

## Estado

Primera entrega del proyecto terminal: capítulos 1 a 3 (introducción, marco
teórico y metodología), revisados por el asesor. El ajuste de modelos, la
auditoría de equidad, la mitigación y la discusión de resultados corresponden a
las entregas siguientes.

Ver [CHANGELOG.md](CHANGELOG.md) para el historial de cambios.

## Licencia y uso de los datos

Los datos provienen de fuentes publicadas bajo los
[Términos de Libre Uso de la Información del Gobierno de México](https://datos.gob.mx/libreusomx)
y no contienen identificadores personales directos.
