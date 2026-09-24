## Introducción
**Problema computacional**:  $f: \Sigma^* \to \mathcal{P}(\Sigma^*)$ Donde $\Sigma$ es un alfabeto, $\Sigma^*$ representa cadenas de 0 o más elementos de ese alfabeto (entradas), y $\mathcal{P}(\Sigma^*)$ es la función conjunto potencia que mapea datos de entrada a un conjunto de datos de salida (que puede contener 0, 1 o más soluciones).

Tipos de problemas (como función):
- **Tratables**: se resuelven eficientemente o con un coste asumible (recursos limitados).
- **Intratables**: se resuelves pero consumen excesivos recursos.
- **Incomputables**: no se pueden resolver.

![[Pasted image 20260924124053.png|408]]

**Algoritmo**: conjunto ordenado de operaciones matemáticas que hallan la solución de un problema.

![[Pasted image 20260924124533.png]]

El nivel de dificultad de un problema viene dada por la mejor opción que ofrecen los algoritmos conocidos.

En la IA, el espacio de búsqueda de soluciones es inmenso (intratable) si se
quiere encontrar la solución exacta. Para ello se usan heurísticos que proporcionan soluciones aproximadas.

## Órdenes de magnitud
Relaciona cómo crece una cantidad de recursos (tiempo $T$ y espacio $S$) atendiendo a cómo crece el tamaño de la entrada $n$ al algoritmo $A$.

**Principio de invarianza**: dos implementaciones de un mismo algoritmo en lenguajes o arquitecturas distintas difieren en consumo de recursos únicamente por una constante multiplicativa: $\exists c, d \in \mathbb{R}^+,\ T_1(n) \le c·T_2(n)$ y $\ T_2(n) \le d · T_1(n) \implies T_1(n) \in \Theta(T_2(n))$ y $T_2(n) \in \Theta(T_1(n))$

**Notación asintótica**: describe el comportamiento del consumo de recursos cuando el tamaño de la entrada $n \rightarrow \infty$.
- $o(g(n))$: conjunto de funciones acotadas superiormente de forma estricta por un múltiplo de $g(n)$. Complejidad por debajo de cualquier múltiplo de $g$.
- $O(g(n))$: conjunto de funciones acotadas superiormente por un múltiplo de $g(n)$. Peor caso de un algoritmo.
-  $\Theta(g(n))$: conjunto de funciones en el mismo orden de complejidad que $g(n)$. Complejidad igual que la función $g$.
- $\Omega(g(n))$: conjunto de funciones acotadas inferiormente por un múltiplo de $g(n)$. Mejor caso de un algoritmo.
-  $\omega(g(n))$: conjunto de funciones acotadas inferiormente de forma estricta por un múltiplo de $g(n)$. Complejidad por encima de cualquier múltiplo de $g$.

![[Pasted image 20260924133316.png]]

![[Pasted image 20260924135037.png]]

Órdenes de crecimiento: $1 \ll \log n \ll n \ll n\log n \ll n^2 \ll n^3 \ll ... \ll 2^n \ll n!$

![[Pasted image 20260924135238.png]]

## Complejidad algoritmos
Reglas prácticas:
- **Instrucciones simples**: asignaciones, operaciones aritméticas, lectura/escritura y acceso a posiciones de arrays son de coste $\Theta(1)$.
- **Composición de instrucciones**: sean dos instrucciones $I_1, I_2 \rightarrow T_{I_1, I_2}(n) = T_1(n) + T_2(n) = \max(T_1(n), T_2(n))$
- **Instrucciones de selección (if-else)**: $T_{\text{selección}}(n) = T_{\text{condición}}(n) + \max(T_1(n),..., T_k(n))$
- **Instrucciones de iteración (bucles)**:

	![[Pasted image 20260924135931.png|541]]
	
	![[Pasted image 20260924135956.png|544]]

- **Subprogramas**:
	- **No recursivos**: se identifican las operaciones básicas (bucle más interno) y se resuelve el sumatorio
	
		![[Pasted image 20260924140221.png|484]]

	- **Recursivos**: teorema maestro $T(n) = a · T(\frac{n}{b}) + f(n)$ con $T(1) = \Theta(1)$ y $f(n) \in \Theta(n^d), d \ge 0$. Donde $a \ge 1$ es el número de subproblemas recursivos, $b > 1$ es el factor de reducción y $f(n)$ es el trabajo no recursivo.

		![[Pasted image 20260924140657.png|402]]

		![[Pasted image 20260924140737.png]]

## Complejidad problemas
Tipos de problemas:
- **Función**: toma una entrada y devuelve una salida (valor calculado). Por ejemplo calcular la longitud del camino más corto.
- **Búsqueda**: busca una estructura $S$ que cumpla el predicado $Q(I, S)$, siendo $I$ la entrada. Por ejemplo buscar un camino de A a B.
- **Umbral**: busca $S$ (verificador) que cumpla la función numérica $F(I,S) \le k$ para un valor de umbral $k$. Por ejemplo buscar un camino con longitud menor que $k$.
- **Optimización**: busca $S$ que minimice o maximice la función numérica $F(I,S)$. Por ejemplo buscar el camino más corto.
- **Decisión**: función que devuelve para la entrada $I$ verdadero o falso (existe solución para el problema $I$). $L=\{x \in \Sigma^* \mid x\ \text{es solución al problema}\}$. Por ejemplo comprobar si la suma de dos números es correcta o no.

Complementario de un problema: sea $D$ un problema de decisión, $\bar{D}$ invierte la respuesta. $\bar{L}=\{x \in \Sigma^* \mid x \notin L\}$. Por ejemplo, comprobar si un grafo pertenece a HAMPATH es comprobando la solución. Para comprobar que no pertenece hay que probar todas las combinaciones.

- **Resolver / Computar**: un problema $P$ resuelve o computa un problema si da respuesta a todas las entradas.
- **Decidir**: $P$ siempre termina. Devuelve verdadero si la entrada pertenece al lenguaje o falso en caso contrario.
- **Reconocer**: $P$ devuelve verdadero si pertenece al lenguaje, pero si no pertenece devuelve falso o diverge (no termina).
- **Computable / Decidible:** existe un algoritmo que lo resuelve/decide terminando para todas las entradas.
- **Incomputable / Indecidible:** No existe ningún algoritmo que termine para todas las entradas.