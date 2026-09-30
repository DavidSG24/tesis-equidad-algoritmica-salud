# -*- coding: utf-8 -*-
"""Genera la lista de cotejo de la entrega 2A.

Documento independiente que relaciona cada observacion recibida en la revision
de la entrega 1A con la modificacion realizada y su ubicacion en el documento.
"""
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

DEST = Path("/Users/davidsegundogarcia/Documents/entregas/2A_Lista_de_cotejo_David_Segundo.docx")

NARANJA = RGBColor(0xC0, 0x50, 0x4D)
GRIS = "D9D9D9"

# =============================================================================
#  Observaciones generales (correo del asesor, 21 de septiembre de 2026)
# =============================================================================
GENERALES = [
    ("G1",
     "Moderar las afirmaciones categóricas. Se usan expresiones muy rotundas: que "
     "el problema predictivo está «resuelto» o «saturado», o que sería el «primer» "
     "estudio de cierto tipo. Conviene formularlas de manera más prudente, por "
     "ejemplo «en la literatura revisada no se identificaron…» o «ha sido "
     "ampliamente estudiado…».",
     "Se revisaron todas las afirmaciones de ese tipo. «El problema predictivo ya "
     "está ampliamente resuelto» pasó a «ha sido ampliamente estudiada… los "
     "trabajos revisados reportan modelos con buen desempeño»; el título 2.2.1 "
     "«La parte predictiva mexicana está saturada» pasó a «La predicción de "
     "desenlaces por COVID-19 en México ha sido ampliamente estudiada»; «La "
     "primera auditoría de equidad geográfica» pasó a «Una auditoría… En la "
     "literatura revisada no se identificaron trabajos que aborden esa "
     "combinación». Se ajustaron en el mismo sentido el resumen, la justificación, "
     "las conclusiones y la tabla 1."),
    ("G2",
     "Usar un lenguaje un poco más directo y técnico. En algunos párrafos la "
     "redacción se vuelve demasiado elaborada y puede hacer menos clara una idea "
     "que en realidad es bastante concreta.",
     "Se eliminaron las construcciones retóricas señaladas («El nivel de detalle es "
     "deliberado», «La restricción es deliberada y no un detalle de filtrado», «El "
     "tercer bloque es necesario, y no un refinamiento cosmético», «que de otro "
     "modo parecerían excesivamente conservadoras») y se reescribieron los pasajes "
     "correspondientes en forma directa."),
    ("G3",
     "Revisar con cuidado la relación entre calibración, equalized odds y el "
     "teorema de imposibilidad.",
     "Se reescribió por completo el apartado 2.3.4. El teorema se enuncia ahora con "
     "sus dos condiciones explícitas —prevalencias distintas entre grupos y "
     "clasificador imperfecto— y se precisa la relación entre los tres conceptos: "
     "la calibración es una propiedad del puntaje, mientras que la sensibilidad y "
     "la tasa de falsos positivos son propiedades de la regla de decisión, de modo "
     "que fijar un umbral por entidad no altera la calibración del puntaje "
     "subyacente. Es esa propiedad la que explota la mitigación por "
     "post-procesamiento."),
    ("G4",
     "Distinguir claramente qué resultados ya están demostrados, cuáles son "
     "asociaciones preliminares y cuáles siguen siendo hipótesis.",
     "Se añadió una nota tras el apartado 1.4 que separa los tres estatus: los "
     "resultados de imposibilidad del apartado 2.3.4 son teoremas demostrados, que "
     "se aplican por deducción y no dependen de la evidencia empírica; H1, H2 y H3 "
     "son conjeturas que el capítulo 3 contrasta —H2 no se sostuvo— mientras que H4 "
     "queda pendiente de la validación externa; y la asociación entre disparidad y "
     "marginación es una asociación observacional entre 32 unidades agregadas, sin "
     "pretensión causal. La distinción se refuerza en los apartados 1.7, 3.6.3 y "
     "3.6.5 y en las conclusiones."),
]

