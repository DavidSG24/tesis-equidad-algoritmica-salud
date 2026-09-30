# Guión para el video — 2B. Avance del proyecto de investigación

**David Segundo García** · Proyecto Terminal 2026-2 · MCDI, INFOTEC
Presentación: `presentacion_2b.pdf` (13 diapositivas)

---

## Antes de grabar

- Duración: **6:41** hablando a ritmo normal y **6:16** si vas ágil, contra un
  tope de 7 minutos. Solo se pasa (7:10) si hablas muy despacio, así que no te
  demores y tienes ~20 segundos de margen.
- Pon el PDF en pantalla completa. Verifica que se lean las cifras de las
  diapositivas 11 y 12.
- Está escrito para **contarse, no para leerse**: frases cortas, primera persona y
  marcas de señalamiento («miren el diagrama», «fíjense en la segunda fila»).
  Si te sale natural cambiar una palabra sobre la marcha, hazlo.
- **▸** marca el momento de avanzar de diapositiva.
- **Control de tiempo:** deberías entrar a la diapositiva 8 cerca del minuto
  **3:48**.

---

## 1 · Portada — *0:00*

Hola, buenas tardes. Soy David Segundo García, de la Maestría en Ciencia de Datos
e Información. Mi asesor es el doctor Daniel Cervantes Cabrera.

El título de mi proyecto es largo, pero la idea es simple: quiero saber si un
modelo que predice riesgo clínico funciona igual de bien en todos los estados del
país. Y si no, qué se puede hacer.

**▸**

---

## 2 · Por qué este tema — *0:24*

Empiezo por el porqué.

Predecir mortalidad por COVID con datos mexicanos ya se ha hecho bastante.
Revisé varios trabajos: datos distintos, algoritmos distintos, y todos terminan
en el mismo desempeño.

Lo que no encontré fue a nadie preguntándose si ese desempeño es parejo en todo
el país. Nadie toma la entidad federativa como eje para auditar equidad.

Y aquí eso pesa, porque la entidad no es un dato demográfico más: es donde se
decide, se financia y se opera la atención. Lo cual tiene una ventaja poco común:
si encuentro una inequidad por estado, corregirla sí se puede implementar.

**▸**

---

## 3 · El sesgo algorítmico no es hipotético — *1:04*

Y no es un riesgo teórico. Hay un caso muy conocido, de Obermeyer y sus colegas,
publicado en *Science*.

Miren el diagrama. Un modelo en Estados Unidos tenía que decidir quién necesitaba
más atención, y para medirlo usó el gasto sanitario. El problema es que los
pacientes afroamericanos accedían menos a los servicios, y gastaban menos aunque
estuvieran igual de enfermos. ¿Resultado? Menos recursos para ellos.

Me quedo con dos cosas. Ese modelo ni siquiera usaba la raza, y aun así
discriminó. Y el problema estaba en qué se eligió predecir, no en el algoritmo.

**▸**

---

## 4 · Planteamiento del problema — *1:42*

Entonces, ¿cuál es mi problema?

Un modelo puede tener un promedio excelente y estar fallando siempre con la gente
de los estados con menos infraestructura. Si lo entrenas con datos de entidades
urbanas, puede fallar justo donde el sistema de salud está más débil: en vez de
reducir la desigualdad, la amplifica.

Así que me propongo medirla y corregirla, sin arruinar la utilidad clínica.
Fíjense que la pregunta cambió: ya no es si el modelo acierta, sino cómo reparte
sus errores.

**▸**

---

## 5 · Preguntas y objetivos — *2:15*

De ahí salen cinco preguntas. Si hay disparidades entre entidades, edades y
sexos. Si tienen que ver con la marginación del estado. Qué mitigación funciona y
cuánto cuesta. Si esto se sostiene en otra fuente de datos. Y si hay grupos que
salen peor al cruzarlos.

El objetivo general es armar el modelo, auditar su equidad y mitigar lo que
encuentre. De ahí salen cinco objetivos específicos y cuatro hipótesis, que
reviso al final.

**▸**

---

## 6 · Antecedentes y estado del arte — *2:44*

Los antecedentes vienen de las tres tradiciones que ven arriba, que hasta ahora
habían ido cada una por su lado.

