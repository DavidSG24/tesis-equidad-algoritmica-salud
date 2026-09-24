PROTOCOLO DE TESIS DE MAESTRÍA
Maestría en Ciencia de Datos
Estratificación de riesgo clínico consciente de la equidad: auditoría y mitigación del sesgo geográfico entre entidades federativas en modelos predictivos con datos abiertos de salud de México, con validación externa
Autor: David Segundo
Julio 2026

# Índice

# 1. Resumen
Este protocolo propone un marco de estratificación de riesgo clínico consciente de la equidad. A diferencia de los numerosos trabajos que ya predicen hospitalización o mortalidad por COVID-19 con datos mexicanos, el objeto central de esta tesis no es el desempeño predictivo —que se toma como base resuelta—, sino la justicia del modelo entre subpoblaciones, con énfasis en el sesgo geográfico entre entidades federativas, una dimensión ligada a la desigualdad estructural de infraestructura de salud en México y prácticamente inexplorada en la literatura. Se utilizará la base abierta de COVID-19 de la Dirección General de Epidemiología (DGE) de la Secretaría de Salud (~2.9 millones de registros). El trabajo (i) construye modelos de riesgo de referencia, (ii) audita su equidad por entidad, sexo y grupo etario —y de forma exploratoria en subgrupos interseccionales—, (iii) aplica y compara técnicas de mitigación de sesgo, produciendo una frontera de Pareto entre desempeño y equidad como herramienta de decisión, y (iv) valida externamente la transportabilidad del modelo y de su equidad en la base de Egresos Hospitalarios de la DGIS (2008–2024), un paso que la literatura previa casi nunca da.
# 2. Planteamiento del problema
La saturación hospitalaria y la asignación de recursos escasos son retos persistentes del sistema de salud mexicano. Contar con herramientas que estimen tempranamente el riesgo de un desenlace grave permite priorizar la atención y anticipar necesidades de camas y ventiladores. Sin embargo, la literatura reciente muestra que el problema puramente predictivo ya está ampliamente resuelto para el caso mexicano: existen múltiples modelos con buen desempeño.
El problema no abordado es otro: un modelo puede tener excelente desempeño promedio y, al mismo tiempo, ser sistemáticamente menos preciso para habitantes de entidades con menor infraestructura, para personas mayores o para un sexo determinado. En un país tan heterogéneo como México, un modelo entrenado con datos dominados por entidades urbanas puede desempeñarse peor justo donde el sistema de salud es más débil, amplificando la inequidad en lugar de reducirla. El problema central de esta tesis es, por tanto, diagnosticar y corregir la inequidad del modelo —especialmente la geográfica— sin sacrificar de forma inaceptable su utilidad clínica.
# 3. Trabajos relacionados y vacío de investigación
Esta sección se basa en una revisión de fuentes verificadas individualmente (autor, año, revista y datos empleados). La revisión confirma tres hechos que orientan el diseño de la tesis: la predicción de desenlaces por COVID-19 con datos mexicanos está saturada; los factores geográficos ya se han estudiado, pero como variables predictoras y no como eje de equidad; y la auditoría de equidad sobre datos clínicos mexicanos permanece como un vacío.
## 3.1 La parte predictiva mexicana está saturada
Múltiples trabajos peer-reviewed ya construyen modelos de riesgo sobre la base abierta mexicana con buen desempeño:
- Becerra-Sánchez et al. (2022), Diagnostics (MDPI). Comparan varios modelos sobre datos mexicanos; el mejor (red neuronal) alcanza ~90% de exactitud y F1 de 89.64%, identificando neumonía, edad avanzada e intubación como principales factores de mortalidad.
- Méndez-Astudillo (2024), Frontiers in Big Data. Random Forest y XGBoost sobre más de 20 millones de observaciones mexicanas; concluye que diabetes e hipertensión, junto con la desigualdad económica, definen la mortalidad.
- Otros. Existen trabajos adicionales en Computación y Sistemas (2023), medRxiv (2023) y publicaciones de acceso variado que abordan la misma tarea predictiva sobre la base mexicana. Nota metodológica: algunas de estas fuentes son de baja credibilidad editorial (por ejemplo, revistas estudiantiles) y no se usarán como referencia de autoridad; solo se citan las peer-reviewed verificadas.
Implicación: replicar 'clasificador + SHAP + comorbilidades' sobre esta base sería un trabajo derivativo. Por eso el modelo predictivo se adopta como línea de base y no como aportación.
## 3.2 Lo geográfico ya se estudió, pero como predictor —no como equidad
Un trabajo mexicano reciente (Computación y Sistemas, 2024) muestra que los factores de ubicación —municipio, unidad médica, entidad de nacimiento y de residencia— superan incluso a la edad como predictores de mortalidad por COVID-19 en México. Es un hallazgo relevante que debe reconocerse explícitamente, pero responde a una pregunta distinta de la de esta tesis.
La diferencia es sustantiva. Ese estudio usa la geografía como variable de entrada para responder '¿dónde vives predice tu desenlace?' (epidemiología espacial e importancia de variables). Esta tesis usa la geografía como eje de auditoría para responder '¿el modelo comete más errores en unas entidades que en otras, y cómo se corrige esa inequidad?' (equidad algorítmica y mitigación). No se identificó ningún trabajo que aborde esta segunda pregunta sobre datos mexicanos.
## 3.3 La equidad algorítmica en salud es madura, pero fuera de México
La literatura de fairness en salud es rica, pero está anclada en otros contextos y otros atributos sensibles. Nejadshamsi et al. (JAMIA Open, 2026) auditan y mitigan el sesgo por sexo en clasificación de severidad de COVID-19 usando datos de Canadá (Quebec Biobank); otros trabajos abordan la equidad en el pronóstico de pandemias sobre datos de Estados Unidos. Ninguno usa datos mexicanos ni trata la entidad federativa como atributo sensible ligado a la desigualdad de infraestructura de salud.
## 3.4 El vacío que ocupa esta tesis

