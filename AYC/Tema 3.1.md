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

Por fuerza bruta sería comprobar todos los divisores posibles (entrada de tamaño $n$ y base $k\gt1$) sería $O(2^n)$. Con el algoritmo de Euclides, cada dos iteraciones, se reducen los valores mínimo a la mitad (logaritmos intercambios). La entrada se mide como $\log_2(x)$ bits. Se ejecutan $O(\log x)$ bucles de Euclides, equivalente a $O(n)$ iteraciones. Para calcular el módulo con números de $n$ bits se requiere $O(n^2)$ pasos. Al final tenemos $O(n^3)$.

## Grado de complejidad P
**Equivalencia**: $(L_1 \le_p L_2)\land(L_2 \le_p L_1) \iff L_1 \equiv_p L2$. Cada clase de p-equivalencia es un grado de complejidad.

$(\forall L_1,L_2 \in P) \land (L_1, L_2 \not=\emptyset) \land (L_1, L_2 \not=\Sigma^*) \implies L_1 \le_p L_2$

Se eligen dos cadenas de $L_2$, $u \in L_2$ y $v \not\in L_2$. El transductor $M_f$ simula $M_1$, si $M_1$ acepta $x$, $M_f$ escribe $u$, si rechaza escribe $v$.

$M_f$ opera en tiempo polinómico: $M_1$ decide $L_1 \in P$, opera en tiempo $n^r$ y $M_f$ también. Borrar lo escrito requiere lo mismo, $n^r$. Escribir $u$ o $v$ requiere constantes pasos $k$. El tiempo que opera $M_f$ es $n^r +n^r +k$.

## P-completitud
Reducción en espacio logarítmico $\le_{\log}$. Nos permite diferenciar entre tipos de dificultades de la clase P. $A\le_{\log}B \implies A \le_p B$, pero $A\le_p B \not\implies A \le_{\log} B$.

Un lenguaje $L$ es P-completo para $\le_{\log}$ si: $(L\in P) \land (\forall L'\in P, L' \le_{\log} L)$.

$PATH$ y $SHORTEST-PATH \in NC^2$. La Nick's Class se define sobre una máquina paralela (fáciles de P). Cae a tiempos polilogarítmicos.

$CVP \in$ P-completo, determina si un circuito booleano con entradas fijadas produce salida 1, no se puede paralelizar porque hay que esperar que las señales se propaguen.

## P cerrado bajo complemento (P=co-P)
$\overline{L}=\{w\in\Sigma^* \mid w \not\in L\}$. Si $L\in P \implies \overline{L} \in P$.

Si $L\in P$, existe una mTD $M$ que decide $L$ en poli-tiempo. Existe una $M'$ que decide $\overline{L}$. Solo se invierte la salida (un paso más) y sigue estando en poli-tiempo. $P=co-P$.