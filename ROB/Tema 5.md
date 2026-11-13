## Introducción
Estimar la pose del robot a partir del entorno, medidas de sensores y movimientos de odometría.
- Estimación probabilística: distribución de probabilidad sobre las posibles poses.
- Estimación puntual: estima un único valor de la pose.

Problemas:
- Seguimiento de posición: pose aproximadamente conocida. El objetivo es actualizar la pose a medida que se mueve y corregirlo mediante los sensores.
- Localización global: la pose es desconocida, se encuentra en el mapa y hay que resolver múltiples ubicaciones.
- Robot secuestrado: robot cree estar en una pose pero es incorrecta. Debe detectar el fallo y relocalizarse.

## Posicionamiento por Mínimos Cuadrados
Busca la pose que mejor se adapta a las mediciones ruidosas minimizando el error entre la medida real y la predicha.

### Mínimos Cuadrados Lineales
Dado la observación $z=Hx+e$ ($H$ es una matriz de m$\times$n (ecuaciones · pose))
- m < 3: pose no observable.
- m = 3: solución $\hat{x}=H^{-1}z$
- m > 3: sistema sin solución exacta. Se minimiza: $$\hat{x}=\arg\min_{x} e^Te = \arg\min_{x} \|z - Hx\|^2$$
	La solución es $\hat{x}=(H^TH)^{-1}H^Tz$

### Mínimos Cuadrados Ponderados
Si las mediciones no son fiables, se asigna una matriz de covarianza $Q$: $$\hat{x}= \arg\min_{x} e^T Q^{-1}e = \arg\min_{x} (z- Hx)^T Q^{-1}(z - Hx) = \arg\min_{x} \sum_{i=1}^m \frac{e_i^2}{\sigma_{z_i}^2}$$
La solución es $\hat{x}=(H^TQ^{-1}H)^{-1}H^TQ^{-1}z$ y la covarianza de la estimación $\Sigma = (H^TQ^{-1}H)^{-1}$

Si el error es Gaussiano con media 0, la estimación de Máxima Verosimilitud $x=\arg\max_x p(z\mid x)$ es igual a la solución de Mínimos Cuadrados Ponderados.

### Mínimos Cuadrados No Lineales
Modelo no lineal del sensor $z=h(x)+e$. No existe solución directa. Se parte de una estimación $x_k$y se linealiza localmente mediante expansión de Taylor de primer orden. $$h(x)\approx h(x_k)+J_{h_k}\delta$$
donde $J_{h_k} = \left. \frac{\partial h}{\partial x} \right|_{x_k}$ es la Jacobiana de $h$ en $x_k$. 

Para Mínimos Cuadrados Ponderados no lineales, se usa el algoritmo de Gauss-Newton:
- Incremento de pose $\delta = [\delta_x,\delta_y,\delta_\theta]^T$: $\delta = (J_h^TQ^{-1}J_h)^{-1}J_h^TQ^{-1}(z-h(x_k))$
- $x_{k+1}=x_k+\delta$
- Repetir hasta que $\| \delta \|$ sea pequeño.

## Registro de Mapas / Conjunto de Puntos
Estima la transformación rígida ($R$, $t$) para alinear dos conjuntos de puntos observados.
- Registro contra un mapa global: localización global.
- Registro contra escaneo previo: odometría visual / scan matching.

### Puntos de Landmarks
Se conocen parejas ($m_i$, $q_i$).
- Transformación del punto: $$x \oplus q_i = t + Rq_i = \begin{bmatrix} x + q_x \cos\theta - q_y \sin\theta \\ y + q_x \sin\theta + q_y \cos\theta \end{bmatrix}$$
- Optimización del error cuadrático: $${\hat{t}, \hat{R}} = \arg\min_{t, R} \sum_{i=1}^N |m_i - (Rq_i + t)|^2$$

### Puntos de Escaneo
Correspondencias entre puntos desconocidos.
- Algoritmo ICP: repetir hasta convergencia:
	1. Para cada punto $q_i$, asociarlo al $m_j$ más cercano del otro conjunto.
	2. Resolver un paso de Gauss-Newton minimizando $E(R,t)=\sum^{n}_{i=1} \| m_j-Rq_i-t\|^2$
- Garantiza convergencia a un mínimo local.

## Filtrado Bayesiano
Estima la creencia sobre todas las posibles poses $bel(\mathbf{x}_t) = p(x_t \mid z_{1:t}, u_{1:t})$. Se repite:
- Predicción: $$\overline{bel}(x_t) = \int p(x_t \mid x_{t-1}, u_t) bel(x_{t-1}) dx_{t-1}$$
- Corrección: $$bel(x_t) = \eta p(z_t \mid x_t) \overline{bel}(x_t)$$siendo $\eta$ una constante de normalización.

### Filtro en Malla
Representa la probabilidad en cada celda $i$ mediante un histograma: $p_i = P(X = \text{cell}_i)$, con $\sum_i p_i = 1$.
- Predicción (priori): $\overline{bel}(x_t) = \sum_{x_{t-1}} P(x_t \mid x_{t-1}, u_t) bel(x_{t-1})$
- Corrección (posteriori): $bel(x_t) = \eta P(z_t \mid x_t) \overline{bel}(x_t)$

### Filtro de Kalman
Solución exacta del filtro de Bayes para sistemas lineales y Gaussianos. El belief se representa con ($\mu_t, \Sigma_t$).
- Modelo de movimiento lineal: $x_t=A_tx_{t-1}+B_tt_t+\epsilon_t$ donde $\epsilon_t \sim N(0, R_t)$
- Modelo de medida lineal: $z_t=C_tx_t+\delta_t$ donde $\delta_t \sim N(0,Q_t)$

