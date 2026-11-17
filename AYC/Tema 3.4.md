## $CLIQUE \in NPC$
$CLIQUE = \{\langle G, k \rangle \mid G \text{ contiene un clique de tamaño } k\}$

### $CLIQUE \in NP$
- **Decisión con mTnD**: de forma no determinista selecciona un subconjunto $c$ de $k$ nodos de $G$ ($O(n)$). Comprueba que $G$ contenga todas las arcos entre los nodos de $c$ ($O(n^3)$).
- **Verificación con mTD**: comprueba que el certificado $|c| = k$ ($O(n)$), que $c \subseteq V$ ($O(n^2)$) y que existan todas las aristas entre los nodos de $c$ ($O(n^3)$).

### $3SAT \le_p CLIQUE$
![[Pasted image 20261113192151.png]]

**Gadget**: la función $f(\phi)$ genera $\langle G, k \rangle$, donde $k$ es el número de cláusulas. Para cada cláusula $C_i = (a_i \lor b_i \lor c_i)$, se crean 3 nodos en $G$ (llamados terna). Se conectan dos nodos mediante un arco si y solo si:
1. Pertenecen a cláusulas (ternas) distintas.
2. Sus literales no son contradictorios (es decir, no son $x$ y $\bar{x}$).

![[Pasted image 20261113192306.png]]

![[Pasted image 20261113192316.png]]

**Doble implicación**:
- **SI (**$\Rightarrow$**)**: si $\phi$ es satisfacible, elegimos un literal TRUE por cláusula; al no haber contradicciones ni aristas dentro de la misma cláusula, forman un clique de tamaño $k = m$.
- **SÓLO SI (**$\Leftarrow$**)**: un clique de tamaño $k$ exige tomar un nodo por cláusula sin aristas entre literales opuestos, lo que define una asignación que satisface $\phi$.

**Complejidad de** $f$: se crean $3k$ nodos ($O(k)$) y hasta $O(k^2)$ arcos. La comprobación de aristas requiere tiempo $O(1)$ por par, construyendo el grafo en tiempo $O(k^2)$, (polinómico).

## $VERTEX-COVER \in NPC$
$VERTEX-COVER = \{\langle G, k \rangle \mid \text{existe } c \subseteq V \text{ con } |c| \le k \text{ que cubre todos los arcos}\}$

### $VERTEX-COVER \in NP$
- **Decisión con mTnD**: selecciona de forma no determinista un subconjunto $c$ con $|c| \le k$ ($O(n)$) y comprueba que toda arista de $G$ toque al menos un nodo de $c$ ($O(n^3)$).
- **Verificación con mTD**: verifica que el certificado $c$ sea subconjunto válido de nodos de $G$ ($O(n^2)$), que $|c| \le k$ ($O(n)$) y que cubra todas las aristas $E$ ($O(n^3)$).

### $3SAT \le_p VERTEX-COVER$
![[Pasted image 20261113193203.png]]

**Gadget**: para una fórmula $\phi$ con $l$ variables y $m$ cláusulas:
1. Se crean $l$ bloques de variables: cada uno consiste en una pareja de nodos $(x_i, \bar{x}_i)$ unidos por un arco ($2l$ nodos y $l$ arcos en total).
2. Se crean $m$ bloques de cláusulas: cada uno es un triángulo de 3 nodos representando los 3 literales de la cláusula ($3m$ nodos y $3m$ arcos).
3. Se une cada literal del bloque de variables con los nodos de literal idéntico en los triángulos de las cláusulas ($3m$ arcos).
4. Se fija el valor objetivo $k = l + 2m$.

![[Pasted image 20261113193414.png]]

![[Pasted image 20261113193435.png]]

**Doble implicación**:
- **SI (**$\Rightarrow$**)**: si $\phi$ es satisfacible, elegimos los $l$ nodos de variables verdaderas y los $2m$ nodos de literales falsos en las cláusulas, cubriendo todas las aristas con $k = 2m + l$ nodos.
- **SÓLO SI (**$\Leftarrow$**)**: un recubrimiento de tamaño $2m+l$ fuerza a dejar un nodo libre por cláusula que debe ser cubierto desde su variable, garantizando que cada cláusula tiene un literal TRUE.

**Complejidad de** $f$: se construye $2l + 3m$ nodos y $l + 6m$ arcos en tiempo $O(l + m) = O(n)$, (polinómico).

## $SUBSET-SUM \in NPC$
$SUBSET-SUM = \{\langle S, t \rangle \mid \exists S' \subseteq S \text{ tal que } \sum_{x \in S'} x = t\}$

### $SUBSET-SUM \in NP$
- **Decisión con mTnD**: selecciona de forma no determinista un subconjunto $c \subseteq S$ ($O(n)$), calcula la suma de sus elementos ($O(n)$) y acepta si la suma coincide con $t$.
- **Verificación con mTD**: verifica que $c \subseteq S$ validando frecuencias ($O(n^2)$ u $O(n \log n)$), suma los elementos ($O(n)$) y compara con $t$.

