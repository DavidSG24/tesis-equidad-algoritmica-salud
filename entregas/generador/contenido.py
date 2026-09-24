# -*- coding: utf-8 -*-
"""Contenido de la entrega 1B, adaptado de los fuentes LaTeX de la tesis.

Formato de bloques:
  ('h2', texto)        -> titulo de seccion  (1.1, 2.3, ...)
  ('h3', texto)        -> titulo de subseccion (1.1.1, ...)
  ('p',  texto)        -> parrafo de cuerpo; **negrita** admitida
  ('b',  texto)        -> vineta
  ('nota', texto)      -> parrafo destacado (sangrado, cursiva)
  ('fig', ruta, pie)   -> figura con pie numerado
  ('tab', pie, filas)  -> tabla con encabezado en filas[0]
  ('blank',)           -> parrafo vacio
"""

# =============================================================================
#  Portada
# =============================================================================
PORTADA = {
    "titulo": "Estratificación de riesgo clínico consciente de la equidad",
    "subtitulo": ("Auditoría y mitigación del sesgo geográfico entre entidades "
                  "federativas en modelos predictivos con datos abiertos de "
                  "salud de México"),
    "tipo": "(TESIS)",
    "alumno": "David Segundo García",
    "asesor": "Dr. Daniel Alejandro Cervantes Cabrera",
    "fecha": "agosto, 2026.",
}

# =============================================================================
#  Resumen
# =============================================================================
RESUMEN = [
    ('p', "La predicción de hospitalización y mortalidad por COVID-19 con datos "
          "mexicanos ha sido ampliamente estudiada, y los trabajos revisados convergen "
          "en niveles de desempeño similares. Esta tesis desplaza el objeto de estudio: "
          "no pregunta si un modelo "
          "acierta, sino **si acierta por igual**, con énfasis en el sesgo geográfico "
          "entre entidades federativas, una dimensión asociada a la desigualdad "
          "estructural del sistema de salud en México sobre la que la literatura "
          "revisada no arrojó trabajos previos."),
    ('p', "El trabajo se apoya en la base abierta de COVID-19 de la Dirección General "
          "de Epidemiología (DGE), restringida a casos confirmados del año 2021 "
          "(n = 2,526,649; mortalidad observada 5.60 %). Sobre ese conjunto de datos se construye "
          "un flujo de trabajo reproducible de ingesta, limpieza y preparación con "
          "control estricto "
          "de fuga de información, se entrena un modelo de referencia de mortalidad al "
          "primer contacto y se calibra mediante regresión isotónica sobre un bloque "
          "independiente. Ese modelo es el sujeto de una auditoría de equidad por "
          "entidad federativa, sexo y grupo etario, y de las tres familias de mitigación "
          "de sesgo —pre, in y post-procesamiento— evaluadas sobre un punto de operación "
          "clínico común de 80 % de sensibilidad."),
    ('p', "El presente documento corresponde a la primera entrega del proyecto terminal "
          "y reporta los tres primeros capítulos: la introducción, con el planteamiento "
          "del problema y el protocolo de investigación; el marco teórico "
          "—antecedentes, estado del arte, bases teóricas y marco conceptual—; y la "
          "metodología, con la construcción y caracterización de la base de datos. La "
          "contribución esperada es una auditoría de equidad geográfica de un "
          "modelo clínico sobre datos abiertos mexicanos —no identificada en la "
          "literatura revisada—, acompañada de una frontera de "
          "Pareto equidad–desempeño utilizable como instrumento de decisión antes del "
          "despliegue."),
    ('blank',),
    ('p', "**Palabras clave:** equidad algorítmica, sesgo geográfico, estratificación de "
          "riesgo, COVID-19, datos abiertos de salud, calibración, igualdad de "
          "probabilidades (equalized odds), frontera de Pareto."),
]

# =============================================================================
#  Presentacion (hoja preliminar de la plantilla; el capitulo 1 es la
#  Introduccion propiamente dicha, como en la tesis)
# =============================================================================
PRESENTACION = [
    ('p', "La saturación hospitalaria y la asignación de recursos escasos son retos "
          "persistentes del sistema de salud mexicano. Contar con herramientas que "
          "estimen con anticipación el riesgo de un desenlace grave —en este trabajo, "
          "la defunción del paciente— permite priorizar la "
          "atención y anticipar necesidades de camas y ventiladores. Para el caso "
          "mexicano, la predicción de desenlaces por COVID-19 a partir de la base "
          "abierta de la Secretaría de Salud ha sido ampliamente estudiada: los "
          "trabajos revisados reportan modelos con buen desempeño "
          "(Becerra-Sánchez et al., 2022; Méndez-Astudillo, 2024)."),
    ('p', "Sin embargo, un modelo puede tener excelente desempeño "
          "promedio y, al mismo tiempo, ser sistemáticamente menos preciso para "
          "habitantes de entidades con menor infraestructura, para personas mayores o "
          "para un sexo determinado. En un país tan heterogéneo como México, un modelo "
          "entrenado con datos dominados por entidades urbanas puede desempeñarse peor "
          "justo donde el sistema de salud es más débil, amplificando la inequidad en "
          "lugar de reducirla. Medir esa inequidad y corregirla "
          "—especialmente la geográfica— sin sacrificar la utilidad clínica del "
          "modelo es el problema central de este trabajo."),
    ('p', "Esta primera entrega comprende los tres primeros capítulos del proyecto "
          "terminal. En el **capítulo 1** se presenta la introducción: fija el "
          "planteamiento del "
          "problema y el protocolo de investigación —preguntas, objetivos e "
          "hipótesis—, la justificación, las contribuciones esperadas y los límites y "
          "alcances de lo que aquí se reporta. El **capítulo 2** desarrolla el marco "
          "teórico en cuatro apartados: los antecedentes del problema, el estado del "
          "arte con el análisis crítico de las investigaciones recientes, las bases "
          "teóricas que sustentan la auditoría de equidad —es decir, la evaluación del "
          "desempeño del modelo calculado por separado en cada grupo de población, con "
          "el fin de detectar diferencias sistemáticas entre grupos— y el marco "
          "conceptual con las "
          "definiciones operacionales que se emplean en el resto de la tesis. El "
          "**capítulo 3** documenta la metodología: las fuentes de información, la "
          "construcción del conjunto de datos de análisis, la definición de variables nuevas, "
          "el preprocesamiento con control de fuga de información y el análisis "
          "exploratorio que caracteriza la heterogeneidad entre entidades federativas."),
    ('p', "Un criterio considerado en todo el documento conviene enunciarlo "
          "aquí: la revisión crítica de modelos pronósticos de COVID-19 documentó "
          "que la mayoría presentaba alto riesgo de sesgo por selección del conjunto de datos, "
          "fuga de información y ausencia de validación (Wynants et al., 2020). Las "
          "decisiones de este trabajo —la restricción a casos confirmados, la exclusión "
          "explícita de variables posteriores al punto de predicción y la partición en "
          "tres bloques— se toman para no repetir esos defectos, y se documentan con el "
          "detalle que exigen las guías de reporte de modelos predictivos en salud "
          "(Collins et al., 2015)."),
]

