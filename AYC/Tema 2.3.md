## Complejidad en tiempo
### Clases básicas de complejidad en tiempo
Sea $t: \mathbb{N} \to \mathbb{N}$, se define la clase de complejidad temporal:
- $TIME(t(n)) = \{ L \mid L \text{ se decide en tiempo } O(t(n)) \text{ por una mTD} \}$ 
- $NTIME(t(n)) = \{ L \mid L \text{ se decide en tiempo } O(t(n)) \text{ por una mTnD} \}$

Se mide como el número de pasos (veces que se ejecuta la función de transición $\delta$) que realiza la máquina antes de terminar para cualquier entrada de longitud $n$.

### Teorema de aceleración lineal de tiempo
En la mTD multicinta, las constantes multiplicativas del tiempo de ejecución no alteran la clase de complejidad temporal. Es posible acelerar una computación por un factor constante sin cambiar su orden de crecimiento asintótico.

Sea $L \in TIME(f(n))$. Entonces, para cualquier $\varepsilon > 0$, se cumple que: $L \in TIME(f'(n))$ donde $f'(n) = \varepsilon \cdot f(n) + n + 2$ (el +2 es porque se llega al final y se vuelve a la última celda válida de la entrada)

Se construye una máquina $M'$ con un nuevo alfabeto $\Gamma'$ que agrupa $m$ símbolos de la cinta original en una sola celda. Leer la entrada original e ir escribiéndola de forma comprimida en otra cinta consume $n$ pasos.

![[Pasted image 20261003143024.png]]

$M'$ simula repetidamente $m$ pasos de la máquina original $M$ realizando 6 o menos pasos propios. Si no se permitiese dejar la cabeza quieta ($S$), serían 7 pasos.

Seleccionando un valor de $m = \lceil 6 / \varepsilon \rceil$, el tiempo peor caso de $M'$ es $|x| + 2 + 6 \lceil f(x)/m \rceil \le \varepsilon \cdot f(n) + n + 2$.

Para problemas que requiere leer toda la entrada, $t(n) \ge n$:
- $f(n)$ es superlineal: la constante $c$ en el término dominante pude pequeña. Por lo general, $TIME(f(n)) = TIME(O(f(n)))$
- $f(n)$ es lineal: $f(n) = c \cdot n$ con $c > 1$. $c$ puede tomar un valor cercano a uno pero no menor. Por tanto, $TIME(c \cdot n)$ no se puede acelerar a $TIME(\varepsilon \cdot n)$ para $0 < \varepsilon < 1$.

Cualquier cota de tiempo cumple $t(n) \ge n$.

### Clases centrales de complejidad de tiempo
- $P$ **(Tiempo Polinómico Determinista)**: $P = \bigcup_{k \ge 1} TIME(n^k)$
- $NP$ **(Tiempo Polinómico No Determinista)**: $NP = \bigcup_{k \ge 1} NTIME(n^k)$
- $EXP$ **(Tiempo Exponencial Determinista)**: $EXP = \bigcup_{k \ge 1} TIME(2^{n^k})$

![[Pasted image 20261003144510.png]]

**Modelos de Acceso Aleatorio (RAM)**: modelo donde se puede acceder a cualquier índice de la entrada al instante sin leerla toda. $TIME(\log n)$

## Complejidad en espacio
### Clases básicas de complejidad en espacio
Sea $s: \mathbb{N} \to \mathbb{N}$, se define la clase de complejidad espacial:
- $SPACE(s(n)) = \{ L \mid L \text{ se decide en espacio } O(s(n)) \text{ por una mTD} \}$ 
- $NSPACE(s(n)) = \{ L \mid L \text{ se decide en espacio } O(s(n)) \text{ por una mTnD} \}$

Se mide como el número máximo de celdas distintas visitadas en las cintas de trabajo durante la ejecución para cualquier entrada de longitud $n$.

**Espacio sublineal**: en modelos de mT se necesita leer la entrada (tiempo $n$) y la propia entrada necesita espacio $n$. Para ello cambiamos al modelo offline.

**mT offline**: una cinta de entrada (lectura) y una de trabajo (las celdas ocupadas son las que se consideran para determinar el espacio ocupado).

![[Pasted image 20261004154745.png]]

### Teorema de compresión lineal de espacio
Si $L$ es aceptado por una mTD o mTnD de $k$ cintas acotado espacialmente por $s(n)$, para cualquier $c \gt 0$, $L$ es aceptado por una mT multicinta ($k$ cintas) o unicinta acotada por $c·s(n)$.

Se comprime símbolos de cada cinta agrupándolos de $m$ en $m$ (un vector). Para $k$ cintas se agrupan de $m$ en $m$ (una matriz). $m$ se elige tal que $2 \le c·k·m$.

![[Pasted image 20261004155757.png]]

La nueva mT $M'$ no usa más de $\left \lceil \frac{s(n)}{k·m} \right \rceil$ celdas, usando una cota $\left \lceil \frac{s(n)}{k·m} \right \rceil \le 2·\frac{s(n)}{k·m}$. Dada una $k$ si elegimos un $m$ grande, tendremos una $c$ pequeña $\frac{2}{k·m} \le c · s(n)$. El alfabeto cambiará y habrá muchos más estados y transiciones, pero seguirá siendo finito.

![[Pasted image 20261004160323.png]]

Cualquier cota de espacio cumple $s(n) \ge \log n$.

### Clases centrales de complejidad en espacio
- $L$ **(Espacio Logarítmico Determinista):** $L = SPACE(\log n)$
- $NL$ **(Espacio Logarítmico No Determinista):** $NL = NSPACE(\log n)$
- $PSPACE$ **(Espacio Polinómico Determinista):** $PSPACE = \bigcup_{k \ge 1} SPACE(n^k)$

![[Pasted image 20261004160756.png]]

**Teorema de Savitch**: cualquier problema que puede ser resuelto por una mTnD usando un espacio determinado, puede resolverse en una mTD elevando ese espacio al cuadrado. $NSPACE(s(n)) \subseteq SPACE((s(n)^2)$ con $s(n) \ge \log n$.

## Relación entre complejidades de tiempo y espacio
El espacio usable con $TIME(f(n))$ es $O(f(n))$ celdas.
El tiempo usable con $SPACE(f(n))$ es $2^{O(f(n))}$ configuraciones posibles.

Sea $f,g: \mathbb{N} \to \mathbb{N}$. Si existe $n_0 \in \mathbb{N}: \forall n \ge n_0, f(n) \le g(n)$
- $TIME(f(n)) \subseteq TIME(g(n))$.
- $NTIME(f(n)) \subseteq NTIME(g(n))$.
- $SPACE(f(n)) \subseteq SPACE(g(n))$
- $NSPACE(f(n)) \subseteq NSPACE(g(n))$

Por monotonía por cota de función, si tenemos un margen superior de recursos $g(n)\ge f(n)$, cualquier problema que se decide con la cota más pequeña $f(n)$, también se decide en $g(n)$.

Sea $f: \mathbb{N} \to \mathbb{N}$
- $TIME(f(n)) \subseteq NTIME(f(n))$: una mTD es un caso de la mTnD (simplemente hace una sola transición, en vez de usar varias alternativas de ramificación).
- $SPACE(f(n)) \subseteq NSPACE(f(n))$: una mTD es un caso de la mTnD (cualquier lenguaje decidible en espacio $f(n)$ está contenido en la clase no determinista equivalente).
- $TIME(f(n)) \subseteq SPACE(f(n))$: en $f(n)$ pasos se alcanza $f(n)$ celdas. En un tiempo limitado por $f(n)$ es imposible visitar o modificar más de $f(n)$ celdas.
- $NTIME(f(n)) \subseteq NSPACE(f(n))$: en $f(n)$ pasos se alcanza $f(n)$ celdas. En un tiempo limitado por $f(n)$ es imposible visitar o modificar más de $f(n)$ celdas.
- $NTIME(f(n)) \subseteq SPACE(f(n))$: se puede simular el árbol de $f(n)$ pasos mediante recorrido en profundidad (DFS) reutilizando las celdas.

$SPACE(f(n)) \subseteq TIME(2^{O(f(n))})$: el número total de configuraciones distintas posibles de una máquina usando espacio $f(n)$ está acotado por $2^{O(f(n))}$. Como se trata de una mTD que decide (debe detenerse siempre), no puede repetir ninguna configuración. Por ello, su tiempo de ejecución está acotado por el número total de configuraciones posibles $2^{O(f(n))}$.

$NSPACE(f(n)) \subseteq TIME(2^{O(f(n))})$: usando un espacio de memoria $f(n)$, la máquina solo puede formar un número de configuraciones distintas, a lo sumo $2^{O(f(n))}$. Una mTD puede recorrer todo el grafo de configuraciones posibles mediante Búsqueda en Anchura (BFS) para ver si existe una rama de aceptación, tardando a lo sumo un tiempo de $2^{O(f(n))}$.

Es mejor tener espacio acotado (tiempo infinito) que tiempo acotado (espacio infinito).

![[Pasted image 20261004202316.png]]

- $L \subseteq NL$: todo algoritmo determinista es un caso particular de no determinista. $SPACE(f(n)) \subseteq NSPACE(f(n))$.
- $NL \subseteq P$: una mTnD en espacio $O(\log n)$ genera un grafo de configuraciones con $2^{O(\log n)} = n^c$ nodos. Encontrar el camino con un algoritmo BFS toma tiempo polinómico $O(n^c)$. $NSPACE(f(n)) \subseteq TIME(2^{O(f(n))})$.
- $P \subseteq NP$: el caso determinista es un caso particular del no determinista. $TIME(f(n)) \subseteq NTIME(f(n))$
- $P \subseteq PSPACE$: una mTD que da $t(n)$ pasos no accede a más de $t(n)$ celdas. $TIME(f(n)) \subseteq SPACE(f(n))$.
- $NP \subseteq PSPACE$: una mTnD que da $t(n)$ pasos no accede a más de $t(n)$ celdas. Una mTD puede recorrer todas sus ramas usando $t(n)$ celdas. $NTIME(f(n)) \subseteq SPACE(f(n))$.
- $PSPACE \subseteq EXP$: el número total de configuraciones distintas está acotado por $2^{O(f(n))}$. Como la mTD debe detenerse, su tiempo de ejecución determinista está acotado por $2^{O(f(n))} \in EXP$. $SPACE(f(n)) \subseteq TIME(2^{O(f(n))})$

![[Pasted image 20261004203158.png]]