# =============================================================================
#  Observaciones puntuales marcadas en el documento
# =============================================================================
PUNTUALES = [
    # ---- Presentación -------------------------------------------------------
    ("1", "Presentación",
     "«estimen tempranamente el riesgo» — texto tachado.",
     "Se sustituyó por «estimen con anticipación el riesgo», en la presentación y "
     "en el apartado 1.1."),
    ("2", "Presentación / 1.1",
     "«sin sacrificar de forma inaceptable la utilidad clínica» — «de forma "
     "inaceptable» tachado.",
     "Se eliminó la expresión. La frase quedó como «sin sacrificar la utilidad "
     "clínica del modelo»."),
    ("3", "Presentación",
     "«El capítulo 1 es la introducción» — corrección a «se presenta».",
     "Se reescribió como «En el capítulo 1 se presenta la introducción»."),
    ("4", "Presentación",
     "«auditoría de equidad» subrayado: definir mejor el término.",
     "Se añadió la definición en el punto de primera aparición: «la evaluación del "
     "desempeño del modelo calculado por separado en cada grupo de población, con "
     "el fin de detectar diferencias sistemáticas entre grupos»."),
    ("5", "Presentación",
     "«Un criterio recorre todo el documento y conviene enunciarlo desde el "
     "principio» — tachado, sugerencia «considerado en».",
     "Se reescribió como «Un criterio considerado en todo el documento conviene "
     "enunciarlo aquí»."),
    # ---- Capítulo 1 ---------------------------------------------------------
    ("6", "1.1",
     "«el riesgo de un desenlace grave» subrayado, con la marca «¿sí?».",
     "Se precisó el término: «un desenlace grave —entendido aquí como la defunción "
     "del paciente registrada en la propia base—»."),
    ("7", "1.1",
     "«el problema puramente predictivo ya está ampliamente resuelto» subrayado, "
     "con las marcas «¿sí?» y «solo es COVID».",
     "Se moderó la afirmación y se acotó el dominio: «En el caso mexicano, y en el "
     "dominio específico de COVID-19, la tarea predictiva ha sido ampliamente "
     "estudiada: los trabajos revisados reportan modelos con buen desempeño»."),
    ("8", "1.1",
     "«El problema no abordado es otro.» — tachado, sugerencia «Sin embargo, un…».",
     "Se eliminó la frase y el párrafo abre ahora con «Sin embargo, un modelo puede "
     "tener excelente desempeño promedio…»."),
    ("9", "1.1",
     "«diagnosticar y corregir la inequidad del modelo» subrayado: «¿cómo "
     "diagnosticas un modelo predictivo?».",
     "Se reformuló como «medir la inequidad del modelo y corregirla» y se añadió un "
     "pasaje que explica en qué consiste cada operación: medir es calcular las "
     "métricas por separado en cada grupo y compararlas; corregir es intervenir "
     "sobre los datos, el entrenamiento o la regla de decisión."),
    ("10", "1.1",
     "«cuestión ya resuelta en este dominio» subrayado: «¿sí? solo dos referencias "
     "en el caso de COVID».",
     "Se moderó a «cuestión ampliamente tratada en este dominio»."),
    ("11", "1.1.1",
     "«el gasto sanitario, estaba ya distorsionado por el acceso desigual a los "
     "servicios» subrayado.",
     "Se reescribió el mecanismo paso a paso: el modelo predecía el gasto futuro y "
     "lo usaba como medida de necesidad; los pacientes afroamericanos accedían "
     "menos a los servicios y generaban menos gasto con la misma enfermedad; el "
     "desenlace medía entonces el acceso tanto como la necesidad."),
    ("12", "1.2",
     "«etiquetas explícitas —P, OE, H—»: «de una vez, por qué significan».",
     "Se explicitó el significado: «P para cada pregunta de investigación, OE para "
     "cada objetivo específico y H para cada hipótesis»."),
    ("13", "1.2",
     "P1: «sobre datos mexicanos» tachado, sugerencia «en general».",
     "Se eliminó la restricción. P1 quedó: «Dado un modelo de riesgo con buen "
     "desempeño global, ¿existen disparidades de desempeño entre entidades "
     "federativas, grupos etarios y sexos?»."),
    ("14", "1.2",
     "P2: «plantéala mejor».",
     "Se reformuló de modo que la relación quede contrastable: «Si esas "
     "disparidades existen, ¿la magnitud de la disparidad de cada entidad se "
     "asocia con su grado de marginación? Es decir, ¿el modelo se desempeña peor "
     "en las entidades más marginadas, y con qué fuerza y en qué dirección se da "
     "esa asociación?»."),
    ("15", "1.2",
     "P4: «plantéala mejor».",
     "Se reformuló: «¿El desempeño y la equidad del modelo se conservan al "
     "aplicarlo a una fuente de datos distinta de aquella con la que fue "
     "entrenado, o es necesario recalibrarlo para cada contexto?»."),
    ("16", "1.3",
     "«Desarrollar, auditar y mitigar la equidad»: «auditar» subrayado.",
     "Se reescribió el objetivo general incorporando la definición de la operación: "
     "«auditar su equidad —esto es, evaluar su desempeño por separado en cada grupo "
     "de población para detectar diferencias sistemáticas, con énfasis en el sesgo "
     "geográfico entre entidades federativas— y mitigar las disparidades "
     "encontradas»."),
    ("17", "1.3 y siguientes",
     "«canal reproducible» — «canal» tachado, sugerencia «flujo de trabajo u otro "
     "término».",
     "Se sustituyó «canal» por «flujo de trabajo» en todas las apariciones del "
     "documento: OE1, OE4, las contribuciones esperadas y los apartados del "
     "capítulo 3 donde se describe el proceso."),
    ("18", "1.4",
     "H1: «equalized odds» — «ponlo en español».",
     "Se enunció en español con el término inglés como referencia secundaria: "
     "«medibles mediante la igualdad de probabilidades de acierto y error entre "
     "grupos (criterio conocido en la literatura como equalized odds)». El mismo "
     "criterio se aplicó en el apartado 2.3.3, en la tabla de métricas y en el "
     "glosario."),
    ("19", "1.4",
     "H3: «¿no hay alguna otra manera adicional de cuantificar esto?».",
     "Se añadieron dos formas complementarias a la frontera de Pareto: la razón "
     "entre la reducción de la brecha de sensibilidad y la caída del AUROC, y la "
     "pérdida de exactitud balanceada en el punto de operación clínico."),
    ("20", "1.5",
     "«la cuantificación del optimismo que introduce» — «del optimismo» tachado.",
     "Se sustituyó por «la cuantificación del sesgo favorable que introduce»."),
    ("21", "1.6",
     "«es un vacío identificado en la revisión del capítulo 2, no una suposición» — "
     "tachado, sugerencia «ya que» o «debido a que».",
     "Se reescribió como «es un vacío identificado en la revisión del capítulo 2, "
     "ya que la búsqueda no arrojó trabajos que traten la entidad federativa como "
     "atributo sensible…»."),
    ("22", "1.6",
     "«Impacto en la decisión» y «Oportunidad regulatoria»: «hay que moderar un "
     "poco el discurso».",
     "Se retitularon como «Utilidad para la decisión» y «Pertinencia regulatoria», "
     "y se atenuó la redacción de ambos párrafos."),
    ("23", "1.7",
     "«Cohorte. Casos COVID confirmados…»: «¿o sea todo el trabajo se va a hacer "
     "con COVID? Si es así hay que ser más claro en eso».",
     "Se añadió una delimitación nueva al inicio del apartado, «Enfermedad y "
     "periodo», que declara que la totalidad del trabajo empírico se realiza sobre "
     "COVID-19 y únicamente sobre el corte anual 2021, y que el método es "
     "trasladable a otros padecimientos pero eso no se demuestra aquí."),
    ("24", "1.7",
     "«Validación externa»: «no se entiende».",
     "Se reescribió el apartado completo, empezando por definir la operación: "
     "«Validar externamente un modelo es aplicarlo, sin reentrenarlo, a datos "
     "provenientes de una fuente distinta de aquella con la que se ajustó», y "
     "explicando por qué la generalización entre entidades dentro de la misma "
     "fuente es un ejercicio más débil que no la sustituye."),
    ("25", "1.7",
     "«el proxy más directo del mecanismo» — «usa otra palabra».",
     "Se sustituyó por «la medida más directa del mecanismo». La otra aparición del "
     "término, en el apartado 2.1.2, se reescribió como «se usaba como medida "
     "indirecta de la necesidad de atención»."),
    # ---- Capítulo 2 ---------------------------------------------------------
    ("26", "2.1",
     "«la equidad algorítmica en salud» — «algorítmica» tachado; «El problema de "
     "esta tesis vive precisamente en la intersección que ninguna de las tres ha "
     "ocupado» — tachado, sugerencia «pertenece o está en el ámbito».",
     "Se reescribió como «la equidad en salud desarrollada en otros países. El "
     "problema de esta tesis pertenece al ámbito en el que esas tres tradiciones se "
     "cruzan, y en la literatura revisada no se identificaron trabajos situados en "
     "él»."),
    ("27", "2.1.2",
     "«era un proxy contaminado por el acceso desigual» — «un proxy» tachado.",
     "Se reescribió como «se usaba como medida indirecta de la necesidad de "
     "atención, pero reflejaba también el acceso desigual a los servicios»."),
    ("28", "2.1.2",
     "«que de otro modo parecerían excesivamente conservadoras» — tachado.",
     "Se eliminó la frase."),
    ("29", "2.1.3",
     "«aprendizaje automático justo» — «justo» tachado.",
     "Se sustituyó por «aprendizaje automático con criterios de equidad»."),
    ("30", "2.2",
     "«delimitan el vacío que este trabajo ocupa» subrayado: «hay que moderarse en "
     "estos comentarios».",
     "Se reescribió como «delimitan el espacio en el que se sitúa este trabajo»."),
    ("31", "2.2.1",
     "«evidencia más fuerte de saturación» — «saturación» marcada con «?».",
     "Se cambió el título del apartado y se moderó la conclusión: «Esa coincidencia "
     "sugiere que el margen de mejora de la tarea puramente predictiva sobre esta "
     "fuente ya no está principalmente en la elección del algoritmo», añadiendo que "
     "la afirmación se apoya en un número reducido de trabajos y debe tomarse como "
     "una lectura de la literatura disponible."),
    ("32", "2.2.3",
     "«revela dos vacíos, no uno» — «no uno» tachado.",
     "Se eliminó. La frase quedó «El contraste con esta literatura revela dos "
     "vacíos»."),
    ("33", "2.2.3",
     "«tienden a perseguir ruido» — «perseguir» corregido; «Este trabajo opera en "
     "ese régimen, poco explorado» subrayado: «moderación».",
     "Se sustituyó por «tienden a ajustarse al ruido de la muestra» y se moderó la "
     "afirmación final: «sobre el que la literatura revisada ofrece menos evidencia "
     "que sobre el caso de dos o tres grupos comparables»."),
    ("34", "2.3.1",
     "«La discriminación mide la capacidad de ordenar pacientes por riesgo y se "
     "resume en el AUROC» — marca «?»; «Es insensible a transformaciones monótonas "
     "del puntaje» subrayado.",
     "Se dividió la oración y se explicó el concepto con un ejemplo: «Esta métrica "
     "depende solo del orden de los puntajes y no de su valor: si a todos los "
     "pacientes se les multiplicara el puntaje por diez, o se les aplicara "
     "cualquier otra transformación que respete el orden —lo que se denomina una "
     "transformación monótona—, el AUROC no cambiaría»."),
    ("35", "2.3.2",
     "«agrupan los valores de cada variable en cubetas» — «cubetas» subrayado; "
     "«reponderando» marcado.",
     "Se sustituyó por «agrupan los valores de cada variable en un número fijo de "
     "intervalos antes de buscar los puntos de corte del árbol» y «ponderando la "
     "función de pérdida, de modo que cada caso con desenlace positivo pese más "
     "que cada caso negativo»."),
    ("36", "2.3.3",
     "«Equalized odds (separación)» — corrección: poner «Separación» primero.",
     "Se reordenaron los tres criterios con el nombre en español al frente: "
     "«Independencia, o paridad demográfica», «Separación, o igualdad de "
     "probabilidades de acierto y error (en la literatura en inglés, equalized "
     "odds)» y «Suficiencia, o calibración por grupo»."),
    ("37", "2.3.6",
     "Definición de la frontera de Pareto subrayada: «no se entiende».",
     "Se reescribió en pasos explícitos: cada política produce un par de valores "
     "(disparidad, desempeño); al representarlas todas en un plano, muchas quedan "
     "descartadas porque existe otra mejor en ambos ejes; la frontera es el "
     "conjunto de las que sobreviven, y elegir entre ellas es una decisión de "
     "política y no técnica."),
    ("38", "2.4.3",
     "«no se delegan a una biblioteca» — añadir «computacional».",
     "Se sustituyó por «no se delegan a una biblioteca computacional de terceros»."),
    # ---- Capítulo 3 ---------------------------------------------------------
    ("39", "Capítulo 3",
     "«El nivel de detalle es deliberado.» — tachado.",
     "Se eliminó la frase del párrafo introductorio del capítulo."),
    ("40", "3.3.1 (antes 3.1.1)",
     "«índice de marginación» subrayado: definir.",
     "Se añadió la definición de CONAPO y la construcción del índice: «la carencia "
     "de oportunidades y de acceso a bienes y servicios básicos de una población; "
     "el índice la resume en una sola cifra por entidad a partir de indicadores de "
     "educación, vivienda, ingreso y distribución de la población»."),
    ("41", "Todo el documento",
     "Separadores de miles: «8 830 345» corregido con comas.",
     "Se aplicó el separador de coma a todas las cifras del documento: 8,830,345; "
     "2,526,649; 1,515,988; 631,663; 378,998; 297,685; 141,499; 15,221 y 651,956."),
    ("42", "3.3.3 (antes 3.1.2)",
     "«casos COVID confirmados» — «¿qué significa?».",
     "Se añadió la definición operacional completa, con los tres valores de "
     "CLASIFICACION_FINAL: 1, confirmado por asociación epidemiológica; 2, por "
     "dictaminación de un comité; 3, por prueba de laboratorio. Se indica además "
     "qué casos quedan excluidos."),
    ("43", "3.3.3",
     "«La restricción es deliberada y no un detalle de filtrado.» — tachado.",
     "Se eliminó la frase."),
    ("44", "3.3.3 (antes 3.1.3)",
     "EDAD: «los valores fuera del intervalo [0, 120] se marcan como faltantes» — "
     "«¿se eliminan?».",
     "Se aclaró que el registro no se elimina: «se consideran errores de captura y "
     "se sustituyen por un valor faltante; el registro no se elimina, porque el "
     "resto de sus variables sigue siendo válido y el modelo maneja los faltantes "
     "de forma nativa. Esta situación afecta al 0.0013 % del conjunto de datos»."),
    ("45", "3.3.3",
     "grupo_edad: «con cortes en 0–17, 18–39…» — sugerencia «intervalos».",
     "Se sustituyó por «Variable categórica con cuatro intervalos: 0–17, 18–39, "
     "40–59 y 60 o más años»."),
    ("46", "3.3.3",
     "«formato Parquet» subrayado con «?».",
     "Se añadió la explicación del formato: «un formato de archivo de código "
     "abierto que guarda las tablas por columnas en lugar de por filas, lo que "
     "reduce el tamaño en disco y acelera la lectura selectiva de variables en "
     "conjuntos de millones de registros»."),
    ("47", "3.4 (antes 3.2)",
     "«cómo se reparte la cohorte entre ajuste y evaluación» — «¿validación y "
     "prueba?», «conjunto de datos de entrenamiento».",
     "Se explicitaron los tres bloques: «cómo se reparte el conjunto de datos entre "
     "los bloques de entrenamiento, calibración y prueba», con remisión al "
     "apartado que los detalla."),
    ("48", "3.4.3 (antes 3.2.3)",
     "«El tercer bloque es necesario, y no un refinamiento cosmético.» — tachado; "
     "«parámetros ajustados a datos» — sugerencia «basados en los datos».",
     "Se eliminó la primera frase y se reescribió la segunda como «parámetros "
     "estimados a partir de los datos»."),
    ("49", "3.3.4 (antes 3.3.1)",
     "«un factor cercano a 280» — marca «¿%?».",
     "Se aclaró la naturaleza de la cifra: «No se trata de una diferencia de 280 "
     "puntos porcentuales, sino de una razón entre ambas proporciones: la entidad "
     "con peor registro tiene una proporción de faltantes cerca de 280 veces mayor "
     "que la de mejor registro»."),
    ("50", "3.3.4",
     "«los indicadores de ausencia no se usan como predictores» subrayado: «¿por "
     "qué? Tal vez valdría la pena hacerlo, o justificar mejor por qué no».",
     "Se añadió un párrafo completo de justificación: usarlos mejoraría el "
     "desempeño, pero se sostendría sobre una variable que describe a la unidad "
     "que registra y no al paciente, que es el mecanismo de sesgo de Obermeyer et "
     "al. (2019) y el objeto mismo de estudio; además dependen de prácticas "
     "administrativas locales inestables. Se deja como trabajo futuro cuantificar "
     "el desempeño cedido mediante un modelo alterno que sí los incluya."),
    ("51", "Todo el documento",
     "«cohorte» — sugerencia de sustituirlo por «grupo / conjunto de datos».",
     "Se sustituyó el término en la totalidad del documento: cuerpo, títulos de "
     "apartado, pies de figura y tabla, índices, glosario y celdas de tabla. El "
     "apartado que antes se titulaba «Construcción de la cohorte y definición del "
     "desenlace» es ahora el 3.3.3, «Construcción del conjunto de datos y "
     "definición del desenlace», y la entrada del glosario pasó a «Conjunto de "
     "datos de análisis»."),
    ("52", "3.3.5 (antes 3.3.3)",
     "«obliga a reponderar la función de pérdida» — marcado.",
     "Se sustituyó por «obliga a ponderar la función de pérdida —asignando más peso "
     "a los casos con desenlace positivo, que son minoría—»."),
    ("53", "3.3.5",
     "«parte de cualquier disparidad geográfica observada podría no ser geográfica "
     "en absoluto» subrayado con «?».",
     "Se explicó el problema de confusión con un ejemplo: si el modelo se desempeña "
     "peor en las entidades con más adultos mayores, el resultado admite dos "
     "lecturas —que falla en esas entidades o que falla en los adultos mayores "
     "estén donde estén— y los datos agregados por entidad no permiten separarlas. "
     "Se nombró explícitamente a la edad como variable de confusión."),
    ("54", "3.3.5",
     "«la restricción del análisis al subgrupo de 60 años o más»: «¿o sea solo te "
     "quedas con edad ≤ 59? ¿No es quitar mucha información?».",
     "Se aclaró el sentido de la comprobación, que es el contrario al que sugiere "
     "la nota: se conserva a los pacientes de 60 años o más, no se descartan. Se "
     "subrayó además que es un análisis complementario y no el principal —la "
     "auditoría se realiza sobre el conjunto completo— y que ese subgrupo "
     "concentra una parte sustancial de las defunciones (mortalidad de 25.6 % "
     "frente a 5.60 % global), de modo que se pierden registros pero muchos menos "
     "casos del desenlace que se quiere estimar."),
]

