DOCUMENTO DE FUNDAMENTACIÓN
Maestría en Ciencia de Datos
¿Por qué este tema de tesis?
Justificación integral para desarrollar —y sostener— una auditoría de equidad de modelos de riesgo clínico, con énfasis en el sesgo geográfico, sobre datos abiertos de salud de México
David Segundo
Julio 2026

# Índice

# Cómo usar este documento
Este texto responde a una sola pregunta con toda la profundidad posible: por qué vale la pena tomar este tema de tesis y, sobre todo, por qué conviene sostenerlo hasta el final en lugar de cambiarlo a medio camino. Está pensado como tu 'documento ancla': el que revisas cuando dudes de la decisión, y del que puedes extraer párrafos casi textuales para el capítulo de justificación de la tesis, para la carta de exposición de motivos ante tu comité, o para explicar el proyecto a un tercero. Se organiza de lo general (el problema de salud del país) a lo particular (tus objetivos personales), y cierra con una sección honesta sobre riesgos y por qué son manejables.
# 1. Resumen ejecutivo: siete razones en una página
Antes del detalle, la tesis en su forma más comprimida. Este tema es el correcto por siete razones que se refuerzan entre sí:
- Importa de verdad. México vive una epidemia de enfermedades crónicas —diabetes, hipertensión, obesidad— que son la principal causa de muerte del país; predecir el riesgo grave tiene impacto real.
- Los datos existen y son gratuitos. La base abierta de la Secretaría de Salud te permite empezar hoy, sin trámites largos ni costos, con millones de registros reales mexicanos.
- Es técnicamente completo. Toca todo el ciclo de la ciencia de datos: limpieza, modelado, evaluación, explicabilidad y ética, lo que lo hace ideal para demostrar dominio de maestría.
- Tiene un diferenciador verificado. La revisión de literatura confirmó que la predicción de desenlaces con datos mexicanos ya está saturada, pero la auditoría de equidad geográfica entre entidades federativas sobre esos datos no existe: ahí está tu originalidad.
- Es aplicable a México. Al usar datos del propio sistema de salud, tus resultados son transferibles al contexto nacional, que es exactamente tu meta.
- Es una buena inversión profesional. La IA en salud es uno de los mercados de mayor crecimiento en la región y la demanda de estos perfiles se dispara.
- Es viable en tiempo y recursos. El alcance está acotado, los datos son tabulares y las herramientas son abiertas: se puede terminar en el plazo de una maestría.
# 2. El problema importa: la carga de enfermedad en México
La primera prueba que debe pasar cualquier tema de tesis es la de la relevancia: ¿resuelve o ilumina un problema que le importa a alguien más allá del autor? En este caso la respuesta es contundente, y las cifras oficiales lo respaldan.
## 2.1 Una epidemia metabólica
Según la Encuesta Nacional de Salud y Nutrición (ENSANUT 2022), el 18.4% de los adultos mayores de 20 años vive con diabetes (12.6% diagnosticada y 5.8% sin diagnosticar), y el 75.2% presenta sobrepeso u obesidad. La prevalencia de obesidad creció 21.4% entre 2006 y 2022. No se trata de padecimientos marginales: describen el estado de salud de la mayoría de la población adulta del país.
## 2.2 Y son la principal causa de muerte
El INEGI registró 796,321 defunciones en México durante 2024. Las enfermedades del corazón encabezan la lista, seguidas por la diabetes mellitus y los tumores malignos. Diabetes e hipertensión no solo son frecuentes: matan, y lo hacen a gran escala. La siguiente tabla sintetiza el panorama.

| Indicador | Cifra | Fuente |
|---|---|---|
| Adultos con diabetes (>20 años) | 18.4% | ENSANUT 2022 |
| Adultos con sobrepeso u obesidad | 75.2% | ENSANUT 2022 |
| Aumento de obesidad 2006–2022 | +21.4% | ENSANUT 2022 |
| Defunciones totales en México, 2024 | 796,321 | INEGI (EDR 2024) |
| Primeras causas de muerte | Cardiovasculares, diabetes, tumores | INEGI (EDR 2024) |

