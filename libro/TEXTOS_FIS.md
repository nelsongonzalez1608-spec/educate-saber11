# Física · textos de las preguntas de entrenamiento para la guía de clase

Lo lee `textos_fis.py` con el mismo formato de `TEXTOS_BIO.md` (y de las secciones de Sociales en
`TEXTOS_GUIA_DOCENTE.md`). Cada pregunta trae su texto completo, el enunciado, las cuatro opciones,
por qué la clave es esa —resuelta a mano el 10 nov 2026, con cuentas y unidades, y cruzada con
`fisN_icfes.py` y `tablero/icfes.csv`— y lo que el profesor debe hacer notar.

Donde dice `[[figura]]` la guía dibuja la tabla, el esquema o la gráfica de la pregunta
(`textos_fis.FIGURAS`), redibujados con los mismos datos del cuaderno. Cuando las opciones son
dibujos, los cuatro van en la columna de las opciones (`textos_fis.FIG_OPCIONES`).

Membrete en pantalla: «Pregunta Saber 11». La procedencia de cada pregunta (cuadernillo y número)
está en `tablero/icfes.csv`, columna `fuente`. Dos salen del compilado ASED, que no es del ICFES:
la primera de la misión 1 y la primera de la misión 2. La guía lo dice en la nota del profe.

---

## FÍSICA · MISIÓN 1 · páginas 228 y 232 (entrenamiento ICFES)

### Pregunta 1 (página 228) · Los paquetes del supermercado · clave **C**
**Fuente:** compilado ASED pre código 11, capítulo 9, sección Mecánica clásica, ítem 13 (no es del ICFES). **Competencia:** Uso comprensivo del conocimiento científico. **Estrategia del cuaderno:** 1 · Las fuerzas, una por una.

> Una persona sale del supermercado con dos paquetes que pesan 5 kgf, uno en cada mano. Para llegar a su casa debe recorrer 2 cuadras de 100 metros cada una. El trayecto recorrido por la persona es completamente horizontal, lo hace sin detenerse y llega en 2 minutos a su casa.

**Pregunta:** Sobre el trabajo mecánico en kgf × m realizado, podemos afirmar que

**Opciones:**
A. tiene un valor de 2000 kgf × m ya que el trabajo es fuerza × distancia.
B. es indeterminable porque el trabajo siempre se realiza contra la gravedad.
C. es nulo porque la fuerza para sostener los paquetes no es en la dirección del movimiento.
D. su valor numérico es de 500 kgf × m por cada paquete.

**Verificada resolviéndola:** la mano sostiene cada paquete con una fuerza vertical, hacia arriba (5 kgf, igual a su peso), y el camino es horizontal: entre la fuerza y el desplazamiento hay 90°, y W = F · d · cos 90° = 5 kgf · 200 m · 0 = 0 (C). A multiplica 10 kgf × 200 m sin mirar la dirección de la fuerza; D hace una cuenta parecida para cada paquete, y tampoco sale de la fórmula (5 kgf × 200 m daría 1000, no 500); B dice que el trabajo «siempre» es contra la gravedad, y no es así.

**Lo que el profesor debe hacer notar**

- Dos flechas antes de cualquier cuenta: hacia dónde empuja la mano (arriba) y hacia dónde va el camino (al frente). Si son perpendiculares, esa fuerza no trabaja.
- La persona se cansa, pero eso es el trabajo de sus músculos por dentro, no trabajo sobre el paquete. Es la misma idea de la pregunta 6 de la misión 5.
- El kgf (kilogramo-fuerza) es una unidad antigua: 1 kgf ≈ 9,8 N. Los 2 minutos sobran: el tiempo no entra en el trabajo.

### Pregunta 2 (página 228) · La montaña rusa de la gráfica · clave **D**
**Fuente:** cuadernillo de preguntas de Ciencias Naturales Saber 11 (Icfes), pregunta 43. **Competencia:** Uso comprensivo del conocimiento científico. **Estrategia del cuaderno:** 2 · La gráfica cuenta el movimiento.

> Un estudiante calculó la energía potencial de un vagón en una montaña rusa. La gráfica representa los datos obtenidos por el estudiante.
>
> [[figura]]

**Pregunta:** De los siguientes modelos de montaña rusa, ¿cuál explica la gráfica obtenida por el estudiante?

**Opciones:**
A. El modelo A.
B. El modelo B.
C. El modelo C.
D. El modelo D.

**Verificada resolviéndola:** la energía potencial gravitacional crece con la altura, así que la gráfica es un dibujo de qué tan alto está el vagón. Dice: muy alto al principio; abajo del todo en t₁; arriba otra vez en t₂, pero menos que al principio; abajo en t₃; y en t₄, a media altura, sin cambiar. Solo el modelo D cuenta esa historia: la caída, el fondo, la cima del rizo, el fondo y el tramo alto del final (D). En A el vagón está en lo más bajo en t₂, justo cuando la gráfica marca un pico; en B está abajo en t₁ y en t₂; en C empieza abajo, y la gráfica empieza en lo más alto.

**Lo que el profesor debe hacer notar**

- Que traduzcan la gráfica a alturas, instante por instante, antes de mirar los dibujos: t₁ abajo, t₂ arriba, t₃ abajo, t₄ a media altura.
- La energía potencial no dice qué tan rápido va el vagón: solo qué tan alto está.

### Pregunta 3 (página 232) · Tres objetos que caen distinto · clave **C**
**Fuente:** cuadernillo de preguntas de Ciencias Naturales Saber 11 (Icfes), pregunta 13. **Competencia:** Indagación. **Estrategia del cuaderno:** 3 · El experimento justo.

