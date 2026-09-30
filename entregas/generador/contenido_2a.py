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
    ('p', "El presente documento corresponde a la segunda entrega del proyecto terminal "
          "y reporta los tres primeros capítulos: la introducción, con el planteamiento "
          "del problema y el protocolo de investigación; el marco teórico "
          "—antecedentes, estado del arte, bases teóricas y marco conceptual—; y el "
          "marco metodológico, desarrollado sobre el proceso CRISP-DM y que abarca "
          "desde el entendimiento del problema hasta las condiciones de "
          "implementación de la solución. La "
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
    ('p', "Esta segunda entrega comprende los tres primeros capítulos del proyecto "
          "terminal, con el marco metodológico desarrollado por completo y las "
          "observaciones de la primera entrega atendidas. En el **capítulo 1** se "
          "presenta la introducción: fija el "
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
          "**capítulo 3** desarrolla el marco metodológico siguiendo las seis fases de "
          "CRISP-DM: el entendimiento del negocio con sus criterios de éxito, la "
          "comprensión de los datos y su exploración, la preparación con control de "
          "fuga de información, el modelado con la calibración del puntaje, la "
          "evaluación en sus dos niveles —desempeño global y auditoría de equidad— y "
          "las condiciones de implementación de la solución propuesta."),
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
             "por deducción, no por evidencia empírica. Las hipótesis H1, H2 y H3 son "
             "conjeturas que el capítulo 3 contrasta y que podían resultar falsas —H2 en "
             "efecto no se sostuvo—, mientras que H4 queda pendiente de la validación "
             "externa. Y la asociación entre disparidad y marginación que examina H2 es, "
             "en el mejor de los casos, una asociación observacional entre 32 unidades "
             "agregadas, sin pretensión causal."),

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
          "desenlace solo es posible en el 11.8 % de los casos; el apartado 3.3.3 "
          "documenta esa propiedad estructural y el 3.6.5 examina sus consecuencias, "
          "que resultan considerables."),
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
          "el marco teórico y el marco metodológico completo, incluidos el modelado, "
          "la auditoría de equidad y la mitigación con sus resultados. El capítulo de "
          "resultados detallados y la discusión corresponden a las entregas "
          "siguientes del proyecto terminal."),
    ('nota', "Los límites anteriores no son concesiones retóricas. Cualquier afirmación "
             "de esta tesis que dependa de H4 o de intervalos de confianza se marca "
             "como preliminar en el punto donde aparece."),
]