| Dimensión | Estado en la literatura | Aporte de esta tesis |
|---|---|---|
| Predicción de desenlace (MX) | Saturado (Becerra-Sánchez 2022; Méndez-Astudillo 2024) | Línea de base, no aportación |
| Geografía como predictor (MX) | Estudiado (Comp. y Sistemas 2024) | Se distingue: geografía como eje de equidad |
| Fairness en salud | Maduro, pero fuera de MX (JAMIA Open 2026) | Se traslada y adapta al contexto mexicano |
| Auditoría de equidad por entidad (MX) | No identificado | Eje central y original |
| Mitigación + frontera de Pareto (MX) | No identificado | Herramienta de decisión entregable |
| Validación externa de la equidad | Rara vez realizada | Transportabilidad a la base DGIS |

En una frase: sabemos que la geografía predice la mortalidad en México y que la equidad algorítmica importa en otros países, pero nadie ha preguntado todavía si un modelo clínico entrenado con datos mexicanos es igual de preciso entre entidades federativas, ni cómo corregir esa inequidad. Esa es la contribución.
# 4. Justificación
La relevancia del proyecto se sostiene en cuatro pilares. Datos: la base de la DGE es pública, masiva y con desenlace claro, lo que permite empezar de inmediato. Pertinencia nacional: al usar datos del propio sistema de salud mexicano y tratar la entidad federativa como eje, los hallazgos son directamente transferibles a la política de salud del país. Originalidad: la equidad geográfica sobre datos mexicanos es un vacío documentado (sección 3). Impacto: una frontera de Pareto equidad–desempeño es un insumo concreto para reguladores que deban decidir el umbral aceptable de un modelo antes de desplegarlo.
# 5. Preguntas de investigación
- Dado un modelo de riesgo con buen desempeño global sobre datos mexicanos, ¿existen disparidades de desempeño estadísticamente significativas entre entidades federativas, grupos etarios y sexos?
- ¿Cómo se relaciona la magnitud del sesgo geográfico con indicadores de infraestructura o marginación de cada entidad?
- ¿Qué técnicas de mitigación (pre, in y post procesamiento) reducen mejor esas disparidades, y cuál es el costo en desempeño global expresado como frontera de Pareto?
- ¿Se transfieren tanto el desempeño como la equidad del modelo a una fuente de datos independiente (Egresos Hospitalarios de la DGIS)?
- De forma exploratoria, ¿aparecen inequidades adicionales en subgrupos interseccionales (por ejemplo, adultos mayores de entidades marginadas)?
# 6. Objetivos
## 6.1 Objetivo general
Desarrollar, auditar y mitigar la equidad —con énfasis en el sesgo geográfico entre entidades federativas— de un modelo de estratificación de riesgo clínico basado en datos abiertos de salud de México, validando externamente su transportabilidad.
## 6.2 Objetivos específicos
- Construir un pipeline reproducible de ingesta, limpieza y preparación de la base de la DGE, con control estricto de fuga de información.
- Entrenar un modelo de riesgo de referencia (regresión logística y gradient boosting) con desempeño comparable al estado del arte, como base para el análisis de equidad.
- Auditar la equidad del modelo por entidad federativa, sexo y grupo etario, y correlacionar el sesgo geográfico con indicadores de infraestructura/marginación.
- Aplicar y comparar técnicas de mitigación de sesgo en las tres etapas del pipeline, construyendo la frontera de Pareto entre equidad y desempeño.
- Validar externamente el modelo y su equidad en la base de Egresos Hospitalarios de la DGIS.
- Explorar la equidad en subgrupos interseccionales y traducir los hallazgos a recomendaciones de despliegue.
# 7. Hipótesis
H1. Un modelo con buen desempeño global presentará disparidades de desempeño estadísticamente significativas entre entidades federativas, medibles por equalized odds y calibración por grupo.
H2. La magnitud del sesgo geográfico se asociará negativamente con la infraestructura de salud de cada entidad (peor desempeño donde hay menos recursos).
H3. Las técnicas de mitigación reducirán las disparidades con una pérdida de desempeño global inferior a un umbral predefinido, cuantificable mediante la frontera de Pareto.
H4. El desempeño se transferirá razonablemente a la base DGIS, pero las disparidades de equidad podrían acentuarse, evidenciando la necesidad de recalibrado por contexto.
# 8. Marco teórico
El marco integra tres cuerpos de literatura. En modelos de riesgo clínico se revisan enfoques de predicción de gravedad y mortalidad, con énfasis en calibración y utilidad clínica. En aprendizaje automático tabular se contrastan ensambles de árboles con impulso del gradiente (XGBoost, LightGBM) frente a arquitecturas neuronales para tablas (FT-Transformer, TabNet). En equidad algorítmica se adoptan las definiciones de paridad estadística, igualdad de oportunidades y equalized odds, el teorema de imposibilidad que impide satisfacerlas simultáneamente, y el conjunto de técnicas de mitigación pre, in y post procesamiento. Un apartado específico aborda la equidad de subgrupos pequeños e interseccionales, un problema abierto especialmente pertinente al desagregar por entidad federativa.
# 9. Metodología
## 9.1 Fuentes de datos
Fuente primaria: base abierta de COVID-19 de la DGE (Secretaría de Salud), ~2.9 millones de casos con variables demográficas, entidad de residencia, comorbilidades y desenlaces (hospitalización, UCI, intubación, defunción). Fuente de validación externa: Subsistema Automatizado de Egresos Hospitalarios de la DGIS (2008–2024). Fuente de contexto: indicadores de infraestructura de salud y marginación por entidad (por ejemplo, camas por habitante), para correlacionar con el sesgo geográfico.
## 9.2 Desenlaces, predictores y atributos sensibles
Objetivo: hospitalización y mortalidad como clasificación binaria, usando solo variables disponibles al ingreso (control estricto de fuga de información).
Atributos sensibles: entidad federativa (eje central), sexo y grupo etario; combinaciones interseccionales de forma exploratoria.
## 9.3 Modelo de referencia
Se entrena una línea de base sólida (regresión logística regularizada y gradient boosting con optimización bayesiana), buscando desempeño comparable al estado del arte. Este modelo no es la aportación, sino el sujeto de la auditoría de equidad.
## 9.4 Auditoría de equidad
Se cuantifican disparidades por grupo con Fairlearn/AIF360: diferencias en TPR/FPR (equalized odds), paridad demográfica y calibración por grupo, con intervalos de confianza. Para la dimensión geográfica se estima el desempeño por entidad y se correlaciona con indicadores de infraestructura/marginación, probando la hipótesis H2.
## 9.5 Mitigación y frontera de Pareto
- Preprocesamiento: reponderación de muestras y corrección de representación por entidad.
- In-procesamiento: optimización con restricción de equalized odds.
- Post-procesamiento: ajuste de umbrales por grupo/entidad.
Cada técnica se sitúa en el plano equidad–desempeño para trazar la frontera de Pareto, que constituye la herramienta de decisión entregable.
## 9.6 Validación
Validación cruzada estratificada, validación temporal y validación dejando-una-entidad-fuera. Como paso distintivo, validación externa en la base DGIS para evaluar la transportabilidad del desempeño y, sobre todo, de la equidad.
## 9.7 Métricas