# =============================================================================
#  Desarrollo nuevo de la entrega 2A
# =============================================================================
NUEVO = [
    ("3.1", "Presentación de la metodología",
     "Enfoque cuantitativo, no experimental y retrospectivo. Justificación de "
     "CRISP-DM frente a SEMMA, KDD y TDSP, con sus ventajas y limitaciones. "
     "Adaptación del proceso: la fase de evaluación se desdobla en desempeño "
     "global y auditoría de equidad. Tabla 4 de correspondencia entre fases, "
     "apartados y artefactos."),
    ("3.2", "Entendimiento del negocio",
     "Contexto del problema y decisión que el modelo apoya. Traducción de los "
     "objetivos de negocio a objetivos de minería de datos con criterios de éxito "
     "medibles, fijados antes del modelado (tabla 5). Restricciones de "
     "información, recursos y uso, y riesgo principal identificado."),
    ("3.3", "Comprensión de los datos",
     "Fuentes de información, tipos de datos y estructura del registro, incluida "
     "la codificación de la ausencia. Construcción del conjunto de análisis, "
     "definición del desenlace, calidad del dato y heterogeneidad entre entidades."),
    ("3.4", "Preparación de los datos",
     "Control de fuga de información, limpieza y transformación —con la "
     "justificación de no imputar ni escalar— y partición en tres bloques."),
    ("3.5", "Modelado",
     "Técnicas y herramientas, con la justificación de la familia de algoritmos y "
     "los hiperparámetros documentados (tabla 7). Calibración isotónica del "
     "puntaje, punto de operación declarado y las tres familias de mitigación del "
     "sesgo."),
    ("3.6", "Evaluación",
     "Validación del desempeño global frente a los criterios de éxito; auditoría "
     "de equidad por entidad, sexo y grupo etario (tabla 8); cuantificación de la "
     "incertidumbre por remuestreo y permutación; comparación de las técnicas de "
     "mitigación y frontera de Pareto (tabla 9); y tres análisis de sensibilidad."),
    ("3.7", "Implementación",
     "Descripción de la solución propuesta en sus tres componentes, condiciones y "
     "restricciones de uso derivadas de los resultados, y requisitos de monitoreo, "
     "gobernanza y trabajo pendiente."),
]