# =============================================================================
#  Capitulo 1. Introduccion
# =============================================================================
CAP1 = [
    ('p', "Este capítulo introduce el proyecto terminal. Delimita el problema que se "
          "aborda, formula el protocolo de investigación que lo estructura —preguntas, "
          "objetivos e hipótesis—, argumenta su pertinencia, enuncia las contribuciones "
          "esperadas y fija con precisión los límites de lo que se reporta. El propósito "
          "del último apartado merece subrayarse: los límites no son concesiones "
          "retóricas, sino la condición para que los resultados de los capítulos "
          "siguientes se lean correctamente."),

    ('h2', "1.1 Planteamiento del problema"),
    ('p', "La saturación hospitalaria y la asignación de recursos escasos son retos "
          "persistentes del sistema de salud mexicano. Contar con herramientas que "
          "estimen con anticipación el riesgo de un desenlace grave —entendido aquí "
          "como la defunción del paciente registrada en la propia base— permite "
          "priorizar la "
          "atención y anticipar necesidades de camas y ventiladores. En el caso "
          "mexicano, y en el dominio específico de COVID-19, la tarea predictiva ha "
          "sido ampliamente estudiada: los trabajos revisados reportan modelos con "
          "buen desempeño (Becerra-Sánchez et al., 2022; Méndez-Astudillo, 2024)."),
    ('p', "Sin embargo, un modelo puede tener excelente desempeño "
          "promedio y, al mismo tiempo, ser sistemáticamente menos preciso para "
          "habitantes de entidades con menor infraestructura, para personas mayores o "
          "para un sexo determinado. Esa posibilidad no es hipotética, y el apartado "
          "siguiente documenta el caso de referencia."),
    ('p', "En un país tan heterogéneo como México, un modelo entrenado con datos "
          "dominados por entidades urbanas puede desempeñarse peor justo donde el "
          "sistema de salud es más débil, amplificando la inequidad en lugar de "
          "reducirla. El problema central de esta tesis es, por tanto, **medir la "
          "inequidad del modelo y corregirla —especialmente la geográfica— sin "
          "sacrificar su utilidad clínica**. Medir la inequidad de un modelo "
          "predictivo significa calcular sus métricas de desempeño por separado en "
          "cada grupo de población y comparar los valores obtenidos; corregirla "
          "significa intervenir sobre los datos, el entrenamiento o la regla de "
          "decisión para reducir la diferencia medida. El apartado 2.4 fija estas "
          "definiciones de forma operacional."),
    ('p', "La formulación importa porque el objeto de estudio se desplaza. No se "
          "pregunta si un modelo de riesgo acierta —cuestión ampliamente tratada en "
          "este dominio—, sino si acierta por igual entre grupos de población, y qué "
          "puede "
          "hacerse cuando no lo hace. Ese desplazamiento cambia el instrumento de "
          "evaluación: las métricas agregadas de desempeño resultan insuficientes y "
          "deben acompañarse de métricas de disparidad desagregadas por grupo."),

    ('h3', "1.1.1 El sesgo algorítmico en salud como problema documentado"),
    ('p', "El caso mejor documentado de sesgo algorítmico en salud es un modelo de "
          "gestión poblacional en Estados Unidos que asignaba menos recursos a "
          "pacientes afroamericanos con igual carga de enfermedad. El mecanismo es "
          "instructivo: el sesgo no provenía de usar la raza como predictor —el modelo "
          "no la usaba—, sino del desenlace elegido. El modelo predecía el gasto "
          "sanitario futuro y lo usaba como medida de necesidad de atención; ahora "
          "bien, los pacientes afroamericanos accedían menos a los servicios y, en "
          "consecuencia, generaban menos gasto con la misma enfermedad. El desenlace "
          "medía entonces el acceso tanto como la necesidad (Obermeyer et al., "
          "2019). Un modelo técnicamente correcto reprodujo así una desigualdad "
          "preexistente."),
    ('p', "La lección para este trabajo es directa y condiciona el diseño de los "
          "capítulos siguientes. Primero, la ausencia del atributo sensible entre los "
          "predictores no garantiza equidad; por eso la entidad federativa se excluye "
          "deliberadamente como variable de entrada y se reserva como eje de auditoría. "
          "Segundo, la inequidad puede estar inscrita en la definición del desenlace y "
          "en el proceso de captura del dato, no solo en el algoritmo; por eso el "
          "capítulo 3 documenta con detalle cómo se registran los datos y qué "
          "significan sus códigos de ausencia."),

    ('h2', "1.2 Preguntas de investigación"),
    ('p', "El protocolo de investigación articula el problema anterior en preguntas contrastables, "
          "objetivos verificables e hipótesis que pueden resultar falsas. Se enuncia "
          "con etiquetas explícitas —**P** para cada pregunta de investigación, **OE** "
          "para cada objetivo específico y **H** para cada hipótesis— porque los "
          "capítulos posteriores "
          "referencian cada elemento de forma individual al reportar en qué medida "
          "quedó atendido."),

    ('b', "**P1.** Dado un modelo de riesgo con buen desempeño global, "
          "¿existen disparidades de desempeño entre entidades federativas, "
          "grupos etarios y sexos?"),
    ('b', "**P2.** Si esas disparidades existen, ¿la magnitud de la disparidad de cada "
          "entidad se asocia con su grado de marginación? Es decir, ¿el modelo se "
          "desempeña peor en las entidades más marginadas, y con qué fuerza y en qué "
          "dirección se da esa asociación?"),
    ('b', "**P3.** ¿Qué técnicas de mitigación —pre, in y post-procesamiento— reducen "
          "mejor esas disparidades, y cuál es el costo en desempeño global expresado "
          "como frontera de Pareto?"),
    ('b', "**P4.** ¿El desempeño y la equidad del modelo se conservan al aplicarlo a "
          "una fuente de datos distinta de aquella con la que fue entrenado, o es "
          "necesario recalibrarlo para cada contexto?"),
    ('b', "**P5.** De forma exploratoria, ¿aparecen inequidades adicionales en subgrupos "
          "interseccionales, por ejemplo adultos mayores de entidades marginadas?"),

    ('h2', "1.3 Objetivos"),
    ('h3', "1.3.1 Objetivo general"),
    ('p', "Desarrollar un modelo de estratificación de riesgo clínico basado en datos "
          "abiertos de salud de México, auditar su equidad —esto es, evaluar su "
          "desempeño por separado en cada grupo de población para detectar diferencias "
          "sistemáticas, con énfasis en el sesgo geográfico entre entidades "
          "federativas— y mitigar las disparidades encontradas, "
          "valorando la transportabilidad de sus hallazgos."),
    ('h3', "1.3.2 Objetivos específicos"),
    ('b', "**OE1.** Construir un flujo de trabajo reproducible de ingesta, limpieza y "
          "preparación "
          "de la base de la DGE, con control estricto de fuga de información."),
    ('b', "**OE2.** Entrenar un modelo de riesgo de referencia con desempeño comparable "
          "al estado del arte, como sujeto del análisis de equidad."),
    ('b', "**OE3.** Auditar la equidad del modelo por entidad federativa, sexo y grupo "
          "etario, y examinar la asociación del sesgo geográfico con indicadores "
          "contextuales."),
    ('b', "**OE4.** Aplicar y comparar técnicas de mitigación en las tres etapas del "
          "flujo de trabajo, construyendo la frontera de Pareto entre equidad y "
          "desempeño."),
    ('b', "**OE5.** Explorar la equidad en subgrupos interseccionales y traducir los "
          "hallazgos a recomendaciones de despliegue."),

    ('h2', "1.4 Hipótesis"),
    ('b', "**H1.** Un modelo con buen desempeño global presentará disparidades de "
          "desempeño entre entidades federativas, medibles mediante la igualdad de "
          "probabilidades de acierto y error entre grupos (criterio conocido en la "
          "literatura como equalized odds) y la calibración por grupo."),
    ('b', "**H2.** La magnitud del sesgo geográfico se asociará negativamente con la "
          "infraestructura de salud de cada entidad: peor desempeño donde hay menos "
          "recursos."),
    ('b', "**H3.** Las técnicas de mitigación reducirán las disparidades con una pérdida "
          "de desempeño global inferior a un umbral predefinido. Ese compromiso se "
          "cuantifica de tres formas complementarias: la frontera de Pareto, que lo "
          "muestra completo; la razón entre la reducción de la brecha de sensibilidad "
          "y la caída del AUROC, que resume en un número cuánta equidad se gana por "
          "unidad de desempeño cedida; y la pérdida de exactitud balanceada en el "
          "punto de operación clínico, que expresa el costo en la escala de la "
          "decisión."),
    ('b', "**H4.** El desempeño se transferirá razonablemente a una fuente independiente, "
          "pero las disparidades podrían acentuarse, evidenciando la necesidad de "
          "recalibrado por contexto."),
    ('nota', "Conviene distinguir desde aquí tres tipos de afirmación que este documento "
             "maneja y que no tienen el mismo estatus. Los resultados de imposibilidad "
             "del apartado 2.3.4 son teoremas demostrados y se aplican a este conjunto de datos "
             "por deducción, no por evidencia empírica. Las cuatro hipótesis anteriores "
             "son conjeturas que las entregas siguientes deben contrastar y que pueden "
             "resultar falsas. Y la asociación entre disparidad y marginación que "
             "examina H2 será, en el mejor de los casos, una asociación observacional "
             "preliminar entre 32 unidades agregadas, sin pretensión causal."),

    ('h2', "1.5 Contribuciones esperadas"),
    ('b', "Una auditoría de equidad geográfica —entidad federativa como atributo "
          "sensible— de un modelo de riesgo clínico entrenado sobre datos abiertos "
          "mexicanos. En la literatura revisada no se identificaron trabajos que "
          "aborden esa combinación."),
    ('b', "Una comparación de las tres familias de mitigación bajo un punto de operación "
          "clínico común, que permite documentar si alguna resulta sistemáticamente "
          "superior cuando los grupos son numerosos y de tamaño muy desigual."),
    ('b', "Una frontera de Pareto equidad–desempeño construida con umbrales estimados "
          "fuera de muestra, y la cuantificación del sesgo favorable que introduce "
          "estimarlos en el propio conjunto de prueba."),
    ('b', "Un flujo de trabajo reproducible con contrato de datos explícito entre "
          "etapas, que "
          "verifica procedencia, esquema y criterios de inclusión antes de consumir "
          "cualquier "
          "artefacto intermedio."),

    ('h2', "1.6 Justificación"),
    ('p', "La relevancia del proyecto se sostiene en cinco pilares."),
    ('p', "**Viabilidad de los datos.** La base de la DGE es pública, masiva y con "
          "desenlace claro, lo que permite comenzar de inmediato sin trámites de acceso "
          "ni convenios institucionales. Es una ventaja poco frecuente en investigación "
          "con datos clínicos y elimina el riesgo más común de este tipo de proyecto: "
          "quedarse sin datos."),
    ('p', "**Pertinencia nacional.** Al usar datos del propio sistema de salud mexicano "
          "y tratar la entidad federativa como eje, los hallazgos son directamente "
          "transferibles a la política de salud del país. La organización federal de "
          "los servicios de salud hace que «entidad» no sea una variable demográfica "
          "cualquiera, sino la unidad en la que efectivamente se decide y se financia "
          "la atención."),
    ('p', "**Originalidad documentada.** La equidad geográfica de modelos clínicos sobre "
          "datos mexicanos es un vacío identificado en la revisión del capítulo 2, ya "
          "que la búsqueda no arrojó trabajos que traten la entidad "
          "federativa como atributo sensible en una auditoría de equidad algorítmica."),
    ('p', "**Utilidad para la decisión.** Una frontera de Pareto equidad–desempeño es un "
          "insumo concreto para quien deba autorizar el despliegue de un modelo, "
          "porque presenta un conjunto de "
          "políticas explícitas, cada una con su costo medido, en lugar de una sola "
          "configuración. La elección entre ellas "
          "es normativa, y el entregable la hace visible."),
    ('p', "**Pertinencia regulatoria.** La discusión sobre uso responsable de "
          "inteligencia artificial en el sector público mexicano está en curso. Un "
          "estudio que documente cómo auditar un modelo de salud antes de desplegarlo, "
          "con datos nacionales y método reproducible, puede ser útil como referencia "
          "metodológica además de por sus resultados."),

    ('h3', "1.6.1 Aporte al perfil del programa"),
    ('p', "El trabajo se ubica en el núcleo de la Maestría en Ciencia de Datos e "
          "Información: integra ingesta y preparación de datos masivos, modelado "
          "supervisado, evaluación estadística rigurosa y traducción de resultados a "
          "decisiones. Requiere además una competencia que el programa enfatiza y que "
          "este proyecto ejercita de forma explícita: la capacidad de auditar "
          "críticamente un sistema analítico, incluido el propio."),

    ('h2', "1.7 Alcance y delimitaciones"),
    ('p', "Para que la lectura de los resultados sea correcta conviene fijar con "
          "precisión sus límites. Los siguientes acotan el alcance de lo que este "
          "trabajo puede afirmar."),
    ('b', "**Enfermedad y periodo.** La totalidad del trabajo empírico se realiza sobre "
          "COVID-19, y únicamente sobre el corte anual 2021 de la base de la DGE. No "
          "se emplea la serie histórica completa de la pandemia ni ninguna otra "
          "enfermedad. Los hallazgos son, por tanto, hallazgos sobre un modelo de "
          "mortalidad por COVID-19 en 2021; el método de auditoría es trasladable a "
          "otros padecimientos, pero eso queda fuera de lo que aquí se demuestra."),
    ('b', "**Conjunto de datos.** Casos COVID confirmados, es decir, los registros con resultado "
          "de laboratorio, dictaminación o asociación epidemiológica positiva "
          "(CLASIFICACION_FINAL ∈ {1, 2, 3}); n = 2,526,649. Quedan fuera los casos "
          "negativos, los sospechosos y los no concluyentes."),
    ('b', "**Desenlace.** Mortalidad; es decir, la variable que el modelo estima es la "
          "probabilidad de que el paciente fallezca. La hospitalización se deriva y se "
          "describe en el "
          "análisis exploratorio, pero no se modela en este documento. En este conjunto de datos "
          "fallecer implica estar registrado como hospitalizado, de modo que el "
          "desenlace solo es posible en el 11.8 % de los casos; el capítulo 3 documenta "
          "esa propiedad estructural y el análisis de sensibilidad previsto examina sus "
          "consecuencias."),
    ('b', "**Validación externa.** Validar externamente un modelo es aplicarlo, sin "
          "reentrenarlo, a datos provenientes de una fuente distinta de aquella con la "
          "que se ajustó. La fuente prevista para ello es la base de Egresos "
          "Hospitalarios de la DGIS (Dirección General de Información en Salud, 2024) "
          "y es la que permitiría contrastar H4. Ese ejercicio no se ha realizado, de "
          "modo que H4 se reporta como trabajo pendiente. Lo que sí se evalúa en esta "
          "tesis es la generalización entre entidades federativas dentro de la misma "
          "fuente: un ejercicio más débil, porque el formato de captura y los criterios "
          "de registro son comunes a todas las entidades, y que por tanto no sustituye "
          "a la validación externa."),
    ('b', "**Indicadores contextuales.** El examen de H2 se apoya en el índice de "
          "marginación por entidad de CONAPO 2020 (Consejo Nacional de Población, "
          "2021), que es un agregado socioeconómico estatal. No se emplearon "
          "indicadores de infraestructura de salud por unidad médica, que serían la "
          "medida más directa del mecanismo que H2 postula. La asociación que se "
          "reporte será, por tanto, preliminar."),
    ('b', "**Interpretabilidad.** Se emplea importancia por permutación. No se "
          "calcularon valores SHAP ni análisis de curva de decisión (Vickers y Elkin, "
          "2006)."),
    ('b', "**Alcance de esta entrega.** El presente documento cubre el marco general, "
          "la base de datos y el marco teórico. El ajuste de modelos, la auditoría de "
          "equidad, la mitigación y la discusión de resultados corresponden a las "
          "entregas siguientes del proyecto terminal."),
    ('nota', "Los límites anteriores no son concesiones retóricas. Cualquier afirmación "
             "de esta tesis que dependa de H4 o de intervalos de confianza se marca "
             "como preliminar en el punto donde aparece."),
]

