## Tabla Resumen / Reconocible vs Decidible / Diagrama
- **Lenguaje Turing-decidible**: la mT se detiene siempre para cualquier entrada.
- **Lenguaje Turing-reconocible**: la mT rechaza o diverge cuando $w \notin L$.
- **Indecidible**: Turing-reconocible + Turing-decidible.

Turing-decidible $\subset$ Turing-reconocible $\subset$ Indecidible

Que un lenguaje sea Turing-decidible no es lo mismo que el problema de determinar si un lenguaje es decidible.

Un lenguaje $L$ es decidible $\iff$ $L$ y $\overline{L}$ son de tipo 0.

## Tipo 3: lenguajes regulares
**Autómata Finito Determinista (AFD)**: 5-tupla $M = (Q, \Sigma, \delta, q_0, F)$ donde:
- $Q$: conjunto finito de estados.
- $\Sigma$: alfabeto de entrada.
- $\delta$: función de transición dada por $\delta: Q \times \Sigma \to Q$.
- $q_0 \in Q$: estado inicial.
- $F \subseteq Q$: conjunto de estados finales o de aceptación.

**Gramática regular**: $G = (V, T, P, S)$ donde $V$ son los no terminales, $T$ los terminales ($T \cap V = \emptyset$), $S \in V$ el símbolo inicial y $P$ las producciones.
- **Gramática Regular Derecha:** reglas de la forma $A \to aB$, $A \to a$, $A \to \varepsilon$ (con $A, B \in V$ y $a \in T$).
- **Gramática Regular Izquierda:** reglas de la forma $A \to Ba$, $A \to a$, $A \to \varepsilon$

![[Pasted image 20261003132305.png]]

## Tipo 2: lenguajes independientes del contexto (contexto libre)
**Autómata con Pila No Determinista (APND)**: $M = (Q, \Sigma, \Gamma, \delta, q_0, F)$ donde $\Gamma$ es el alfabeto de la pila y la función de transición es $\delta: Q \times (\Sigma \cup \{\varepsilon\}) \times (\Gamma \cup \{\varepsilon\}) \to \mathcal{P}(Q \times (\Gamma \cup \{\varepsilon\}))$. Es un AFND con una pila.

**Gramática independiente del contexto (contexto libre)**: $G = (V, T, P, S)$ cuyas producciones tienen la forma $V \to (V \cup T)^*$ (el antecedente es una única variable no terminal).

Formas normales de las gramáticas de tipo 2:
- **Forma Normal de Chomsky (FNC)**:
	- Reglas  de la forma $A \to BC$ o $A \to a$.
	- El árbol de derivación binario.
	- Para generar una palabra de longitud $n$, se requieren exactamente $2n-1$ pasos de derivación.
- **Forma Normal de Greibach (FNG)**:
	- Reglas de la forma $A \to a\alpha$ (con $a \in T$ y $\alpha \in V^*$).
	- Cada aplicación de una regla produce exactamente un carácter real de la palabra final.
	- Para generar una palabra de $n$ letras se dan $n$ pasos. Es la forma ideal para sincronizarse con el APND.

## Tipo 1: lenguajes sensibles al contexto
**Autómata Lineal Acotado no determinista (LBA)**: - $M = (Q, \Sigma, \Gamma, \delta, q_0, F, LB, RB)$ donde $LB$ y $RB$ son los marcadores de límite izquierdo y derecho. La función de transición es $\delta: Q \times \Gamma \to \mathcal{P}(Q \times \Gamma \times \{L, R\})$.

Es como una mTnD con espacio limitado y puede escribir en cualquier lado, no solo en la cabeza.

**Gramática sensible al contexto**: reglas de la forma $uXw \to uvw$ (sustituye la variable $X$ por $v \in (V \cup T)^+$ en el contexto $u, w$).

![[Pasted image 20261003133431.png]]

**Teorema de Equivalencia:** toda gramática de longitud creciente, con producciones $u \to w$ tales que $|u| \le |w|$ con $u, w \in (V \cup T)^+$, es equivalente a una gramática sensible al contexto.

## Tipo 0: lenguajes sin restricciones
Se usa una mT o mTnD.

**Gramática sin restricciones**: reglas de reescritura de la forma $(V \cup T)^+ \to (V \cup T)^*$.

Un lenguaje es Turing-reconocible $\iff$ es generado por una gramática sin restricciones.

![[Pasted image 20261003134104.png]]

## Reflexión final

![[Pasted image 20261003134146.png]]

Sobre los dispositivos reconocedores:
- $AFD \equiv AFND$: se puede transformar uno en otro (aunque se complique).
- $APD \subsetneq APND$: existen lenguajes que se reconocen con APND y no APD ($ww^R$: palíndromos).
- $DLBA \stackrel{?}{\equiv} NLBA$: no se sabe.
- $mTD \equiv mTnD$: se puede transformar uno en otro (aunque se complique).

Las equivalencias se demuestran simulando o transformando dispositivos. Las diferencias se prueban mediante técnicas de diagonalización o hallando un lenguaje de separación.