BIBLIOGRAFIA_NUEVA = [
    "Chapman, P., et al. (2000). CRISP-DM 1.0: Step-by-step data mining guide.",
    "Efron, B., y Tibshirani, R. J. (1993). An introduction to the bootstrap.",
    "Fayyad, U., Piatetsky-Shapiro, G., y Smyth, P. (1996). From data mining to "
    "knowledge discovery in databases.",
    "Martínez-Plumed, F., et al. (2021). CRISP-DM twenty years later.",
    "Saito, T., y Rehmsmeier, M. (2015). The precision-recall plot is more "
    "informative than the ROC plot…",
    "Sculley, D., et al. (2015). Hidden technical debt in machine learning systems.",
    "Shearer, C. (2000). The CRISP-DM model: The new blueprint for data mining.",
    "Wirth, R., y Hipp, J. (2000). CRISP-DM: Towards a standard process model for "
    "data mining.",
]


# ---------------------------------------------------------------------------
#  Construccion del documento
# ---------------------------------------------------------------------------
doc = Document()
sec = doc.sections[0]
sec.top_margin = Cm(2.5)
sec.bottom_margin = Cm(2.5)
sec.left_margin = Cm(2.5)
sec.right_margin = Cm(2.5)

normal = doc.styles["Normal"]
normal.font.name = "Arial"
normal.font.size = Pt(11)