# =============================================================================
#  Capitulo 3. Metodologia
# =============================================================================
CAP_METODO = [
    ('p', "Este capítulo documenta la metodología del trabajo empírico, y en particular "
          "la base de datos sobre la que se sostiene: de dónde provienen los datos, "
          "cómo se construyó el conjunto de datos de análisis, qué variables se derivaron, qué "
          "transformaciones se aplicaron y qué muestra su exploración. En un trabajo "
          "cuyo objeto es auditar la equidad de un modelo, el proceso de captura del "
          "dato no es un preliminar técnico: es una fuente candidata de la inequidad "
          "que se pretende medir."),

    ('h2', "3.1 Origen de los datos y construcción del conjunto de análisis"),
    ('p', "La construcción de la base persigue un requisito por encima de los demás: "
          "que el conjunto final contenga únicamente información disponible en el "
          "momento en que se tomaría la decisión clínica que el modelo pretende apoyar. "
          "Todo lo demás —volumen, riqueza de variables, comodidad de formato— está "
          "subordinado a ese requisito."),

    ('h3', "3.1.1 Fuentes de información"),
    ('p', "La **fuente primaria** es la base abierta de COVID-19 de la Dirección "
          "General de Epidemiología (DGE) de la Secretaría de Salud (Dirección General "
          "de Epidemiología, 2022). Se emplea el corte anual COVID19MEXICO2021.csv, que "
          "contiene 8,830,345 registros de notificación del año 2021 con variables "
          "demográficas, entidad de residencia, comorbilidades y desenlaces. Es una "
          "fuente de notificación epidemiológica de cobertura nacional, publicada bajo "
          "los Términos de Libre Uso de la Información del Gobierno de México, sin "
          "identificadores personales directos."),
    ('p', "Como **fuente de contexto** se emplea el índice de marginación por entidad "
          "federativa de CONAPO, edición 2020 (Consejo Nacional de Población, 2021). La "
          "marginación, en la definición de CONAPO, es la carencia de oportunidades y "
          "de acceso a bienes y servicios básicos de una población; el índice la resume "
          "en una sola cifra por entidad a partir de indicadores de educación, "
          "vivienda, ingreso y distribución de la población, y se construye con el "
          "método de distancias "
          "ponderadas al cuadrado sobre el Censo de Población y Vivienda 2020 del "
          "INEGI. Se usa el archivo por entidad "
          "IME_2020.xls, del que se toman el índice y el grado de marginación. Su papel "
          "es examinar la hipótesis H2, es decir, si la disparidad geográfica del modelo "
          "se asocia a la desigualdad estructural de la entidad."),
    ('p', "Como **fuente prevista para la validación externa** se identificó el "
          "Subsistema Automatizado de Egresos Hospitalarios de la DGIS (Dirección "
          "General de Información en Salud, 2024). Su explotación queda fuera del "
          "alcance de esta entrega y se reporta como trabajo pendiente."),

    ('h3', "3.1.2 Construcción del conjunto de datos y definición del desenlace"),
    ('p', "El conjunto de datos de análisis —los registros que cumplen los criterios "
          "de inclusión del estudio— se restringe a **casos COVID confirmados**. En el "
          "diccionario de datos de la DGE, un caso se considera confirmado cuando la "
          "variable CLASIFICACION_FINAL toma uno de tres valores: 1, confirmado por "
          "asociación epidemiológica; 2, confirmado por dictaminación de un comité; y "
          "3, confirmado por prueba de laboratorio. Se excluyen los casos sospechosos, "
          "los negativos y los no concluyentes. El filtro "
          "produce n = 2,526,649 registros "
          "con una mortalidad observada de 5.60 % y una tasa de hospitalización de "
          "11.78 %."),
    ('p', "Un modelo de "
          "mortalidad **por COVID** debe estimarse sobre enfermos de COVID. Incluir "
          "casos negativos y sospechosos mezcla poblaciones con mecanismos de riesgo "
          "distintos y diluye la señal: la prevalencia del desenlace cae entonces a "
          "2.06 % y el modelo pasa a describir mortalidad en población tamizada, que es "
          "otra pregunta. La diferencia entre 5.60 % y 2.06 % separa dos poblaciones con "
          "riesgo basal muy distinto."),
    ('p', "El desenlace modelado es la **defunción**, derivada del campo FECHA_DEF: la "
          "base codifica 9999-99-99 para paciente vivo. En el conjunto de datos hay 141,499 "
          "defunciones registradas."),
    ('nota', "El conjunto de datos tiene una propiedad estructural que condiciona toda lectura "
             "posterior y conviene declarar aquí. Entre los casos confirmados, el número "
             "de defunciones registradas como ambulatorias es cero: fallecer implica "
             "estar registrado como hospitalizado. El desenlace solo es posible, por "
             "tanto, en el 11.8 % del conjunto de datos (n = 297,685), y el resto son casos que "
             "no pueden fallecer por construcción. Esto no invalida la tarea —estimar "
             "riesgo al primer contacto sobre todo caso confirmado es precisamente el "
             "triage que motiva la tesis— pero significa que parte de la discriminación "
             "del modelo consistirá en separar ambulatorios de hospitalizados. El "
             "análisis de sensibilidad previsto cuantifica cuánta."),

    ('h3', "3.1.3 Creación y definición de nuevas variables"),
    ('p', "La base original codifica las categóricas con enteros y usa códigos "
          "especiales para la ausencia: 97 (no aplica), 98 (se ignora) y 99 (no "
          "especificado). El conjunto analítico se deriva del original mediante las "
          "siguientes construcciones."),
    ('b', "**defuncion.** Indicador binario derivado de FECHA_DEF (1 si existe fecha de "
          "defunción registrada). Es la variable objetivo."),
    ('b', "**hospitalizado.** Indicador binario derivado de TIPO_PACIENTE. Se usa para "
          "describir el conjunto de datos y para el análisis de sensibilidad, **nunca** como "
          "predictor de mortalidad."),
    ('b', "**EDAD.** Se conserva en años. Los valores fuera del intervalo [0, 120] se "
          "consideran errores de captura y se sustituyen por un valor faltante; el "
          "registro **no se elimina**, porque el resto de sus variables sigue siendo "
          "válido y el modelo maneja los faltantes de forma nativa. Esta situación "
          "afecta al 0.0013 % del conjunto de datos."),
    ('b', "**sexo_mujer.** Indicador binario (1 = mujer) derivado de SEXO, dejando "
          "faltante el código 99."),
    ('b', "**entidad_nombre.** ENTIDAD_RES se traduce a nombre mediante el catálogo "
          "oficial de 32 entidades; los códigos 97 a 99 quedan sin etiqueta. Esta es la "
          "variable que actúa como atributo sensible de la auditoría."),
    ('b', "**grupo_edad.** Variable categórica con cuatro intervalos: 0–17, 18–39, "
          "40–59 y 60 o "
          "más años. Se define una única vez para todo el flujo de trabajo, a fin de "
          "que los "
          "análisis por edad sean comparables entre etapas."),
    ('b', "**Once pares por comorbilidad.** Cada variable clínica —diabetes, EPOC, asma, "
          "inmunosupresión, hipertensión, otra comorbilidad, enfermedad cardiovascular, "
          "obesidad, enfermedad renal crónica, tabaquismo y neumonía— produce dos "
          "columnas: una binaria con sufijo _bin (1 = sí, 0 = no, faltante en otro caso) "
          "y un **indicador de faltante** con sufijo _na."),
    ('p', "La decisión de conservar la ausencia como información, en lugar de imputarla "
          "a ciegas, merece justificarse porque no es la práctica habitual. Su "
          "frecuencia difiere entre entidades y su presencia se asocia al desenlace, de "
          "modo que la ausencia es en sí misma un posible mecanismo de inequidad "
          "geográfica; el apartado 3.3 lo documenta con cifras. El conjunto resultante "
          "tiene 31 columnas y se almacena en formato Parquet —un formato de archivo "
          "de código abierto que guarda las tablas por columnas en lugar de por filas, "
          "lo que reduce el tamaño en disco y acelera la lectura selectiva de "
          "variables en conjuntos de millones de registros—, acompañado de un "
          "manifiesto que registra procedencia, número de filas, esquema, tasas "
          "observadas y versiones de biblioteca, de modo que ninguna etapa posterior "
          "consuma un artefacto sin verificar su origen."),

    ('h2', "3.2 Preprocesamiento de los datos"),
    ('p', "El preprocesamiento comprende tres decisiones: qué variables se admiten como "
          "predictores, cómo se tratan los valores especiales y cómo se reparte el "
          "conjunto de datos entre los bloques de entrenamiento, calibración y "
          "prueba. El apartado 3.2.3 detalla esa partición."),

    ('h3', "3.2.1 Control de fuga de información"),
    ('p', "El control de fuga de información es la decisión metodológica más importante "
          "del flujo de trabajo. El punto de predicción es el **primer contacto**, de "
          "modo que "
          "ninguna variable posterior a ese momento puede ser predictor. Se excluyen "
          "explícitamente:"),
    ('b', "**UCI** e **INTUBADO**, que describen el curso hospitalario y solo se conocen "
          "después de la decisión que el modelo pretende apoyar."),
    ('b', "**FECHA_DEF** y todo lo derivado de ella, salvo el desenlace mismo."),
    ('b', "**TIPO_PACIENTE** como predictor de mortalidad, por ser posterior al triage."),
    ('p', "Los predictores admitidos son, por tanto, la edad, el sexo y once "
          "comorbilidades o signos registrados al primer contacto. Los indicadores de "
          "ausencia se conservan en el conjunto para el análisis descriptivo, pero no "
          "se emplean como predictores. La entidad federativa tampoco se incluye entre "
          "las entradas: se reserva como atributo sensible para auditar."),
    ('nota', "La inclusión de NEUMONIA merece justificación aparte. En el formato de la "
             "DGE se captura en el primer contacto y no durante la evolución "
             "hospitalaria, por lo que es admisible en ese punto. Aun así resulta el "
             "predictor más informativo del modelo, de modo que la validez de esa "
             "captura es un supuesto del que dependen los resultados. El análisis de "
             "sensibilidad reentrena el modelo sin ella para acotar cuánto del "
             "desempeño y de la inequidad descansan en esa única variable."),

    ('h3', "3.2.2 Limpieza y recodificación"),
    ('p', "Sobre las variables derivadas en el apartado 3.1.3 se aplica un tratamiento "
          "uniforme: los códigos 97 a 99 se convierten en faltante explícito y quedan "
          "registrados en el indicador correspondiente; la edad se acota al intervalo "
          "plausible; y las categóricas se traducen a etiquetas legibles mediante los "
          "catálogos oficiales del diccionario de datos. No se aplica imputación. El "
          "modelo principal previsto maneja los valores faltantes de forma nativa, lo "
          "que evita introducir en los datos un supuesto que no se puede verificar."),

    ('h3', "3.2.3 Partición de datos"),
    ('p', "Se emplea una partición en tres bloques, estratificada por el desenlace y con "
          "semilla fija:"),
    ('b', "**Prueba** (25 %, n = 631,663). Se separa primero y no interviene en ninguna "
          "decisión de ajuste. Sobre él se calculan todas las métricas que se "
          "reportan."),
    ('b', "**Calibración** (20 % del resto, n = 378,998). Se usa exclusivamente para "
          "ajustar la transformación de calibración y los umbrales por grupo de la "
          "mitigación por post-procesamiento."),
    ('b', "**Entrenamiento** (el remanente, n = 1,515,988). Ajuste de los modelos."),
    ('p', "Tanto la "
          "calibración como los umbrales por entidad son parámetros estimados a partir "
          "de los datos; "
          "si se estiman sobre el conjunto de prueba, las métricas resultantes están "
          "sesgadas a favor del modelo. Separar el bloque de calibración es lo que "
          "permite "
          "después cuantificar ese sesgo en lugar de heredarlo."),

    ('h2', "3.3 Análisis exploratorio de los datos"),
    ('p', "La exploración persigue dos objetivos: verificar que la calidad del dato "
          "admite el análisis propuesto y caracterizar la heterogeneidad que motiva la "
          "pregunta de investigación."),

    ('h3', "3.3.1 Calidad del dato y estructura de la ausencia"),
    ('p', "La calidad es alta en las variables clave: la edad tiene 0.0013 % de valores "
          "faltantes, y el sexo y la entidad de residencia están completos. En las "
          "comorbilidades, la proporción de códigos de ausencia oscila entre 0.17 % y "
          "0.88 %, con el máximo en OTRA_COM."),
    ('p', "Esa ausencia **no es ruido aleatorio**, lo que justifica conservarla en lugar "
          "de imputarla. En nueve de las once comorbilidades, los registros con código "
          "de ausencia tienen una mortalidad hasta 2.2 veces mayor que los que sí están "
          "codificados: en EPOC, 12.5 % frente a 5.6 %. En NEUMONIA la relación se "
          "invierte por completo (razón 0.017), lo que es coherente con que sea el "
          "predictor dominante: no registrar neumonía acompaña a los casos leves."),
    ('p', "Más relevante para el eje de este trabajo es que la frecuencia de la ausencia "
          "difiere entre entidades: la máxima proporción de faltantes por "
          "entidad va de 0.02 % en Quintana Roo a 5.55 % en el Estado de México. No "
          "se trata de una diferencia de 280 puntos porcentuales, sino de una razón "
          "entre ambas proporciones: la entidad con peor registro tiene una proporción "
          "de faltantes cerca de 280 veces mayor que la de mejor registro. La calidad "
          "del registro clínico es, por tanto, "
          "desigual entre entidades, y constituye un mecanismo plausible de inequidad "
          "geográfica. La tabla 4 resume la estructura de "
          "esa ausencia variable por variable."),
    ('p', "Este trabajo documenta esa desigualdad pero no la incorpora al modelo: los "
          "indicadores de ausencia **no se usan como predictores**, y la decisión "
          "merece justificarse porque la alternativa es defendible. Usarlos "
          "probablemente mejoraría el desempeño, dado que la ausencia se asocia al "
          "desenlace. El motivo de no hacerlo es que esa mejora se sostendría sobre "
          "una variable que no describe al paciente sino a la unidad que lo registra: "
          "el modelo aprendería a asignar más riesgo a quien fue atendido en una "
          "unidad con registro deficiente, que es precisamente el mecanismo de sesgo "
          "que documenta Obermeyer et al. (2019) y que esta tesis se propone medir. "
          "Incorporarlo como predictor convertiría el objeto de estudio en parte del "
          "instrumento. Además, la proporción de faltantes depende de prácticas "
          "administrativas locales que pueden cambiar de un año a otro, de modo que un "
          "modelo que dependiera de ellas sería frágil fuera del conjunto de datos de ajuste. "
          "Queda como trabajo futuro cuantificar cuánto desempeño se cede por esta "
          "decisión, mediante un modelo alterno que sí los incluya."),
    ('tab', "Estructura de la ausencia en las variables clínicas del conjunto de datos "
            "de análisis.",
     [["Variable", "Ausencia (%)", "Mortalidad con ausencia (%)", "Mortalidad sin ausencia (%)", "Razón"],
      ["EPOC", "0.18", "12.47", "5.59", "2.23"],
      ["CARDIOVASCULAR", "0.18", "12.47", "5.59", "2.23"],
      ["TABAQUISMO", "0.18", "12.28", "5.59", "2.20"],
      ["RENAL_CRONICA", "0.18", "12.22", "5.59", "2.19"],
      ["ASMA", "0.17", "11.87", "5.59", "2.12"],
      ["INMUSUPR", "0.18", "11.78", "5.59", "2.11"],
      ["HIPERTENSION", "0.18", "11.44", "5.59", "2.05"],
      ["DIABETES", "0.19", "11.42", "5.59", "2.04"],
      ["OBESIDAD", "0.17", "11.03", "5.59", "1.97"],
      ["OTRA_COM", "0.88", "5.45", "5.60", "0.97"],
      ["NEUMONIA", "0.57", "0.10", "5.63", "0.02"]]),

    ('h3', "3.3.2 Heterogeneidad entre entidades federativas"),
    ('p', "La figura 1 muestra la heterogeneidad que motiva la tesis. El tamaño de "
          "muestra por entidad varía por un factor de 43 —de 15,221 a 651,956 "
          "registros— y las tasas de defunción difieren por un factor de 5.6 entre los "
          "extremos."),
    ('fig', "eda_por_entidad.png",
     "Heterogeneidad entre entidades federativas en el conjunto de datos: tasa de defunción "
     "(izquierda) y tamaño de muestra (derecha)."),
    ('p', "Esa doble heterogeneidad —de volumen y de riesgo basal— es exactamente la "
          "condición de la que cabe esperar un desempeño desigual, y por dos mecanismos "
          "distintos que conviene no confundir. El desequilibrio de volumen implica que "
          "el ajuste está dominado por unas pocas entidades grandes. La diferencia de "
          "prevalencia implica, además, que un umbral de decisión único no puede "
          "significar lo mismo en todas ellas; el apartado 2.3 formaliza por qué esto "
          "último no es un defecto corregible del modelo, sino una imposibilidad "
          "matemática."),

    ('h3', "3.3.3 Distribución del riesgo y del desenlace"),
    ('p', "La figura 2 resume la distribución de las variables predictoras y su relación "
          "con el desenlace. Tres rasgos orientan el modelado. Primero, el desbalance "
          "de clases es de 16.9 a 1, lo que obliga a ponderar la función de pérdida "
          "—asignando más peso a los casos con desenlace positivo, que son minoría— y "
          "—como consecuencia— a recalibrar después el puntaje. Segundo, la mortalidad "
          "crece de forma marcadamente monótona con la edad, desde 0.29 % en el grupo "
          "más joven hasta 25.6 % en el de 60 años o más, un gradiente de casi dos "
          "órdenes de magnitud que anticipa que la edad concentrará buena parte de la "
          "señal. Tercero, la prevalencia de las comorbilidades registradas es "
          "moderada, de modo que su aporte marginal por encima de la edad y la neumonía "
          "es limitado."),
    ('fig', "eda2021_profundo.png",
     "Análisis exploratorio del conjunto de datos de 2021: distribución de las variables "
     "predictoras y su relación con el desenlace."),
    ('p', "El gradiente por edad tiene una consecuencia para la auditoría que conviene "
          "anticipar. La edad explica buena parte del riesgo, y la composición etaria "
          "no es la misma en todas las entidades: unas tienen población más envejecida "
          "que otras. Si el modelo se desempeña peor en las entidades con más adultos "
          "mayores, ese resultado admite dos lecturas distintas —que el modelo falla "
          "en esas entidades, o que falla en los adultos mayores estén donde estén— y "
          "los datos agregados por entidad no permiten separarlas. En términos "
          "estadísticos, la edad es una variable de confusión de la disparidad "
          "geográfica."),
    ('p', "El diseño de la auditoría incorpora por eso una comprobación adicional: "
          "repetir el análisis de disparidad entre entidades usando únicamente a los "
          "pacientes de 60 años o más. Conviene subrayar que se trata de un **análisis "
          "complementario y no del análisis principal**: la auditoría se realiza sobre "
          "el conjunto de datos completo, y este subconjunto se examina además de ella, no en su "
          "lugar. Al comparar solo pacientes de edad semejante, la composición etaria "
          "deja de explicar las diferencias entre entidades; si la disparidad persiste "
          "dentro de ese grupo, la explicación geográfica se refuerza. El subgrupo "
          "tiene además la mortalidad más alta del conjunto de datos, 25.6 % frente a 5.60 % "
          "global, de modo que concentra una parte sustancial de las defunciones: se "
          "pierden registros, pero muchos menos casos del desenlace que se quiere "
          "estimar. Es la comprobación mínima para distinguir una "
          "explicación de la otra."),
]

