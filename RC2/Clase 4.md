# Aprendizaje bayesiano
## Aprendizaje con redes bayesianas
Construir automáticamente una red probabilística a partir de datos:
- Aprendizaje paramétrico: se conoce la estructura de la red y se aprende sus parámetros (probabilidades condicionadas dados sus padres).
- Aprendizaje estructural: se aprende la estructura de los enlaces y sus parámetros probabilísticos a partir de datos.

### Aprendizaje paramétrico con datos completos
Un modelo $\vec{\theta}$ representa la asignación de valores a las $R$ probabilidades que se desean estimar: $$\vec{\theta}=(\theta_1, \theta_2,...,\theta_R)$$
Dado un conjunto $O$ de $n$ observaciones, hay que buscar el modelo $\vec{\theta}$ que maximice la verosimilitud (derivadas): $$L(\vec{\theta}/O)=P(=O_1, ..., O_n/\vec{\theta})=\prod^{n}_{i=1}P(O_i/\vec{\theta})$$

![[Pasted image 20261113155953.png]]

![[Pasted image 20261113160008.png]]

![[Pasted image 20261113160947.png]]

$$L(\theta, O)=\theta_1 · (1 - \theta_1) · \theta_1=\theta_1^2-\theta_1^3 \\
L'(\theta, O)=2\theta_1 - 3\theta_1^2 = 0 \implies \theta_1=0, \theta_1=2/3 \\
L''(\theta, O)=2-6\theta_1=2-6·2/3=-2 \\
L''(\theta, O)=2-6\theta_1=2-6·0=2
$$

El máximo es $\theta_1=2/3$. El modelo de máxima verosimilitud para una red bayesiana de la que tenemos $n$ observaciones se halla asignando a cada parámetro la frecuencia relativa calculada a partir de las $n$ observaciones. Se puede calcular contando las frecuencias observadas.

Se suele usar: $$l(\vec{\theta}/O)=\log(L(\vec{\theta}/O))=\sum_i \log(P(O_i/\vec{\theta})) \\ 
\hat{l}(\vec{\theta}/O)=\frac{1}{n}\sum_i \log(P(O_i/\vec{\theta}))$$

Dado que $0 \le L \le 1$, sus logaritmos satisfacen $l \le 0$ y $\hat{l} \le 0$.

### Aprendizaje paramétrico con datos incompletos (EM)
Si faltan datos:
- Sustituir por la moda.
- Eliminar las observaciones incompletas.
- Aplicar EM para encontrar los parámetros que maximizan la verosimilitud.

Algoritmo EM (Expectation Maximization): toma de entrada un conjunto de $n$ observaciones incompletas y la estructura de la red.
- Inicializamos $\vec{\theta} \leftarrow \vec{\theta}_0$ y evaluar $l\leftarrow l(\vec{\theta}_0)$.
	- Expectation: para cada dato desconocido $d\in O$, se calcula su valor esperado mediante probabilidades condicionadas derivadas de $\vec{\theta}$ actual.
	- Maximization: se reestima los parámetros del modelo asignando la estimación de máxima verosimilitud sobre la base ponderada por las expectativas: $\vec{\theta} \leftarrow EMV(O)$.
	- Calcular la nueva log-verosimilitud $l'$ y el incremento $\Delta l = l'-l$.
- Repetir hasta que $\Delta l \le \epsilon$.

![[Pasted image 20261113165239.png]]

Inicializamos y evaluamos:
$$ 
\theta_{0,1} = P(a)=0.5 \\
\theta_{0,2} = P(b/a) = 0.5 \\
\theta_{0,3} = P(b/\lnot a) = 0.5 \\
\theta_{0,4} = P(c/b) = 0.5 \\
\theta_{0,5} = P(c/\lnot b) = 0.5
$$
$$
P(O_1/\theta) = P(a) · P(b/a) · P(c/b) = 0.125 \\
P(O_2/\theta) = P(a) · P(b/a) · P(\lnot c/b) = 0.125 \\
P(O_3/\theta) = P(a) · P(\lnot b/a) · P(\lnot c/\lnot b) = 0.125 \\
P(O_4/\theta) = P(\lnot a) · P(b/\lnot a) · P(\lnot c/b) = 0.125 \\
P(O_5/\theta) = P(\lnot a) · P(\lnot b/\lnot a) · P(c/\lnot b) = 0.125 \\
P(O_6/\theta) = P(a) · P(\lnot b/a) · P(c/\lnot b) + P(a) · P(\lnot b/a) · P(\lnot c/\lnot b)= 0.25
$$
$$ \hat{l} = 1/6 · \log(0.125) · 5 + \log(0.25)=−1.9639$$

Expectation: 
$$  $$

## Clasificador Naive Bayes
## Evaluación de modelos probabilísticos
### Función de verosimilitud
### Otras medidas de rendimiento