### $3SAT \le_p SUBSET-SUM$
![[Pasted image 20261113194527.png]]

**Gadget**: para una fórmula $\phi$, $f(\phi)$ construye los números de $S$ con $l$ variables y $m$ cláusulas:
1. Se crea una columna para cada variable y cláusula.
2. Cada columna tiene asignada 2 filas (uno representa TRUE y otro FALSE). 
	- Tienen 1 en la columna de su fila correspondiente. 0 en las demás.
	- Tienen 1 si la variable aparece en la cláusula correspondiente. 0 en las demás.
3. El valor $t$ se define con un 1 en las columnas de variables (elije $x$ o $\lnot x$) y un 3 en las columnas de cláusulas (al menos una variable satisface la cláusula).
4. Sea cada fila escrita como un número en base 10, un subconjunto de ellas tiene que sumar $t$.

![[Pasted image 20261113200948.png]]

![[Pasted image 20261113201002.png]]

**Doble implicación**:
- **SI (**$\Rightarrow$**)**: si $\phi$ es satisfacible, elegimos $y_i$ o $z_i$ según la verdad y ajustamos con $0, 1$ o $2$ números de relleno ($g_j, h_j$) por cláusula para que la suma exacta en cada columna sea $t$.
- **SÓLO SI (**$\Leftarrow$**)**: sumar $1$ en variables exige elegir $y_i$ XOR $z_i$ (asignación válida), y sumar $3$ en cláusulas obliga a tener $\ge 1$ literal TRUE (el relleno aporta como máximo $2$).

**Complejidad de** $f$: se genera $2l + 2m$ filas de $l + m$ dígitos en tiempo $O(n^3)$ (relleno + comprobación de si la variable pertenece a la cláusula o no), (polinómico).

## $HAMPATH \in NPC$
$HAMPATH = \{\langle G, s, t \rangle \mid \text{existe un camino en } G \text{ de } s \text{ a } t \text{ que visita cada nodo exactamente una vez}\}$

### $HAMPATH \in NP$
- **Decisión con mTnD**: escribe una lista no determinista de $n$ vértices comenzando en $s$ y terminando en $t$ ($O(n)$), comprobando la existencia de arcos consecutivos sin repetición de nodos ($O(n^2)$).
- **Verificación con mTD**: con el certificado $c$ (secuencia de vértices), se comprueba que cada nodo de $c$ está en $G$, no se repite, inicie en $s$ y finalice en $t$ ($O(n^2)$) y que cada par consecutivo corresponda a una arista existente en $G$ $O(n^3)$.

### $3SAT \le_p HAMPATH$
![[Pasted image 20261113202309.png]]

**Gadget**: se crea un diamante para cada variable (con una entrada $s$, salida $t$ y nodos en la horizontal):
- En la horizontal hay $3m+3$ nodos (2 por cláusula, 1 para separación de cláusulas (evitar atajos), 1 final y 2 de los bordes). $s$ y $t$ se conecta a los extremos.
- Cuando el camino entra por $s$ y cruza la horizontal:
	- $x$ es TRUE: recorre la horizontal de izquierda a derecha.
	- $x$ es FALSE: recorre la horizontal de derecha a izquierda.
- Cada clausula se representa con un nodo, fuera de los diamantes, y se desvía desde sus correspondientes literales. Para cada literal en una cláusula, añadimos dos arcos:
	- Si $x\in C$: el salto es de izquierda a derecha.
	- Si $\lnot x \in C$: el salto es de derecha a izquierda.
- Si la cláusula es satisfecha por $x$, el camino visita $C$. Cada nodo de cláusula debe ser recorrido al menos una de las variables que la satisfacen.

![[Pasted image 20261113205145.png]]

![[Pasted image 20261113205155.png]]

![[Pasted image 20261113205711.png]]

![[Pasted image 20261113205725.png]]

![[Pasted image 20261113205736.png]]

![[Pasted image 20261113205744.png]]

**Doble implicación**:
- **SI (**$\Rightarrow$**)**: si $\phi$ es satisfacible, recorremos la cadena de cada variable $x_i$ de izquierda a derecha si es TRUE o de derecha a izquierda si es FALSE. Al atravesar la cadena de una variable que satisface la cláusula $C_j$, tomamos un desvío que visita el nodo $C_j$ y regresa a la cadena, formando un camino de $s$ a $t$ que visita todos los vértices una vez.
- **SÓLO SI (**$\Leftarrow$**)**: si existe un camino hamiltoniano de $s$ a $t$, la estructura de los diamantes fuerza a atravesar cada cadena de variable de forma completa en una sola dirección, definiendo una asignación de verdad. Para que el camino visite cada nodo de cláusula $C_j$, debe realizar desvíos válidos desde las cadenas de variables con la polaridad correspondiente, garantizando que cada cláusula posee al menos un literal TRUE que satisface $\phi$.

**Complejidad de $f$**: genera $O(l \cdot m) = O(n^2)$ nodos y arcos en tiempo $O(n^2)$.