# =============================================================================
#  Capitulo 2. Marco teorico y trabajos relacionados
# =============================================================================
CAP_MARCO = [
    ('p', "Este capítulo construye el marco teórico del proyecto en cuatro apartados. "
          "El primero expone los antecedentes: qué se ha hecho antes sobre este problema "
          "y en qué contexto académico se inscribe. El segundo analiza críticamente el "
          "estado del arte, comparando enfoques y resultados hasta identificar el vacío "
          "que el trabajo ocupa. El tercero desarrolla las bases teóricas —los modelos "
          "y teoremas que sustentan la auditoría de equidad— y el cuarto fija el marco "
          "conceptual, con las definiciones operacionales que se emplean en el resto de "
          "la tesis."),

    # ---------------------------------------------------------------- 3.1
    ('h2', "2.1 Antecedentes"),
    ('p', "Los antecedentes de este trabajo provienen de tres tradiciones que hasta "
          "ahora han avanzado por separado: la predicción de desenlaces por COVID-19 con "
          "datos mexicanos, la epidemiología espacial de la mortalidad en México y la "
          "equidad en salud desarrollada en otros países. El problema de "
          "esta tesis pertenece al ámbito en el que esas tres tradiciones se cruzan, y "
          "en la literatura revisada no se identificaron trabajos situados en él."),

    ('h3', "2.1.1 Estudios previos sobre predicción de desenlaces en México"),
    ('p', "Desde la publicación de la base abierta de la DGE en 2020, un número "
          "considerable de trabajos ha construido modelos de riesgo sobre ella. Dos son "
          "representativos por su alcance y por estar revisados por pares. "
          "Becerra-Sánchez et al. (2022) comparan varios algoritmos sobre datos "
          "mexicanos y alcanzan alrededor de 90 % de exactitud, identificando neumonía, "
          "edad avanzada e intubación como principales factores asociados a la "
          "mortalidad. Méndez-Astudillo (2024) aplica random forest y gradient boosting "
          "sobre más de veinte millones de observaciones y concluye que diabetes e "
          "hipertensión, junto con la desigualdad económica, definen la mortalidad."),
    ('p', "Ambos comparten estructura: un clasificador supervisado, atribución de "
          "importancia sobre comorbilidades y evaluación mediante métricas agregadas. "
          "Es la línea que se toma aquí como punto de partida, no como aportación."),

    ('h3', "2.1.2 Antecedentes sobre el sesgo algorítmico en salud"),
    ('p', "El antecedente fundacional del problema de equidad es el estudio de la "
          "asignación de recursos en un sistema de salud estadounidense, donde un modelo "
          "de gestión poblacional asignaba menos atención a pacientes afroamericanos con "
          "igual carga de enfermedad (Obermeyer et al., 2019). Su valor como antecedente "
          "no está en la magnitud del sesgo, sino en el mecanismo: el desenlace elegido "
          "—el gasto sanitario— se usaba como medida indirecta de la necesidad de "
          "atención, pero reflejaba también el acceso desigual a los servicios. El "
          "sesgo estaba en la definición del problema, no en el algoritmo."),
    ('p', "Un antecedente de otra naturaleza, pero decisivo para el diseño, es la "
          "revisión crítica de modelos pronósticos de COVID-19 de Wynants et al. (2020): "
          "la mayoría de los modelos revisados presentaba alto riesgo de sesgo, "
          "principalmente por selección del conjunto de datos, fuga de información y ausencia de "
          "validación. Junto con la guía TRIPOD de reporte de modelos predictivos en "
          "salud (Collins et al., 2015), esa revisión define el estándar metodológico "
          "que este trabajo se compromete a cumplir y explica varias decisiones del "
          "capítulo 3."),

    ('h3', "2.1.3 Contexto académico del problema"),
    ('p', "El problema se sitúa en la confluencia de tres campos. De la **informática "
          "médica** toma el objeto —los modelos de predicción clínica— y sus estándares "
          "de evaluación y reporte. Del **aprendizaje automático con criterios de "
          "equidad**, subcampo "
          "consolidado en la última década, toma los criterios formales de equidad, los "
          "resultados de imposibilidad y las técnicas de mitigación. De la **salud "
          "pública** toma la pregunta que da sentido a las dos anteriores: quién queda "
          "peor atendido, y si un sistema técnico nuevo corrige o amplifica una "
          "desigualdad que ya existía."),
    ('p', "La particularidad del caso mexicano justifica tratarlo por separado y no como "
          "una aplicación más. La organización federal de los servicios de salud hace "
          "que la entidad federativa no sea una variable demográfica cualquiera, sino la "
          "unidad en la que se decide, se financia y se opera la atención. Un atributo "
          "sensible que coincide con la unidad administrativa de decisión tiene una "
          "propiedad poco común: la mitigación por grupo es, en este contexto, "
          "administrativamente implementable, algo que rara vez ocurre con atributos "
          "como la raza o el sexo."),

    # ---------------------------------------------------------------- 3.2
    ('h2', "2.2 Estado del arte"),
    ('p', "Este apartado analiza críticamente la producción reciente, comparando "
          "enfoques y resultados en lugar de describirlos en serie. La revisión se "
          "apoya en fuentes verificadas individualmente contra el registro del editor y "
          "sostiene tres afirmaciones que, juntas, delimitan el espacio en el que se "
          "sitúa este trabajo."),

    ('h3', "2.2.1 La predicción de desenlaces por COVID-19 en México ha sido "
           "ampliamente estudiada"),
    ('p', "La comparación de los trabajos disponibles sobre la base abierta de la DGE "
          "arroja un "
          "patrón de convergencia. Becerra-Sánchez et al. (2022) y Méndez-Astudillo "
          "(2024) emplean conjuntos de datos, algoritmos y periodos distintos, y sin embargo "
          "coinciden en el desempeño alcanzado y en el conjunto de variables "
          "informativas —edad, neumonía y las comorbilidades metabólicas—. Esa "
          "coincidencia sugiere que el margen de mejora de la tarea puramente "
          "predictiva sobre esta fuente ya no está principalmente en la elección del "
          "algoritmo. La afirmación se apoya en un número reducido de trabajos "
          "revisados por pares, de modo que debe tomarse como una lectura de la "
          "literatura disponible y no como un resultado establecido."),
    ('p', "La implicación metodológica es directa: replicar el esquema «clasificador más "
          "atribución de importancia sobre comorbilidades» sería un trabajo derivativo. "
          "Por eso el modelo predictivo se adopta aquí como línea de base y no como "
          "aportación. La comparación con esta literatura debe además hacerse con "
          "cautela, porque los trabajos de referencia reportan exactitud y F1 y no "
          "AUROC, de modo que las cifras no son directamente homologables."),
    ('nota', "Un examen crítico de esta literatura revela un problema que condiciona el "
             "diseño de este trabajo. La variable INTUBADO, que aparece entre los "
             "factores más informativos en parte de ella, describe el curso hospitalario "
             "y no está disponible al primer contacto. Usarla como predictor de "
             "mortalidad en ese punto constituye fuga de información, precisamente el "
             "defecto que Wynants et al. (2020) señalan como más frecuente. Esta tesis "
             "la excluye explícitamente, lo que hace esperable un desempeño algo menor "
             "que el reportado por los trabajos que la incorporan."),

    ('h3', "2.2.2 Lo geográfico ya se estudió, pero como predictor"),
    ('p', "Maldonado-Sifuentes et al. (2024) muestran que los factores de ubicación "
          "—municipio, unidad médica, entidad de nacimiento y de residencia— superan "
          "incluso a la edad como predictores de mortalidad por COVID-19 en México. Es "
          "un hallazgo relevante que debe reconocerse, y es el trabajo más cercano al "
          "de esta tesis en la literatura nacional. Responde, sin embargo, a una "
          "pregunta distinta."),
    ('p', "La diferencia es sustantiva y vale la pena precisarla, porque de ella depende "
          "la originalidad de este trabajo. Ese estudio usa la geografía como variable "
          "de **entrada** para responder «¿dónde vives predice tu desenlace?», una "
          "pregunta de epidemiología espacial e importancia de variables. Esta tesis usa "
          "la geografía como eje de **auditoría** para responder «¿el modelo comete más "
          "errores en unas entidades que en otras, y cómo se corrige esa inequidad?», "
          "una pregunta de equidad algorítmica y mitigación. Que la entidad sea "
          "informativa como predictor no dice nada sobre si el modelo es igualmente "
          "confiable en cada entidad: son propiedades independientes, y de hecho un "
          "modelo que **no** use la entidad puede aun así rendir de forma desigual entre "
          "ellas."),

    ('h3', "2.2.3 La equidad algorítmica en salud es madura, pero fuera de México"),
    ('p', "La literatura de equidad en salud es rica y está anclada en otros contextos y "
          "otros atributos sensibles. Nejadshamsi et al. (2026) auditan y mitigan el "
          "sesgo por sexo en clasificación de severidad de COVID-19 con datos de Canadá, "
          "y es el trabajo metodológicamente más próximo al diseño que aquí se propone. "
          "En imagen médica, Ricci Lara et al. (2022) documentan de forma sistemática "
          "cómo los sesgos de composición de las conjuntos de datos de entrenamiento se trasladan "
          "al desempeño por subgrupo."),
    ('p', "El contraste con esta literatura revela dos vacíos. El primero es "
          "geográfico en el sentido trivial: no se identificó trabajo alguno que use "
          "datos mexicanos tratando la entidad federativa como atributo sensible ligado "
          "a la desigualdad de infraestructura de salud. El segundo es metodológico y "
          "más interesante: la literatura de equidad trabaja casi siempre con dos o tres "
          "grupos de tamaño comparable —hombre/mujer, dos o tres categorías raciales—, "
          "mientras que auditar 32 entidades cuyo tamaño de muestra varía por un factor "
          "de 43 plantea un problema estadístico distinto. Con muchos grupos pequeños, "
          "los estimadores de brecha máxima están sesgados al alza y los métodos que "
          "optimizan esa brecha tienden a ajustarse al ruido de la muestra. Este "
          "trabajo opera en ese régimen, sobre el que la literatura revisada ofrece "
          "menos evidencia que sobre el caso de dos o tres grupos comparables."),

    ('h3', "2.2.4 Tendencias, vacíos y áreas de oportunidad"),
    ('p', "El análisis anterior permite identificar tres tendencias. La primera es el "
          "desplazamiento del interés desde el desempeño agregado hacia el desempeño "
          "desagregado por subgrupo, visible tanto en las guías de reporte como en la "
          "literatura de equidad. La segunda es el reconocimiento de que la calibración, "
          "y no solo la discriminación, es un requisito para el uso clínico. La tercera "
          "es el abandono de la búsqueda de un único «modelo justo» en favor de "
          "instrumentos que expliciten el intercambio entre criterios, consecuencia "
          "directa de los resultados de imposibilidad del apartado 2.3."),
    ('p', "La tabla 1 sintetiza la posición de este trabajo respecto de la literatura "
          "revisada."),
    ('tab', "Posición de esta tesis respecto de la literatura.",
     [["Dimensión", "Estado en la literatura", "Aporte de esta tesis"],
      ["Predicción de desenlace (México)", "Ampliamente estudiada", "Línea de base, no aportación"],
      ["Geografía como predictor (México)", "Estudiada", "Se distingue: geografía como eje de equidad"],
      ["Equidad algorítmica en salud", "Madura, fuera de México", "Se traslada y adapta al contexto mexicano"],
      ["Auditoría de equidad por entidad (México)", "No identificada en la revisión", "Eje central del trabajo"],
      ["Mitigación y frontera de Pareto (México)", "No identificada en la revisión", "Instrumento de decisión entregable"],
      ["Equidad con muchos grupos desiguales", "Menos documentada", "Régimen de trabajo: 32 grupos, factor 43 de tamaño"],
      ["Transportabilidad de la equidad", "Rara vez evaluada", "Validación interna; externa como trabajo pendiente"]]),
    ('p', "En una frase: la literatura revisada muestra que la geografía predice la "
          "mortalidad en México y que "
          "la equidad algorítmica ha sido estudiada en otros países, pero no se "
          "identificaron trabajos que examinen "
          "si un modelo clínico entrenado con datos mexicanos es igual de "
          "preciso entre entidades federativas, ni cómo corregir esa inequidad."),

    # ---------------------------------------------------------------- 3.3
    ('h2', "2.3 Bases teóricas"),
    ('p', "Este apartado desarrolla los modelos y resultados formales que sustentan la "
          "investigación. Se organizan en tres bloques: la teoría de evaluación de "
          "modelos de riesgo clínico, la de aprendizaje automático sobre datos "
          "tabulares y la de equidad algorítmica, que aporta el resultado teórico "
          "central del trabajo."),

    ('h3', "2.3.1 Evaluación de modelos de riesgo clínico"),
    ('p', "Un modelo de estratificación de riesgo estima la probabilidad de un desenlace "
          "—aquí, la defunción— a partir de información disponible en el momento en que "
          "se toma la decisión clínica. Su evaluación exige separar dos propiedades que "
          "se confunden con frecuencia."),
    ('p', "La **discriminación** mide la capacidad de ordenar a los pacientes por "
          "riesgo, es decir, de asignar un puntaje más alto a quien fallece que a quien "
          "sobrevive. Se resume en el AUROC. Esta métrica depende solo del orden de los "
          "puntajes y no de su valor: si a todos los pacientes se les multiplicara el "
          "puntaje por diez, o se les aplicara cualquier otra transformación que "
          "respete el orden —lo que se denomina una transformación monótona—, el AUROC "
          "no cambiaría. De ahí que "
          "un modelo pueda discriminar perfectamente y, aun así, emitir probabilidades "
          "muy alejadas del riesgo real. La **calibración** mide justamente eso: si de "
          "cada cien pacientes a "
          "quienes el modelo asigna un riesgo de 20 % fallecen efectivamente veinte. Van "
          "Calster et al. (2019) argumentan que la calibración es el talón de Aquiles de "
          "la analítica predictiva en medicina, porque un modelo descalibrado desplaza "
          "sistemáticamente las decisiones de umbral sin que el AUROC lo delate."),
    ('p', "Esa distinción es la base teórica de una decisión central de este trabajo: la "
          "auditoría de equidad se realiza sobre el puntaje **calibrado**. La razón es "
          "que, sin calibrar, el error de calibración medido por grupo queda dominado "
          "por el sesgo global de entrenamiento y no por la inequidad entre grupos, que "
          "es el objeto de estudio."),
    ('p', "En conjuntos de datos con desenlaces poco frecuentes, el AUPRC complementa al AUROC "
          "porque es sensible al desbalance de clases. Y como toda métrica agregada "
          "oculta la distribución de errores, la evaluación de un modelo destinado al "
          "despliegue debe reportarse en el **punto de operación** previsto y no en un "
          "umbral arbitrario. Las guías de reporte recogen estos requisitos de manera "
          "sistemática (Collins et al., 2015)."),

    ('h3', "2.3.2 Aprendizaje automático sobre datos tabulares"),
    ('p', "Para datos tabulares heterogéneos, los ensambles de árboles con impulso del "
          "gradiente siguen siendo el punto de referencia práctico frente a "
          "arquitecturas neuronales. Las implementaciones basadas en histogramas "
          "agrupan los valores de cada variable en un número fijo de intervalos antes "
          "de buscar los puntos de corte del árbol, "
          "lo que reduce el costo de entrenamiento de forma sustancial y las hace "
          "viables en millones de registros (Ke et al., 2017). En este trabajo se "
          "emplea HistGradientBoostingClassifier de scikit-learn (Pedregosa et al., "
          "2011), que además maneja valores faltantes de forma nativa —propiedad "
          "relevante aquí, porque la codificación de ausencia de la base de la DGE "
          "resulta informativa, como documenta el apartado 3.3.1, y no conviene "
          "imputarla a ciegas."),
    ('p', "El desbalance de clases se atiende ponderando la función de pérdida, de modo "
          "que cada caso con desenlace positivo pese más que cada caso negativo. Esa "
          "decisión tiene una consecuencia poco discutida: los puntajes resultantes "
          "dejan de ser probabilidades calibradas y sobreestiman el riesgo absoluto. La "
          "corrección estándar es una transformación monótona ajustada sobre datos no "
          "vistos, como la regresión isotónica (Zadrozny y Elkan, 2002). Por ser "
          "monótona, preserva el ordenamiento —y con él el AUROC— mientras corrige el "
          "nivel."),

    ('h3', "2.3.3 Criterios formales de equidad algorítmica"),
    ('p', "Sea A un atributo sensible, Y el desenlace observado, Ŷ la predicción binaria "
          "y R el puntaje de riesgo. Las tres familias de criterios que se emplean en "
          "esta tesis corresponden a las tres relaciones de independencia posibles "
          "entre esas variables:"),
    ('b', "**Independencia, o paridad demográfica.** P(Ŷ = 1 | A = a) constante en a. "
          "Iguala la tasa de selección entre grupos, sin condicionar al desenlace."),
    ('b', "**Separación, o igualdad de probabilidades de acierto y error** (en la "
          "literatura en inglés, equalized odds). P(Ŷ = 1 | Y = y, A = a) constante en "
          "a para "
          "y ∈ {0, 1}; es decir, igualdad simultánea de sensibilidad y tasa de falsos "
          "positivos (Hardt et al., 2016). Su relajación al caso y = 1 —la igualdad de "
          "oportunidades— es la que más importa clínicamente: significa que el modelo "
          "detecta a quien va a fallecer con la misma probabilidad en todos los grupos."),
    ('b', "**Suficiencia, o calibración por grupo.** P(Y = 1 | R = r, A = a) constante "
          "en "
          "a. Significa que un riesgo de 0.3 quiere decir lo mismo en cada entidad "
          "federativa."),

    ('h3', "2.3.4 El teorema de imposibilidad"),
    ('p', "Los tres criterios del apartado anterior no son compatibles entre sí. El "
          "resultado, demostrado de forma independiente por Chouldechova (2017) y por "
          "Kleinberg et al. (2017), se enuncia así: si la prevalencia del desenlace "
          "difiere entre grupos y el clasificador no es perfecto, entonces la "
          "suficiencia (calibración por grupo) y la separación (igualdad simultánea de "
          "sensibilidad y de tasa de falsos positivos) no pueden cumplirse a la vez. "
          "Las dos condiciones del enunciado importan: si todos los grupos tuvieran la "
          "misma prevalencia, o si el clasificador acertara siempre, el conflicto "
          "desaparecería. Es un teorema, no una regularidad empírica; se aplica a este "
          "trabajo por deducción y no depende de los resultados que las entregas "
          "siguientes obtengan."),
    ('p', "Conviene precisar la forma que toma en este conjunto de datos, porque las dos "
          "condiciones se verifican. Las tasas de mortalidad por entidad difieren por "
          "un factor de "
          "5.6, como documenta el apartado 3.3.2, y ningún modelo de riesgo clínico "
          "acierta siempre. Se sigue que, sobre un puntaje calibrado por entidad, "
          "ningún conjunto de reglas de decisión puede igualar **a la vez** la "
          "sensibilidad y la tasa de falsos positivos entre entidades. Sí puede "
          "igualarse **una** de las dos, y aquí es donde la relación entre los tres "
          "conceptos se vuelve operativa: la calibración es una propiedad del puntaje, "
          "mientras que la sensibilidad y la tasa de falsos positivos son propiedades "
          "de la regla de decisión, es decir, del umbral que se aplica sobre ese "
          "puntaje. Fijar un umbral distinto por entidad no altera la calibración del "
          "puntaje subyacente, y permite escoger cuál de las "
          "dos tasas se reparte por igual, a costa de desigualar la otra. La "
          "mitigación por post-procesamiento del apartado 2.3.5 explota exactamente "
          "esa propiedad."),
    ('p', "La consecuencia práctica es la que estructura el entregable de la tesis. La "
          "elección entre criterios es normativa y no estadística; por eso el resultado "
          "adecuado no es un único modelo «justo», sino una frontera que explicite el "
          "intercambio y traslade la decisión a quien tiene la responsabilidad de "
          "tomarla."),

    ('h3', "2.3.5 Técnicas de mitigación del sesgo"),
    ('p', "Las técnicas se clasifican por la etapa del flujo de trabajo en la que "
          "intervienen, y "
          "cada familia tiene supuestos distintos sobre dónde reside el problema."),
    ('b', "**Pre-procesamiento.** Modifican los datos antes de entrenar: reponderación "
          "de muestras, remuestreo o corrección de representación. Son agnósticas al "
          "modelo, pero solo actúan sobre el desequilibrio de representación; suponen, "
          "por tanto, que la inequidad proviene de la composición de la muestra."),
    ('b', "**In-procesamiento.** Incorporan la restricción de equidad en la "
          "optimización. La reducción por gradiente exponenciado convierte el problema "
          "restringido en una secuencia de problemas ponderados y admite restricciones "
          "de separación, o equalized odds (Bird et al., 2020)."),
    ('b', "**Post-procesamiento.** Ajustan la regla de decisión sobre un modelo ya "
          "entrenado, típicamente eligiendo un umbral por grupo (Hardt et al., 2016). "
          "Son las más eficaces cuando el problema no es el ordenamiento sino dónde se "
          "corta, y las más controvertidas porque usan el atributo sensible en el "
          "momento de la decisión."),
    ('p', "Un problema abierto especialmente pertinente aquí es la equidad de subgrupos "
          "pequeños: al desagregar por 32 entidades, los estados con menos registros "
          "producen estimaciones de sensibilidad con varianza alta, y los métodos que "
          "optimizan brechas máximas tienden a ajustarse al ruido. De ahí que el diseño "
          "incorpore un criterio explícito de soporte mínimo por grupo y procedimientos "
          "de cuantificación de la incertidumbre."),

    ('h3', "2.3.6 La frontera de Pareto como instrumento de decisión"),
    ('p', "El teorema de imposibilidad convierte la mitigación en un problema de "
          "compromiso: ganar equidad cuesta desempeño, y hay que decidir cuánto se "
          "está dispuesto a ceder. El objeto teórico adecuado para representar esa "
          "decisión es una frontera de Pareto."),
    ('p', "Su construcción es la siguiente. Cada política de despliegue —cada forma "
          "concreta de fijar los umbrales de decisión— produce un par de valores: "
          "cuánta disparidad queda entre entidades y cuánto desempeño global se "
          "conserva. Al representar todas las políticas posibles en un plano cuyos "
          "ejes son esas dos cantidades, muchas quedan descartadas de inmediato, "
          "porque existe otra que es mejor en los dos ejes a la vez. La frontera de "
          "Pareto es el conjunto de las que sobreviven a esa criba: aquellas en las "
          "que ya no es posible reducir más la disparidad sin perder desempeño, ni "
          "recuperar desempeño sin aumentar la disparidad. Elegir entre ellas ya no es "
          "un problema técnico —ninguna es objetivamente mejor que otra— sino una "
          "decisión de política."),
    ('p', "En el diseño de esta tesis, la frontera se traza interpolando linealmente "
          "entre el umbral global τ y el umbral específico de cada entidad τg, mediante "
          "τg(α) = (1 − α)·τ + α·τg, con α ∈ [0, 1]. Cada valor de α define una política "
          "concreta: α = 0 es el modelo sin mitigar y α = 1 la corrección completa por "
          "entidad. El conjunto de pares (brecha de sensibilidad, desempeño global) es "
          "el instrumento entregable, porque traslada al responsable de la política una "
          "elección que es normativa y no técnica, en lugar de esconderla en un valor "
          "por omisión."),

    # ---------------------------------------------------------------- 3.4
    ('h2', "2.4 Marco conceptual"),
    ('p', "Este apartado fija el significado de los conceptos centrales del trabajo y su "
          "traducción a cantidades medibles. La distinción entre definición conceptual y "
          "definición operacional se mantiene de forma explícita, porque buena parte de "
          "la confusión en la literatura de equidad proviene de nombrar «sesgo» a cosas "
          "que se miden de maneras incompatibles."),

    ('h3', "2.4.1 Conceptos centrales"),
    ('b', "**Estratificación de riesgo clínico.** Asignación de una probabilidad de "
          "desenlace adverso a cada paciente, con el fin de ordenar la atención. Se "
          "distingue del diagnóstico en que no afirma un estado presente, sino un curso "
          "probable."),
    ('b', "**Punto de predicción.** Momento del proceso de atención en el que el modelo "
          "emitiría su estimación. En este trabajo es el primer contacto. Es un concepto "
          "definitorio y no un detalle de implementación: fija qué información es "
          "admisible como predictor."),
    ('b', "**Fuga de información.** Uso como predictor de información que no está "
          "disponible en el punto de predicción. Produce un desempeño aparente que no se "
          "puede reproducir en despliegue."),
    ('b', "**Atributo sensible.** Variable respecto de la cual se exige que el "
          "comportamiento del modelo sea equitativo. En este trabajo, la entidad "
          "federativa de residencia; secundariamente, el sexo y el grupo etario."),
    ('b', "**Sesgo geográfico.** Diferencia sistemática en la calidad de las "
          "predicciones del modelo entre entidades federativas. No es la diferencia de "
          "riesgo entre entidades —que es un hecho epidemiológico— sino la diferencia en "
          "cuán bien el modelo estima ese riesgo."),
    ('b', "**Auditoría de equidad.** Evaluación del desempeño del modelo desagregado por "
          "los valores de un atributo sensible, con el fin de detectar disparidades."),
    ('b', "**Mitigación.** Intervención sobre los datos, el entrenamiento o la regla de "
          "decisión con el fin de reducir una disparidad medida."),
    ('b', "**Punto de operación.** Umbral de decisión sobre el puntaje de riesgo que "
          "convierte una probabilidad en una acción. Todas las métricas dependientes de "
          "umbral se reportan en un punto de operación único y declarado, para que las "
          "comparaciones entre etapas sean válidas."),
    ('b', "**Transportabilidad.** Grado en que el desempeño y la equidad de un modelo se "
          "conservan al aplicarlo a una población o fuente distinta de la de ajuste."),

    ('h3', "2.4.2 Variables del estudio"),
    ('p', "La tabla 2 resume las variables del estudio con su papel, tipo y definición "
          "operacional."),
    ('tab', "Variables del estudio y sus definiciones operacionales.",
     [["Variable", "Papel", "Tipo", "Definición operacional"],
      ["defuncion", "Dependiente", "Binaria",
       "1 si FECHA_DEF contiene una fecha válida; 0 si contiene el código 9999-99-99"],
      ["EDAD", "Independiente", "Continua",
       "Edad en años al momento del registro, acotada al intervalo [0, 120]"],
      ["sexo_mujer", "Independiente / sensible", "Binaria",
       "1 = mujer, 0 = hombre, derivada de SEXO; faltante si el código es 99"],
      ["Once comorbilidades (_bin)", "Independientes", "Binarias",
       "1 = sí, 0 = no, faltante para los códigos 97 a 99"],
      ["entidad_nombre", "Atributo sensible", "Categórica (32)",
       "Entidad de residencia (ENTIDAD_RES) traducida con el catálogo oficial; no se usa como predictor"],
      ["grupo_edad", "Atributo sensible", "Categórica (4)",
       "Cortes fijos en 0–17, 18–39, 40–59 y 60 o más años"],
      ["hospitalizado", "Auxiliar", "Binaria",
       "Derivada de TIPO_PACIENTE; solo para descripción y análisis de sensibilidad"],
      ["Índice de marginación", "Contextual", "Continua",
       "Índice CONAPO 2020 por entidad, unido por clave de entidad"]]),

    ('h3', "2.4.3 Definiciones operacionales de las métricas"),
    ('p', "La tabla 3 traduce los conceptos anteriores a las cantidades que se calculan. "
          "Las métricas de equidad se implementan de forma explícita, y no se delegan a "
          "una biblioteca computacional de terceros, para que el cálculo sea auditable "
          "línea por línea; son "
          "equivalentes a las definiciones de Fairlearn (Bird et al., 2020)."),
    ('tab', "Definiciones operacionales de las métricas por dimensión de evaluación.",
     [["Dimensión", "Métrica", "Definición operacional"],
      ["Discriminación", "AUROC",
       "Área bajo la curva ROC sobre el conjunto de prueba"],
      ["Discriminación", "AUPRC",
       "Área bajo la curva precisión–exhaustividad; se reporta junto con su razón "
       "respecto de la prevalencia, que es su línea base"],
      ["Calibración", "Puntaje de Brier",
       "Error cuadrático medio entre probabilidad predicha y desenlace observado"],
      ["Calibración", "Error de calibración por grupo",
       "Máxima diferencia absoluta, entre grupos, entre riesgo medio predicho y "
       "observado"],
      ["Equidad", "Brecha de sensibilidad",
       "Diferencia entre la máxima y la mínima sensibilidad por grupo en el punto de "
       "operación; criterio de separación o equalized odds)"],
      ["Equidad", "Brecha de tasa de falsos positivos",
       "Diferencia entre la máxima y la mínima tasa de falsos positivos por grupo"],
      ["Equidad", "Brecha de AUROC",
       "Diferencia entre el máximo y el mínimo AUROC por grupo"],
      ["Equidad", "Brecha de tasa de selección",
       "Diferencia entre la máxima y la mínima proporción de casos marcados como de "
       "riesgo (paridad demográfica)"],
      ["Interpretabilidad", "Importancia por permutación",
       "Caída del AUROC al permutar aleatoriamente cada variable"],
      ["Utilidad agregada", "Exactitud balanceada",
       "Media de sensibilidad y especificidad en el punto de operación"]]),
    ('p', "Dos criterios operacionales complementan la tabla. **Soporte por grupo:** un "
          "grupo se considera evaluable si tiene al menos 500 observaciones y 20 casos "
          "positivos en el bloque correspondiente; por debajo de ese umbral, la varianza "
          "de la estimación domina cualquier señal de inequidad, y los grupos "
          "descartados se reportan de forma explícita en lugar de omitirse en silencio. "
          "**Incertidumbre:** las brechas se acompañan de intervalos de confianza por "
          "remuestreo estratificado por entidad y de una prueba de permutación sobre la "
          "etiqueta de grupo, porque la diferencia entre el máximo y el mínimo de 32 "
          "estimaciones ruidosas está sesgada al alza aun en ausencia de todo efecto."),
]