def _sombrear(celda, color):
    tcPr = celda._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), color)
    tcPr.append(shd)


def titulo(texto, size=16, color=NARANJA, space_before=0, space_after=10):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    r = p.add_run(texto)
    r.bold = True
    r.font.size = Pt(size)
    r.font.color.rgb = color
    r.font.name = "Arial"
    return p


def encabezado(texto):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(texto)
    r.bold = True
    r.font.size = Pt(12.5)
    r.font.color.rgb = NARANJA
    r.font.name = "Arial"
    return p


def parrafo(texto, size=11, italic=False, space_after=8):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    for i, chunk in enumerate(texto.split("**")):
        if not chunk:
            continue
        r = p.add_run(chunk)
        r.bold = (i % 2 == 1)
        r.italic = italic
        r.font.size = Pt(size)
        r.font.name = "Arial"
    return p


def tabla(encabezados, filas, anchos):
    t = doc.add_table(rows=1, cols=len(encabezados))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for j, (celda, txt) in enumerate(zip(t.rows[0].cells, encabezados)):
        _sombrear(celda, GRIS)
        celda.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = celda.paragraphs[0].add_run(txt)
        r.bold = True
        r.font.size = Pt(10)
        r.font.name = "Arial"
    for fila in filas:
        celdas = t.add_row().cells
        for j, txt in enumerate(fila):
            par = celdas[j].paragraphs[0]
            par.alignment = (WD_ALIGN_PARAGRAPH.CENTER if j == 0
                             else WD_ALIGN_PARAGRAPH.JUSTIFY)
            par.paragraph_format.space_after = Pt(2)
            r = par.add_run(txt)
            r.font.size = Pt(9.5)
            r.font.name = "Arial"
    for fila in t.rows:
        for celda, ancho in zip(fila.cells, anchos):
            celda.width = Cm(ancho)
    return t


