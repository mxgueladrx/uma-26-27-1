## Ejercicio 1
### 1. Cola con Cola ($A \leftarrow B \rightarrow C$)
B influye tanto en A como en C. Los nodos A y C son dependientes a priori (comparten una causa común), pero se vuelven independientes cuando conocemos el valor de B.

**Enunciado**: Un centro educativo analiza la relación entre la motivación de un estudiante, su asistencia a clase y sus resultados académicos. La motivación influye tanto en la asistencia como en los resultados.
- **A**: Asistencia regular.
- **B**: Motivación alta.
- **C**: Buenos resultados académicos.

![[Pasted image 20261024000041.png]]

![[Pasted image 20261023235816.png]]

![[Pasted image 20261023235831.png]]

![[Pasted image 20261023235842.png]]

Sin evidencias de B; A y C son dependientes porque comparten una causa común:
$$P(A)=0.6·0.9+0.4·0.3=0.66 \\ P(C)=0.6·0.8+0.4·0.2=0.56$$
Si fuera independientes se cumpliría: $$P(A,C)=P(A)·P(C) \\ P(A,C)=0.6·0.9·0.8+0.4·0.3·0.2=0.456 \\ P(A)·P(C)=0.66·0.56=0.3696$$
Como son diferentes, son dependientes. Ahora vamos a introducir la evidencia B = Si. La probabilidad de asistencia ya no cambia al conocer los resultados académicos: $$P(A\mid B,C)=\frac{P(A,B,C)}{P(B,C)}=\frac{P(A\mid B)P(B,C)}{P(B,C)}=P(A\mid B)$$
Lo mismo ocurre con los buenos resultados académicos. Podemos ver en la captura de abajo que el resultado es la misma probabilidad a priori que definimos antes (cuando se sabe con certeza que B = si). Por tanto, A y C son condicionalmente independientes dado B.

![[Pasted image 20261024000518.png]]

### 2. Cabeza con Cola ($A \rightarrow B \rightarrow C$)
A influye en B y B influye en C. Los nodos A y C son dependientes, pero se vuelven independientes cuando conocemos B.

**Enunciado**: Un hospital estudia la relación entre una infección, la aparición de fiebre y la realización de una prueba médica. La infección puede provocar fiebre, y la fiebre está relacionada con la probabilidad de obtener un resultado positivo en la prueba.
- **A**: El paciente tiene una infección.
- **B**: El paciente tiene fiebre.
- **C**: La prueba médica da positivo.

![[Pasted image 20261024115310.png]]

![[Pasted image 20261024115319.png]]

![[Pasted image 20261024115329.png]]

![[Pasted image 20261024115340.png]]

Sin evidencias de B, A y C son dependientes: $$P(A)=0.1 \\ P(C)=0.1·0.8·0.8+0.1·0.2·0.05+0.9·0.1·0.8+0.9·0.9·0.05=0.1775 $$
Si fueran independientes: $$P(A,C)=P(A)·P(C) \\ P(A,C)=0.1(0.8·0.8+0.2·0.05)=0.065 \\ P(A)·P(C)=0.1·0.1775=0.01775$$
Como son diferentes, son dependientes. Ahora vamos a introducir la evidencia B = Si. Una vez conocida la fiebre, saber si la prueba ha dado positivo no aporta información adicional sobre la infección dentro de este modelo. $$P(A\mid B,C)=\frac{P(A,B,C)}{P(B,C)}=\frac{P(A\mid B)P(B,C)}{P(B,C)}=P(A\mid B)$$
Podemos ver en la captura de abajo que el resultado de C es la misma probabilidad a priori que definimos antes (cuando se sabe con certeza que B = si). Por tanto, A y C son condicionalmente independientes dado B.

![[Pasted image 20261024121712.png]]

### 3. Cabeza con Cabeza ($A \rightarrow C \leftarrow B$ : OR)
A y B son independientes a priori si no se conoce C. Al conocer C, A y B se vuelven independientes.

**Enunciado**: En una fábrica hay instaladas cámaras de seguridad con sensores. La alarma se activa si algún sensor detecta movimiento o aperturas de puertas.
- **A**: el sensor de movimiento se activa.
- **B**: el sensor de apertura se activa.
- **C**: la alarma se activa.

![[Pasted image 20261024122910.png]]

![[Pasted image 20261024122926.png]]

![[Pasted image 20261024122936.png]]

![[Pasted image 20261024122947.png]]

Como los sensores son independientes: $$P(A,B)=P(A)·P(B) \\ P(A,B)=0.1·0.2=0.02 \\ P(A)·P(B)=0.1·0.2=0.02$$
Vamos a introducir la evidencia de que la alarma se ha activado, C = si. Como el modelo es un OR, o A = si o B = si. La probabilidad a priori de que C = si es: $$P(C=1)=1-(0.9)(0.8)=0.28$$
Ahora, calculamos la probabilidad A y B dado C: $$P(A\mid C)=\frac{0.1}{0.28}=0.3571 \\ P(B\mid C)=\frac{0.2}{0.28}=0.7143$$
Como: $$P(A,B\mid C)=\frac{0.02}{0.28}=0.0714 \\ P(A\mid C)·P(B\mid C)=0.3571·0.7143=0.2551$$