> El profesor de Juan le entrega tres objetos de igual volumen y forma, pero de diferente material, y le pide que los deje caer desde la altura de sus hombros y observe el tiempo de caída al suelo, de cada uno de ellos. Juan observa que los tres tardan tiempos diferentes para llegar al suelo, a pesar de que los tres están sometidos a la misma aceleración gravitacional.

**Pregunta:** Teniendo en cuenta la información anterior, ¿cuál de las siguientes preguntas se puede contestar a partir de las observaciones que realizó Juan?

**Opciones:**
A. ¿El tiempo de caída de los objetos depende de la altura de lanzamiento?
B. ¿La fuerza gravitacional es proporcional a la masa de los objetos?
C. ¿La fuerza neta que actúa sobre cada uno de los objetos es diferente?
D. ¿La forma de los objetos está relacionada con diferencias en la fuerza de fricción?

**Verificada resolviéndola:** Juan cambió solo el material: el volumen, la forma y la altura fueron iguales. Si los tres caen con la misma gravedad y aun así tardan distinto, sus aceleraciones fueron distintas, y la aceleración la da la fuerza neta sobre cada uno (el peso menos el empuje del aire, que no los frena igual): esa pregunta sí se contesta con lo que observó (C). A pregunta por la altura y D por la forma, que no se cambiaron; B pide relacionar fuerza y masa, y Juan no midió ni masas ni fuerzas.

**Lo que el profesor debe hacer notar**

- Es de indagación: no pide física nueva, pide la ficha del experimento justo. ¿Qué cambió Juan? ¿Qué dejó igual? ¿Qué observó?
- Una pregunta solo se contesta si lo que ella pregunta es justo lo que se cambió o lo que se midió.

### Pregunta 4 (página 232) · El salto desde el puente · clave **D**
**Fuente:** cuadernillo de preguntas de Ciencias Naturales Saber 11 (Icfes), pregunta 17. **Competencia:** Uso comprensivo del conocimiento científico. **Estrategia del cuaderno:** 4 · Lo que se conserva.

> El salto bungee es un deporte que se practica generalmente en puentes. En uno de estos saltos, el deportista se lanzará desde un puente de 65 metros de altura, utilizando una banda elástica que tiene una longitud sin estirar de 30 metros y que puede estirarse 30 metros más.

**Pregunta:** Cuando el deportista ha descendido apenas 20 metros de altura, ¿cuál de las siguientes transformaciones de energía se habrá dado?

**Opciones:**
A. De energía cinética a potencial elástica.
B. De energía cinética a potencial gravitacional.
C. De energía potencial gravitacional a potencial elástica.
D. De energía potencial gravitacional a cinética.

**Verificada resolviéndola:** la banda mide 30 m sin estirar: durante los primeros 30 m de caída va floja y no hace fuerza. A los 20 m solo ha actuado la gravedad: el deportista perdió altura y ganó rapidez, de energía potencial gravitacional a cinética (D). La energía elástica (A y C) aparece después de los 30 m, cuando la banda empieza a estirarse; B es al revés, sería subir.

**Lo que el profesor debe hacer notar**

- Que marquen en una regla dos puntos: dónde empieza a estirarse la banda (a los 30 m) y dónde va el deportista (a los 20 m).
- La palabra que decide es «apenas»: todavía falta la transformación de abajo. Con la banda estirada del todo, a los 60 m, el deportista se detiene 5 m por encima del fondo.
- El cuadernillo trae una foto del puente; no hace falta para responder y no se proyecta.

---

## FÍSICA · MISIÓN 2 · páginas 235 y 239 (entrenamiento ICFES)

### Pregunta 1 (página 235) · El globo que sube · clave **C**
**Fuente:** compilado ASED pre código 11, capítulo 9, sección Mecánica clásica, ítem 10 (no es del ICFES). **Competencia:** Explicación de fenómenos. **Estrategia del cuaderno:** 1 · El calor va del caliente al frío.

> Para elevar un globo se calienta con fuego el aire que está dentro de él.

**Pregunta:** La explicación más acertada de por qué el globo se eleva, es que al calentar el aire

**Opciones:**
A. la presión contra las paredes internas del globo es mayor que la presión externa.
B. una parte del aire sale con velocidad hacia abajo, generando un impulso hacia arriba.
C. una parte del aire sale del globo, disminuyendo la densidad y generando un empuje que lo eleva.
D. el plástico del globo se tensa disminuyendo su peso específico y el globo se eleva.

**Verificada resolviéndola:** el fuego le pasa calor al aire de adentro, que se expande; como el globo está abierto por abajo, parte de ese aire sale. Adentro queda menos aire en el mismo volumen: el globo con su aire pesa menos que el aire frío que desplaza, y el empuje de ese aire lo sube (C). A: en un globo abierto la presión de adentro es casi la de afuera; B describe un cohete, no un globo; D: el plástico no pesa menos por tensarse.

**Lo que el profesor debe hacer notar**

- La cadena tiene tres eslabones: el calor entra al aire, el aire caliente queda menos denso, el empuje gana al peso. Que la escriban antes de mirar las opciones.
- Es el mismo principio de la pregunta 8 del taller: el aire caliente sube porque es menos denso.

### Pregunta 2 (página 235) · Dos litros en la misma estufa · clave **C**
**Fuente:** cuadernillo de preguntas de Ciencias Naturales Saber 11 (Icfes), pregunta 22. **Competencia:** Uso comprensivo del conocimiento científico. **Estrategia del cuaderno:** 2 · La cuenta del calor.

> Una estudiante calentó en una estufa, durante 1 minuto, un litro de agua que inicialmente estaba a 15 °C. La temperatura final del agua fue 17 °C.