# --- portada ---------------------------------------------------------------
titulo("LISTA DE COTEJO", 18, space_after=4)
titulo("2A. Proyecto integrador: desarrollo del marco metodológico y mejora del "
       "documento de tesis", 12.5, space_after=18)

datos = doc.add_table(rows=0, cols=2)
datos.style = "Table Grid"
for etiqueta, valor in [
        ("Alumno", "David Segundo García"),
        ("Asesor", "Dr. Daniel Alejandro Cervantes Cabrera"),
        ("Programa", "Maestría en Ciencia de Datos e Información — INFOTEC"),
        ("Asignatura", "Proyecto Terminal 2026-2, Unidad 2"),
        ("Entrega anterior", "1B. Análisis de antecedentes y marco teórico"),
        ("Revisión atendida", "Correo y anotaciones del asesor, 21 de septiembre de 2026"),
        ("Fecha de entrega", "25 de septiembre de 2026")]:
    celdas = datos.add_row().cells
    _sombrear(celdas[0], GRIS)
    r = celdas[0].paragraphs[0].add_run(etiqueta)
    r.bold = True
    r.font.size = Pt(10)
    r.font.name = "Arial"
    r2 = celdas[1].paragraphs[0].add_run(valor)
    r2.font.size = Pt(10)
    r2.font.name = "Arial"
    celdas[0].width = Cm(4.2)
    celdas[1].width = Cm(11.8)

