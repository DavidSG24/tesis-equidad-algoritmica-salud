# Changelog

Todos los cambios relevantes de este proyecto se documentan en este archivo.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y el proyecto se adhiere a [Versionado Semántico](https://semver.org/lang/es/).

## [No publicado]

### Añadido

- Control de versiones del proyecto: `.gitignore`, `README.md` raíz y este
  `CHANGELOG.md`.

## [2.1.0] - 2026-09-28

Entrega 2B: presentación en video del avance del proyecto.

### Añadido

- Presentación en Beamer de 13 diapositivas (`entregas/presentacion_2b/`), con
  identidad visual propia y las figuras del análisis.
- Guión de locución en registro hablado, con marca de tiempo por diapositiva y
  punto de control de ritmo. Duración medida: 6:41 a ritmo normal, sobre un tope
  de 7 minutos.
- Versión alterna de 19 diapositivas, conservada por si cambia el límite de
  duración.

## [2.0.0] - 2026-09-25

Segunda entrega: marco metodológico y atención a las observaciones de la 1B.

### Añadido

- Capítulo 3 reescrito como marco metodológico completo sobre las seis fases de
  CRISP-DM, con una adaptación propia: la evaluación se desdobla en desempeño
  global y auditoría de equidad.
- Apartados nuevos de entendimiento del negocio (con criterios de éxito
  medibles), modelado, evaluación e implementación.
- Lista de cotejo que relaciona cada una de las 58 observaciones del asesor con
  la modificación realizada y su ubicación.
- Resaltado automático en amarillo de todo lo que cambió respecto de la versión
  revisada, por comparación contra el documento original.
- Ocho referencias nuevas del marco metodológico (CRISP-DM, KDD, remuestreo,
  curvas de precisión–exhaustividad y deuda técnica en aprendizaje automático).
- Generadores `contenido_2a.py`, `armar_entrega_2a.py` y `lista_cotejo_2a.py`.

### Modificado

- Terminología unificada en todo el documento: «cohorte» pasa a «conjunto de
  datos» y «canal» a «flujo de trabajo».

## [1.1.0] - 2026-09-23

Primera entrega (capítulos 1 a 3) corregida a partir de la revisión del asesor
del 21 de septiembre de 2026.

### Añadido

- Nota tras las hipótesis que distingue teoremas demostrados, hipótesis por
  contrastar y asociaciones observacionales preliminares.
- Delimitación explícita «Enfermedad y periodo» en el alcance: todo el trabajo
  empírico es COVID-19 sobre el corte 2021.
- Justificación de por qué los indicadores de ausencia no se usan como
  predictores, y la cuantificación de ese costo como trabajo futuro.
- Explicación del papel de la edad como variable de confusión de la disparidad
  geográfica, y aclaración de que el análisis en el subgrupo de 60 años o más es
  complementario y no sustituye al análisis principal.
- Dos formas adicionales de cuantificar el compromiso equidad–desempeño en H3,
  además de la frontera de Pareto.
- Definiciones de «desenlace grave», «auditoría de equidad», «casos COVID
  confirmados», «marginación», «validación externa», formato Parquet y el
  significado de las etiquetas P, OE y H.

### Modificado

- Moderadas las afirmaciones categóricas: «problema resuelto» y «saturado» pasan
  a «ampliamente estudiado»; «la primera auditoría» pasa a «no se identificaron
  trabajos en la literatura revisada».
- Reescrito el apartado 2.3.4 para enunciar el teorema de imposibilidad con sus
  dos condiciones y precisar la relación entre calibración, separación y regla de
  decisión.
- Reescrita la definición de frontera de Pareto (2.3.6) en pasos explícitos.
- Terminología: «cohorte» pasa a «conjunto de datos»; «canal» a «flujo de
  trabajo»; «proxy» a «medida indirecta»; criterios de equidad enunciados en
  español antes que en inglés.
- Separadores de miles con coma en todas las cifras.

### Eliminado

- Frases marcadas por el asesor: «El nivel de detalle es deliberado», «La
  restricción es deliberada y no un detalle de filtrado», «El tercer bloque es
  necesario, y no un refinamiento cosmético», entre otras.

## [1.0.0] - 2026-08-26

### Añadido

- Primera entrega del proyecto terminal: capítulos 1 a 3 en formato Word sobre la
  plantilla institucional de INFOTEC.
- Flujo de trabajo reproducible de ingesta y preparación de la base de la DGE,
  con control de fuga de información.
- Cuadernos de análisis 01 a 06: exploración, modelo de referencia, auditoría de
  equidad, mitigación y frontera de Pareto, transportabilidad e incertidumbre.
- Documento LaTeX de la tesis, protocolo, presentación y plan de trabajo.