Qué significa para tu tesis: un modelo que estratifique el riesgo de hospitalización y muerte en pacientes con estas comorbilidades no es un ejercicio académico abstracto; ataca el núcleo del perfil epidemiológico mexicano. Esa es una justificación de peso que ningún jurado va a cuestionar.
# 3. Por qué la ciencia de datos es la herramienta adecuada
Que el problema sea importante no basta; hay que mostrar que tu disciplina puede aportar algo que otras no. En sistemas de salud con recursos limitados —camas, personal, equipo—, la pregunta operativa recurrente es a quién priorizar. Los modelos predictivos convierten datos que ya se recolectan de todos modos en una señal accionable de riesgo, sin costo marginal de recolección.
La ciencia de datos encaja aquí por tres motivos. Primero, hay volumen y estructura: millones de registros tabulares con desenlaces conocidos, condiciones ideales para el aprendizaje supervisado. Segundo, el problema es de estratificación de riesgo, exactamente la clase de tarea donde los modelos calibrados superan a las reglas heurísticas. Tercero, la salud exige explicabilidad y equidad, y el estado del arte de la ciencia de datos —valores SHAP, métricas de fairness— ya ofrece herramientas maduras para ambas. En pocas palabras: el problema pide justo lo que tu maestría enseña.
# 4. Por qué estos datos: la base abierta de la Secretaría de Salud
La elección del conjunto de datos suele decidir el éxito o el naufragio de una tesis. Muchos proyectos mueren esperando acceso a datos clínicos o atrapados en trámites de comités de ética. Este dataset evita ese destino.
- Acceso inmediato y gratuito. Es de descarga pública, con diccionario de datos y catálogos; puedes empezar el análisis exploratorio esta misma semana.
- Escala real. Cerca de 2.9 millones de casos: suficiente para entrenar modelos robustos, validar por subgrupos y hacer análisis de equidad con potencia estadística.
- Riqueza clínica. Incluye edad, sexo, entidad, comorbilidades (diabetes, hipertensión, obesidad, EPOC, asma, ERC, inmunosupresión, tabaquismo), y desenlaces claros: hospitalización, UCI, intubación y defunción.
- Bajo riesgo ético. No contiene identificadores directos, lo que simplifica enormemente el manejo de privacidad frente a datos de expediente clínico.
- Es mexicano. Los patrones que aprenda el modelo reflejan a la población del país, no a cohortes extranjeras que luego no generalizan.
- Tiene literatura de referencia. Ya existen estudios que usaron esta base para estimar factores de riesgo, lo que te da puntos de comparación y valida que el dato sirve.
Una objeción previsible es que se trata de datos de COVID-19, un tema que parece del pasado. La respuesta es que el objeto de estudio real no es el virus, sino la relación entre comorbilidades crónicas y desenlace grave —una pregunta permanente— y que este dataset es simplemente el mejor vehículo público disponible para estudiarla en población mexicana. Además, la sección 9 explica cómo la base de Egresos Hospitalarios de la DGIS sirve como puente natural hacia un objeto de estudio aún más general.
# 5. El diferenciador verificado: equidad geográfica sobre datos mexicanos
Un modelo predictivo de riesgo, por sí solo, ya no es novedoso. La revisión del estado del arte —con fuentes verificadas una por una— lo confirmó: predecir hospitalización o mortalidad por COVID-19 con la base abierta mexicana está saturado. Becerra-Sánchez et al. (Diagnostics, 2022) alcanzan ~90% de exactitud sobre datos mexicanos, y Méndez-Astudillo (Frontiers in Big Data, 2024) modela la mortalidad con Random Forest y XGBoost cruzando comorbilidades y desigualdad económica. Replicar ese camino sería producir un trabajo derivativo.
Incluso lo geográfico ya se abordó: un estudio de 2024 (Computación y Sistemas) muestra que la ubicación pesa más que la edad como predictor de mortalidad. Pero ahí está la sutileza que hace original a tu tesis: ese trabajo usa la geografía como variable de entrada ('¿dónde vives predice tu desenlace?'), mientras que tú la usarás como eje de auditoría ('¿el modelo se equivoca más en unas entidades que en otras, y cómo lo corrijo?'). Son preguntas distintas, y la segunda no está resuelta para México.
La equidad algorítmica en salud es un campo maduro a nivel internacional (por ejemplo, Nejadshamsi et al. en JAMIA Open, 2026, con datos de Canadá), pero anclado fuera de México y en atributos como sexo o raza/etnia. No se identificó ningún trabajo que audite y mitigue el sesgo de desempeño entre entidades federativas sobre datos clínicos mexicanos. Ese es, literalmente, el hueco que ocupa tu tesis.
Reencuadrar el modelo predictivo como línea de base y colocar la equidad geográfica en el centro eleva la tesis en tres dimensiones. En lo académico, la vuelve original y publicable, porque ataca un vacío documentado. En lo técnico, te obliga a dominar métricas y métodos de frontera (equalized odds, reponderación, ajuste de umbrales por entidad, fronteras de Pareto). Y en lo ético, convierte al trabajo en una salvaguarda: su propósito explícito es impedir que la IA amplifique las desigualdades regionales de salud del país.
# 6. Pertinencia nacional: aplicable al sector salud de México
Tu meta declarada es aplicar o enfocar el trabajo en el sector salud mexicano. Este tema cumple esa meta por construcción, no como añadido. Al entrenar y validar con datos del propio sistema de salud del país, los hallazgos —qué comorbilidades pesan más, cómo se distribuye el riesgo entre entidades, dónde el modelo es menos justo— son directamente interpretables y accionables para instituciones mexicanas.
La estrategia de validación refuerza esta pertinencia: al evaluar el modelo dejando una entidad federativa fuera, se estima explícitamente qué tan bien generaliza a regiones no vistas, un problema muy concreto para un país tan heterogéneo como México. Y el análisis de equidad por entidad produce, casi como subproducto, un mapa de dónde el modelo funciona peor, información valiosa para cualquier despliegue nacional.
# 7. Buena inversión profesional: el mercado te acompaña
Una tesis también es una carta de presentación profesional, y esta apunta a un mercado en expansión acelerada. El mercado latinoamericano de IA en salud pasó de 0.47 mil millones de dólares en 2024 a una proyección de 3.78 mil millones en 2033, con una tasa de crecimiento anual compuesta cercana al 26%. México, en particular, muestra el crecimiento más rápido de la región: la demanda de habilidades de IA y aprendizaje automático subió 148% desde 2023.
Traducido a tu carrera: al terminar tendrás un portafolio demostrable en el cruce de tres competencias muy solicitadas —ciencia de datos aplicada, dominio de salud e IA responsable/equidad— sobre datos reales y con impacto social. Es un perfil difícil de encontrar y fácil de defender en una entrevista o ante un comité académico.