# --- nota metodologica -----------------------------------------------------
encabezado("Cómo leer este documento")
parrafo(
    "Este documento relaciona cada observación recibida en la revisión de la "
    "entrega 1A con la modificación realizada y su ubicación en el documento de "
    "tesis. Se organiza en tres partes: las observaciones generales del correo "
    "del asesor, las observaciones puntuales marcadas en rojo sobre el documento, "
    "y el desarrollo nuevo que corresponde a esta entrega.")
parrafo(
    "**Todas las modificaciones aparecen resaltadas en color amarillo dentro del "
    "documento de tesis.** El resaltado se generó comparando de forma automática "
    "cada párrafo de la versión actual contra la versión que recibió el asesor, de "
    "modo que queda marcado todo lo que cambió y nada que no haya cambiado. El "
    "capítulo 3 aparece resaltado casi en su totalidad por ser desarrollo nuevo de "
    "esta entrega; los pocos párrafos sin resaltar son pasajes que se conservan sin "
    "cambio de la entrega anterior.")
parrafo(
    "La numeración de los apartados del capítulo 3 cambió respecto de la entrega "
    "anterior, porque el capítulo se reorganizó según las seis fases de CRISP-DM. "
    "Donde es pertinente, la tabla indica entre paréntesis la numeración antigua.")

