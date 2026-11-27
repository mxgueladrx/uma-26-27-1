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
Los sensores devuelven una medida real + error. La medida real $v$ se calcula como $v=h(x,m)$ siendo $x$ la pose del robot y $m$ el mapa (formado por ubicaciones de objetos). La observación $z$ se modela como $p(z \mid v) = p(z \mid x, m)$.

Representación de mapas:
- **Mapas basado en landmarks**: cada landmark tiene una posición y descriptor.
- **Mapa de ocupación de rejilla**: cada celda almacena la probabilidad de estar ocupado.

Interpretación:
- $L(x\mid m, z)$ **verosimilitud**: evalúa cómo de probable es que $x$ sea el estado verdadero dado el mapa $m$ y la medida del sensor $z$. PDF a posteriori.
- $p(z\mid x,m)$ **condicional**: probabilidad de observar $z$ si el robot está en $x$ y dado un mapa $m$. $z=h(x,m)+w$.

Error gaussiano: $$p(z\mid x,m)=K·\exp{(-\frac{1}{2} [z-h(x,m)]^T·Q^{-1}· [z-h(x,m)])} \\ z\sim N(h(x,m), Q) \qquad \qquad \qquad w = [z-h(x,m)]\sim N(0,Q)$$
Siendo $Q$ la matriz de covarianza 2x2 (incertidumbre del sensor).

### Modelos de observación basados en landmarks
Mapa formado por landmarks $m$ y posiciones $m_i=[x_i, y_i]^T$. Los sensores miden:

![[Pasted image 20261126191444.png]]

- Distancia y ángulo: $$z_i = \begin{bmatrix} d_i \\ \theta_i \end{bmatrix} = h(x, m_i) + w_i = \begin{bmatrix} \sqrt{(x_i - x)^2 + (y_i - y)^2} \\ \operatorname{atan2}(y_i - y, x_i - x) - \theta \end{bmatrix} + w_i$$
	Siendo $h(x,m_i)$ la predicción de $z$ dado $z$ y $m_i$ (gaussiana).

La posición $m_i$ en el marco de referencia global dado la pose $x=[x,y, \theta]^T$ y la medida del sensor $z=[r, \alpha]^T$ es: $$m=\begin{bmatrix} x+r\cos(\theta + \alpha) \\ y+r\sin(\theta + \alpha)\end{bmatrix}$$
Propagación de incertidumbre de la posición del landmark: como la pose $x$ y la medida del sensor $z$ tienen ruido, la covarianza estimada del landmark $m$ es: $$ \Sigma_m \approx J_x\Sigma_xJ_x^T+J_z\Sigma_zJ_z^T$$
Siendo $\Sigma_m$ 2x2, $\Sigma_x$ 3x3 y $\Sigma_z$ 2x2.
- $J_x$ es el jacobiano respecto a la pose $x$: $$J_x = \begin{bmatrix} 1 & 0 & -r \sin(\theta + \alpha) \\ 0 & 1 & r \cos(\theta + \alpha) \end{bmatrix}$$
- $J_z$ es el jacobiando respecto a la medida $z$: $$J_z = \begin{bmatrix} \cos(\theta + \alpha) & -r \sin(\theta + \alpha) \\ \sin(\theta + \alpha) & r \cos(\theta + \alpha) \end{bmatrix}$$
### Beam model
Se usa en sensores que dan la distancia al obstáculo más cercano en la dirección que apunta. La probabilidad de dar en el blanco es gaussiano:

![[Pasted image 20261126202140.png|362]]

$$p_{\text{hit}}(z | x, m) = \eta_{\text{hit}} \frac{1}{\sigma \sqrt{2\pi}} \exp \left( -\frac{(z - z_{\text{exp}})^2}{2\sigma^2} \right)$$
Donde $\eta_{text{hit}}$ es un factor de normalización para restringir la gaussiana al intervalo $[0, z_{\text{max}}]$.

Un modelo combinado mixto: $$p(z\mid x,m)=\alpha_{\text{hit}} p_{\text{hit}}(z\mid x,m)+\alpha_{\text{unexp}} p_{\text{unexp}}(z\mid x,m)+ \alpha_{\text{rand}} p_{\text{rand}}(z\mid x,m)+\alpha_{\text{max}} p_{\text{max}}(z\mid x,m)$$
Dado el modelo $\theta = \{\alpha_{\text{hit}}, \alpha_{\text{unexp}}, \alpha_{\text{rand}}, \alpha_{\text{max}}\}$, hay que maximizar la verosimilitud: $$\arg \max_{\theta} \sum \log p(z | x, m; \theta)$$

### Modelo de campo de verosimilitud
Solo se verifica el punto final, no el haz entero. Se calcula sin ninguna suposición de donde se encuentra el sensor. Representa un campo de probabilidad (representando la probabilidad de que haya un obstáculo en ese punto).

![[Pasted image 20261126204414.png|224]]
