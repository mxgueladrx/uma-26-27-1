# Robot sensing
## Tipos de sensores para robots
**Propioceptivos**: mide el estado interno y movimiento del robot (batería, posición de la rueda, aceleración...)

**Exteroceptivos**: mide propiedades del entorno (distancia o ángulos a objetos, intensidad de la luz...)
- **Pasivos**: usa energía del entorno.
- **Activos**: emite su propia energía (luz, ruido, sonido). Mayor consumo pero mejor rendimiento el condiciones de cambios de luz.

**Landmarks**: característica u objeto reconocible del entorno cuya observación puede asociarse con un elemento de un mapa (edificio, montaña, keypoints...). No necesitan instalarse, y es flexible y adaptable a otros entornos.

**Beacons (balizas)**: marca instalada o designada intencionadamente para facilitar la detección, identificación y localización (satélites, QR, radio...). Proporciona una posición absoluta y permite algoritmos simples y eficientes.

Medidas en robótica:
- **Range**: distancia a un landmark ($z=r$).
- **Bearing**: dirección o ángulo hacia un landmark ($z=\alpha$).
- **Range+bearing**: ambas a la vez ($z=[r, \alpha ] ^T$).
- **Triangulación**: localización de un punto midiendo ángulos ($\theta_1, \theta_2$) hacia él desde balizas conocidas.
- **Trilateración**: localización de un punto midiendo distancias ($r_1, r_2$) a balizas conocias.

### GPS
Son balizas móviles. El posicionamiento se basa en trilateración con distancias a satélites (al menos 4 para estimar la posición 3D).

**Transmisión del satélite**: ondas de radio codificas con la identidad, ubicación y hora.

**Segmento de control**: red terrestre de estaciones de monitorización y de control maestro.

**Fuentes de error**: tiempo, efectos atmosféricos, trayectos múltiples, visibilidad limitada, efecto del cañón urbano.

Precisión típica: 
- **Stand-alone GPS**: sin correcciones adicionales (precisión típica SPS: 3 - 10 m).
- **Differential GPS (DGPS)**: usa una estación de referencia cercana para correcciones (SPS 0.5 - 3 m).
- **RTK GPS**: medidas de fase de la portadora y correcciones en tiempo real (SPS 1 - 5 cm).

### Sonares
Envía un pulso ultrasónico que rebota con el obstaculo y lo detecta el receptor. Se mide el tiempo de ida y vuelta ($\Delta t$) para la distancia: $$r=\frac{c_s\Delta t}{2}$$donde $c_s\approx 343$ m/s es la velocidad del sonido en el aire. El ancho de haz efectivo de 30º. 

Tiene un bajo coste, compacto, útil para obstáculos, bajo consumo y alcance 2 - 4 m.

Pobre resolución angular, sensibilidad al tipo de superficie, pérdida de esquinas y reflexiones múltiples.

### Lidars
Pulsos láser y mide el tiempo de vuelo: $$r=\frac{c\Delta t}{2}$$donde $c\approx 3·10^8$ m/s. Un espejo giratorio barre el entorno obteniendo nubes de puntos 2D o 3D. Hay varias formas de medición:
- **Pulsed time-of-flight (ToF)**: pulsos láser cortos y mide $\Delta t$ directamente. Bueno para largos alcances.
- **Phase Shift (amplitud modulada)**: luz modulada ($f_m$) continuamente y mide el desfase $\Delta\phi$ de la señal recibida. Bueno para cortos alcances: $$r=\frac{c\Delta\phi}{4\pi f_m}$$
Alcance hasta 200 m, precisión a nivel 1 - 5 cm, excelente resolución angular 0.1º - 1º, caros. 

Se degrada ante lluvia/niebla/polvo, objetos oscuros o absorbentes, reflexiones especulares y distorsiones por objetos en movimiento.

### Cámaras
**Single camera**: información de bearing. Un píxel proyecta una línea en el espacio.

**Stereo cameras**: dos vistas separadas por un baseline para obtener la distancia y orientación mediante triangulación de la línea de visión de dos píxeles.

**RGB-D cameras**: imagen RGB y un mapa de profundidad por píxel. No tiene parte móvil y rango de 0.2 - 4 m.

## Modelos de sensores probabilísticos
Los sensores devuelven una medida real + error. La medida real $v$ se calcula como $v=h(x,m)$ donde $x$ es la pose y $m$ el mapa. La observación real $z$ se modela como $Z \sim p(z\mid v)$.

Asumiendo un error aditivo gaussiano $w\sim N(0,Q)$, la distribución de la medida respecto al estado se define como: $$p(z\mid x, m)=N(z;h(x,m),Q)$$
Cuando una observación tiene $K$ mediciones $z=[z_1, z_2,...,z_K]^T$, las mediciones son condicionalmente independientes dada la pose $x$ y el mapa $m$: $$p(z\mid x,m) = \prod^{K}_{k=1}p(z_k \mid x,m)$$
Un mapa $m$ es una representación espacial del entorno. Formas geométricas de representación de mapas:
- **Mapas basado en landmarks**: cada landmark tiene una posición y descriptor.
- **Mapa de ocupación de rejilla**: cada celda almacena la probabilidad de estar ocupado.

En algoritmos de localización basados en Bayes, la actualización de la pose del robot usa una relación: $$p(x \mid z, m) \propto p(z \mid x, m)· p(x \mid m)$$
La interpretación de $p(z\mid x,m)$ varía según la variable que permanece fija:
- **Probabilidad condicional** $p(z\mid x,m)$: deja fijo $x$ y $m$. Describe la PDF sobre las mediciones $z$ que puede generar el sensor $\int^{\infty}_{-\infty} p(z\mid x,m) dz = 1$
- **Verosimilitud** $p(z\mid x,m)=L(x;m,z)$: deja fijo la medida real observada $z$ y $m$. Evalúa que tan compatible es cada $x$ con la medida real $z$ recibida. No es una PDF sobre $x$. $\int^{\infty}_{-\infty} L(x; m,z) dx \not= 1$

![[Pasted image 20261027203201.png]]

### Sensores de landmarks
Cuando el mapa esta formado por landmarks $m_i$ y posiciones $m_i=[x_i, y_i]^T$, los sensores observan:
- **Range y bearing**: para un robot en la pose $x=[x,y,\theta]^T$, la medida observada $z_i$ sobre el landmark $m_i$, se expresa como: $$z_i = \begin{bmatrix} d_i \\ \theta_i \end{bmatrix} = h(x, m_i) + w_i = \begin{bmatrix} \sqrt{(x_i - x)^2 + (y_i - y)^2} \\ \operatorname{atan2}(y_i - y, x_i - x) - \theta \end{bmatrix} + w_i$$donde $w_i\sim N(0,Q_i)$ es el ruido de medida gaussiano.
- **Data association**:


### Sensores basados en escaneo