# =============================================================================
#  Capitulo 3. Marco metodologico
# =============================================================================
CAP_METODO = [
    ('p', "Este capítulo desarrolla el marco metodológico del proyecto. Expone primero "
          "el enfoque general y el proceso que lo estructura; después recorre ese "
          "proceso fase por fase, desde el entendimiento del problema hasta la "
          "implementación de la solución propuesta. En un trabajo cuyo objeto es "
          "auditar la equidad de un modelo, el proceso de captura del dato no es un "
          "preliminar técnico: es una fuente candidata de la inequidad que se pretende "
          "medir, y por eso recibe un tratamiento detallado."),

    # ------------------------------------------------------------------ 3.1
    ('h2', "3.1 Presentación de la metodología"),
    ('p', "El enfoque de esta investigación es **cuantitativo, no experimental y "
          "retrospectivo**. Es cuantitativo porque las preguntas se responden con "
          "cantidades medibles —métricas de desempeño y de disparidad calculadas sobre "
          "una muestra—, no con interpretación de material cualitativo. Es no "
          "experimental porque no hay asignación de tratamientos ni control de "
          "condiciones: se observa un registro administrativo ya generado. Y es "
          "retrospectivo porque ese registro corresponde a hechos ocurridos en 2021, "
          "anteriores al estudio. Estas tres características fijan el alcance de lo que "
          "el trabajo puede afirmar: describe asociaciones y cuantifica desempeño, pero "
          "no establece relaciones causales."),
    ('p', "El proceso que organiza el trabajo empírico es **CRISP-DM** (Cross-Industry "
          "Standard Process for Data Mining), propuesto por Chapman et al. (2000) y "
          "descrito por Wirth y Hipp (2000) y sintetizado por Shearer (2000). CRISP-DM "
          "divide un proyecto de minería de "
          "datos en seis fases —entendimiento del negocio, comprensión de los datos, "
          "preparación de los datos, modelado, evaluación e implementación— y admite "
          "retornos entre ellas: un hallazgo de la fase de evaluación puede obligar a "
          "revisar la preparación de los datos, y así sucesivamente. Martínez-Plumed et "
          "al. (2021) documentan que sigue siendo el proceso de referencia dos décadas "
          "después de su publicación, y señalan al mismo tiempo su principal "
          "limitación: fue concebido para proyectos de explotación comercial y no "
          "contempla de forma explícita las preocupaciones de equidad y rendición de "
          "cuentas que hoy acompañan a los sistemas de decisión."),
    ('p', "La elección merece justificarse frente a las alternativas. **SEMMA**, de SAS, "
          "cubre únicamente el ciclo analítico —muestrear, explorar, modificar, modelar "
          "y evaluar— y omite tanto el entendimiento del negocio como la "
          "implementación, que en este trabajo son precisamente las fases donde se "
          "decide qué significa que un modelo sea equitativo y qué implicaría "
          "desplegarlo. **KDD** (Fayyad et al., 1996) es más general y está orientado "
          "al descubrimiento de conocimiento, con menor prescripción operativa. "
          "**TDSP**, de Microsoft, añade prácticas de ingeniería valiosas, pero supone "
          "un equipo y una infraestructura de despliegue que no corresponden a un "
          "proyecto terminal individual. CRISP-DM ofrece el mejor equilibrio para este "
          "caso: cubre el ciclo completo, es independiente de la herramienta y su "
          "vocabulario es comprensible para los destinatarios del trabajo, que "
          "incluyen responsables de política de salud y no solo especialistas "
          "técnicos. Su desventaja —la ausencia de una fase de equidad— se atiende con "
          "la adaptación que se describe enseguida."),
    ('p', "La adaptación consiste en **desdoblar la fase de evaluación**. En su forma "
          "estándar, esa fase pregunta si el modelo alcanza los criterios de éxito "
          "definidos al inicio, lo que se verifica con métricas agregadas. Aquí la "
          "evaluación se realiza en dos niveles: primero el desempeño global, como es "
          "habitual, y después el desempeño desagregado por los valores del atributo "
          "sensible, que es la auditoría de equidad. El segundo nivel puede devolver el "
          "proyecto a la fase de modelado —para aplicar una técnica de mitigación— sin "
          "que el primero haya detectado problema alguno. Esa asimetría es el hallazgo "
          "metodológico que este trabajo pretende ilustrar: un modelo puede satisfacer "
          "todos los criterios de éxito agregados y, aun así, no ser desplegable."),
    ('p', "La tabla 4 traduce las fases del proceso a los apartados de este capítulo y "
          "a los artefactos que produce cada una, de modo que la trazabilidad entre el "
          "marco y el trabajo realizado sea verificable."),
    ('tab', "Correspondencia entre las fases de CRISP-DM, los apartados de este "
            "capítulo y los artefactos producidos.",
     [["Fase CRISP-DM", "Apartado", "Artefacto producido"],
      ["Entendimiento del negocio", "3.2",
       "Objetivos de minería de datos y criterios de éxito medibles"],
      ["Comprensión de los datos", "3.3",
       "Conjunto de datos de análisis, manifiesto y análisis exploratorio"],
      ["Preparación de los datos", "3.4",
       "Conjunto analítico con control de fuga y partición en tres bloques"],
      ["Modelado", "3.5",
       "Modelo de referencia calibrado y tres variantes de mitigación"],
      ["Evaluación", "3.6",
       "Métricas globales, auditoría de equidad e intervalos de incertidumbre"],
      ["Implementación", "3.7",
       "Frontera de Pareto como instrumento de decisión y condiciones de despliegue"]]),
    ('nota', "El orden de exposición no refleja el orden real de ejecución. El trabajo "
             "avanzó de forma iterativa: la primera auditoría de equidad reveló que el "
             "error de calibración por grupo estaba dominado por el sesgo global de "
             "entrenamiento, lo que obligó a volver a la fase de modelado e introducir "
             "la calibración isotónica sobre un bloque independiente, y esa decisión a "
             "su vez obligó a rehacer la partición de los datos. El capítulo presenta "
             "el resultado de esas iteraciones, no su cronología."),

    # ------------------------------------------------------------------ 3.2
    ('h2', "3.2 Entendimiento del negocio"),
    ('p', "En un proyecto del sector público el «negocio» es la operación del servicio. "
          "Aquí esa operación es la atención hospitalaria durante un episodio de "
          "demanda extraordinaria, y el problema que la tensiona es la asignación de "
          "recursos escasos —camas, ventiladores, personal— entre pacientes que llegan "
          "de forma simultánea y con pronósticos muy distintos."),

    ('h3', "3.2.1 Contexto del problema"),
    ('p', "La decisión que el modelo pretende apoyar ocurre en el **primer contacto** "
          "del paciente con el sistema de salud: el momento en que se registra el caso "
          "y se decide si se le trata de forma ambulatoria o se le hospitaliza. Quien "
          "toma esa decisión dispone de información limitada —edad, sexo, "
          "comorbilidades declaradas y signos observables— y debe emitir un juicio de "
          "riesgo con ella. Una herramienta que estime ese riesgo de forma "
          "reproducible permite ordenar la atención y anticipar la demanda de recursos."),
    ('p', "El contexto mexicano añade una condición que estructura todo el trabajo. La "
          "organización federal de los servicios de salud hace que la entidad "
          "federativa no sea una variable demográfica cualquiera, sino la unidad en la "
          "que se decide, se financia y se opera la atención. Las entidades difieren "
          "entre sí en infraestructura, en prácticas de registro y en perfil "
          "demográfico, y esas diferencias se trasladan a los datos con los que "
          "cualquier modelo se entrena. Un modelo ajustado sobre el agregado nacional "
          "queda dominado por las entidades con más registros, y puede resultar menos "
          "preciso justo donde el sistema es más frágil."),
    ('p', "De ahí que el problema de negocio no sea únicamente «estimar el riesgo con "
          "precisión», sino «estimar el riesgo con una precisión comparable en todo el "
          "país». Un instrumento que acierte en promedio pero falle sistemáticamente en "
          "un subconjunto de entidades desplazaría recursos en contra de esa población, "
          "y lo haría con la apariencia de objetividad que confiere un sistema "
          "automatizado."),

    ('h3', "3.2.2 Objetivos del proyecto y criterios de éxito"),
    ('p', "CRISP-DM distingue los objetivos de negocio de los objetivos de minería de "
          "datos, y exige que cada uno se acompañe de un criterio de éxito verificable. "
          "La distinción evita un error frecuente: dar por exitoso un proyecto porque "
          "el modelo alcanza una métrica alta, sin haber comprobado que esa métrica "
          "responde a la necesidad que originó el trabajo. La tabla 5 hace explícita "
          "esa traducción para los objetivos específicos enunciados en el apartado 1.3."),
    ('tab', "Traducción de los objetivos de negocio a objetivos de minería de datos "
            "con criterios de éxito medibles.",
     [["Objetivo de negocio", "Objetivo de minería de datos", "Criterio de éxito"],
      ["Disponer de un estimador de riesgo utilizable en el primer contacto",
       "Ajustar un clasificador binario de mortalidad con variables disponibles en ese punto (OE1, OE2)",
       "AUROC ≥ 0.90 y sensibilidad de 80 % en el punto de operación declarado"],
      ["Que las probabilidades emitidas signifiquen lo mismo en todo el país",
       "Calibrar el puntaje sobre un bloque independiente (OE2)",
       "Error máximo de calibración por entidad ≤ 0.05"],
      ["Saber si la herramienta atiende por igual a toda la población",
       "Medir el desempeño desagregado por entidad, sexo y grupo etario (OE3)",
       "Brechas reportadas con intervalos de confianza y prueba de significancia"],
      ["Corregir la inequidad sin inutilizar la herramienta",
       "Aplicar y comparar mitigación pre, in y post-procesamiento (OE4)",
       "Reducción de la brecha de sensibilidad con pérdida de exactitud balanceada < 2 puntos"],
      ["Entregar a quien decide un instrumento y no una imposición técnica",
       "Construir la frontera de Pareto equidad–desempeño (OE4, OE5)",
       "Conjunto de políticas con su costo medido, estimado fuera de muestra"]]),
    ('p', "Los criterios anteriores se fijaron **antes** de ejecutar el modelado, y "
          "conviene dejar constancia de ello porque un umbral definido después de ver "
          "los resultados no es un criterio, sino una descripción. El apartado 3.6 "
          "reporta cuáles se cumplieron y cuáles no."),
    ('p', "El proyecto opera además bajo tres restricciones declaradas. **De "
          "información:** solo se admiten variables disponibles en el punto de "
          "predicción, lo que excluye buena parte de lo que registra la base. **De "
          "recursos:** el ajuste debe ser viable en una estación de trabajo "
          "convencional sobre millones de registros, lo que condiciona la familia de "
          "algoritmos. **De uso:** el resultado es un insumo para una decisión humana y "
          "no un sistema de decisión automática, de modo que la interpretabilidad y la "
          "calibración importan tanto como la discriminación."),
    ('nota', "El riesgo principal identificado en esta fase, y que condicionó el diseño "
             "de las siguientes, es la fuga de información. La revisión de Wynants et "
             "al. (2020) documenta que es el defecto más frecuente en los modelos "
             "pronósticos de COVID-19 publicados. Un modelo que use variables "
             "posteriores a la decisión alcanza un desempeño aparente excelente y es "
             "inservible en operación. El apartado 3.4.1 describe el control adoptado."),

    # ------------------------------------------------------------------ 3.3
    ('h2', "3.3 Comprensión de los datos"),
    ('p', "Esta fase persigue dos objetivos: documentar el origen y la naturaleza de "
          "los datos, y verificar que su calidad admite el análisis propuesto. La "
          "exploración cumple además una función sustantiva en este trabajo, porque "
          "caracteriza la heterogeneidad entre entidades que motiva la pregunta de "
          "investigación."),

    ('h3', "3.3.1 Fuentes de información"),
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
          "método de distancias ponderadas al cuadrado sobre el Censo de Población y "
          "Vivienda 2020 del INEGI. Se usa el archivo por entidad IME_2020.xls, del que "
          "se toman el índice y el grado de marginación. Su papel es examinar la "
          "hipótesis H2, es decir, si la disparidad geográfica del modelo se asocia a "
          "la desigualdad estructural de la entidad."),
    ('p', "Como **fuente prevista para la validación externa** se identificó el "
          "Subsistema Automatizado de Egresos Hospitalarios de la DGIS (Dirección "
          "General de Información en Salud, 2024). Su explotación queda fuera del "
          "alcance de esta entrega y se reporta como trabajo pendiente."),

    ('h3', "3.3.2 Tipos de datos y estructura del registro"),
    ('p', "La base de la DGE es un archivo **tabular** en el que cada fila es un caso "
          "notificado y cada columna una variable del formato de estudio "
          "epidemiológico. No hay datos no estructurados —texto libre, imagen o "
          "señal—, lo que simplifica la preparación y orienta la elección del algoritmo "
          "hacia las familias que mejor rinden sobre datos tabulares heterogéneos."),
    ('p', "Las variables son de cuatro tipos. Una **continua**, la edad en años. Varias "
          "**categóricas nominales** codificadas con enteros que remiten a catálogos "
          "oficiales: el sexo, la entidad de residencia, el tipo de paciente y la "
          "clasificación final del caso. Once **dicotómicas** que registran "
          "comorbilidades y signos, codificadas con 1 para «sí» y 2 para «no». Y varias "
          "**de fecha**, entre ellas la fecha de defunción, de la que se deriva la "
          "variable objetivo."),
    ('p', "Un rasgo del formato condiciona todo el tratamiento posterior: la ausencia no "
          "se codifica como vacío, sino con tres valores especiales que significan cosas "
          "distintas. El código **97** indica «no aplica», el **98** «se ignora» y el "
          "**99** «no especificado». La distinción importa porque no todas esas "
          "situaciones representan la misma falta de información, y porque su "
          "frecuencia varía entre entidades, como documenta el apartado 3.3.4."),

    ('h3', "3.3.3 Construcción del conjunto de datos y definición del desenlace"),
    ('p', "El conjunto de datos de análisis —los registros que cumplen los criterios "
          "de inclusión del estudio— se restringe a **casos COVID confirmados**. En el "
          "diccionario de datos de la DGE, un caso se considera confirmado cuando la "
          "variable CLASIFICACION_FINAL toma uno de tres valores: 1, confirmado por "
          "asociación epidemiológica; 2, confirmado por dictaminación de un comité; y "
          "3, confirmado por prueba de laboratorio. Se excluyen los casos sospechosos, "
          "los negativos y los no concluyentes. El filtro produce n = 2,526,649 "
          "registros con una mortalidad observada de 5.60 % y una tasa de "
          "hospitalización de 11.78 %."),
    ('p', "Un modelo de mortalidad **por COVID** debe estimarse sobre enfermos de "
          "COVID. Incluir casos negativos y sospechosos mezcla poblaciones con "
          "mecanismos de riesgo distintos y diluye la señal: la prevalencia del "
          "desenlace cae entonces a 2.06 % y el modelo pasa a describir mortalidad en "
          "población tamizada, que es otra pregunta. La diferencia entre 5.60 % y "
          "2.06 % separa dos poblaciones con riesgo basal muy distinto."),
    ('p', "El desenlace modelado es la **defunción**, derivada del campo FECHA_DEF: la "
          "base codifica 9999-99-99 para paciente vivo. En el conjunto de datos hay "
          "141,499 defunciones registradas."),
    ('nota', "El conjunto de datos tiene una propiedad estructural que condiciona toda "
             "lectura posterior y conviene declarar aquí. Entre los casos confirmados, "
             "el número de defunciones registradas como ambulatorias es cero: fallecer "
             "implica estar registrado como hospitalizado. El desenlace solo es "
             "posible, por tanto, en el 11.8 % del conjunto de datos (n = 297,685), y "
             "el resto son casos que no pueden fallecer por construcción. Esto no "
             "invalida la tarea —estimar riesgo al primer contacto sobre todo caso "
             "confirmado es precisamente el triage que motiva la tesis— pero significa "
             "que parte de la discriminación del modelo consistirá en separar "
             "ambulatorios de hospitalizados. El apartado 3.6.5 cuantifica cuánta."),
    ('p', "La base original codifica las categóricas con enteros y usa códigos "
          "especiales para la ausencia. El conjunto analítico se deriva del original "
          "mediante las siguientes construcciones."),
    ('b', "**defuncion.** Indicador binario derivado de FECHA_DEF (1 si existe fecha de "
          "defunción registrada). Es la variable objetivo."),
    ('b', "**hospitalizado.** Indicador binario derivado de TIPO_PACIENTE. Se usa para "
          "describir el conjunto de datos y para el análisis de sensibilidad, **nunca** "
          "como predictor de mortalidad."),
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
          "40–59 y 60 o más años. Se define una única vez para todo el flujo de "
          "trabajo, a fin de que los análisis por edad sean comparables entre etapas."),
    ('b', "**Once pares por comorbilidad.** Cada variable clínica —diabetes, EPOC, "
          "asma, inmunosupresión, hipertensión, otra comorbilidad, enfermedad "
          "cardiovascular, obesidad, enfermedad renal crónica, tabaquismo y neumonía— "
          "produce dos columnas: una binaria con sufijo _bin (1 = sí, 0 = no, faltante "
          "en otro caso) y un **indicador de faltante** con sufijo _na."),
    ('p', "La decisión de conservar la ausencia como información, en lugar de imputarla "
          "a ciegas, merece justificarse porque no es la práctica habitual. Su "
          "frecuencia difiere entre entidades y su presencia se asocia al desenlace, de "
          "modo que la ausencia es en sí misma un posible mecanismo de inequidad "
          "geográfica; el apartado 3.3.4 lo documenta con cifras. El conjunto "
          "resultante tiene 31 columnas y se almacena en formato Parquet —un formato de "
          "archivo de código abierto que guarda las tablas por columnas en lugar de por "
          "filas, lo que reduce el tamaño en disco y acelera la lectura selectiva de "
          "variables en conjuntos de millones de registros—, acompañado de un "
          "manifiesto que registra procedencia, número de filas, esquema, tasas "
          "observadas y versiones de biblioteca, de modo que ninguna etapa posterior "
          "consuma un artefacto sin verificar su origen."),

    ('h3', "3.3.4 Calidad del dato y estructura de la ausencia"),
    ('p', "La calidad es alta en las variables clave: la edad tiene 0.0013 % de valores "
          "faltantes, y el sexo y la entidad de residencia están completos. En las "
          "comorbilidades, la proporción de códigos de ausencia oscila entre 0.17 % y "
          "0.88 %, con el máximo en OTRA_COM."),
    ('p', "Esa ausencia **no es ruido aleatorio**, lo que justifica conservarla en "
          "lugar de imputarla. En nueve de las once comorbilidades, los registros con "
          "código de ausencia tienen una mortalidad hasta 2.2 veces mayor que los que "
          "sí están codificados: en EPOC, 12.5 % frente a 5.6 %. En NEUMONIA la "
          "relación se invierte por completo (razón 0.017), lo que es coherente con que "
          "sea el predictor dominante: no registrar neumonía acompaña a los casos "
          "leves."),
    ('p', "Más relevante para el eje de este trabajo es que la frecuencia de la ausencia "
          "difiere entre entidades: la máxima proporción de faltantes por entidad va de "
          "0.02 % en Quintana Roo a 5.55 % en el Estado de México. No se trata de una "
          "diferencia de 280 puntos porcentuales, sino de una razón entre ambas "
          "proporciones: la entidad con peor registro tiene una proporción de faltantes "
          "cerca de 280 veces mayor que la de mejor registro. La calidad del registro "
          "clínico es, por tanto, desigual entre entidades, y constituye un mecanismo "
          "plausible de inequidad geográfica. La tabla 6 resume la estructura de esa "
          "ausencia variable por variable."),
    ('p', "Este trabajo documenta esa desigualdad pero no la incorpora al modelo: los "
          "indicadores de ausencia **no se usan como predictores**, y la decisión "
          "merece justificarse porque la alternativa es defendible. Usarlos "
          "probablemente mejoraría el desempeño, dado que la ausencia se asocia al "
          "desenlace. El motivo de no hacerlo es que esa mejora se sostendría sobre una "
          "variable que no describe al paciente sino a la unidad que lo registra: el "
          "modelo aprendería a asignar más riesgo a quien fue atendido en una unidad "
          "con registro deficiente, que es precisamente el mecanismo de sesgo que "
          "documenta Obermeyer et al. (2019) y que esta tesis se propone medir. "
          "Incorporarlo como predictor convertiría el objeto de estudio en parte del "
          "instrumento. Además, la proporción de faltantes depende de prácticas "
          "administrativas locales que pueden cambiar de un año a otro, de modo que un "
          "modelo que dependiera de ellas sería frágil fuera del conjunto de datos de "
          "ajuste. Queda como trabajo futuro cuantificar cuánto desempeño se cede por "
          "esta decisión, mediante un modelo alterno que sí los incluya."),
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

    ('h3', "3.3.5 Heterogeneidad entre entidades federativas"),
    ('p', "La figura 1 muestra la heterogeneidad que motiva la tesis. El tamaño de "
          "muestra por entidad varía por un factor de 43 —de 15,221 a 651,956 "
          "registros— y las tasas de defunción difieren por un factor de 5.6 entre los "
          "extremos."),
    ('fig', "eda_por_entidad.png",
     "Heterogeneidad entre entidades federativas en el conjunto de datos: tasa de "
     "defunción (izquierda) y tamaño de muestra (derecha)."),
    ('p', "Esa doble heterogeneidad —de volumen y de riesgo basal— es exactamente la "
          "condición de la que cabe esperar un desempeño desigual, y por dos mecanismos "
          "distintos que conviene no confundir. El desequilibrio de volumen implica que "
          "el ajuste está dominado por unas pocas entidades grandes. La diferencia de "
          "prevalencia implica, además, que un umbral de decisión único no puede "
          "significar lo mismo en todas ellas; el apartado 2.3 formaliza por qué esto "
          "último no es un defecto corregible del modelo, sino una imposibilidad "
          "matemática."),
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
     "Análisis exploratorio del conjunto de datos de 2021: distribución de las "
     "variables predictoras y su relación con el desenlace."),
    ('p', "El gradiente por edad tiene una consecuencia para la auditoría que conviene "
          "anticipar. La edad explica buena parte del riesgo, y la composición etaria "
          "no es la misma en todas las entidades: unas tienen población más envejecida "
          "que otras. Si el modelo se desempeña peor en las entidades con más adultos "
          "mayores, ese resultado admite dos lecturas distintas —que el modelo falla en "
          "esas entidades, o que falla en los adultos mayores estén donde estén— y los "
          "datos agregados por entidad no permiten separarlas. En términos "
          "estadísticos, la edad es una variable de confusión de la disparidad "
          "geográfica."),
    ('p', "El diseño de la auditoría incorpora por eso una comprobación adicional: "
          "repetir el análisis de disparidad entre entidades usando únicamente a los "
          "pacientes de 60 años o más. Conviene subrayar que se trata de un **análisis "
          "complementario y no del análisis principal**: la auditoría se realiza sobre "
          "el conjunto de datos completo, y este subconjunto se examina además de ella, "
          "no en su lugar. Al comparar solo pacientes de edad semejante, la composición "
          "etaria deja de explicar las diferencias entre entidades; si la disparidad "
          "persiste dentro de ese grupo, la explicación geográfica se refuerza. El "
          "subgrupo tiene además la mortalidad más alta del conjunto de datos, 25.6 % "
          "frente a 5.60 % global, de modo que concentra una parte sustancial de las "
          "defunciones: se pierden registros, pero muchos menos casos del desenlace que "
          "se quiere estimar. Es la comprobación mínima para distinguir una explicación "
          "de la otra."),

    # ------------------------------------------------------------------ 3.4
    ('h2', "3.4 Preparación de los datos"),
    ('p', "La preparación comprende tres decisiones: qué variables se admiten como "
          "predictores, cómo se tratan los valores especiales y cómo se reparte el "
          "conjunto de datos entre los bloques de entrenamiento, calibración y prueba."),

    ('h3', "3.4.1 Control de fuga de información"),
    ('p', "El control de fuga de información es la decisión metodológica más importante "
          "del flujo de trabajo. El punto de predicción es el **primer contacto**, de "
          "modo que ninguna variable posterior a ese momento puede ser predictor. Se "
          "excluyen explícitamente:"),
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
             "captura es un supuesto del que dependen los resultados. Reentrenar el modelo "
             "sin ella, para acotar cuánto del desempeño y de la inequidad descansan en "
             "esa única variable, queda como trabajo pendiente. Lo que el apartado "
             "3.6.5 sí acota es cuánto del desempeño proviene de separar ambulatorios "
             "de hospitalizados, que es la otra fuente de discriminación aparente."),

    ('h3', "3.4.2 Limpieza y transformación"),
    ('p', "Sobre las variables derivadas en el apartado 3.3.3 se aplica un tratamiento "
          "uniforme: los códigos 97 a 99 se convierten en faltante explícito y quedan "
          "registrados en el indicador correspondiente; la edad se acota al intervalo "
          "plausible; y las categóricas se traducen a etiquetas legibles mediante los "
          "catálogos oficiales del diccionario de datos. **No se aplica imputación.** "
          "El modelo principal maneja los valores faltantes de forma nativa, lo que "
          "evita introducir en los datos un supuesto que no se puede verificar."),
    ('p', "Tampoco se aplican transformaciones de escala. Los ensambles de árboles son "
          "invariantes a transformaciones monótonas de las variables de entrada, de "
          "modo que estandarizar o normalizar la edad no alteraría el ajuste y sí "
          "restaría legibilidad a la interpretación posterior. Las variables binarias "
          "entran directamente y no requieren codificación adicional; la única "
          "categórica de más de dos niveles, la entidad federativa, no es predictor, "
          "de modo que el problema de su codificación no se presenta."),

    ('h3', "3.4.3 Partición de los datos"),
    ('p', "Se emplea una partición en tres bloques, estratificada por el desenlace y con "
          "semilla fija:"),
    ('b', "**Prueba** (25 %, n = 631,663). Se separa primero y no interviene en ninguna "
          "decisión de ajuste. Sobre él se calculan todas las métricas que se reportan."),
    ('b', "**Calibración** (20 % del resto, n = 378,998). Se usa exclusivamente para "
          "ajustar la transformación de calibración y los umbrales por grupo de la "
          "mitigación por post-procesamiento."),
    ('b', "**Entrenamiento** (el remanente, n = 1,515,988). Ajuste de los modelos."),
    ('p', "Tanto la calibración como los umbrales por entidad son parámetros estimados "
          "a partir de los datos; si se estiman sobre el conjunto de prueba, las "
          "métricas resultantes están sesgadas a favor del modelo. Separar el bloque de "
          "calibración es lo que permite después cuantificar ese sesgo en lugar de "
          "heredarlo. El apartado 3.6.4 reporta su magnitud, que resulta considerable."),

    # ------------------------------------------------------------------ 3.5
    ('h2', "3.5 Modelado"),
    ('p', "Esta fase produce el objeto de estudio de la tesis. Conviene subrayar el "
          "matiz: el modelo no es la aportación del trabajo, sino el sujeto sobre el "
          "que se practica la auditoría. Por eso la elección de la técnica privilegia "
          "la comparabilidad con el estado del arte por encima de la originalidad."),

    ('h3', "3.5.1 Técnicas y herramientas utilizadas"),
    ('p', "El algoritmo principal es un **ensamble de árboles con impulso del gradiente "
          "basado en histogramas**, en la implementación HistGradientBoostingClassifier "
          "de scikit-learn (Pedregosa et al., 2011). La elección responde a tres "
          "razones. Primera, para datos tabulares heterogéneos esta familia sigue "
          "siendo el punto de referencia práctico frente a las arquitecturas "
          "neuronales. Segunda, el agrupamiento previo de los valores en intervalos "
          "reduce el costo de entrenamiento lo suficiente para que el ajuste sobre 1.5 "
          "millones de registros sea viable en una estación de trabajo convencional "
          "(Ke et al., 2017). Tercera, y decisiva aquí, maneja los valores faltantes de "
          "forma nativa, lo que permite conservar la ausencia como información en lugar "
          "de imputarla."),
    ('p', "Como **modelo de contraste** se ajusta una regresión logística sobre el mismo "
          "conjunto de predictores. No compite por ser el modelo final: sirve para "
          "verificar que la ganancia del ensamble justifica su menor transparencia. El "
          "apartado 3.6.1 reporta la comparación, y el resultado condiciona la lectura "
          "de todo el trabajo."),
    ('p', "La tabla 7 documenta los hiperparámetros. Se fijaron por criterio y no por "
          "búsqueda exhaustiva, decisión que conviene declarar: una búsqueda en "
          "rejilla sobre millones de registros habría consumido el presupuesto de "
          "cómputo del proyecto para mejorar una métrica que no es el objeto de "
          "estudio. La semilla se fija en todas las etapas que involucran aleatoriedad "
          "—partición, ajuste y remuestreo— para que el flujo sea reproducible."),
    ('tab', "Hiperparámetros del modelo de referencia.",
     [["Hiperparámetro", "Valor", "Justificación"],
      ["max_iter", "300", "Número de árboles; suficiente para estabilizar la pérdida en validación"],
      ["learning_rate", "0.05", "Tasa conservadora, coherente con un número alto de iteraciones"],
      ["max_depth", "6", "Limita la interacción entre variables y contiene el sobreajuste"],
      ["class_weight", "balanced", "Compensa el desbalance de 16.9 a 1 ponderando la clase minoritaria"],
      ["random_state", "42", "Semilla fija para reproducibilidad"]]),
    ('p', "El entorno de ejecución es Python 3.14 con scikit-learn para el modelado y la "
          "calibración, pandas y pyarrow para el manejo del conjunto de datos, Fairlearn "
          "(Bird et al., 2020) para la mitigación por in-procesamiento, SciPy para las "
          "pruebas estadísticas y matplotlib para las figuras. Las versiones exactas se "
          "registran en el archivo de dependencias y en el manifiesto del conjunto de "
          "datos, de modo que el resultado sea reproducible."),

    ('h3', "3.5.2 Calibración del puntaje"),
    ('p', "Ponderar la función de pérdida para compensar el desbalance tiene una "
          "consecuencia poco discutida: los puntajes resultantes dejan de ser "
          "probabilidades y sobreestiman el riesgo absoluto. En este caso el riesgo "
          "medio predicho por el modelo crudo es de 20.54 % frente a una mortalidad "
          "observada de 5.60 %, es decir, casi cuatro veces mayor. Un puntaje así "
          "ordena bien a los pacientes, pero no puede interpretarse como probabilidad "
          "ni compararse entre grupos."),
    ('p', "La corrección es una **regresión isotónica** ajustada sobre el bloque de "
          "calibración (Zadrozny y Elkan, 2002), que no interviene en el "
          "entrenamiento. Por ser una transformación monótona preserva el ordenamiento "
          "—y con él el AUROC— mientras corrige el nivel. El efecto es el esperado: el "
          "puntaje de Brier baja de 0.0866 a 0.0323 y el riesgo medio predicho pasa a "
          "5.58 %, prácticamente idéntico al observado."),
    ('p', "Esta decisión no es un refinamiento técnico, sino un requisito del objeto de "
          "estudio. **La auditoría de equidad se realiza sobre el puntaje calibrado**, "
          "porque sin calibrar el error de calibración medido por grupo queda dominado "
          "por el sesgo global de entrenamiento y no por la inequidad entre grupos. La "
          "magnitud del efecto lo confirma: el error máximo de calibración por entidad "
          "pasa de 0.2108 con el puntaje crudo a 0.0231 con el calibrado. Auditar sobre "
          "el puntaje crudo habría producido un diagnóstico de inequidad geográfica que "
          "en realidad era un artefacto del entrenamiento."),

    ('h3', "3.5.3 Punto de operación"),
    ('p', "Toda métrica dependiente de umbral exige declarar el punto en el que se "
          "calcula. Un modelo no tiene una sensibilidad: tiene una sensibilidad por "
          "cada umbral posible. Comparar etapas o grupos en umbrales distintos produce "
          "diferencias que no son atribuibles al modelo."),
    ('p', "El punto de operación se fija en una **sensibilidad objetivo de 80 %**, "
          "elegida por criterio clínico: en un instrumento de triage cuyo fin es no "
          "dejar pasar a quien va a fallecer, el costo del falso negativo supera al del "
          "falso positivo. El umbral que alcanza esa sensibilidad sobre el bloque de "
          "calibración es **0.1562**, y produce en prueba una sensibilidad de 79.52 % "
          "con una tasa de falsos positivos de 5.92 %. Todas las métricas dependientes "
          "de umbral que se reportan en el apartado 3.6, y todas las comparaciones "
          "entre técnicas de mitigación, se calculan en ese mismo punto."),

    ('h3', "3.5.4 Técnicas de mitigación del sesgo"),
    ('p', "Se aplican las tres familias descritas en el apartado 2.3.5, una por cada "
          "etapa del flujo en la que es posible intervenir. La comparación bajo un "
          "punto de operación común es parte de la aportación del trabajo, porque la "
          "literatura suele reportar cada familia por separado."),
    ('b', "**Pre-procesamiento.** Reponderación de las observaciones por entidad "
          "federativa antes del ajuste, de modo que cada entidad contribuya a la "
          "pérdida en proporción distinta a su tamaño. Supone que la inequidad proviene "
          "del desequilibrio de representación."),
    ('b', "**In-procesamiento.** Reducción por gradiente exponenciado con restricción "
          "de igualdad de probabilidades de acierto y error, en la implementación de "
          "Fairlearn (Bird et al., 2020). Convierte el problema restringido en una "
          "secuencia de problemas ponderados. Supone que la inequidad puede corregirse "
          "durante la optimización."),
    ('b', "**Post-procesamiento.** Umbral de decisión específico por entidad, estimado "
          "sobre el bloque de calibración. Supone que el problema no está en el "
          "ordenamiento de los pacientes sino en dónde se corta, y es la única de las "
          "tres que usa el atributo sensible en el momento de la decisión."),
    ('p', "Sobre la tercera se construye además la **frontera de Pareto**, interpolando "
          "linealmente entre el umbral global τ y el umbral específico de cada entidad "
          "τg mediante τg(α) = (1 − α)·τ + α·τg, con α ∈ [0, 1]. Cada valor de α define "
          "una política de despliegue concreta, desde el modelo sin mitigar (α = 0) "
          "hasta la corrección completa por entidad (α = 1)."),

    # ------------------------------------------------------------------ 3.6
    ('h2', "3.6 Evaluación"),
    ('p', "La evaluación se organiza en los dos niveles anunciados en el apartado 3.1: "
          "primero el desempeño global frente a los criterios de éxito fijados en el "
          "3.2, después el desempeño desagregado que constituye la auditoría de "
          "equidad. El segundo nivel es el que produce los hallazgos de este trabajo."),

    ('h3', "3.6.1 Validación del desempeño global"),
    ('p', "Todas las cifras de este apartado se calculan sobre el bloque de prueba "
          "(n = 631,663), que no intervino en ninguna decisión de ajuste. El modelo "
          "calibrado alcanza un **AUROC de 0.9503** y un **AUPRC de 0.5533**. Este "
          "segundo valor debe leerse contra su línea base, que es la prevalencia del "
          "desenlace: 0.5533 frente a 0.056 representa una mejora de 9.88 veces sobre "
          "la clasificación aleatoria, lectura que el AUROC por sí solo no permite en "
          "cohortes desbalanceadas (Saito y Rehmsmeier, 2015). El puntaje de Brier es "
          "de 0.0323 y el error máximo de calibración por entidad, de 0.0231."),
    ('p', "La comparación con el modelo de contraste arroja un resultado que conviene "
          "reportar con honestidad: la regresión logística alcanza un AUROC de 0.9489 "
          "frente a 0.9503 del ensamble. La diferencia es de 0.0014, es decir, "
          "prácticamente nula. **La señal de estos datos es esencialmente lineal en los "
          "predictores admitidos**, y el ensamble no aporta capacidad explicativa "
          "adicional relevante. El hallazgo no invalida el diseño —el sujeto de la "
          "auditoría debe ser comparable al estado del arte, y lo es— pero sí obliga a "
          "no presentar la elección del algoritmo como una contribución."),
    ('p', "La importancia por permutación confirma esa lectura y concentra la señal en "
          "dos variables. La caída de AUROC al permutar NEUMONIA es de 0.1057 y al "
          "permutar EDAD de 0.0789; ninguna de las once restantes supera 0.003. El "
          "modelo es, en la práctica, un estimador basado en dos variables, con las "
          "comorbilidades aportando ajustes marginales."),
    ('p', "Frente a los criterios de éxito de la tabla 5, el desempeño global los "
          "cumple: AUROC por encima de 0.90, sensibilidad de 79.52 % en el punto de "
          "operación declarado y error de calibración por entidad muy por debajo de "
          "0.05. Si la evaluación terminara aquí, el proyecto se declararía exitoso."),

    ('h3', "3.6.2 Auditoría de equidad"),
    ('p', "El segundo nivel de evaluación desagrega esas mismas métricas por los valores "
          "del atributo sensible. La figura 3 muestra el desempeño entidad por "
          "entidad y la tabla 8 resume las brechas por cada eje auditado, "
          "calculadas como la diferencia entre el máximo y el mínimo por grupo en el "
          "punto de operación común."),
    ('tab', "Brechas de desempeño por eje de auditoría, en el punto de operación "
            "común (umbral 0.1562).",
     [["Eje", "Brecha de sensibilidad", "Brecha de FPR", "Brecha de AUROC", "Brecha de selección", "Error máx. de calibración"],
      ["Entidad federativa (32 grupos)", "0.2935", "0.0867", "0.0563", "0.1556", "0.0231"],
      ["Sexo (2 grupos)", "0.0393", "0.0268", "0.0082", "0.0448", "0.0005"],
      ["Grupo etario (4 grupos)", "0.5824", "0.3026", "0.0903", "0.4408", "0.0008"]]),
    ('p', "El resultado central es la primera fila. Un modelo con AUROC global de 0.9503 "
          "presenta una **brecha de sensibilidad de 29.35 puntos porcentuales entre "
          "entidades federativas**: la entidad mejor atendida por el modelo ve "
          "detectados cerca de treinta puntos más de sus casos fatales que la peor "
          "atendida, con el mismo umbral y el mismo puntaje calibrado. La hipótesis H1 "
          "queda sostenida por la evidencia."),
    ('fig', "equidad_por_entidad.png",
     "Desempeño del modelo desagregado por entidad federativa: AUROC y sensibilidad "
     "en el punto de operación común."),
    ('p', "La segunda fila ofrece un contraste útil. Por sexo, las brechas son de un "
          "orden de magnitud menor —3.93 puntos de sensibilidad— lo que indica que el "
          "modelo trata de forma comparable a hombres y mujeres. La tercera fila, en "
          "cambio, exhibe la mayor disparidad de todo el estudio: **58.24 puntos de "
          "sensibilidad entre grupos etarios**. El modelo detecta al 26.62 % de los "
          "casos fatales entre menores de 18 años y a una fracción muy superior entre "
          "adultos mayores. Esa disparidad no era el objeto de estudio y no se buscó, "
          "pero es demasiado grande para omitirla: el instrumento es, en su forma "
          "actual, inadecuado para población pediátrica."),

    ('h3', "3.6.3 Cuantificación de la incertidumbre"),
    ('p', "Con 32 grupos de tamaño muy desigual, la diferencia entre el máximo y el "
          "mínimo de 32 estimaciones ruidosas está sesgada al alza aun en ausencia de "
          "todo efecto. Reportar la brecha sin acompañarla de una medida de "
          "incertidumbre sería, por tanto, insuficiente. Se emplean dos procedimientos "
          "complementarios."),
    ('p', "El primero es un **remuestreo con 1000 réplicas** estratificado por entidad "
          "(Efron y Tibshirani, 1993), que produce un intervalo de confianza para cada "
          "brecha. La brecha de sensibilidad observada de 0.2935 tiene un intervalo de "
          "[0.2671, 0.3535], y la de AUROC de 0.0563 uno de [0.0496, 0.0697]. Ninguno "
          "de los dos se acerca al cero."),
    ('p', "El segundo es una **prueba de permutación con 1000 réplicas** sobre la "
          "etiqueta de entidad, que construye la distribución de la brecha bajo la "
          "hipótesis de que el modelo se comporta igual en todas ellas. Esa "
          "distribución nula tiene una mediana de 0.0737 y un percentil 95 de 0.1062 "
          "para la sensibilidad: es decir, el propio ruido del muestreo produce brechas "
          "aparentes de hasta diez puntos. La brecha observada de 0.2935 las supera con "
          "holgura, con un valor p de 0.001 tanto para la sensibilidad como para el "
          "AUROC."),
    ('p', "El criterio de soporte fijado en el apartado 2.4.3 —al menos 500 "
          "observaciones y 20 casos positivos por grupo— se cumple en las 32 entidades "
          "del bloque de prueba, de modo que ninguna queda excluida de la auditoría "
          "principal. En el análisis complementario restringido a los pacientes de 60 "
          "años o más, en cambio, Chiapas queda por debajo del umbral con 482 "
          "observaciones. El resultado se reporta con ambos criterios, en lugar de "
          "elegir el más favorable: excluyendo a Chiapas, el rango de AUROC entre las "
          "31 entidades restantes es de 0.2045, con Chihuahua como peor caso (0.7374); "
          "relajando el umbral a 300 observaciones para conservar las 32, el rango "
          "sube a 0.2537. La diferencia entre ambas cifras ilustra de forma concreta "
          "por qué el estadístico de brecha máxima es sensible a los grupos pequeños."),
    ('p', "El procedimiento aporta además una lectura que matiza el hallazgo. De los 496 "
          "pares de entidades comparables, solo el 52.6 % tiene intervalos de confianza "
          "disjuntos; es decir, en casi la mitad de los pares la diferencia observada no "
          "puede distinguirse del ruido. **La brecha global es real y significativa, "
          "pero el ordenamiento entidad por entidad no debe interpretarse como un "
          "ranking.** Los extremos —la mejor y la peor entidad— sí son distinguibles "
          "entre sí."),

    ('h3', "3.6.4 Evaluación de la mitigación y frontera de Pareto"),
    ('p', "La tabla 9 compara las tres familias de mitigación bajo el punto de operación "
          "común. La columna de exactitud balanceada mide el costo en desempeño global."),
    ('tab', "Comparación de las técnicas de mitigación en el punto de operación común.",
     [["Técnica", "Brecha de sensibilidad", "Brecha de FPR", "Tasa de selección", "Exactitud balanceada"],
      ["Sin mitigar (umbral global)", "0.294", "0.087", "0.100", "0.868"],
      ["Pre-procesamiento (reponderación)", "0.290", "0.082", "0.099", "0.865"],
      ["In-procesamiento (gradiente exponenciado)", "0.445", "—", "—", "—"],
      ["Post-procesamiento (umbral por entidad)", "0.140", "0.101", "0.102", "0.871"],
      ["Post-procesamiento, umbrales estimados en prueba", "0.022", "0.107", "0.101", "0.869"]]),
    ('p', "Tres lecturas se desprenden de la tabla. La primera es que el "
          "**pre-procesamiento no funciona** en este problema: reduce la brecha de "
          "0.294 a 0.290, una mejora indistinguible del ruido. Su supuesto —que la "
          "inequidad proviene del desequilibrio de representación— no describe este "
          "caso, y el resultado es coherente con la ausencia de correlación entre "
          "disparidad y tamaño de muestra (r = 0.024, p = 0.896)."),
    ('p', "La segunda es que el **in-procesamiento empeora la situación**, elevando la "
          "brecha de 0.294 a 0.445. El comportamiento es el previsto por la literatura "
          "para el régimen de muchos grupos pequeños: el método optimiza la brecha "
          "máxima, y con 32 grupos de tamaño desigual esa brecha está dominada por las "
          "entidades con menos datos, de modo que el algoritmo termina ajustándose al "
          "ruido de esos grupos."),
    ('p', "La tercera es que el **post-procesamiento sí funciona**: reduce la brecha de "
          "0.294 a 0.140 —a menos de la mitad— y lo hace sin costo, con una exactitud "
          "balanceada que pasa de 0.868 a 0.871. El criterio de éxito de la tabla 5, "
          "que admitía hasta dos puntos de pérdida, se cumple con holgura."),
    ('nota', "La última fila de la tabla 9 cuantifica el sesgo favorable que introduce "
             "estimar los umbrales sobre el mismo conjunto en el que se evalúan. Al "
             "hacerlo, la brecha aparente cae a 0.022 en lugar de 0.140: una reducción "
             "seis veces mayor, enteramente espuria. Es la razón por la que el bloque "
             "de calibración se separó desde el principio, y una advertencia para "
             "interpretar los resultados de mitigación publicados que no declaran dónde "
             "se estimaron sus umbrales."),
    ('p', "La figura 4 presenta la frontera de Pareto, que traslada el resultado "
          "anterior a un conjunto de políticas. Al recorrer α de 0 a 1, la brecha de "
          "sensibilidad desciende de 0.2935 a 0.1402 mientras la exactitud balanceada "
          "se mantiene entre 0.866 y 0.871, sin tendencia descendente. En este problema "
          "concreto **la disyuntiva entre equidad y desempeño no se materializa**: la "
          "corrección por umbral es esencialmente gratuita. El instrumento conserva su "
          "valor porque hace visible esa conclusión en lugar de postularla."),
    ('fig', "pareto_mitigacion.png",
     "Frontera de Pareto equidad–desempeño. Cada punto es una política de despliegue "
     "definida por el parámetro de interpolación α."),

    ('h3', "3.6.5 Análisis de sensibilidad y validación de la generalización"),
    ('p', "Tres comprobaciones adicionales acotan la validez de los hallazgos."),
    ('p', "La primera examina la **asociación con la marginación** que postula H2. La "
          "correlación entre el índice de CONAPO y la sensibilidad por entidad es de "
          "r = −0.178 con un valor p de 0.328, y con el AUROC de r = −0.071 con p de "
          "0.700. Agrupando por grado de marginación, las entidades de grado «muy alto» "
          "alcanzan un AUROC medio de 0.9485 y las de grado «muy bajo» de 0.9399: la "
          "diferencia, si acaso, va en sentido contrario al esperado. **H2 no queda "
          "sostenida por la evidencia.** La disparidad geográfica existe, pero la "
          "marginación socioeconómica agregada no la explica. Sí aparece en cambio una "
          "asociación con la tasa de mortalidad de la entidad (r = −0.373, p = 0.036), "
          "coherente con el mecanismo de prevalencia que formaliza el teorema de "
          "imposibilidad."),
    ('p', "La segunda es una **validación por dejar-una-entidad-fuera**: se reajustan 32 "
          "modelos, cada uno excluyendo del entrenamiento a una entidad, y se evalúa "
          "sobre la entidad excluida. La pérdida mediana de AUROC es de −0.0006, con un "
          "rango de −0.0108 a 0.0066, y 19 de las 32 entidades empeoran. La brecha de "
          "sensibilidad se mantiene en 0.2684 frente a 0.2935 del diseño interno. "
          "**La disparidad no proviene de que unas entidades estén sobrerrepresentadas "
          "en el entrenamiento**, porque persiste cuando ninguna lo está. Conviene "
          "insistir en que se trata de validación interna: usa la misma fuente y el "
          "mismo formato de captura, de modo que no sustituye a la validación externa "
          "que sustentaría H4."),
    ('p', "La tercera restringe la evaluación al **subconjunto de pacientes "
          "hospitalizados** (n = 297,685), donde el desenlace es efectivamente posible. "
          "El resultado es la limitación más seria del trabajo: el AUROC cae de 0.9503 "
          "a 0.7001 y el puntaje de Brier sube de 0.0323 a 0.2179. Buena parte de la "
          "discriminación aparente del modelo consistía en separar ambulatorios de "
          "hospitalizados, tarea más fácil que estimar el riesgo dentro del grupo "
          "hospitalizado. La brecha entre entidades, además, se agrava en términos de "
          "AUROC, de 0.0563 a 0.1494, con Chiapas en 0.611 y Tabasco en 0.7604. "
          "**Entre quienes efectivamente pueden fallecer, el modelo es mucho menos "
          "preciso y mucho más desigual de lo que sugiere la métrica global.**"),
    ('nota', "Este último resultado obliga a moderar cualquier lectura optimista de los "
             "apartados anteriores. El AUROC de 0.9503 es correcto para la tarea tal "
             "como se definió —estimar riesgo al primer contacto sobre todo caso "
             "confirmado— pero no debe leerse como la capacidad del modelo para "
             "ordenar por riesgo a los pacientes graves. El apartado 3.7 traslada esta "
             "restricción a las condiciones de despliegue."),

    # ------------------------------------------------------------------ 3.7
    ('h2', "3.7 Implementación"),
    ('p', "La fase de implementación de CRISP-DM responde a qué se hace con el modelo "
          "una vez evaluado. Conviene declarar de entrada el alcance: este trabajo **no "
          "despliega un sistema en producción** ni lo propone. Lo que entrega es un "
          "instrumento de decisión y un conjunto de condiciones que tendrían que "
          "satisfacerse antes de considerar un despliegue."),

    ('h3', "3.7.1 La solución propuesta"),
    ('p', "La solución tiene tres componentes. El primero es el **flujo de trabajo "
          "reproducible**, que va del archivo original de la DGE al conjunto analítico "
          "con un contrato de datos explícito entre etapas: cada artefacto intermedio "
          "se acompaña de un manifiesto con su procedencia, esquema, número de filas y "
          "tasas observadas, y ninguna etapa consume un artefacto sin verificarlo. Su "
          "valor no es el modelo que produce, sino que hace auditable el camino."),
    ('p', "El segundo es el **modelo calibrado con su punto de operación declarado**, "
          "serializado junto con la transformación de calibración y el umbral. Se "
          "entrega como una función que recibe las trece variables del primer contacto "
          "y devuelve una probabilidad de defunción interpretable como tal, no un "
          "puntaje sin escala."),
    ('p', "El tercero, y el que constituye la aportación de la tesis, es la **frontera "
          "de Pareto como instrumento de decisión**. Cada valor de α define una política "
          "de despliegue con su costo medido: α = 0 aplica un umbral único nacional y "
          "acepta una brecha de 29 puntos de sensibilidad; α = 1 aplica un umbral por "
          "entidad y la reduce a 14 puntos. La elección entre ellas es normativa y "
          "corresponde a quien autoriza el despliegue, no al analista. El entregable "
          "hace visible esa decisión en lugar de esconderla en un valor por omisión."),
    ('p', "Que la frontera resulte plana en este caso —la equidad se gana sin costo de "
          "desempeño— no resta valor al instrumento. Esa planitud es un hallazgo, no "
          "una propiedad conocida de antemano, y solo puede afirmarse porque se "
          "construyó la frontera completa."),

    ('h3', "3.7.2 Condiciones y restricciones de uso"),
    ('p', "Los resultados del apartado 3.6 imponen condiciones que cualquier "
          "implementación tendría que respetar."),
    ('b', "**Ámbito de aplicación.** El modelo estima riesgo al primer contacto sobre "
          "casos COVID confirmados. Entre pacientes ya hospitalizados su desempeño cae "
          "a un AUROC de 0.7001, de modo que **no debe usarse para priorizar dentro del "
          "hospital**, que es una tarea distinta y requeriría otro modelo."),
    ('b', "**Restricción por edad.** La brecha de sensibilidad entre grupos etarios es "
          "de 58 puntos y el modelo detecta apenas el 26.62 % de los casos fatales "
          "pediátricos. Su uso debe restringirse a población adulta hasta que se "
          "disponga de un modelo específico."),
    ('b', "**Umbral por entidad.** Si se adopta una política con α > 0, el umbral "
          "aplicable depende de la entidad y debe recalcularse con datos locales, no "
          "trasladarse de los valores aquí reportados."),
    ('b', "**Decisión asistida, no automática.** El puntaje es un insumo para el juicio "
          "clínico. Con una tasa de falsos positivos de 5.92 % en el punto de "
          "operación, un uso automático desplazaría recursos de forma sistemática sobre "
          "un volumen considerable de pacientes."),
    ('b', "**Validez temporal.** El modelo se ajustó sobre el corte de 2021, en una "
          "fase específica de la pandemia y con una población con cobertura de "
          "vacunación distinta de la actual. Su transportabilidad a otro periodo no se "
          "ha evaluado."),

    ('h3', "3.7.3 Monitoreo, gobernanza y trabajo pendiente"),
    ('p', "Un modelo desplegado es un sistema vivo, y la literatura de ingeniería "
          "documenta que su mantenimiento acumula deuda técnica con rapidez cuando no "
          "se instrumenta desde el inicio (Sculley et al., 2015). Tres mecanismos "
          "serían necesarios. El primero es el **monitoreo de la calibración por "
          "entidad**, que es el indicador más sensible a la deriva: un desplazamiento "
          "de la prevalencia local invalida el umbral antes de que el AUROC lo delate. "
          "El segundo es la **reauditoría periódica de las brechas**, con los mismos "
          "procedimientos de incertidumbre del apartado 3.6.3, porque una disparidad "
          "corregida en el despliegue puede reaparecer al cambiar la población. El "
          "tercero es el **registro de las decisiones asistidas**, sin el cual no es "
          "posible evaluar si el instrumento mejoró o empeoró los desenlaces reales."),
    ('p', "La gobernanza exige además que el punto de operación y la política α elegida "
          "sean decisiones documentadas y atribuibles, no configuraciones técnicas. La "
          "discusión sobre uso responsable de inteligencia artificial en el sector "
          "público mexicano está en curso, y un modelo de salud desplegado sin ese "
          "registro no sería auditable por terceros."),
    ('p', "Queda pendiente, y así se reporta, la **validación externa** sobre la base de "
          "Egresos Hospitalarios de la DGIS, que es la que sustentaría H4. La "
          "validación por dejar-una-entidad-fuera del apartado 3.6.5 evalúa la "
          "generalización geográfica dentro de la misma fuente y no la sustituye, "
          "porque el formato de captura y los criterios de registro son comunes a todas "
          "las entidades."),
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
          "resulta informativa, como documenta el apartado 3.3.4, y no conviene "
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
          "trabajo por deducción y no depende de los resultados empíricos que el "
          "capítulo 3 reporta."),
    ('p', "Conviene precisar la forma que toma en este conjunto de datos, porque las dos "
          "condiciones se verifican. Las tasas de mortalidad por entidad difieren por "
          "un factor de "
          "5.6, como documenta el apartado 3.3.5, y ningún modelo de riesgo clínico "
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
    ('p', "Este documento corresponde a la segunda entrega del proyecto terminal y "
          "cubre la introducción, el marco teórico y el marco metodológico completo, "
          "desarrollado sobre las seis fases de CRISP-DM. Las "
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
    ('p', "**Sobre el marco metodológico y sus resultados.** Las seis fases del "
          "proceso quedan cubiertas, y la evaluación en dos niveles produce el "
          "hallazgo central del trabajo: un modelo que satisface todos los criterios "
          "de éxito agregados —AUROC de 0.9503, sensibilidad de 79.52 % en el punto "
          "de operación y error de calibración por entidad de 0.0231— presenta una "
          "brecha de sensibilidad de 29.35 puntos porcentuales entre entidades "
          "federativas. La hipótesis H1 queda sostenida, con un intervalo de "
          "confianza de [0.2671, 0.3535] y un valor p de 0.001 frente a una "
          "distribución nula cuya mediana es de 0.0737."),
    ('p', "**Sobre las hipótesis que no se sostuvieron.** H2 no encuentra respaldo: la "
          "correlación entre el índice de marginación y la sensibilidad por entidad es "
          "de −0.178 con un valor p de 0.328. La disparidad geográfica existe, pero la "
          "marginación socioeconómica agregada no la explica; sí aparece en cambio una "
          "asociación con la tasa de mortalidad de la entidad (r = −0.373, p = 0.036), "
          "coherente con el mecanismo que formaliza el teorema de imposibilidad. El "
          "resultado obliga a reformular el mecanismo que H2 postulaba, y sugiere que "
          "los indicadores de infraestructura por unidad médica serían una medida más "
          "pertinente que el agregado estatal."),
    ('p', "**Sobre la mitigación.** De las tres familias evaluadas bajo un punto de "
          "operación común, solo el post-procesamiento resulta eficaz: reduce la "
          "brecha de 0.294 a 0.140 y lo hace sin costo en exactitud balanceada, que "
          "incluso mejora de 0.868 a 0.871. El pre-procesamiento no produce efecto "
          "apreciable y el in-procesamiento empeora la brecha hasta 0.445, "
          "comportamiento coherente con el régimen de muchos grupos pequeños y de "
          "tamaño desigual. La frontera de Pareto resulta plana, de modo que en este "
          "problema la disyuntiva entre equidad y desempeño no llega a materializarse."),
    ('p', "**Sobre la limitación más seria.** Restringida a los pacientes "
          "hospitalizados —el único subconjunto donde el desenlace es posible— la "
          "discriminación del modelo cae de un AUROC de 0.9503 a 0.7001, y la brecha "
          "de AUROC entre entidades se agrava de 0.0563 a 0.1494. Buena parte del "
          "desempeño aparente consistía en separar ambulatorios de hospitalizados. "
          "Este resultado condiciona toda lectura de las cifras globales y se traslada "
          "a las restricciones de uso del apartado 3.7.2."),
    ('p', "**Decisiones metodológicas que deben mantenerse.** Tres quedan fijadas por "
          "lo anterior y ya están incorporadas al capítulo 3, de modo que las etapas "
          "siguientes deben conservarlas. Primera, la auditoría se realiza sobre el "
          "puntaje calibrado, porque sobre el puntaje crudo el error de calibración por "
          "grupo mide el sesgo global de entrenamiento y no la inequidad: la diferencia "
          "entre 0.2108 y 0.0231 muestra la magnitud del artefacto que se evitaría. "
          "Segunda, toda métrica dependiente de umbral se reporta en un punto de "
          "operación único y declarado, para que las comparaciones entre etapas sean "
          "válidas. Tercera, las brechas se acompañan de una medida de incertidumbre, "
          "porque con 32 grupos de tamaño muy desigual el estadístico de brecha máxima "
          "está sesgado al alza."),
    ('p', "**Trabajo pendiente.** Quedan tres tareas, y así se reportan. La validación "
          "externa sobre una fuente independiente, que es la que sustentaría H4 y la "
          "única que permitiría afirmar que los hallazgos se transfieren fuera de la "
          "base de la DGE. El reentrenamiento del modelo sin la variable NEUMONIA, para "
          "acotar cuánto del desempeño y de la inequidad descansan en ese único "
          "predictor. Y la reformulación del mecanismo que H2 postulaba, con "
          "indicadores de infraestructura de salud por unidad médica en lugar del "
          "agregado socioeconómico estatal que resultó no explicar la disparidad."),
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

    "Chapman, P., Clinton, J., Kerber, R., Khabaza, T., Reinartz, T., Shearer, C., "
    "y Wirth, R. (2000). CRISP-DM 1.0: Step-by-step data mining guide. SPSS Inc.",

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

    "Efron, B., y Tibshirani, R. J. (1993). An introduction to the bootstrap. "
    "Chapman & Hall.",

    "Fayyad, U., Piatetsky-Shapiro, G., y Smyth, P. (1996). From data mining to "
    "knowledge discovery in databases. AI Magazine, 17(3), 37\u201354. "
    "https://doi.org/10.1609/aimag.v17i3.1230",

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

    "Mart\u00ednez-Plumed, F., Contreras-Ochando, L., Ferri, C., Hern\u00e1ndez-Orallo, J., "
    "Kull, M., Lachiche, N., Ram\u00edrez-Quintana, M. J., y Flach, P. (2021). CRISP-DM "
    "twenty years later: From data mining processes to data science trajectories. "
    "IEEE Transactions on Knowledge and Data Engineering, 33(8), 3048\u20133061. "
    "https://doi.org/10.1109/TKDE.2019.2962680",

    "M\u00e9ndez-Astudillo, J. (2024). The impact of comorbidities and economic inequality on "
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

    "Saito, T., y Rehmsmeier, M. (2015). The precision-recall plot is more "
    "informative than the ROC plot when evaluating binary classifiers on imbalanced "
    "datasets. PLOS ONE, 10(3), e0118432. "
    "https://doi.org/10.1371/journal.pone.0118432",

    "Sculley, D., Holt, G., Golovin, D., Davydov, E., Phillips, T., Ebner, D., "
    "Chaudhary, V., Young, M., Crespo, J.-F., y Dennison, D. (2015). Hidden "
    "technical debt in machine learning systems. En Advances in Neural Information "
    "Processing Systems 28 (pp. 2503\u20132511). Curran Associates.",

    "Shearer, C. (2000). The CRISP-DM model: The new blueprint for data mining. "
    "Journal of Data Warehousing, 5(4), 13\u201322.",

    "Van Calster, B., McLernon, D. J., van Smeden, M., Wynants, L., y Steyerberg, E. W. "
    "(2019). Calibration: The Achilles heel of predictive analytics. BMC Medicine, "
    "17(1), 230. https://doi.org/10.1186/s12916-019-1466-7",

    "Vickers, A. J., y Elkin, E. B. (2006). Decision curve analysis: A novel method for "
    "evaluating prediction models. Medical Decision Making, 26(6), 565–574. "
    "https://doi.org/10.1177/0272989X06295361",

    "Wirth, R., y Hipp, J. (2000). CRISP-DM: Towards a standard process model for "
    "data mining. En Proceedings of the 4th International Conference on the "
    "Practical Applications of Knowledge Discovery and Data Mining (pp. 29\u201339).",

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
        "**CRISP-DM:** Proceso de referencia para proyectos de minería de datos "
        "(Cross-Industry Standard Process for Data Mining). Divide el trabajo en seis "
        "fases —entendimiento del negocio, comprensión de los datos, preparación, "
        "modelado, evaluación e implementación— entre las que se admiten retornos.",
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
        "**Prueba de permutación:** Procedimiento que reasigna al azar la etiqueta de "
        "grupo muchas veces para construir la distribución de una brecha bajo la "
        "hipótesis de que el modelo se comporta igual en todos los grupos. Permite "
        "distinguir una disparidad real del ruido del muestreo.",
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
        "**Remuestreo:** Procedimiento que extrae repetidamente muestras con "
        "reemplazo del conjunto observado para estimar la variabilidad de un "
        "estadístico y construir intervalos de confianza sin suponer una "
        "distribución teórica.",
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
    ("CRISP-DM", "Proceso estándar intersectorial para minería de datos (del "
                 "inglés “Cross-Industry Standard Process for Data Mining”)"),
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
    ("KDD", "Descubrimiento de conocimiento en bases de datos (del inglés "
             "“Knowledge Discovery in Databases”)"),
    ("MCDI", "Maestría en Ciencia de Datos e Información"),
    ("ML", "Aprendizaje automático (del inglés “Machine Learning”)"),
    ("ROC", "Característica operativa del receptor (del inglés "
             "“Receiver Operating Characteristic”)"),
    ("SEMMA", "Muestrear, explorar, modificar, modelar y evaluar (del inglés "
               "“Sample, Explore, Modify, Model, Assess”)"),
    ("SHAP", "Explicaciones aditivas de Shapley (del inglés "
              "“SHapley Additive exPlanations”)"),
    ("TDSP", "Proceso de ciencia de datos en equipo (del inglés "
              "“Team Data Science Process”)"),
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
          "en el apartado 3.4.1. La columna «Disponible al primer contacto» es el "
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
          "el análisis descriptivo del apartado 3.3.4, pero no se emplean como entradas "
          "del modelo."),
]
