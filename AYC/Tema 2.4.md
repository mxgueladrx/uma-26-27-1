## Alternativas ante un problema
Para diseñar un programa eficiente hay tres alternativas:
- Conseguir un algoritmo eficiente y demostrar formalmente que no se puede mejorar (ej. encontrar el máximo en un vector en tiempo $O(n)$).
- Demostrar que ningún otro profesional ha conseguido una solución eficiente para un problema equivalente y aportar la mejor solución conocida.
- Demostrar que es imposible o intratable.

**Relación informal entre problemas**: si tenemos un algoritmo para resolver B y existe una transformación para resolver A usando B:
- A no puede ser más difícil que B.
- B es al menos tan difícil como A.
- A es reducible a B (A $\le$ B).

![[Pasted image 20261005113025.png]]

## Reducción muchos a uno ($\le_m$)
Si A es reducible a B y tenemos un algoritmo para B, entonces tenemos un algoritmo para A. Si A es reducible a B y no existe un algoritmo para A, entonces no existe un algoritmo para B.

Sea $f: \Sigma^* \to \Sigma^*$ una función computable. Se dice que A es reducible a B mediante $f$ (A $\le_m$B) si: $\forall w \in \Sigma^*, \quad w \in A \iff f(w) \in B$.

$\le_m$ indica que es computable (sin mencionar la complejidad). $\le_T$ es la Turing reducibilidad donde se permite interactuar múltiples veces con un oráculo de B.

**Teoremas de cierre**: sean A y B dos lenguajes sobre $\Sigma$:
- $(A \le_m B) \land (B \text{ es decidible}) \implies A \text{ es decidible}$.
- $(A \le_m B) \land (B \text{ es reconocible}) \implies A \text{ es reconocible}$.
Sea $M_f$ la mTD que calcula $f$ y $M_B$ la mTD que decide B, construimos $M'$ sobre cada entrada $w$, aplicamos $M_f$ para obtener $f(w)$, ejecutamos $M_B$ sobre $f(w)$ y aceptar o rechazar según decida $M_B$
- $(A \le_m B) \land (A \text{ no decidible}) \implies B \text{ no decidible}$.
- $(A \le_m B) \land (A \text{ no reconocible}) \implies B \text{ es reconocible}$
Se aplica la equivalencia lógica $P \implies Q \equiv \neg Q \implies \neg P$

**Propiedades**:
- **Reflexiva**: $A \le_m A$.
- **Transitiva**: Si $A \le_m B$ y $B \le_m C \implies A \le_m C$.
- **No es simétrica**: $A \le_m B \not\implies B \le_m A$.
- **Equivalencia**: $(A \le_m B) \land (B \le_m A) \iff A \equiv_m B$. Cada clase de m-equivalencia define un grado (conjunto de problemas o lenguajes con el mismo nivel de dificultad de incomputabilidad) de incomputabilidad en la jerarquía aritmética.

**Grado de los lenguajes decidibles**: $\forall L_1, L_2 \in REC$ con $L_1, L_2 \neq \emptyset$ y $L_1, L_2 \neq \Sigma^*$, se cumple que $L_1 \le_m L_2$. Se eligen dos cadenas de $L_2$, $u \in L_2$ y $v \not\in L_2$. El transductor $M_f$ simula $M_1$, si $M_1$ acepta $x$, $M_f$ escribe $u$, si rechaza escribe $v$.

![[Pasted image 20261005115705.png]]

- Si $L_2 = \emptyset$, no existe cadena $u \in L_2$ a la que mapear los elementos aceptados.
- Si $L_2 = \Sigma^*$, no existe cadena $v \notin L_2$ a la que mapear los elementos rechazados

La clase REC se divide en 3 clases de equivalencia: la clase $\Sigma^*$ (siempre acepta), la $\emptyset$ (siempre rechaza) y el resto de lenguajes decidibles no triviales (representados habitualmente por el lenguaje de números pares $EVEN$).

### Reducción de Karp ($\le_p$)
El caso de un problema X y buscando eficiencia:
- Si X es reducible a B y tenemos un algoritmo eficiente para B, tenemos uno eficiente para X. $X \le_p B$.
- Si A es reducible a X y no existe un algoritmo eficiente para A, no existe uno eficiente para X. $A \le_p X$.

Sea $f: \Sigma^* \to \Sigma^*$ una función computable en tiempo polinómico (poli-t). $A$ es reducible en tiempo polinómico a $B$ ($A \le_p B$) si: $\exists f$ computable en poli-t tal que  $\forall w \in \Sigma^*,\ w \in A \iff f(w) \in B$.

Para aplicar $A \le_p B$:
- Se define $f$.
- Demostrar que $f$ se ejecuta en poli-t, existe una mTD.
- Demostrar que $w  \in A \implies f(w) \in B$ y $x \notin A \implies f(x) \notin B$ (o su equivalente $f(x) \in B \implies x \in A$).

HAMPATH y HAMCYCLE. Se pueden usar uno de ellos para resolver el otro:
- $HAMPATH \le_p HAMCYCLE$: la función $f(G)$, dado un grafo $G=(V,E)$ para $HAMPATH$, se crea $G'=(V', E')$ añadiendo un nuevo nodo $v$ conectado con arcos a todos los demás vértices de $V$. Insertar 1 nodo y $|V|=n$ arcos toma tiempo $O(n^2)$. Existe un camino hamiltoniano abierto en $G \iff$ existe un ciclo hamiltoniano cerrado en $G'$ (pasando por el nuevo nodo $v$).
- $HAMCYCLE \le_p HAMPATH$: la función $f(G)$ se selecciona un nodo $v$, se duplica como $v'$, se reorientan los arcos que llegaban a $v$ hacia $v'$, y se añaden dos nodos especiales $s$ (inicial) y $t$ (final) conectados con arcos $(s, v)$ y $(v', t)$. Añadir 3 nodos y reorientar arcos se realiza en tiempo $O(n^2)$. Existe un ciclo en $G \iff$ existe un camino de $s$ a $t$ que recorre todo $G'$.
Ambos problemas son equivalentes ($HAMPATH \equiv_p HAMCYCLE$)

## Reducción, cierre y completitud