| Dimensión | Métricas |
|---|---|
| Discriminación | AUROC, AUPRC, sensibilidad/especificidad a umbrales clínicos |
| Calibración | Brier, curva de calibración, calibración por grupo y por entidad |
| Utilidad clínica | Análisis de curva de decisión (net benefit) |
| Equidad | Equalized odds, paridad demográfica, disparidad de desempeño por entidad |
| Interpretabilidad | Importancia global y explicaciones locales por valores SHAP |

## 9.8 Herramientas y reproducibilidad
Python con pandas, scikit-learn, XGBoost/LightGBM, PyTorch, SHAP y Fairlearn/AIF360. Proyecto versionado en Git, semillas controladas, registro de experimentos y entorno declarado para asegurar replicabilidad.
# 10. Consideraciones éticas y de privacidad
La base de la DGE es pública y no contiene identificadores directos, por lo que el riesgo de reidentificación es bajo; aun así, se maneja bajo principios de minimización y uso responsable. Dado que el producto es un modelo de apoyo a la decisión, se enfatiza el uso con humano en el circuito y se discuten los riesgos de automatización. El propio enfoque de equidad es una salvaguarda ética: busca explícitamente evitar que el modelo perpetúe desigualdades regionales de atención.
# 11. Cronograma tentativo

