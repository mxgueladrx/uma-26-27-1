![[Pasted image 20261009165841.png]]

Antes de todo voy a asignar a cada nodo un identificador:
- **Madre gen inventado**: M
- **Padre gen inventado**: P
- **Gen inventado**: G
- **Alzheimer**: A
- **Daño cerebral**: D
- **Edad avanzada**: E
- **Bajo nivel de estudios**: B
- **Test MMSE**: T
- **Perdida de memoria**: PM
- **Perdida de autonomía**: PA

## Pregunta 1
**¿Qué independencias/dependencias entre las variables de la red implican las hipótesis de independencia condicional?**

$\forall X \in V$ y $\forall Y \in V - \{X \cup de(X) \cup pa(X)\} \implies X$ es independiente de $Y$ dado $pa(X)$

- $X = M$ ind $\{P, E, B\}$ a priori
- $X = P$ ind $\{M, E, B\}$ a priori
- $X = G$ ind $\{E, B\}$ dados $\{M, P\}$
- $X = A$ ind $\{M, P, E, B\}$ dados $\{G\}$
- $X = D$ ind $\{M, P, G, E, B\}$ dados $\{A\}$
- $X = E$ ind $\{M, P, G, A, D, B, PM, PA\}$ a priori
- $X = B$ ind $\{M, P, G, A, D, E, PM, PA\}$ a priori
- $X = T$ ind $\{M, P, G, A, PM, PA\}$ dados $\{D, E, B\}$
- $X = PM$ ind $\{M, P, G, A, E, B, T\}$ dados $\{D\}$
- $X = PA$ ind $\{M, P, G, A, D, E, B, T\}$ dados $\{PM\}$

## Pregunta 2
**Si suponemos ciertas las hipótesis de independencia condicional, ¿cuántas probabilidades sería necesario especificar?. Dar estos valores de una forma coherente con el sentido común.**

Sabiendo que todas las variables son binarias, para un nodo con $n$ padres se necesita $2^n$ probabilidades independientes (ya que el complementario se calcula como $1-p$).

- $M: k=0 \implies 2^0 = 1$ probabilidades. 
	- $P(M) = 0.2$
- $P: k=0 \implies 2^0 = 1$ probabilidades. 
	- $P(P) = 0.2$
- $G: k=2 \implies 2^2 = 4$ probabilidades. 
	- $P(G\mid M, P) = 0.75$
	- $P(G\mid M, \overline{P}) = 0.5$
	- $P(G\mid \overline{M}, P) = 0.5$
	- $P(G\mid \overline{M}, \overline{P}) = 0$
- $A: k=1 \implies 2^1 = 2$ probabilidades. 
	- $P(A\mid G) = 0.85$
	- $P(A\mid \overline{G}) = 0.05$
- $D: k=1 \implies 2^1 = 2$ probabilidades. 
	- $P(D\mid A) = 0.90$
	- $P(D\mid \overline{A}) = 0.02$
- $E: k=0 \implies 2^0 = 1$ probabilidades.
	- $P(E)=0.3$
- $B: k=0 \implies 2^0 = 1$ probabilidades. 
	- $P(B)=0.25$
- $T: k=3 \implies 2^3 = 8$ probabilidades. 
	- $P(T \mid D, E, B) = 0.99$
	- $P(T \mid D, E, \overline{B}) = 0.95$
	- $P(T \mid D, \overline{E}, B) = 0.95$
	- $P(T \mid D, \overline{E}, \overline{B}) = 0.90$
	- $P(T \mid \overline{D}, E, B) = 0.85$
	- $P(T \mid \overline{D}, E, \overline{B}) = 0.60$
	- $P(T \mid \overline{D}, \overline{E}, B) = 0.50$
	- $P(T \mid \overline{D}, \overline{E}, \overline{B}) = 0.05$
- $PM: k=1 \implies 2^1 = 2$ probabilidades. 
	- $P(PM \mid D) = 0.85$
	- $P(PM\mid \overline{D}) = 0.05$