**Pregunta:** Si ahora calienta 2 litros de agua que inicialmente están a 15 °C, en la misma estufa durante un minuto, ¿cuál será la temperatura final de los 2 litros de agua?

**Opciones:**
A. 19 °C.
B. 17 °C.
C. 16 °C.
D. 15 °C.

**Verificada resolviéndola:** la misma estufa durante el mismo minuto entrega el mismo calor. Con 1 L (1000 g): Q = 1000 g · 1 cal/(g·°C) · 2 °C = 2000 cal. Con 2 L (2000 g) y las mismas 2000 cal: ΔT = 2000 cal ÷ (2000 g · 1 cal/(g·°C)) = 1 °C. La temperatura final es 15 °C + 1 °C = 16 °C (C). A supone que el doble de agua sube el doble; B repite el resultado de un litro; D supone que no sube nada.

**Lo que el profesor debe hacer notar**

- Que escriban qué es igual en los dos casos (la estufa y el minuto: el mismo calor) y qué cambió (la masa).
- Supone que la estufa entrega lo mismo las dos veces y que se pierde lo mismo: es lo que la pregunta da por hecho.

### Pregunta 3 (página 239) · El agua que hierve, molécula por molécula · clave **B**
**Fuente:** cuadernillo de preguntas de Ciencias Naturales Saber 11 (Icfes), pregunta 1. **Competencia:** Uso comprensivo del conocimiento científico. **Estrategia del cuaderno:** 3 · Lo que hacen las partículas.

> A continuación, se muestra un modelo de la distribución de las moléculas de agua en estado líquido, en un recipiente cerrado.
>
> [[figura]]
>
> Cuando este recipiente se calienta manteniendo la presión constante, la distribución de las moléculas cambia, modificando el estado del agua.

**Pregunta:** ¿Cuál de los siguientes modelos muestra correctamente la distribución de las moléculas de agua en estado líquido y gaseoso?

**Opciones:**
A. El modelo A.
B. El modelo B.
C. El modelo C.
D. El modelo D.

**Verificada resolviéndola:** al hervir, las moléculas se mueven más rápido y se separan hasta ocupar todo el recipiente, pero cada una sigue siendo H₂O: un oxígeno con dos hidrógenos. El modelo B tiene las moléculas enteras repartidas por todo el recipiente (B). A separa los oxígenos de los hidrógenos, es decir, rompe las moléculas; C deja las moléculas apretadas como en el líquido, solo que arriba; D tiene átomos sueltos y revueltos.

**Lo que el profesor debe hacer notar**

- La trampa es la D: «el gas está desordenado» es cierto, pero desordenado no es roto.
- Hervir es un cambio físico: cambian la distancia y la rapidez de las moléculas, no las moléculas.

### Pregunta 4 (página 239) · Hervir agua a 25 km de altura · clave **A**
**Fuente:** cuadernillo de preguntas de Ciencias Naturales Saber 11 (Icfes), pregunta 27. **Competencia:** Explicación de fenómenos. **Estrategia del cuaderno:** 4 · El ambiente decide el cambio de fase.

> El siguiente modelo representa la relación entre la altura y la cantidad de partículas de aire.
>
> [[figura]]
>
> Una olla con agua hierve a una temperatura de 100 °C, cuando la altura es de 0 km.

**Pregunta:** Teniendo en cuenta que el punto de ebullición corresponde a la temperatura a la cual la presión de vapor del líquido iguala a la presión atmosférica, si se pone a calentar la misma cantidad de agua a una altura de 25 km, ¿qué le sucede al agua?

**Opciones:**
A. Hierve a una temperatura menor que 100 °C, porque la presión es menor en esta altura.
B. Hierve a una temperatura mayor que 100 °C, porque la presión es menor en esta altura.
C. Nunca hierve, porque en esta altura hay muy poca cantidad de aire.
D. Se congela, porque al no haber aire el agua pasará a estado sólido.

**Verificada resolviéndola:** en el modelo, a 25 km hay muchas menos partículas de aire que a 0 km: la presión atmosférica es mucho menor. El agua hierve cuando la presión de su vapor iguala la de afuera, y con menos presión afuera eso pasa a menor temperatura: hierve por debajo de 100 °C (A). B tiene bien la razón y mal la conclusión; C confunde poca presión con que no pueda hervir; D dice que sin aire el agua se congela, y nada en el texto lo sostiene.

**Lo que el profesor debe hacer notar**

- Dato para ti: a 25 km la presión es de unos 2,5 kPa, la cuadragésima parte de la del nivel del mar, y el agua herviría cerca de 21 °C.
- Ejemplo cercano: en Bogotá el agua hierve hacia 92 °C, por la misma razón.

---

## FÍSICA · MISIÓN 3 · páginas 242 y 246 (entrenamiento ICFES)

### Pregunta 1 (página 242) · La resistencia que manda a 90 °C · clave **B**
**Fuente:** cuadernillo de preguntas de Ciencias Naturales Saber 11 (Icfes), pregunta 31. **Competencia:** Indagación. **Estrategia del cuaderno:** 1 · Busca el dato que decide.

> La siguiente gráfica muestra la relación entre la resistencia eléctrica y la temperatura para cuatro resistencias eléctricas (R₁, R₂, R₃ y R₄).
>
> [[figura]]
>
> Un estudiante realiza actividades experimentales y encuentra que la corriente eléctrica en un circuito es inversamente proporcional a la resistencia eléctrica. Se le solicita al estudiante construir un circuito usando una de estas resistencias, de forma que pase la menor cantidad de corriente eléctrica a 90 °C.

