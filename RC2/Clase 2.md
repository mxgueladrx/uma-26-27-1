## Variables aleatorias
Función que asigna un valor numérico a cada resultado posible de un experimento aleatorio.
- **Variables aleatorias discretas**: toman valores en un conjunto finito o infinito numerable.
- **Variables aleatorias continuas**: toman valores en un conjunto continuo o intervalo de números reales.

## Distribuciones de probabilidad
Función que describe cómo se reparte la probabilidad entre los posibles valores que puede tomar una variable aleatoria.

En el discreto re representa como $p_X(x)=P(X=x)$. Debe cumplir:
- $\forall x \mid 0 \le P(X=x) \le 1$
- $\sum_{x} P(X=x)=1$

---
![[Pasted image 20260916175545.png]]

$P(X=0)$ es la probabilidad de que ninguno cumpla el mismo día.
$P(X=1)=1-P(X=0)=1-(\frac{364}{365}·\frac{363}{365} ... \frac{326}{365}) \approx 0.9$

---

## Distribuciones conjunta y marginal
**Distribución de probabilidad conjunta**: probabilidad de cada combinación simultánea de valores de un vector aleatorio $X$ a través de una función que se llama función de distribución de masa de probabilidad conjunta. $p_X(x)=P(X_1=x_1, X_2=x_2,...,X_n=x_n$. Debe cumplir:
- $p_X(x) \ge 0$
- $\sum_{X}p_X(x)=1$

**Distribución marginal**: asigna una probabilidad a una variable $X_i$ sin fijar los valores de las demás variables. $p_{X_i}(X_i=x_i)=\sum_{X_1}...\sum_{X_{i-1}} \sum_{X_{i+1}}...\sum_{X_n} p_X(X_1=x_1,...,X_n=x_n)$

---
![[Pasted image 20260916181201.png]]

---

## Probabilidad condicionada
Calcula la probabilidad de que una variable aleatoria $X$ tome un valor $x$ cuando se conoce otra aleatoria $Y$ con valor $y$. $P(X=x \mid Y=y)=\frac{P(X=x, Y=y)}{P(Y=y)}$. Debe cumplir que $P(Y=y) \gt 0$

---
![[Pasted image 20260916181752.png]]
hacer tambien

$P(Z=0 \mid Y=0)=\frac{P(Z=0, Y=0)}{P(Y=0)}=\frac{0.5588}{0.725}=0.77$

---

## Independencia de variables aleatorias
**Definición por probabilidad condicional**: dos variables $X$ e $Y$ son independientes cuando conocer el valor de una no modifica la distribución de probabilidad de la otra $P(X=x \mid Y=y)=P(X=x), \forall Y \mid P(Y=y)\gt0$

**Definición por probabilidad conjunta**: si $P(X=x, Y=y) = P(X=x) · P(Y=y)$

---
![[Pasted image 20260916182624.png]]
a) Como son independientes, $P(X=1, Y=1) = 0.02 · 0.03=0.0006$
b) Como son independientes y $P(Y=1)\gt 0$ entonces $P(X=1 \mid Y=1) = P(X=1)=0.02$
c) $P(X=1 \cup Y=1)=0.02+0.03-0.0006=0.0494$

---

## Independencia condicional de variables aleatorias
$X$ e $Y$ son condicionalmente independientes dada $Z$ si, una vez conocido $Z$, conocer $Y$ no modifica la distribución de $X$. $P(X=x \mid Y=y, Z=z)=P(X=x \mid Z=z)$. También puede ser $P(X=x, Y=y \mid Z=z)=P(X=x \mid Z=z) · P(Y=y \mid Z=z)$

## Ley de probabilidad total
Sea $X$ una variable aleatoria discreta e $Y$ otra. Para cualquier $y$, $P(Y=y)=\sum^{n}_{i=1}P(Y=y\mid X=x_i)·P(X=x_i)$

## Teorema de Bayes
Calcula la probabilidad de una hipótesis $X$ cuando se observa nueva evidencia $Y$ mediante $P(X \mid Y)=\frac{P(Y\mid X) · P(X)}{P(Y)}$ si $P(Y) \gt 0$
- $P(X)$ es la probabilidad a priori: creencia inicial sobre $X$ antes de observar $Y$
- $P(Y\mid X)$ es la verosimilitud: probabilidad de observar $Y$ según $X$
- $P(Y)$ es la probabilidad de $Y$. Se suele usar la ley de la probabilidad total
- $P(X\mid Y)$ es la probabilidad a posteriori: creencia actualizada sobre $X$ después de observar $Y$

---
![[Pasted image 20260916185206.png]]
hacer

---

## Regla de la cadena
Calcula la probabilidad conjunta de un conjunto de variables aleatorias mediante el producto de probabilidades condicionadas. Para $n$ variables aleatorias, $P(X_1,...X_n)=P(X_1)·P(X_2\mid X_1)·P(X_3\mid X_1,X_2)...P(X_n \mid X_1,...,X_{n-1})$

---
![[Pasted image 20260916185706.png]]


---