- $PA: k=1 \implies 2^1 = 2$ probabilidades. 
	- $P(PA \mid PM) = 0.80$
	- $P(PA\mid \overline{PM}) = 0.02$

Necesitaríamos un total de $1+1+4+2+2+1+1+8+2+2=24$ probabilidades.

## Pregunta 3
**Si no podemos suponer las hipótesis de independencia condicional, ¿qué probabilidades deberíamos pedir al experto? ¿Cuántos valores son, en total?.**

Debemos pedir al experto la probabilidad para cada combinación de $P(M, P, G, A, D, E, B, T, PM, PA)$

Para una red con $n$ nodos no bayesiana se necesitarían $2^n - 1$ probabilidades. Como nuestra red tiene $n=10$ nodos, se necesitaría $2^{10}- 1 = 1023$ probabilidades.

## Pregunta 4
**¿Cómo podemos calcular la probabilidad conjunta a partir de las condicionadas?.**

Usando el teorema fundamentar (factorización de la probabilidad) de la forma $P(x1,...,x_n)=\prod P(x_i \mid pa(x_i))$.

$P(M, P, G, A, D, E, B, T, PM, PA)=P(M)·P(P)·P(G\mid M, P)·P(A\mid G)·P(D\mid A)·P(E)·P(B)·P(T\mid D, E, B)·P(PM\mid D)·P(PA\mid PM)$

## Pregunta 5
**Aplicando el teorema de factorización, indica cómo se calcularía la probabilidad de un valor concreto de un nodo de tu red dados dos valores concretos de dos nodos de tu red.**

Vamos a calcular la probabilidad de que un paciente tenga alzheimer $A$ sabiendo que suspende el test MMSE $T$ y tiene pérdida de autonomía $PA$.

$$P(A=\text{si} \mid T=\text{f}, PA=\text{si}) = \frac{P(A=\text{si}, T=\text{f}, PA=\text{si})}{P(T=\text{f}, PA=\text{si})}$$

$$= \frac{\sum_{M, P, G, D, E, B, PM} P(M, P, G, A=\text{si}, D, E, B, T=\text{f}, PM, PA=\text{si})}{\sum_{A, M, P, G, D, E, B, PM} P(M, P, G, A, D, E, B, T=\text{f}, PM, PA=\text{si})}$$

$$= \frac{128 \text{ sumandos} \cdot 9 \text{ multiplicaciones}}{256 \text{ sumandos} \cdot 9 \text{ multiplicaciones}}$$

## Pregunta 6
**Quédate con una subestructura de tu red que tenga al menos 4 nodos y forma de árbol y aplica el algoritmo de propagación para redes en forma de árbol para inicializar la red y realizar 
alguna inferencia.**

Usaremos la subred: $PA \leftarrow PM \leftarrow D \rightarrow T$

![[Pasted image 20261025162928.png]]

Para ello hemos tenido que ajustar algunas probabilidades:
- Nodo D: en la red original, $D$ dependía de $A$, por lo que el valor 0.9 era la probabilidad condicionada $P(D \mid A)$. Al aislar la subred, $D$ pasa a ser el nodo raíz y requiere su probabilidad a priori marginal $P(D) = P(D \mid A)P(A) + P(D \mid \overline{A})P(\overline{A}) \approx 20\%$.
- Nodo T: en la red original, $T$ dependía de 3 padres ($D$, $E$ y $B$). $T$ pasa a tener un único padre ($D$). Las probabilidades las creamos nosotros por sentido común, con un 90% de suspenso si tiene $D$, y un 20% si no tiene $D$.

![[Pasted image 20261025173919.png]]

![[Pasted image 20261025173940.png]]

![[Pasted image 20261025173949.png]]

![[Pasted image 20261025173932.png]]

![[Pasted image 20261025194303.png]]

![[Pasted image 20261025194309.png]]

![[Pasted image 20261025194313.png]]

Vemos que todas las probabilidades coinciden.