**Pregunta:** Si las tendencias de resistencia como función de la temperatura se mantienen, ¿cuál resistencia se debe utilizar?

**Opciones:**
A. R₁, porque tiene la mayor resistencia eléctrica desde los 40 °C hasta los 80 °C.
B. R₂, porque su resistencia eléctrica será la mayor a 90 °C.
C. R₃, porque tiene la menor resistencia desde los 40 °C hasta los 80 °C.
D. R₄, porque su resistencia eléctrica no depende de la temperatura.

**Verificada resolviéndola:** menos corriente pide la mayor resistencia (I = V ÷ R), y la pregunta es a 90 °C. A 80 °C, R₁ y R₂ valen 5 Ω, R₄ vale 4 Ω y R₃, 2 Ω. Siguiendo la tendencia: R₁ sube parejo, medio ohmio cada 20 °C (unos 5,25 Ω a 90 °C); R₂ sube cada vez más rápido (de 60 a 80 °C subió 1,2 Ω): a 90 °C pasa de 5,5 Ω; R₃ baja y R₄ no cambia. La mayor a 90 °C es R₂ (B). A y C razonan con el tramo de 40 a 80 °C, no con 90 °C; D dice algo cierto de R₄ que no responde la pregunta.

**Lo que el profesor debe hacer notar**

- El dato que decide está fuera de la gráfica: hay que mirar hacia dónde va cada curva después de 80 °C.
- La A es la trampa: R₁ es la mayor entre 40 y 80 °C, pero a 90 °C ya no.

### Pregunta 2 (página 242) · Tres cargas en triángulo · clave **A**
**Fuente:** cuadernillo de preguntas de Ciencias Naturales Saber 11 (Icfes), pregunta 42. **Competencia:** Uso comprensivo del conocimiento científico. **Estrategia del cuaderno:** 2 · Dibuja el campo primero.

> De la ley de Coulomb se sabe que la fuerza eléctrica debido a la interacción entre cargas de signos iguales es repulsiva y entre cargas de signos opuestos es atractiva. La siguiente figura muestra un sistema conformado por tres cargas eléctricas.
>
> [[figura]]

**Pregunta:** ¿Cuál de las siguientes figuras muestra la fuerza eléctrica que ejercen la carga 2 y la carga 3 sobre la carga 1?

**Opciones:**
A. La figura A.
B. La figura B.
C. La figura C.
D. La figura D.

**Verificada resolviéndola:** la carga 1 es positiva. La 2 también es positiva: se repelen, y la fuerza de 2 sobre 1 va sobre la línea que las une, alejándose de 2 (hacia arriba y a la derecha). La 3 es negativa: se atraen, y la fuerza de 3 sobre 1 apunta hacia 3 (hacia abajo y a la derecha). Esa es la figura A. B pone las dos al revés; C pone las dos como repulsión; D, las dos como atracción.

**Lo que el profesor debe hacer notar**

- Una flecha por cada carga vecina, sobre la línea que une las dos cargas: primero los signos, después si se atraen o se repelen.
- Las dos flechas se dibujan sobre la carga 1, que es la que recibe las fuerzas.

### Pregunta 3 (página 246) · Hacia dónde se mueve la carga −q · clave **A**
**Fuente:** cuadernillo Saber 11 2016-1, 2.ª sesión, Ciencias Naturales, ítem 72. **Competencia:** Explicación de fenómenos. **Estrategia del cuaderno:** 3 · Signo, sentido y unidad.

> En la figura se muestra un campo eléctrico E, generado por dos esferas cargadas; en el interior del campo eléctrico se coloca una carga negativa −q, tal como se muestra en la figura.
>
> [[figura]]

**Pregunta:** De acuerdo con la información anterior, ¿cuál de las siguientes figuras muestra la dirección en la que se moverá la carga −q al ser liberada desde el reposo?

**Opciones:**
A. La figura A.
B. La figura B.
C. La figura C.
D. La figura D.

**Verificada resolviéndola:** las líneas de campo salen de la esfera positiva y llegan a la negativa; donde está −q, el campo va a lo largo de la línea, en el sentido de sus flechas. Sobre una carga negativa la fuerza va al revés del campo (F = q · E, con q negativa): a lo largo de la línea, de regreso hacia la esfera positiva. Eso muestra la figura A. B va a favor del campo (sería una carga positiva); C y D son perpendiculares a la línea, y una carga que parte del reposo arranca en la dirección de la fuerza.

**Lo que el profesor debe hacer notar**

- La negativa va hacia la positiva: tiene sentido, se atraen. El signo cambia el sentido, no la línea.
- La pregunta es por la dirección al soltarla. Después la carga no sigue exactamente la línea, pero eso no se pregunta.

### Pregunta 4 (página 246) · Dos esferas que se tocan · clave **A**
**Fuente:** cuadernillo de preguntas de Ciencias Naturales Saber 11 (Icfes), pregunta 19. **Competencia:** Explicación de fenómenos. **Estrategia del cuaderno:** 4 · Del modelo al mecanismo.

> En un metal que pierde electrones, la cantidad de protones es mayor que la de electrones y, por tanto, la carga total es positiva y se representa con signos +. Se tienen dos esferas metálicas idénticas: una esfera (1) inicialmente con carga + Q y otra esfera (2) inicialmente neutra. Al ponerlas en contacto y luego separarlas, se observa que las dos esferas quedan con cargas iguales + Q/2, como muestra la figura.
>
> [[figura]]

**Pregunta:** Con base en la información anterior, ¿qué sucedió al poner las esferas en contacto?