De la tabla, fíjense en la segunda fila, porque ahí está la originalidad. Que la
entidad prediga bien la mortalidad no me dice nada sobre si el modelo es igual de
confiable en cada estado. De hecho, un modelo que ni siquiera use la entidad
puede rendir desigual entre ellas. Y eso es lo que me pasó.

Las filas resaltadas son donde no encontré trabajos previos.

**▸**

---

## 7 · Bases teóricas — *3:19*

Ahora, dos conceptos que se confunden mucho.

La discriminación mide si el modelo ordena bien a los pacientes por riesgo. La
calibración mide otra cosa: si de cada cien a los que les pone veinte por ciento
de riesgo, efectivamente se mueren veinte.

Y no es un detalle académico. Yo audito sobre el puntaje ya calibrado, porque si
no, lo que mides por grupo es el sesgo del entrenamiento y no la inequidad.

**▸**

---

## 8 · El teorema de imposibilidad — *3:48*

Esta es la parte teórica más importante.

Chouldechova y Kleinberg demostraron algo incómodo: si la prevalencia es distinta
entre grupos y tu clasificador no es perfecto, no puedes tener calibración por
grupo y separación al mismo tiempo. No es cuestión de esforzarse más.

Y eso se cumple en mis datos: las tasas de mortalidad entre estados difieren por
un factor de cinco punto seis.

Lo importante es la salida práctica. La calibración es propiedad del puntaje,
mientras que la sensibilidad depende de dónde pongas el umbral. Así que un umbral
distinto por estado no mueve la calibración, y me deja escoger cuál de las dos
tasas igualo.

**▸**

---

## 9 · La frontera de Pareto — *4:31*

Si no puedo tener las dos cosas, buscar «el modelo justo» no tiene sentido. Lo
que sí lo tiene es una frontera: todas las políticas donde ya no puedes ganar
equidad sin perder desempeño.

Y esa decisión no me toca a mí, es normativa. Por eso el entregable se la pasa a
quien autoriza el despliegue, con el costo de cada opción ya medido.

**▸**

---

## 10 · Marco metodológico — *4:56*

Para el trabajo empírico uso CRISP-DM, porque cubre el ciclo completo. Tiene un
problema: no contempla nada de equidad. Así que lo adapté.

La adaptación es la fase resaltada. La evaluación la hago en dos niveles: primero
el desempeño global, y después desagregado por grupo. Y el segundo nivel te puede
mandar de regreso al modelado aunque el primero no haya detectado nada.

**▸**

---

## 11 · Avances: datos y hallazgo principal — *5:22*

Vamos a los resultados. Trabajo con dos y medio millones de casos confirmados del
corte 2021, y dejo la entidad fuera del modelo a propósito, para usarla como eje
de auditoría.

Este es el hallazgo. El modelo da un AUROC de cero punto noventa y cinco, con
ochenta por ciento de sensibilidad: visto así, cumple todos los criterios que me
había fijado.

Pero cuando lo abro por estado, la brecha de sensibilidad es de casi treinta
puntos. Mismo modelo, mismo umbral. Y no es ruido: el valor p es de cero punto
cero cero uno.

**▸**

---

## 12 · Las hipótesis y lo pendiente — *6:00*

¿Y las hipótesis? La primera se sostuvo, y la tercera también: de las tres
familias de mitigación solo funcionó el post-procesamiento, que baja la brecha a
la mitad sin costo. La cuarta queda pendiente.

La segunda no se sostuvo: la disparidad existe, pero la marginación no la
explica.

Y termino con la limitación más seria, que hay que decirla: si me quedo solo con
los hospitalizados, el AUROC se cae a cero punto setenta.

**▸**

---

## 13 · Cierre — *6:29*

Para cerrar: un modelo puede acertar en promedio y estar fallando siempre en la
misma parte del país. Medirlo antes de desplegarlo es una decisión de método.

Muchas gracias.

---

## Si vas retrasado

Lo más prescindible, en orden:

1. Diapositiva 2 — el último párrafo, sobre por qué la corrección es
   implementable en México.
2. Diapositiva 9 — la frontera de Pareto se entiende con la primera frase.
3. Diapositiva 12 — el párrafo de la limitación de los hospitalizados.

Con esos tres cortes bajas alrededor de un minuto.