# --- tabla 1: generales ----------------------------------------------------
encabezado("1. Observaciones generales del correo del asesor")
tabla(["#", "Observación recibida", "Modificación realizada"],
      [(n, obs, mod) for n, obs, mod in GENERALES],
      [1.2, 6.9, 7.9])

# --- tabla 2: puntuales ----------------------------------------------------
doc.add_page_break()
encabezado("2. Observaciones puntuales marcadas en el documento")
parrafo("Se atendieron las 54 observaciones señaladas en rojo. El criterio "
        "seguido fue el indicado por el asesor: el subrayado señala texto que "
        "debía definirse o precisarse mejor; el tachado, texto que debía "
        "reformularse o eliminarse.", space_after=10)
tabla(["#", "Apartado", "Observación recibida", "Modificación realizada"],
      [(n, ap, obs, mod) for n, ap, obs, mod in PUNTUALES],
      [1.0, 2.3, 6.1, 6.6])

# --- tabla 3: desarrollo nuevo ---------------------------------------------
doc.add_page_break()
encabezado("3. Desarrollo nuevo de esta entrega: el marco metodológico")
parrafo("El capítulo 3 se reorganizó por completo siguiendo las seis fases de "
        "CRISP-DM. El contenido de la entrega anterior —fuentes de información, "
        "construcción del conjunto de datos, preprocesamiento y análisis "
        "exploratorio— se conserva íntegro y queda integrado en las fases de "
        "comprensión y preparación de los datos.", space_after=10)
tabla(["Apartado", "Fase", "Contenido desarrollado"],
      [(ap, fase, cont) for ap, fase, cont in NUEVO],
      [1.8, 4.2, 10.0])

encabezado("4. Actualización de la bibliografía")
parrafo("Se conservan las veinte referencias de los capítulos anteriores y se "
        "incorporan ocho fuentes nuevas, empleadas en el marco metodológico. El "
        "total asciende a 28 referencias en formato APA 7.", space_after=10)
for r in BIBLIOGRAFIA_NUEVA:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Cm(1.0)
    p.paragraph_format.first_line_indent = Cm(-0.6)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.0
    run = p.add_run("•  " + r)
    run.font.size = Pt(10)
    run.font.name = "Arial"

doc.save(str(DEST))
print("OK ->", DEST)
print(f"observaciones generales: {len(GENERALES)} | puntuales: {len(PUNTUALES)} | "
      f"apartados nuevos: {len(NUEVO)} | referencias nuevas: {len(BIBLIOGRAFIA_NUEVA)}")