**Opciones:**
A. De la esfera 2 pasaron electrones hacia la esfera 1.
B. De la esfera 2 pasaron protones hacia la esfera 1.
C. De la esfera 1 pasaron electrones hacia la esfera 2.
D. De la esfera 1 pasaron protones hacia la esfera 2.

**Verificada resolviéndola:** en un metal solo se mueven los electrones; los protones están en los núcleos. La esfera 2 era neutra y quedó con + Q/2: perdió electrones. La esfera 1 pasó de + Q a + Q/2: su carga positiva bajó, así que ganó electrones. Los electrones pasaron de la 2 a la 1 (A). B y D mueven protones; C da el sentido contrario.

**Lo que el profesor debe hacer notar**

- «Positiva» quiere decir «le faltan electrones». Contar lo que falta es la mitad de la pregunta.
- La carga total no cambia: + Q antes, + Q/2 + Q/2 después.

---

## FÍSICA · MISIÓN 4 · páginas 249 y 253 (entrenamiento ICFES)

### Pregunta 1 (página 249) · El detector fuera del agua · clave **D**
**Fuente:** cuadernillo de preguntas de Ciencias Naturales Saber 11 (Icfes), pregunta 9. **Competencia:** Uso comprensivo del conocimiento científico. **Estrategia del cuaderno:** 1 · La fuente pone la frecuencia.

> Un investigador sumerge un detector de sonido en agua para grabar los sonidos emitidos por los animales. El detector muestra la longitud de onda, la frecuencia, la velocidad de propagación y la distancia a la que se produce el sonido emitido por los animales. El investigador saca el detector del agua y registra un sonido.

**Pregunta:** ¿Cuál cambio de las variables mencionadas le permite asegurar al investigador que el sonido se trasmite por el aire y no por el agua?

**Opciones:**
A. La longitud de onda.
B. La frecuencia de la onda.
C. La forma de la onda.
D. La velocidad de la onda.

**Verificada resolviéndola:** la frecuencia la pone el animal que hace el sonido y no cambia al pasar de un medio a otro (B no sirve). La rapidez la pone el medio: unos 1500 m/s en el agua y unos 340 m/s en el aire; si el detector marca unos 340 m/s, el sonido viajó por el aire (D). La longitud de onda también cambia (λ = v ÷ f), pero depende a la vez de la fuente y del medio, así que sola no identifica el medio (A). La forma de la onda (C) tampoco.

**Lo que el profesor debe hacer notar**

- La A es la trampa razonable: si la frecuencia no cambia y la rapidez sí, la longitud de onda cambia. Pero para reconocer el medio sirve la magnitud que depende solo del medio.
- Para cada magnitud, preguntar: ¿quién la pone, el animal o el agua?

### Pregunta 2 (página 249) · El farol visto desde el agua · clave **C**
**Fuente:** cuadernillo de preguntas de Ciencias Naturales Saber 11 (Icfes), pregunta 32. **Competencia:** Explicación de fenómenos. **Estrategia del cuaderno:** 2 · Dibújalo antes de elegir.

> Los rayos de luz emitidos por objetos luminosos viajan en línea recta dentro de un mismo medio, como se muestra en la Figura 1. Si un rayo de luz pasa de aire a agua cambia su dirección, como se muestra en la Figura 2.
>
> [[figura]]

**Pregunta:** Cuando una piscina está vacía, un nadador observa el farol que está en el borde, como se observa en la figura 1; luego, cuando se llena la piscina como se muestra en la figura 2, ¿cómo verá el nadador el farol?

**Opciones:**
A. Más bajo.
B. De la misma altura.
C. Más alto.
D. Invertido.

**Verificada resolviéndola:** con la piscina llena, la luz del farol entra al agua, va más lenta y se dobla acercándose a la normal: le llega al nadador más empinada que antes. El ojo no sabe que la luz se dobló: prolonga en línea recta el rayo que le llega, y esa recta apunta más arriba que el farol de verdad. Lo ve más alto (C). Para verlo más bajo (A) la luz tendría que doblarse al revés; de la misma altura (B), no doblarse; invertido (D) es lo que hace una lente, no una superficie plana de agua.

**Lo que el profesor debe hacer notar**

- Que prolonguen con una regla el último tramo del rayo de la figura 2 antes de mirar las opciones.
- Es lo mismo que pasa con una moneda en el fondo de un vaso, pero al revés: allá el ojo está en el aire y la moneda parece más cerca de la superficie.

### Pregunta 3 (página 253) · Dos parlantes y una sola nota · clave **C**
**Fuente:** cuadernillo Saber 11 2016-1, 2.ª sesión, Ciencias Naturales, ítem 70. **Competencia:** Explicación de fenómenos. **Estrategia del cuaderno:** 3 · Concluye solo lo observado.

> Un estudiante camina por el frente de dos parlantes ubicados afuera de la emisora del colegio. Dentro de la emisora la profesora de física toca la nota «do», en un clarinete, para ayudar al profesor de música a afinar algunos instrumentos musicales. El estudiante nota que hay lugares en donde el sonido del clarinete se escucha más fuerte mientras que en otros no, y los marca como se muestra en la siguiente figura.
>
> [[figura]]

**Pregunta:** Si el estudiante le pregunta a la profesora la razón por la cual en los puntos negros el sonido se escucha más fuerte que en los blancos, ¿cuál de las siguientes argumentaciones debe darle la profesora al estudiante?

**Opciones:**
A. Porque las ondas de sonido interfieren constructivamente en los puntos negros, y en los puntos blancos se reflejan.
B. Porque las ondas de sonido interfieren constructivamente y destructivamente en todos los puntos, pero en los blancos las ondas se refractan.
C. Porque las ondas de sonido interfieren constructivamente en los puntos negros, y destructivamente, en los puntos blancos.
D. Porque las ondas de sonido interfieren destructivamente en los puntos blancos y negros, pero en los negros se reflejan y se refractan.