# =============================================================================
#  Conclusiones (parciales de esta entrega)
# =============================================================================
CONCLUSIONES = [
    ('p', "Este documento corresponde a la primera entrega del proyecto terminal y "
          "cubre el análisis y desarrollo conceptual: la introducción con el "
          "planteamiento del problema, el marco teórico y la metodología con la "
          "construcción y caracterización de la base de datos. Las "
          "conclusiones que siguen son, por tanto, parciales, y se refieren a lo que "
          "estas tres etapas permiten ya afirmar."),
    ('p', "**Sobre el planteamiento.** La revisión del estado del arte sostiene el "
          "vacío que motiva el trabajo, ya que los trabajos disponibles sobre "
          "predicción de "
          "desenlaces por COVID-19 con datos mexicanos convergen en niveles de "
          "desempeño similares, la geografía se ha estudiado como predictor y no como "
          "eje de "
          "equidad, y la literatura de equidad algorítmica en salud está anclada en "
          "otros países y otros atributos sensibles. En la literatura revisada no se "
          "identificaron trabajos que respondan si un modelo "
          "clínico entrenado con datos mexicanos es igual de preciso entre entidades "
          "federativas."),
    ('p', "**Sobre la metodología y la base de datos.** El conjunto de datos construido —casos "
          "COVID confirmados del corte 2021— es viable para el análisis "
          "propuesto: 2,526,649 casos confirmados con una mortalidad observada de "
          "5.60 % y una calidad alta en las variables clave. La exploración documenta "
          "además las dos condiciones de las que cabe esperar inequidad: el tamaño de "
          "muestra por entidad varía por un factor de 43 y las tasas de defunción por un "
          "factor de 5.6. Un tercer hallazgo, no previsto, es que la calidad del "
          "registro clínico es también desigual entre entidades —la proporción de "
          "códigos de ausencia va de 0.02 % a 5.55 %—, lo que constituye un mecanismo "
          "candidato de inequidad que el trabajo documenta pero deliberadamente no "
          "explota."),
    ('p', "**Sobre el marco teórico.** El teorema de imposibilidad, combinado con el "
          "factor de 5.6 entre las tasas de mortalidad por entidad, permite anticipar "
          "un resultado antes de ajustar cualquier modelo: sobre un puntaje calibrado no "
          "existirá ninguna regla de decisión que iguale simultáneamente la sensibilidad "
          "y la tasa de falsos positivos entre entidades. Conviene subrayar el estatus "
          "de esta afirmación: es una deducción a partir de un teorema demostrado y de "
          "una cifra observada en el conjunto de datos, no una hipótesis pendiente de contraste "
          "ni un hallazgo empírico propio. Esa imposibilidad no es un "
          "obstáculo del método, sino la razón por la que el entregable de la tesis debe "
          "ser una frontera de compromiso y no un modelo único."),
    ('p', "**Recomendaciones para la etapa siguiente.** Tres decisiones quedan fijadas "
          "por lo anterior. Primera, la auditoría debe realizarse sobre el puntaje "
          "calibrado, porque sobre el puntaje crudo el error de calibración por grupo "
          "mide el sesgo global de entrenamiento y no la inequidad. Segunda, toda "
          "métrica dependiente de umbral debe reportarse en un punto de operación único "
          "y declarado, para que las comparaciones entre etapas sean válidas. Tercera, "
          "las brechas deben acompañarse de una medida de incertidumbre, porque con 32 "
          "grupos de tamaño muy desigual el estadístico de brecha máxima está sesgado al "
          "alza. Queda pendiente, y así se reporta, la validación externa sobre una "
          "fuente independiente, que es la que sustentaría la hipótesis H4."),
]

