# Mapping
Estimar el mapa $m$ del entorno asumiendo poses $x_{1:t}$ conocidas a partir de mediciones de sensores $z_{1:t}$: $$p(m\mid z_{1:t},x_{1:t})$$
## Tipos de Mapas para Robots Móviles
Mapas 2D:
- Landmark map: representación dispersa basado características usando landmarks.
- Occupancy grid map: representación probabilística discretizada donde cada celda almacena la probabilidad de estar ocupada.
- Topological map: representación de forma de grafo que captura landmarks (nodos) y conectividad.
- Semantic map: representa con etiquetas semánticas a los landmarks.

## Estimación de Mapas de Landmarks
Estimar la posición de $N$ balizas $m=\{m_1,...,m_N\}$ a partir de mediciones: $$z_k=h(x_k,m)+e_k,\quad e_k\sim N(0,Q)$$
Modelo de observación Range-Bearing: para una observación en polares $z_i=[r_i,\alpha_i]^T$ desde la pose $x_v=[x,y,\theta]^T$ y la posición real $m_i=[x_i,y_i]^T$: $$r_i = \sqrt{(x_i - x_v)^2 + (y_i - y_v)^2} + e_r \\ \alpha_i = \text{atan2}\left(\frac{y_i - y_v}{x_i - x_v}\right) - \theta_v + e_\theta \\ [e_r, e_\theta]^T\sim N(0,Q), \quad Q = \begin{bmatrix}
\theta_r^2 & 0 \\ 0 & \sigma_\theta^2
\end{bmatrix}$$
Conversión a Coordenadas Cartesianas Globales: $$m = x_v \oplus z_i = \begin{bmatrix} x_v + r_i \cos(\theta_v + \alpha_i) \\ y_v + r_i \sin(\theta_v + \alpha_i) \end{bmatrix}$$
Propagación de Incertidumbre (Covarianza global $\Sigma_m$): $$\Sigma_m \approx J_{x_v} \Sigma_{x_v} J_{x_v}^T + J_{z_i} \Sigma_{z_i} J_{z_i}^T$$
### Estimación por Mínimos Cuadrados
Calcula las coordenadas del landmark que minimizan el error cuadrático ponderado del batch: $$\hat{m}=\arg\min_m\sum_ke_k^TQ_k^{-1}e_k=\arg\min_m(z-h(m))^TQ^{-1}(z-h(m))$$
#### Modelo de observación lineal ($h(m)=H·m$)
$$\hat{m}_{LS} = (H^T Q^{-1} H)^{-1} H^T Q^{-1} z \\ \Sigma_{\hat{m}} = (H^T Q^{-1} H)^{-1}$$
#### Modelo de observación no lineal:
Algoritmo de Gauss-Newton.
- Linealizar alrededor de la estimación actual $m_0$: $$h(m)\approx h(m_0)+J(m-m_0), \quad J=\left. \frac{\partial h}{\partial m} \right|_{m_0}$$
- Cáculo del incremento de Gauss-Newton: $$\delta = (J^TQ^{-1}J)^{-1}J^TQ^{-1}(z-h(m_0))$$
#### Generalización 1D con varianzas desiguales


### Estimación recursiva mediante EKF
Cada landmark es independiente y dependen de sus observaciones: $$p(m\mid z,x)=\prod_{k=1}^Np(m_k, \mid z_k, x)$$
El mapa no cambia en el tiempo, no existe paso de predicción en el filtro.

#### EKF Mapping
Inicialización de un nuevo landmark: $$m=\begin{bmatrix}
x_v+r\cos(\theta_v+\alpha) \\ y_v+r\sin(\theta_v+\alpha)
\end{bmatrix} \\ \bar{\mu}_m = \begin{bmatrix} \bar{\mu}_m \\ m_{new} \end{bmatrix}, \quad \bar{P}_m = \begin{bmatrix} \bar{P}_m & 0 \\ 0 & Q_{new} \end{bmatrix}, \quad Q_{new} = J \Sigma_{r,\alpha} J^T$$
Actualización de un landmark existente: $$\bar{\mu}_k = \mu_k, \quad \bar{P}_k=P_k \\
\hat{z}_k=h(x_v,\bar{\mu}_k), \quad H_k=\left. \frac{\partial h}{\partial m} \right|_{\bar{\mu}_k} \\
v_k=z_k-\hat{z}_k, \quad S_k=H_k\bar{P}_kH_k^T+Q, \quad K_k=\bar{P}_kH_k^TS_ k^{-1} \\
\mu_k^+ = \bar{\mu}_k+K_kv_k, \quad P_k^+=(I-K_kH_k)\bar{P}_k
$$
## Estimación de Mapas de Rejilla de Ocupación
El entorno se divide en $I\times J$ celdas: $m=\{m_1,...,m_k,...,m_N\}$ con $N=I·J$, donde cada celda $m_k\equiv m_{ij},\ k=(i-1)·J+j$. 

Cada celda $m_k\in \{0,1\}$, siendo 0 vacía y 1 ocupado. La probabilidad de ocupación $p_k=P(m_k=1\mid z_{1:t},x_{1:t})$. 

Las celdas son independientes: $P(m\mid z_{1:t},x_{1:t})\approx\prod_{k=1}^{N}P(m_k\mid z_{1:t},x_{1:t})$.

### Modelo inverso del sensor
Convierte una medida del sensor en evidencia de ocupación de celdas de la trayectoria del haz. Dado la distancia del haz $r$:
- Celdas cruzadas antes del impacto ($\lt r$): $P \lt 0.5$
- Celdas cerca del punto de impacto ($\approx r$): $P\gt 0.5$
- Celdas más allá del impacto ($\gt r$): $P=0.5$