![[Pasted image 20261024124621.png]]

Si fueran independientes serían iguales, pero son diferentes, por lo que A y B son dependientes dado C. El efecto explaining away demuestra que si sabemos que la alarma está activada, conocer que B = no implica que A = si.

### 4. Cabeza con Cabeza ($A \rightarrow C \leftarrow B$ : AND)
A y B son independientes a priori si no se conoce C. Al conocer C, A y B se vuelven independientes.

Usaremos el mismo enunciado que antes, pero esta vez la alarma se activa si ambos sensores se activan.

![[Pasted image 20261024125301.png]]

![[Pasted image 20261024125316.png]]

Antes comprobamos que eran independientes. A continuación vamos a introducir la evidencia C = no, como la alarma solo se activa si ambas están activadas, al menos una esta desactivada: $$P(\lnot C)=1-0.02=0.98 \\ P(A\mid \lnot C)=\frac{0.1·0.8}{0.98}=0.0816 \\ P(B\mid \lnot C)=\frac{0.9·0.2}{0.98}=0.1837 \\ P(A,B\mid \lnot C)=0$$

![[Pasted image 20261024125902.png]]

Si C = si: $$P(A\mid C)=P(B\mid C)=1$$

![[Pasted image 20261024125920.png]]

En este caso, ambas variables quedan determinadas, por lo que su distribución condicionada cumple la igualdad de independencia. Sin embargo, si observamos C = no, las causas son dependientes.

## Ejercicio 2
![[Pasted image 20261024130237.png]]

Aquí tenemos la red inicializada. A continuación veremos su estructura para los diferentes apartados:

### 1. Rojizo y cojea
![[Pasted image 20261024130330.png]]

Sabemos con certeza que es rojizo y cojea, por lo que esas probabilidades aumentan. Al actualizar las probabilidades de los demás nodos, vemos que al final obtenemos un 65% de que sea Wurro.

### 2. Piel escamosa y no cojea
![[Pasted image 20261024130449.png]]

Hacemos lo mismo que antes. Podemos ver que además descarta por completo animales con 5 patas y los Wurros. Al final obtenemos un 72% de que sea una Hobexa.

### 3. Cinco patas con piel suave
![[Pasted image 20261024130635.png]]

Vemos que con esta combinación tambien sabemos que el animal cojea con certeza. Al final obtenemos un 67% de que sea un Wurro.

## Ejercicio 3
![[Pasted image 20261024131429.png]]

### Supuesto 1 - Luis no es alérgico a los gatos
#### Evidencia 1 - Alergia = no
![[Pasted image 20261024131501.png]]

Vemos que la relación AND ya no se cumple, por lo que la única opción para que estornude es que esté resfriado. Además, en la relación OR, al menos uno se tiene que cumplir, como rinitis es 100% no, solo queda saber si está resfriado.

#### Evidencia 2 - Estornuda = si
![[Pasted image 20261024131827.png]]

Como hemos pensado antes, si Luis estornuda, la única opción para que estornude sea porque está resfriado. Todo lo relacionado con el gato no tiene efecto en los estornudos.

#### Evidencia 3 - Arañazos = si
![[Pasted image 20261024132151.png]]

Confirmando que tenemos arañazos en los muebles, sabemos con bastante probabilidad que tenemos un gato. A pesar de eso no afecta a los estornudos ya que no somos alérgicos.

### Supuesto 2 - Luis es alérgico a los gatos
#### Evidencia 1 - Alergia = si
![[Pasted image 20261024132318.png]]

Aunque tengamos alguna alergia, falta confirmar que tenemos un gato para saber que tenemos rinitis (AND). En el caso de que tengamos un gato, la probabilidad de estornudar aumentará. Lo mismo pasará con el resfriado, si lo estamos, también estornudaremos y aumentará esa probabilidad.

#### Evidencia 2 - Estornuda = si
![[Pasted image 20261024132523.png]]

Sabemos además que estornuda, por lo que 100% tiene que estar resfriado o tiene rinitis (o ambas). Vemos que las probabilidades de ambos nodos del OR son casi 50/50.

#### Evidencia 3 - Arañazos = si
![[Pasted image 20261024132643.png]]

Sabiendo que los muebles están arañados, y que la causa de ello es porque tenemos un gato, entonces tenemos rinitis, la razón por la cual Luis estornuda. Eso no significa que no esté resfriado, existe una posibilidad de que también lo esté (es un OR).

## Ejercicio 4