# =============================================================================
#  Fuentes de consulta (APA 7)
# =============================================================================
REFERENCIAS = [
    "Becerra-Sánchez, A., Rodarte-Rodríguez, A., Escalante-García, N. I., "
    "Olvera-González, J. E., De la Rosa-Vargas, J. I., Zepeda-Valles, G., y "
    "Velásquez-Martínez, E. de J. (2022). Mortality analysis of patients with COVID-19 "
    "in Mexico based on risk factors applying machine learning techniques. Diagnostics, "
    "12(6), 1396. https://doi.org/10.3390/diagnostics12061396",

    "Bird, S., Dudík, M., Edgar, R., Horn, B., Lutz, R., Milan, V., Sameki, M., "
    "Wallach, H., y Walker, K. (2020). Fairlearn: A toolkit for assessing and improving "
    "fairness in AI (Informe técnico MSR-TR-2020-32). Microsoft Research. "
    "https://www.microsoft.com/en-us/research/publication/fairlearn-a-toolkit-for-assessing-and-improving-fairness-in-ai/",

    "Chouldechova, A. (2017). Fair prediction with disparate impact: A study of bias in "
    "recidivism prediction instruments. Big Data, 5(2), 153–163. "
    "https://doi.org/10.1089/big.2016.0047",

    "Collins, G. S., Reitsma, J. B., Altman, D. G., y Moons, K. G. M. (2015). "
    "Transparent reporting of a multivariable prediction model for individual prognosis "
    "or diagnosis (TRIPOD): The TRIPOD statement. Annals of Internal Medicine, 162(1), "
    "55–63. https://doi.org/10.7326/M14-0697",

    "Consejo Nacional de Población. (2021). Índices de marginación 2020. Gobierno de "
    "México. https://www.gob.mx/conapo/documentos/indices-de-marginacion-2020-284372",

    "Dirección General de Epidemiología. (2022). Datos abiertos de COVID-19. Secretaría "
    "de Salud, Gobierno de México. "
    "https://www.gob.mx/salud/documentos/datos-abiertos-152127",

    "Dirección General de Información en Salud. (2024). Subsistema Automatizado de "
    "Egresos Hospitalarios (series 2008–2024). Secretaría de Salud, Gobierno de México.",

    "Hardt, M., Price, E., y Srebro, N. (2016). Equality of opportunity in supervised "
    "learning. En Advances in Neural Information Processing Systems 29 (pp. 3315–3323). "
    "Curran Associates.",

    "Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., Ye, Q., y Liu, T.-Y. "
    "(2017). LightGBM: A highly efficient gradient boosting decision tree. En Advances "
    "in Neural Information Processing Systems 30 (pp. 3146–3154). Curran Associates.",

    "Kleinberg, J., Mullainathan, S., y Raghavan, M. (2017). Inherent trade-offs in the "
    "fair determination of risk scores. En 8th Innovations in Theoretical Computer "
    "Science Conference (ITCS 2017) (Vol. 67, pp. 43:1–43:23). Schloss "
    "Dagstuhl–Leibniz-Zentrum für Informatik. "
    "https://doi.org/10.4230/LIPIcs.ITCS.2017.43",

    "Maldonado-Sifuentes, C. E., Vargas-Santiago, M., Leon-Velasco, D. A., "
    "Ortega-García, M. C., Ledo-Mezquita, Y., y Castillo-Velasquez, F. A. (2024). "
    "Leveraging machine learning to unveil the critical role of geographic factors in "
    "COVID-19 mortality in Mexico. Computación y Sistemas, 28(1), 5–18. "
    "https://doi.org/10.13053/CyS-28-1-4908",

    "Méndez-Astudillo, J. (2024). The impact of comorbidities and economic inequality on "
    "COVID-19 mortality in Mexico: A machine learning approach. Frontiers in Big Data, "
    "7, 1298029. https://doi.org/10.3389/fdata.2024.1298029",

    "Nejadshamsi, S., H. Chu, C., McGilton, K. S., Li, X., Ronquillo, C., y "
    "Abbasgholizadeh-Rahimi, S. (2026). Evaluation and improvement of algorithmic "
    "fairness for COVID-19 severity classification using explainable artificial "
    "intelligence-based bias mitigation. JAMIA Open, 9(1), ooaf171. "
    "https://doi.org/10.1093/jamiaopen/ooaf171",

    "Obermeyer, Z., Powers, B., Vogeli, C., y Mullainathan, S. (2019). Dissecting racial "
    "bias in an algorithm used to manage the health of populations. Science, 366(6464), "
    "447–453. https://doi.org/10.1126/science.aax2342",

    "Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., "
    "Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., "
    "Cournapeau, D., Brucher, M., Perrot, M., y Duchesnay, É. (2011). Scikit-learn: "
    "Machine learning in Python. Journal of Machine Learning Research, 12, 2825–2830.",

    "Ricci Lara, M. A., Echeveste, R., y Ferrante, E. (2022). Addressing fairness in "
    "artificial intelligence for medical imaging. Nature Communications, 13(1), 4581. "
    "https://doi.org/10.1038/s41467-022-32186-3",

    "Van Calster, B., McLernon, D. J., van Smeden, M., Wynants, L., y Steyerberg, E. W. "
    "(2019). Calibration: The Achilles heel of predictive analytics. BMC Medicine, "
    "17(1), 230. https://doi.org/10.1186/s12916-019-1466-7",

    "Vickers, A. J., y Elkin, E. B. (2006). Decision curve analysis: A novel method for "
    "evaluating prediction models. Medical Decision Making, 26(6), 565–574. "
    "https://doi.org/10.1177/0272989X06295361",

    "Wynants, L., Van Calster, B., Collins, G. S., Riley, R. D., Heinze, G., Schuit, E., "
    "Albu, E., Arshi, B., Bellou, V., Bonten, M. M. J., Dahly, D. L., Damen, J. A., "
    "Debray, T. P. A., … van Smeden, M. (2020). Prediction models for diagnosis and "
    "prognosis of covid-19: Systematic review and critical appraisal. BMJ, 369, m1328. "
    "https://doi.org/10.1136/bmj.m1328",

    "Zadrozny, B., y Elkan, C. (2002). Transforming classifier scores into accurate "
    "multiclass probability estimates. En Proceedings of the eighth ACM SIGKDD "
    "international conference on Knowledge discovery and data mining (pp. 694–699). ACM. "
    "https://doi.org/10.1145/775047.775151",
]