**Verificada resolviéndola:** los dos parlantes emiten la misma nota, y a cada punto llegan dos ondas. Donde llegan cresta con cresta se suman (interferencia constructiva: sonido fuerte, los puntos negros); donde llegan cresta con valle se anulan (destructiva: sonido débil, los puntos blancos). Eso dice la C. A y D meten reflexión o refracción, que no explican puntos fuertes y débiles alternados; B dice que en todos los puntos pasan las dos cosas a la vez.

**Lo que el profesor debe hacer notar**

- La pista está en el patrón: fuerte, débil, fuerte, débil, a distancias regulares. Eso lo hacen dos ondas que se suman.
- Con un solo parlante no habría puntos blancos: hacen falta las dos fuentes.

### Pregunta 4 (página 253) · La tabla del sonido y sus gráficas · clave **B**
**Fuente:** cuadernillo de preguntas de Ciencias Naturales Saber 11 (Icfes), pregunta 48. **Competencia:** Indagación. **Estrategia del cuaderno:** 4 · Lee la tabla y su escala.

> Una estudiante realizó un experimento para medir la velocidad de propagación del sonido en el aire a diferentes temperaturas. Los resultados que obtuvo se muestran en la siguiente tabla.
>
> [[figura]]

**Pregunta:** ¿Cuál de las siguientes gráficas muestra los resultados del experimento?

**Opciones:**
A. La gráfica A.
B. La gráfica B.
C. La gráfica C.
D. La gráfica D.

**Verificada resolviéndola:** lo que la estudiante cambió (la temperatura) va en el eje horizontal y lo que midió (la velocidad) en el vertical, cada uno con su escala creciente: de 0 a 3 °C y de 331,7 a 333,5 m/s. Cada grado, la velocidad sube 0,6 m/s: una recta que sube. Esa es la gráfica B. A tiene los rótulos de los ejes intercambiados (dice «temperatura» junto a los números de la velocidad); C pone la velocidad abajo con su escala al revés, de 333,5 a 331,7, y D además cambia los rótulos de lugar.

**Lo que el profesor debe hacer notar**

- Primero qué variable va en cada eje y hacia dónde crece su escala; después la forma de la línea.
- La escala de la velocidad no empieza en cero, empieza en 331,7. No está mal, pero hay que leerla.

---

## FÍSICA · MISIÓN 5 · páginas 256 y 260 (entrenamiento ICFES)

### Pregunta 1 (página 256) · Dos pelotas y la tabla de momentos · clave **A**
**Fuente:** cuadernillo Saber 11 2016-1, 2.ª sesión, Ciencias Naturales, ítem 79. **Competencia:** Uso comprensivo del conocimiento científico. **Estrategia del cuaderno:** 1 · Cada magnitud con su fórmula y su unidad.

> Una estudiante suelta varias veces una pelota de 5 kg de masa (pelota 1), desde la parte más alta de una rampa de 1,5 m de altura, para que choque elásticamente con una pelota de masa diferente (pelota 2), que inicialmente se encuentra en reposo, como se muestra en la figura. La estudiante registra en la tabla las variaciones del momento antes y después del choque de cada pelota.
>
> [[figura]]

**Pregunta:** Si la estudiante sabe que la variación del momento es proporcional a la fuerza, ¿en cuál de los lanzamientos la pelota 1 se ejerció mayor fuerza para mover la pelota 2?

**Opciones:**
A. IV.
B. III.
C. II.
D. I.

**Verificada resolviéndola:** la fuerza sobre la pelota 2 se ve en cuánto cambió su momento: después menos antes. Lanzamiento I: 9,00 − 0 = 9,00 kg·m/s; II: 20,60; III: 27,10; IV: 31,60. El mayor cambio es el del lanzamiento IV: opción A. La pelota 1 pierde lo mismo que gana la 2 (27,10 − 18,05 ≈ 9,05; 27,10 − (−4,50) = 31,60): el momento total se conserva. Y la tabla cuadra: 5 kg que bajan 1,5 m llegan a v = √(2 · 9,8 m/s² · 1,5 m) ≈ 5,42 m/s, y 5 kg · 5,42 m/s ≈ 27,1 kg·m/s.

**Lo que el profesor debe hacer notar**

- Las opciones vienen al revés: la A es el lanzamiento IV. Que lean la letra y el número.
- En el lanzamiento IV la pelota 1 rebota hacia atrás (momento negativo): por eso es el cambio más grande.
- El cuadernillo dice «la pelota 1 se ejerció»: quiere decir «la pelota 1 ejerció». Y en rigor el cambio del momento es la fuerza por el tiempo del choque: la pregunta supone que los cuatro choques duran lo mismo.

### Pregunta 2 (página 256) · La piñata en equilibrio · clave **D**
**Fuente:** cuadernillo Saber 11 2016-1, 2.ª sesión, Ciencias Naturales, ítem 52. **Competencia:** Explicación de fenómenos. **Estrategia del cuaderno:** 2 · ¿Quién empuja y hacia dónde?

> En una fiesta, un niño sostiene una piñata por medio de una cuerda que pasa por una polea, como muestra la figura.
>
> [[figura]]

**Pregunta:** La piñata se mantiene en equilibrio y no se cae. Esto ocurre porque

**Opciones:**
A. el peso de la piñata disminuye con la altura.
B. el niño está ubicado debajo de la polea.
C. la polea sostiene por sí sola el peso de la piñata.
D. la fuerza que hace el niño es igual al peso de la piñata.

