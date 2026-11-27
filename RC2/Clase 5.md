# Conjuntos y sistemas difusos
## Conjuntos difusos
La función de pertenencia asigna un grado continuo en el intervalo \[0, 1\]. 

- **Variable lingüística $X$**: concepto que vamos a calificar (edad, altura...).
- **Universo de discurso $U$**: rango de valores que toman los elementos (altura puede ser \[1.4, 2.3\]).
- **Valor lingüístico**: diferentes clasificaciones que hay sobre una variable lingüística (altura puede ser bajo, mediano y alto).
- **Núcleo de un conjunto difuso $A$**: $\text{Núcleo}(A)=\{x\in U \mid \mu_A(x)=1\}$
- **Conjunto difuso**: (valor lingüístico, función de pertenencia).
- **Alfa-corte de un conjunto difuso $A$**: $A_\alpha = \{x\in U \mid \mu_A(x) \ge \alpha \}$. Es estricto si la desigualdad es estricta.
- **Soporte de un conjunto difuso de $A$**: $\text{Soporte}(A)=\{x\in U \mid \mu_A(x) \gt 0\}$
- **Altura de un conjunto difuso $A$**: valor más grande de su función de pertenencia.
- **Conjunto difuso normalizado $A$**: $\exists x \in U \mid \mu_A(x)=1$
- **Punto de cruce de un conjunto difuso $A$**: $x\in U \mid \mu_A(x)=0.5$
- **Conjunto difuso unitario (singleton)**: su soporte es un único punto $x\in U$ tal que la función de pertenencia de $x$ es 1.
- Un conjunto difuso $A$ está incluido en un conjunto difuso $B$ si $\forall x\in U \mid \mu_A(x)\le \mu_B(x)$

![[Pasted image 20261125181255.png]]

![[Pasted image 20261125181330.png]]

Núcleo = 1.7
Soporte(A) = $[1.5, 1.9]$
Alfa-corte 0.5 = $[1.6, 1.8]$
Puntos de cruce: 1.6 y 1.8

![[Pasted image 20261125182003.png]]




## Funciones de pertenencia
![[Pasted image 20261125182023.png]]

![[Pasted image 20261125182039.png]]

**Gamma**: valores más altos.
**L**: valores más bajos.
**Trapezoidal y lambda o triangular**: valores medios.

## Etiquetas lingüísticas
Se definen conuntos difusos a partir de otros con una función $f(y)$.

![[Pasted image 20261125183027.png]]

![[Pasted image 20261125183049.png]]

## Conjunto total, conjunto vacío, relación de inclusión
### Complementario
Definido por una función $c: [0,1] \to [0,1]$ que debe cumplir:
1. Concordancia con el caso nítido: $c(1)=0, c(0)=1$.
2. Estrictamente decreciente: $\alpha > \beta \implies c(\alpha) < c(\beta)$.
3. Involución: $c(c(\alpha)) = \alpha$

![[Pasted image 20261125184137.png]]

### Intersección
Definida por funciones $i:[0,1]\times [0,1]\to[0,1]$ que cumplen concordancia nítida, conmutatividad, asociatividad, identidad ($i(\alpha, 1) = \alpha$) y monotonía.

![[Pasted image 20261125184310.png]]

### Unión
Definida por funciones $u: [0,1] \times [0,1] \to [0,1]$ que cumplen concordancia nítida, conmutatividad, asociatividad, identidad ($u(\alpha, 0) = \alpha$) y monotonía.

![[Pasted image 20261125184501.png]]

## Operaciones con conjuntos difusos
