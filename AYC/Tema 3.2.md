## Clase NP
NP es la clase de lenguajes decididos por mTnD utilizando tiempo polinómico (poli-tiempo), definida formalmente como $NP = \bigcup_{k \ge 1} NTIME(n^k)$ con $k \ge 1$. Puede computar todo lo incluido en P.

### Grados en la clase NP
**Grado de equivalencia**: según $\le_p$ se define como $deg_p(L) = \{L' \mid L' \equiv_p L\}$, donde $L \equiv_p L'$ implica $(L \le_p L') \land (L' \le_p L)$. En NP se distinguen las siguientes estructuras de grados:

**Grado de la clase NP** (con $\le_p$): no existe.
**Grados en la clase NP** (con $\le_p$):
- **Grado de la clase NP-completo**: por demostrar que todos son equivalentes.
- **Grados entre P y NP-completos (NP-intermedios)**: si P $\not=$ NP, hay infinitos grados.
**Grados de la clase P**: todos son equivalentes.

### Definición de clase NP usando el concepto de verificador
Usar mTnD es problemático porque asume modelos de cómputo no disponibles en la realidad o mTD que consumen tiempo exponencial.

**Verificador** ($V$): algoritmo determinista para un lenguaje $A$ definido como $$A = \{w \mid V \text{ acepta } <w, c> \text{ para alguna cadena } c\}$$
**Certificados** ($c$): información adicional de longitud polinómica respecto a $|w|$ que permite a $V$ verificar la pertenencia de $w$ a $A$ en poli-tiempo.

**Teorema**: $$L \in NP \iff L \text{ es decidido por mTnD en poli-tiempo} \iff L \text{ es verificado por mTD en poli-tiempo}$$
- **Demostración** $\implies$ **(solo si)**: dado un verificador mTD $V$ en poli-tiempo $O(n^k)$, se construye una mTnD $N$ que, sobre la entrada $<w>$, selecciona de forma no determinista $c$ ($|c| \le k$), ejecuta $V(<w, c>)$ y acepta si $V$ acepta.
- **Demostración** $\impliedby$ **(si)**: dada una mTnD $N$, se construye un verificador mTD $V$ que toma $<w, c>$, donde $c$ describe la secuencia de elecciones no deterministas (una rama de ejecución de $N$), simulando a $N$ y aceptando si dicha rama acepta.

### Ejemplos de problemas en NP
#### HAMPATH
$$HAMPATH = \{<G, s, t> \mid G \text{ es un grafo dirigido con un camino hamiltoniano de } s \text{ a } t\}$$
**Se decide con una mTnD en poli-tiempo**: selecciona no deterministamente $m$ vértices $p_1, \dots, p_m$, comprueba ausencia de repeticiones, inicio en $s$, fin en $t$ y existencia de los arcos $(p_i, p_{i+1})$ en poli-tiempo.

**Se verifica con una mTD en poli-tiempo**: toma el certificado $c$ y comprueba en poli-tiempo que contiene los nodos ordenados sin repeticiones de $s$ a $t$ conectados por arcos de $G$.

#### CLIQUE
$$CLIQUE = \{<G, k> \mid G=(V, E) \text{ es un grafo no dirigido con un } k\text{-clique}\}$$
Un clique en un grafo no dirigido es un subgrafo completo.

**Se decide con una mTnD en poli-tiempo**: selecciona no deterministamente un subconjunto $c$ de $k$ nodos de $G$ y comprueba en poli-tiempo que $G$ contiene todos los arcos que conectan los nodos de $c$ y acepta.

**Se verifica con una mTD en poli-tiempo**: toma el certificado $c$ y comprueba en poli-tiempo que tiene $k$ nodos, es un conjunto y que $G$ contiene todos los arcos entre sus nodos.

#### SUBSET-SUM
$$SUBSET-SUM = \{<S, t> \mid S = \{x_1, \dots, x_k\} \text{ y para algún } \{y_1, \dots, y_l\} \subseteq S \text{ tenemos que } \sum y_i = t\}$$
Los conjuntos de $x$ e $y$ son multiconjuntos (puede haber repeticiones). $S$ son enteros no negativos.

**Se decide con una mTnD en poli-tiempo**: selecciona no deterministamente un subconjunto $c$ de $S$, calcula la suma en poli-tiempo y acepta si es igual a $t$.

**Se verifica con una mTD en poli-tiempo**: toma el certificado $c$, comprueba en poli-tiempo que es un subconjunto de $S$ y calcula la suma y acepta si es igual a $t$.

#### Otros problemas
- $SAT = \{<\phi> \mid \phi \text{ es una fórmula booleana satisfacible} \}$
- $3SAT = \{ <\phi> \mid \phi \text{ es una 3FNC fórmula booleana satisfacible}\}$
- $VERTEX-COVER = \{ <G, k> \mid G = (V,E) \text{ es un grafo no dirigido y existe un conjunto } C\subseteq V, |C| \le k \text{, tal que } \forall (u,v) \in E, u\in C \lor v\in C\}$

## Clase co-NP
**Complementario de un problema**: para un lenguaje $L$, su complementario es $\overline{L} = \{x \in \Sigma^* \mid x \notin L\}$, el cual invierte el resultado del problema de decisión. Existe una asimetría: para $HAMPATH$ hay certificados cortos (el camino), mientras que para $\overline{HAMPATH}$ la única prueba conocida requiere agotar todo el espacio de búsqueda.

**co-NP**: conjunto de lenguajes cuyos complementarios están en NP. $$co-NP=\{L \subseteq \Sigma^*\mid \overline{L} \in NP\}$$
No se sabe si co-NP es cerrada bajo complemento ni su relación con NP:
- **Desde la mTnD**: una mTnD acepta si existe al menos una rama de aceptación. Para rechazar o certificar el complementario, debe verificar que todas las ramas fallan, lo que requiere certificar $2^n$ ramas fallidas.
- **Desde el verificador mTD**: comprobar un certificado demuestra que una solución es válida, pero un certificado no válido no permite descartar que existan otras opciones sin probar la totalidad de los certificados.

Ejemplos: 
- $TAUT = \{<\phi> \mid \phi \text{ es una tautología (fórmula válida)}\}$
- $SAT \in NP$
- $TAUT \in co-NP$
- $\overline{SAT} \not= TAUT$
- $\overline{SAT} = UNSAT \in co-NP$