# =============================================================================
#  Glosario
# =============================================================================
GLOSARIO = [
    ("A", [
        "**AUROC:** Área bajo la curva ROC. Resume la capacidad de un modelo para "
        "ordenar correctamente a los pacientes por riesgo. Es insensible a "
        "transformaciones monótonas del puntaje, por lo que no informa sobre la "
        "calidad de las probabilidades emitidas.",
        "**AUPRC:** Área bajo la curva de precisión y exhaustividad. Complementa al "
        "AUROC en conjuntos de datos con desenlaces poco frecuentes, porque es sensible al "
        "desbalance de clases.",
        "**Atributo sensible:** Variable respecto de la cual se exige que el "
        "comportamiento del modelo sea equitativo. En este trabajo, la entidad "
        "federativa de residencia.",
        "**Auditoría de equidad:** Evaluación del desempeño de un modelo desagregado "
        "por los valores de un atributo sensible, con el fin de detectar disparidades "
        "sistemáticas.",
    ]),
    ("C", [
        "**Calibración:** Correspondencia entre la probabilidad predicha y la "
        "frecuencia observada del desenlace. Un modelo está calibrado si, entre los "
        "pacientes a quienes asigna un riesgo de 20 %, fallece aproximadamente el "
        "20 %.",
        "**Conjunto de calibración:** Bloque de datos reservado exclusivamente para "
        "ajustar la transformación de calibración y los umbrales por grupo, sin "
        "intervenir en el entrenamiento ni en la evaluación final.",
        "**Conjunto de datos de análisis:** Registros que satisfacen los criterios de "
        "inclusión del estudio. Aquí, los casos COVID confirmados del corte anual "
        "2021.",
    ]),
    ("D", [
        "**Discriminación:** Capacidad de un modelo para ordenar a los pacientes por "
        "riesgo. Se distingue de la calibración, que se refiere al nivel absoluto de "
        "la probabilidad estimada.",
        "**Definición operacional:** Traducción de un concepto a una regla de cálculo "
        "verificable sobre los datos disponibles.",
    ]),
    ("E", [
        "**Equalized odds (separación, o igualdad de probabilidades de acierto y "
        "error):** Criterio de equidad que exige igualdad simultánea de "
        "sensibilidad y tasa de falsos positivos entre grupos. Su relajación al caso "
        "de los positivos se conoce como igualdad de oportunidades.",
        "**Estratificación de riesgo:** Asignación de una probabilidad de desenlace "
        "adverso a cada paciente con el fin de ordenar la atención.",
    ]),
    ("F", [
        "**Frontera de Pareto:** Conjunto de políticas de despliegue tales que no "
        "existe otra que mejore la equidad sin empeorar el desempeño, ni al contrario. "
        "Es el instrumento con el que este trabajo hace explícito el compromiso entre "
        "ambos objetivos.",
        "**Fuga de información:** Uso como predictor de información no disponible en "
        "el punto de predicción. Produce un desempeño aparente que no se reproduce en "
        "despliegue.",
    ]),
    ("P", [
        "**Paridad demográfica:** Criterio de equidad que exige igual tasa de "
        "selección entre grupos, sin condicionar al desenlace observado.",
        "**Punto de operación:** Umbral de decisión que convierte el puntaje de riesgo "
        "en una acción. Todas las métricas dependientes de umbral se reportan en un "
        "punto de operación único y declarado.",
        "**Punto de predicción:** Momento del proceso de atención en el que el modelo "
        "emitiría su estimación. En este trabajo, el primer contacto.",
    ]),
    ("R", [
        "**Regresión isotónica:** Transformación monótona, ajustada sobre datos no "
        "vistos, que corrige el nivel de las probabilidades sin alterar el "
        "ordenamiento y por tanto sin afectar al AUROC.",
    ]),
    ("S", [
        "**Sesgo geográfico:** Diferencia sistemática en la calidad de las "
        "predicciones del modelo entre entidades federativas. No debe confundirse con "
        "la diferencia de riesgo entre entidades, que es un hecho epidemiológico.",
        "**Sensibilidad:** Proporción de casos con desenlace positivo que el modelo "
        "marca correctamente como de riesgo, en el punto de operación establecido.",
    ]),
    ("T", [
        "**Teorema de imposibilidad:** Resultado según el cual, si la prevalencia del "
        "desenlace difiere entre grupos y el clasificador no es perfecto, la "
        "calibración por grupo (suficiencia) y la igualdad simultánea de sensibilidad "
        "y tasa de falsos positivos (separación, o equalized odds) no pueden "
        "satisfacerse a la vez.",
        "**Transportabilidad:** Grado en que el desempeño y la equidad de un modelo se "
        "conservan al aplicarlo a una población o fuente distinta de la de ajuste.",
    ]),
]

