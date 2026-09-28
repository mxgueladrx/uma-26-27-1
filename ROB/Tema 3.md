## Cinemática de robots con ruedas
Locomoción: acción de moverse de un lado a otro.
Posición del robot en el instante $t$: $r(t)=\begin{bmatrix}x(t) \\ y(t)\end{bmatrix}$
Posición de un robot $\mathbf{x}=\begin{bmatrix}x \\ y \\ \theta \end{bmatrix} = \begin{bmatrix}\mathbf{r} \\ \theta \end{bmatrix}$ en la posición $\mathbf{r}$ y orientación $\theta$.
Holonomico: vehículo que se desplaza en cualquier dirección. Los no holonomicos tienen velocidad lateral igual a 0.

Dos tipos de conducción no holonomico: diferencial (2 actuadores, velocidad en las 2 ruedas) y ackermann (velocidad en las traseras y las de delante giran, volante).

ICR (Centro Instantáneo de Rotación): es la intersección de los ejes extendidos de las ruedas.

![[Pasted image 20260924174913.png]]

Un chasis solo tiene un ICR y una $\omega$ (velocidad angular). La rueda $i$ sigue un círculo de radio $R_i$. La velocidad de la rueda es $v_i=\omega · R_i$.

![[Pasted image 20260924175106.png]]

### Conducción diferencial

![[Pasted image 20260924175823.png]]

A partir de las velocidades del centro de las ruedas: $R=\frac{l}{2}·\frac{(v_l+v_r)}{v_r-v_l}$ y $\omega =\frac{v_r - v_l}{l}$
La velocidad lineal del punto P: $v_p=\omega · R = \frac{v_l + v_r}{2}$
La velocidad angular de las ruedas: $\omega_r=\frac{v_r}{r_r}$ y $\omega_l=\frac{v_l}{r_l}$ siendo $r$ el radio de cada rueda.

Posición incremental del robot: cuánto se ha movido el robot.

![[Pasted image 20260924180832.png]]

![[Pasted image 20260924181117.png]]

## Posiciones y transformaciones planares

La posición $\mathbf{x}_2$ de un robot si se mueve $\Delta \mathbf{x}=\mathbf{x}_{12}$ de la posición $\mathbf{x}_1$
- Traslación: $\mathbf{x}_2=\mathbf{x}_1 + \mathbf{x}_{12}=\begin{bmatrix}x_1+x_{12} \\ y_1 + y_{12}\end{bmatrix}$
- Traslación + Rotación: $\mathbf{x}_2=\mathbf{x}_1  \oplus \mathbf{x}_{12}=\begin{bmatrix}x_1 + x_{12} \cos \theta_1 - y_{12} \sin \theta_1 \\ y_1 + x_{12}\sin \theta_1 + y_{12} \cos \theta_1 \\ \theta_1 + \theta_{12} \end{bmatrix}$ 

![[Pasted image 20260924184128.png]]

![[Pasted image 20260924185341.png]]

![[Pasted image 20260924190504.png]]

## Modelos de movimientos deterministas

### Modelo de movimiento de velocidad de entrada

### Modelo de movimiento de odometría de entrada

## Modelos de movimientos probabilísticos