| Fase | Actividades | Meses |
|---|---|---|
| 1. Fundamentación | Revisión de literatura, estado del arte y protocolo | 1–2 |
| 2. Datos | Ingesta, limpieza, EDA y contexto por entidad | 2–4 |
| 3. Modelo base | Modelo de referencia y validación | 4–5 |
| 4. Auditoría de equidad | Métricas por grupo y correlación geográfica | 5–7 |
| 5. Mitigación | Técnicas de mitigación y frontera de Pareto | 7–9 |
| 6. Validación externa | Transportabilidad en base DGIS | 9–10 |
| 7. Redacción | Resultados, discusión, tesis y defensa | 10–12 |

# 12. Resultados esperados y contribución
Se espera entregar: un modelo de riesgo de referencia comparable al estado del arte; un diagnóstico cuantitativo de la inequidad del modelo entre entidades, sexos y edades, correlacionado con la infraestructura de salud; una frontera de Pareto equidad–desempeño con técnicas de mitigación evaluadas; y evidencia de transportabilidad a una fuente independiente. La contribución es la primera auditoría de equidad geográfica de un modelo clínico sobre datos abiertos mexicanos, con implicaciones directas para el despliegue responsable de IA en el sistema de salud del país.
# 13. Referencias verificadas
Las siguientes fuentes fueron verificadas individualmente (autor, año, revista y datos empleados).
- Fuente primaria: Dirección General de Epidemiología, Secretaría de Salud. Base abierta de COVID-19 y diccionario de datos.
- Validación externa: DGIS, Subsistema Automatizado de Egresos Hospitalarios, 2008–2024.
- Becerra-Sánchez, A. et al. (2022). Mortality Analysis of Patients with COVID-19 in Mexico Based on Risk Factors Applying Machine Learning Techniques. Diagnostics, 12(6), 1396. DOI: 10.3390/diagnostics12061396. [Datos: México] — línea de base predictiva.
- Méndez-Astudillo, J. (2024). The impact of comorbidities and economic inequality on COVID-19 mortality in Mexico: a machine learning approach. Frontiers in Big Data. DOI: 10.3389/fdata.2024.1298029. [Datos: México] — antecedente del eje de inequidad.
- (2024). Leveraging Machine Learning to Unveil the Critical Role of Geographic Factors in COVID-19 Mortality in Mexico. Computación y Sistemas. [Datos: México] — geografía como predictor; se contrasta con el enfoque de equidad de esta tesis.
- Nejadshamsi, S. et al. (2026). Evaluation and improvement of algorithmic fairness for COVID-19 severity classification using XAI-based bias mitigation. JAMIA Open, 9(1), ooaf171. DOI: 10.1093/jamiaopen/ooaf171. [Datos: Canadá] — referente de fairness fuera de México.
Nota: NHSJS (National High School Journal of Science) apareció en las búsquedas pero es una revista estudiantil; se excluye como referencia de autoridad. Las URLs se incluyen en el mensaje que acompaña este documento.