**Verificada resolviéndola:** la piñata está quieta: la fuerza neta sobre ella es cero. Sobre ella actúan su peso, hacia abajo, y la tensión de la cuerda, hacia arriba, y son iguales. Una polea fija solo cambia la dirección de la cuerda: la tensión que sostiene la piñata es la misma con la que hala el niño, así que la fuerza del niño es igual al peso de la piñata (D). A: el peso no cambia en unos metros de altura; B: dónde está el niño no es una fuerza; C: la polea sola no sostiene nada si nadie hala la cuerda.

**Lo que el profesor debe hacer notar**

- Dos flechas sobre la piñata antes de mirar las opciones: el peso hacia abajo y la tensión hacia arriba.
- Supone una polea sin rozamiento y una cuerda liviana, como se hace siempre en el colegio.

### Pregunta 3 (página 260) · Repetir la medida de los resortes · clave **A**
**Fuente:** cuadernillo Saber 11 2016-1, 1.ª sesión, Ciencias Naturales, ítem 106. **Competencia:** Indagación. **Estrategia del cuaderno:** 3 · Una variable a la vez.

> Un estudiante tenía algunos resortes y quería saber cuál de ellos era el más elástico. Para esto colgó una masa de 500 g a cada uno de los resortes y midió cuánto se estiraban. Un compañero de clase desea corroborar las medidas realizadas.

**Pregunta:** Para esto, él vuelve a hacer mediciones asegurándose de

**Opciones:**
A. usar la misma masa para probar todos los resortes.
B. que todos los resortes terminen estirados la misma longitud.
C. estirar todos los resortes al mismo tiempo.
D. que todos los resortes tengan el mismo tamaño.

**Verificada resolviéndola:** para comparar qué tan elástico es cada resorte, lo único que cambia es el resorte; lo demás se deja quieto, empezando por la masa que se cuelga (500 g en todos). Si cambia la masa, no se sabe si un resorte se estiró más por ser más elástico o por cargar más (A). B obliga al resultado que se quiere medir; C, estirarlos al mismo tiempo, no cambia cuánto se estira cada uno; D cambiaría los mismos resortes que se quieren comparar.

**Lo que el profesor debe hacer notar**

- No tiene figura ni cuentas: es la ficha de una variable a la vez. ¿Qué se compara? ¿Qué se deja quieto? ¿Qué se mide?
- La B es la trampa del que piensa en el resultado: si todos terminan igual, ya no hay nada que medir.

### Pregunta 4 (página 260) · La pelota que sube por el tubo · clave **D**
**Fuente:** cuadernillo de preguntas de Ciencias Naturales Saber 11 (Icfes), pregunta 26. **Competencia:** Explicación de fenómenos. **Estrategia del cuaderno:** 4 · El principio que explica lo que se ve.

> Un estudiante sopla una pelota por un tubo vertical y esta sube aceleradamente por el tubo, como se muestra en la siguiente figura:
>
> [[figura]]

**Pregunta:** Teniendo en cuenta lo anterior, ¿por qué ocurre esto?

**Opciones:**
A. Porque el peso de la pelota cambia cuando el estudiante sopla aire por el tubo.
B. Porque la fuerza que ejerce el aire que sopla el estudiante es igual que el peso de la pelota.
C. Porque el peso de la pelota es mayor que la fuerza del aire que sopla el estudiante.
D. Porque la fuerza que ejerce el aire que sopla el estudiante es mayor que el peso de la pelota.

**Verificada resolviéndola:** si la pelota sube cada vez más rápido, tiene aceleración hacia arriba, y por la segunda ley de Newton la fuerza neta también va hacia arriba: la fuerza del aire soplado es mayor que el peso (D). Si fueran iguales (B), estaría quieta o subiría con rapidez constante; si el peso fuera mayor (C), la pelota bajaría o frenaría; y el peso no cambia porque alguien sople (A).

**Lo que el profesor debe hacer notar**

- La palabra que decide es «aceleradamente»: aceleración hacia arriba, fuerza neta hacia arriba.
- La B es la trampa más común: fuerzas iguales no quieren decir quieto, quieren decir sin aceleración.

---

## FÍSICA · MISIÓN 6 · páginas 263 y 267 (entrenamiento ICFES)

### Pregunta 1 (página 263) · Cinco resistencias iguales · clave **B**
**Fuente:** cuadernillo Saber 11 2016-1, 1.ª sesión, Ciencias Naturales, ítem 97. **Competencia:** Uso comprensivo del conocimiento científico. **Estrategia del cuaderno:** 1 · Multiplica, divide y lleva las unidades.

> Un circuito se compone de una fuente de voltaje (12 V) y de cinco (5) resistencias (R) de igual valor, conectadas como se muestra en la siguiente figura.
>
> [[figura]]

**Pregunta:** Según lo que se puede observar en la figura, sobre los valores de las corrientes (I) es correcto afirmar que

**Opciones:**
A. las corrientes I1, I2, I3 e I4 son iguales, porque estas corrientes se encuentran en el mismo circuito.
B. las corrientes I2 e I3 son menores que I1, porque I1 se divide en I2 e I3.
C. la corriente I1 es menor que I2 e I3, porque solo fluye a través de una resistencia.
D. la corriente I3 es igual a la corriente I1, porque tanto I3 como I1 fluyen por una sola resistencia.

