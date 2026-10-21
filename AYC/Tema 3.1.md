## Clase P
P es la clase de lenguajes decididos por máquinas de Turing deterministas utilizando tiempo polinómico (poli-tiempo), definida como $P = \bigcup_{k \ge 1} TIME(n^k)$ con $k \ge 1$. Corresponde a la clase de problemas que un ordenador puede resolver de forma eficiente.

**Tesis extendida de Church-Turing (ECTT)**: todos los modelos computacionales deterministas son polinómicamente equivalentes.

**Notación** $\langle \dots \rangle$: codificación razonable de 1 o más objetos en una cadena en poli-tiempo (por ejemplo, grafos codificados como lista o matriz de adyacencia).

## $PATH \in P$ y $SHORTEST-PATH \in P$
$PATH = \{\langle G, s, t \rangle \mid G \text{ es un grafo dirigido que tiene un camino de } s \text{ a } t\}$

Por fuerza bruta sería comprobar $O(n!)$ posibilidades. Usando búsqueda en anchura (BFS) toma $O(n^2)$. Se define una mTD sobre $\langle G,s,t\rangle$ donde marcamos el nodo $s$ ($O(1)$), avanzamos marcando nodos vecinos hasta que no se pueda más ($O(n^3)$). Si al final $t$ termina marcado ($O(1)$), se acepta, sino rechaza.

$SHORTEST-PATH = \{\langle G, s, t, k \rangle \mid G \text{ es un grafo dirigido que tiene un camino de } s \text{ a } t \text{ con longitud } \le k\}$

Por fuerza bruta sería comprobar todos los posibles caminos de longitud 2, 3, ..., $k$ ($O(n!)$). Usando búsqueda en anchura (BFS) toma $O(n^2)$. Se defina una mTD sobre $\langle G, s, t, k \rangle$ donde marcamos $s$ en el nivel 0 ($O(1)$), y del nivel 1 a $k$, marcamos los vecinos con nivel actual ($O(n^3)$). Si al final $t$ esta marcado con nivel $\le k$, se acepta, sino rechaza.

- Demostrar que $SHORTEST-PATH \in P$ por cierre bajo reducción $\le_p$ sabiendo que $PATH \in P$.
	![[Pasted image 20261021132803.png]]
	![[Pasted image 20261021132817.png]]

- Demostrar que $PATH \in P$ por cierre bajo reducción $\le_p$ sabiendo que $SHORTEST-PATH \in P$.
	![[Pasted image 20261021133000.png]]

## $RELPRIME \in P$
$RELPRIME = \{\langle x, y \rangle \mid x \text{ e } y \text{ son primos relativos (coprimos)}\}$

Por fuerza bruta sería comprobar todos los divisores posibles (entrada de tamaño $n$ y base $k\gt1$) sería $O(2^n)$.

## Grado de complejidad P


## P-completitud


## P cerrado bajo complemento (P=co-P)
