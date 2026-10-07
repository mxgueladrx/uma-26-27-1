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
Predice la pose del robor en un tiempo $t$ a partir de su pose anterior y la entrada de movimiento aplicado sobre $[t-1,t]$. Depende de la entrada $u_t$:
- ![[Pasted image 20261001174754.png]]
- ![[Pasted image 20261001174806.png]]

### Modelo de movimiento de velocidad de entrada
![[Pasted image 20261001175403.png]]

Una secuencia de $\{u_i\}^N_{i=1}$, donde cada entrada es mantenida constante durante $\Delta t$, genera una trayectoria de segmentos de curvatura constante.

### Modelo de movimiento de odometría de entrada
![[Pasted image 20261001181222.png]]

## Modelos de movimientos probabilísticos
Hay dos tipos de error:
- Sistemáticos: sesgo que se repite que se soluciona con calibración.
- Random: varía de forma aleatoria entre ejecuciones (distribución de probabilidad)

Se representa con una $p(\mathbf{x}_t\mid \mathbf{x}_{t-1}, \mathbf{u}_t)$.

![[Pasted image 20261001183856.png]]

%%Cual es la prob de q un robot este en la pose 5.47 (es 0). (dibujo de funcion). Si esta en una pose x, es un rango.

Si hay un robot en una tarima y no mido ninguna coordenada, sino las baldosas. Que probabilidad hay que este en la baldosa (...,...)%%

![[Pasted image 20261001185028.png]]

![[Pasted image 20261001185225.png]]

![[Pasted image 20261001185704.png]]

![[Pasted image 20261005173609.png]]

Dada la pose $\mathbf{x}_{t-1}$ y $\mathbf{u}_t$, las poses y entradas anteriores no aportan información de la siguiente pose (cadenas de Markov)

![[Pasted image 20261005173834.png]]

![[Pasted image 20261005175452.png]]

La representación probabilística de las poses puede presentarse:
- **Analítica**: distribución Gaussiana: $\mathbf{x_t} \sim p(\mathbf{x_t} \mid \mathbf{x_{t-1}}, \mathbf{u_t}) \approx N(\mathbf{x_t}; \overline{\mathbf{x}}_t, \Sigma_{x_t})$
- **Muestras**: $\{\mathbf{x}^i_t\}^N_{i=1} \sim p(\mathbf{x_t} \mid \mathbf{x_{t-1}}, \mathbf{u_t}))$ 