**Verificada resolviéndola:** toda la corriente que sale de la fuente pasa por R1: es I1. En el nudo se divide: una parte baja por R2 (I3) y la otra sigue por R3, R4 y R5 (I2); al volver se juntan, e I4 = I1. Como I1 = I2 + I3, cada una de las dos es menor que I1 (B). Con resistencias iguales, la rama de R2 tiene R y la otra 3R, así que I3 = 3 · I2: I3 = ¾ de I1 e I2 = ¼ de I1. A dice que todas son iguales, C que I1 es la menor y D que I3 = I1: las tres contradicen la regla del nudo.

**Lo que el profesor debe hacer notar**

- Que sigan la corriente con el dedo desde la fuente: dónde se divide y dónde se vuelve a juntar.
- Lo que entra a un nudo es lo que sale: ninguna corriente se gasta en el camino. Los 12 V no hacen falta para responder.

### Pregunta 2 (página 263) · El bombillo que se prende sin la fuente · clave **C**
**Fuente:** cuadernillo Saber 11 2016-1, 2.ª sesión, Ciencias Naturales, ítem 73. **Competencia:** Explicación de fenómenos. **Estrategia del cuaderno:** 2 · La energía no desaparece: cambia de forma.

> A continuación se presentan los nombres y las funciones de algunos dispositivos que pueden utilizarse en el circuito de la derecha.
>
> [[figura]]

**Pregunta:** Al pasar el interruptor de la posición 1 a la posición 2, el bombillo se enciende durante un tiempo y luego se apaga. ¿Qué dispositivo debe colocarse en el punto P para que esto ocurra?

**Opciones:**
A. Una resistencia.
B. Un cable.
C. Un condensador.
D. Un interruptor.

**Verificada resolviéndola:** en la posición 1 la fuente queda conectada con el bombillo y con P. En la posición 2 la fuente queda por fuera: si el bombillo se prende, la energía tiene que salir de P, y como se apaga después de un rato, P tenía guardada una cantidad que se acabó. El único de la tabla que almacena energía eléctrica es el condensador (C). Una resistencia (A) o un cable (B) no guardan energía: sin la fuente, el bombillo no prendería. Un interruptor (D) solo abre o cierra el paso.

**Lo que el profesor debe hacer notar**

- La energía no aparece de la nada: si la fuente no está en el circuito, ¿de dónde sale la luz?
- En la posición 1 el bombillo también se prende un instante, mientras el condensador se carga. La pregunta solo mira el paso a la posición 2.

### Pregunta 3 (página 267) · El rebote en la cancha y en el salón · clave **D**
**Fuente:** cuadernillo Saber 11 2016-1, 2.ª sesión, Ciencias Naturales, ítem 77. **Competencia:** Indagación. **Estrategia del cuaderno:** 3 · ¿Alcanzan los datos para esa conclusión?

> Un niño quiere ver qué pelota rebota más, una de tenis o una de baloncesto. Ambas se lanzan desde una altura de 2,0 m. La pelota de tenis lanzada sobre una cancha de césped rebotó 1,0 m; y la pelota de baloncesto, en una cancha de asfalto rebotó 1,5 m (ver figura).
>
> [[figura]]
>
> Cuando el estudiante va al salón de clases e intenta mostrarle el rebote de las pelotas a sus compañeros, no obtiene los mismos resultados.

**Pregunta:** ¿Por qué el estudiante no obtuvo los mismos resultados?

**Opciones:**
A. Porque no se tuvo en cuenta el peso de cada una de las pelotas.
B. Porque no se tuvo en cuenta el material de cada una de las pelotas.
C. Porque todos los objetos deben de rebotar de manera diferente.
D. Porque no se tuvieron las mismas condiciones experimentales.

**Verificada resolviéndola:** lo que cambió entre la prueba y el salón no fueron las pelotas: fue el piso. La de tenis rebotó en césped y la de baloncesto en asfalto; en el salón el piso es otro, así que no se repitieron las condiciones del experimento (D). El peso (A) y el material (B) de las pelotas son los mismos en las dos situaciones; C no explica por qué cambió el resultado.

**Lo que el profesor debe hacer notar**

- Después de revelar, vale la pena decirlo: la prueba original tampoco era justa, porque cambió la pelota y el piso a la vez.
- Un resultado vale para las condiciones en que se obtuvo.

### Pregunta 4 (página 267) · La curva de calentamiento · clave **B**
**Fuente:** cuadernillo de preguntas de Ciencias Naturales Saber 11 (Icfes), pregunta 35. **Competencia:** Uso comprensivo del conocimiento científico. **Estrategia del cuaderno:** 4 · Cuando algo deja de cambiar: el equilibrio.

> En un experimento, un sólido de identidad desconocida se calienta y se mide su temperatura hasta que se evapora, obteniendo la siguiente gráfica. Para identificar el sólido se cuenta con los datos de la tabla.
>
> [[figura]]

**Pregunta:** Teniendo en cuenta la información anterior, ¿a qué sustancia corresponde el sólido inicial?

**Opciones:**
A. Benceno.
B. Agua.
C. Acetonitrilo.
D. 2-butanol.

**Verificada resolviéndola:** en la curva hay dos tramos planos: mientras el sólido se funde y mientras el líquido hierve, el calor que entra no sube la temperatura. Los tramos están a 0 °C y a 100 °C. En la tabla, la única sustancia que se funde a 0 °C y hierve a 100 °C es el agua (B). El benceno (6 y 80 °C), el acetonitrilo (−45 y 82 °C) y el 2-butanol (−115 y 100 °C) no coinciden en las dos.

**Lo que el profesor debe hacer notar**

- La trampa es el 2-butanol: hierve a 100 °C, pero se funde a −115 °C. Hay que mirar los dos tramos.
- Un tramo plano no es que «se dejó de calentar»: el calor se está usando para cambiar de fase.