# =============================================================================
#  Abreviaturas y acronimos
# =============================================================================
ABREVIATURAS = [
    ("Sigla", "Descripción"),
    ("AUPRC", "Área bajo la curva de precisión y exhaustividad (del inglés "
               "“Area Under the Precision-Recall Curve”)"),
    ("AUROC", "Área bajo la curva ROC (del inglés “Area Under the Receiver "
               "Operating Characteristic Curve”)"),
    ("CONAPO", "Consejo Nacional de Población"),
    ("COVID-19", "Enfermedad por coronavirus 2019 (del inglés "
                  "“Coronavirus Disease 2019”)"),
    ("DGE", "Dirección General de Epidemiología, Secretaría de Salud"),
    ("DGIS", "Dirección General de Información en Salud, Secretaría de Salud"),
    ("EDA", "Análisis exploratorio de datos (del inglés "
             "“Exploratory Data Analysis”)"),
    ("EPOC", "Enfermedad pulmonar obstructiva crónica"),
    ("FPR", "Tasa de falsos positivos (del inglés “False Positive Rate”)"),
    ("HGB", "Impulso del gradiente por histogramas (del inglés "
             "“Histogram-based Gradient Boosting”)"),
    ("IA", "Inteligencia artificial (del inglés "
            "“Artificial Intelligence”)"),
    ("INEGI", "Instituto Nacional de Estadística y Geografía"),
    ("INFOTEC", "Centro de Investigación e Innovación en Tecnologías de la "
                 "Información y Comunicación"),
    ("MCDI", "Maestría en Ciencia de Datos e Información"),
    ("ML", "Aprendizaje automático (del inglés “Machine Learning”)"),
    ("ROC", "Característica operativa del receptor (del inglés "
             "“Receiver Operating Characteristic”)"),
    ("SHAP", "Explicaciones aditivas de Shapley (del inglés "
              "“SHapley Additive exPlanations”)"),
    ("TPR", "Tasa de verdaderos positivos o sensibilidad (del inglés "
             "“True Positive Rate”)"),
    ("TRIPOD", "Guía de reporte transparente de modelos de predicción multivariable "
                "(del inglés “Transparent Reporting of a multivariable prediction "
                "model for Individual Prognosis Or Diagnosis”)"),
    ("UCI", "Unidad de cuidados intensivos"),
]

# =============================================================================
#  Anexo 1
# =============================================================================
ANEXO_TITULO = "Variables admitidas y excluidas del modelo"
ANEXO = [
    ('p', "Este anexo detalla el resultado del control de fuga de información descrito "
          "en el apartado 3.2.1. La columna «Disponible al primer contacto» es el "
          "criterio de admisión: una variable solo puede ser predictor si su valor se "
          "conoce en el momento en que el modelo emitiría su estimación."),
    ('tab', "Variables de la base de la DGE y su tratamiento en el estudio.",
     [["Variable original", "Disponible al primer contacto", "Papel en el estudio", "Motivo"],
      ["EDAD", "Sí", "Predictor", "Registrada en la notificación inicial"],
      ["SEXO", "Sí", "Predictor y atributo sensible", "Registrada en la notificación inicial"],
      ["DIABETES", "Sí", "Predictor", "Comorbilidad interrogada al primer contacto"],
      ["EPOC", "Sí", "Predictor", "Comorbilidad interrogada al primer contacto"],
      ["ASMA", "Sí", "Predictor", "Comorbilidad interrogada al primer contacto"],
      ["INMUSUPR", "Sí", "Predictor", "Comorbilidad interrogada al primer contacto"],
      ["HIPERTENSION", "Sí", "Predictor", "Comorbilidad interrogada al primer contacto"],
      ["OTRA_COM", "Sí", "Predictor", "Comorbilidad interrogada al primer contacto"],
      ["CARDIOVASCULAR", "Sí", "Predictor", "Comorbilidad interrogada al primer contacto"],
      ["OBESIDAD", "Sí", "Predictor", "Comorbilidad interrogada al primer contacto"],
      ["RENAL_CRONICA", "Sí", "Predictor", "Comorbilidad interrogada al primer contacto"],
      ["TABAQUISMO", "Sí", "Predictor", "Comorbilidad interrogada al primer contacto"],
      ["NEUMONIA", "Sí (supuesto declarado)", "Predictor",
       "Se captura en el formato inicial; se somete a análisis de sensibilidad por ser "
       "el predictor dominante"],
      ["ENTIDAD_RES", "Sí", "Atributo sensible, no predictor",
       "Se reserva como eje de auditoría; incluirla como entrada impediría medir la "
       "inequidad que se busca"],
      ["CLASIFICACION_FINAL", "Sí", "Criterio de inclusión",
       "Define el conjunto de datos de casos confirmados"],
      ["FECHA_DEF", "No", "Desenlace",
       "Posterior al punto de predicción; solo se usa para derivar la variable objetivo"],
      ["TIPO_PACIENTE", "No", "Excluida como predictor",
       "Posterior al triage; se usa solo para describir y para el análisis de "
       "sensibilidad"],
      ["UCI", "No", "Excluida", "Describe el curso hospitalario"],
      ["INTUBADO", "No", "Excluida",
       "Describe el curso hospitalario; su uso como predictor constituiría fuga de "
       "información"]]),
    ('p', "El resultado es un conjunto de trece predictores: edad, sexo y once "
          "comorbilidades o signos registrados al primer contacto. Los indicadores de "
          "ausencia derivados de esas mismas variables se conservan en el conjunto para "
          "el análisis descriptivo del apartado 3.3.1, pero no se emplean como entradas "
          "del modelo."),
]