| Señal de mercado | Dato | Fuente |
|---|---|---|
| IA en salud, LatAm (2024 → 2033) | USD 0.47B → 3.78B (CAGR ~26%) | IMARC / Grand View |
| Demanda de IA/ML en México desde 2023 | +148% | Reportes de talento IA |
| Posición de México en la región | Mayor crecimiento proyectado | Grand View Research |

# 8. Viabilidad: por qué sí se puede terminar
Un tema puede ser importante y original y aun así ser un mal tema de tesis si no se puede completar en el tiempo disponible. Este supera también esa prueba.
- Datos listos. No dependes de que un hospital te entregue información; el cuello de botella más común de las tesis de salud desaparece.
- Datos tabulares. No requieren la infraestructura ni el cómputo de imágenes médicas o modelos de lenguaje grandes; corren en una laptop o en cómputo modesto en la nube.
- Herramientas abiertas y maduras. Python, scikit-learn, XGBoost/LightGBM, SHAP y Fairlearn/AIF360 están documentadas, son gratuitas y tienen comunidad amplia.
- Alcance modular. Si el tiempo aprieta, el modelo neuronal tabular o la validación externa pueden recortarse sin comprometer el núcleo; si sobra tiempo, se amplían. El proyecto escala con tu calendario.
- Cronograma realista. El protocolo lo distribuye en doce meses con hitos claros, dejando margen para la escritura y la defensa.
# 9. Originalidad, continuidad y por qué no cambiar de tema
La pregunta que planteaste —por qué seguir con esta parte— merece respuesta directa. Cambiar de tema a medio camino es una de las formas más comunes de retrasar o descarrilar una tesis: se pierde el trabajo de revisión, la familiaridad con los datos y el impulso. Sostener este tema es racional por varias razones.
Primero, el tema tiene profundidad suficiente para no agotarse: puedes empezar simple (un modelo de riesgo bien hecho) y, si te entusiasma, profundizar en equidad, en calibración o en explicabilidad, sin cambiar de datos ni de pregunta. Segundo, tiene una ruta de crecimiento natural: la base de Egresos Hospitalarios de la DGIS (2008–2024) permite validar el modelo en una fuente independiente y, más adelante, generalizar de COVID-19 a enfermedades crónicas en general. Es decir, el tema no es un callejón sin salida, sino la puerta de entrada a una línea de investigación que puede extenderse incluso más allá de la maestría.
Empezar con datos de COVID-19 no te encasilla: es el punto de partida más accesible hacia una pregunta permanente —cómo las comorbilidades crónicas determinan el desenlace grave— que puedes seguir explorando con otras bases mexicanas por años.
Tercero, cada componente que ya definiste (limpieza documentada, modelado comparativo, equidad, explicabilidad) es reutilizable. Aunque algún día decidieras aplicarlo a otro padecimiento, el 80% de tu metodología se mantiene. Eso hace que el esfuerzo invertido hoy rinda mañana, lo que es el mejor argumento posible para no abandonar el rumbo.
# 10. Alineación con tus intereses y objetivos
Mencionaste que te gustaría trabajar en la intersección de medicina y datos, y aplicar el trabajo al sector salud de México. Este tema no solo lo permite: lo pone en el centro. Trabajarás con datos clínicos reales, aprenderás el vocabulario y las restricciones del dominio médico (calibración, utilidad clínica, humano en el circuito), y construirás algo cuya utilidad se mide en decisiones de atención. Si tu intención es seguir en salud digital, esta tesis es el primer proyecto de tu portafolio en esa dirección; si más adelante pivotas a otro sector, las competencias en modelado responsable, equidad y explicabilidad son plenamente transferibles.
# 11. Riesgos honestos y por qué son manejables
Ningún tema está libre de riesgos; ocultarlos sería un mal servicio. Estos son los principales y su mitigación.

| Riesgo | Mitigación |
|---|---|
| Percepción de que COVID-19 es un tema 'viejo' | Reencuadrar el objeto de estudio como la relación comorbilidad–desenlace grave; posicionar la equidad como el aporte central. |
| Fuga de información (usar variables posteriores al desenlace) | Definir con rigor la ventana temporal de cada predictor y excluir variables post-hoc; documentarlo en la metodología. |
| Calidad del dato (categorías 'no especificado') | Estrategias explícitas de imputación e indicadores de faltante; análisis de sensibilidad. |
| Desbalance de clases | Ponderación de clase y ajuste de umbral clínico en lugar de sobremuestreo ingenuo; verificar calibración. |
| Alcance que se agranda | Diseño modular: núcleo mínimo garantizado + extensiones opcionales según el tiempo disponible. |

La conclusión práctica es que los riesgos de esta tesis son conocidos, acotados y tienen soluciones estándar en la literatura. No hay incertidumbres estructurales —como depender de un permiso que quizá nunca llegue— que puedan hundir el proyecto.
# 12. Conclusión: la decisión correcta, y sostenida
Tomar este tema es una decisión sólida porque satisface, a la vez, todas las pruebas que un buen tema de tesis debe pasar: importa a nivel de salud pública, es factible con datos que ya tienes, es técnicamente completo, es original gracias al eje de equidad, es aplicable a México y es una buena inversión para tu carrera. Sostenerlo hasta el final es igual de racional: el tema tiene profundidad, una ruta de crecimiento clara y una metodología reutilizable, de modo que cada semana de trabajo se acumula en lugar de perderse.
Dicho de la forma más simple: no es solo un tema que puedes hacer, es un tema que vale la pena hacer y terminar. Y esa combinación —factible, valioso y sostenible— es exactamente lo que separa una tesis que se concluye de una que se abandona.
# 13. Fuentes
- ENSANUT 2022 — Instituto Nacional de Salud Pública (INSP): prevalencia de diabetes, sobrepeso y obesidad.
- INEGI — Estadísticas de Defunciones Registradas (EDR) 2024: causas de muerte y total de defunciones.
- IMARC Group / Grand View Research — Mercado de IA en salud en América Latina, 2024–2033.
- Reportes de talento y adopción de IA en México — crecimiento de la demanda de habilidades de IA/ML.
- Dirección General de Epidemiología, Secretaría de Salud — base abierta de COVID-19 y diccionario de datos (fuente primaria del proyecto).
- Estado del arte verificado: Becerra-Sánchez et al. (Diagnostics, 2022) y Méndez-Astudillo (Frontiers in Big Data, 2024) como línea de base predictiva mexicana; el estudio de factores geográficos (Computación y Sistemas, 2024) como geografía-predictora; y Nejadshamsi et al. (JAMIA Open, 2026) como fairness fuera de México — en conjunto confirman el vacío de auditoría de equidad por entidad sobre datos mexicanos.
Las URLs de las fuentes se incluyen en el mensaje que acompaña este documento.
