## Clase NP
NP es la clase de lenguajes decididos por mTnD utilizando tiempo polinómico (poli-tiempo), definida formalmente como $NP = \bigcup_{k \ge 1} NTIME(n^k)$ con $k \ge 1$. Puede computar todo lo incluido en P.

### Grados en la clase NP
Grado de equivalencia: según $\le_p$ se define como $deg_p(L) = \{L' \mid L' \equiv_p L\}$, donde $L \equiv_p L'$ implica $(L \le_p L') \land (L' \le_p L)$. En NP se distinguen las siguientes estructuras de grados:

Grado de la clase NP (con $\le_p$): no existe.
Grados en la clase NP (con $\le_p$):
- Grado de la clase NP-completo: por demostrar que todos son equivalentes.
- Grados entre P y NP-completos (NP-intermedios): si P $\not=$ NP, hay infinitos grados.
Grados de la clase P: todos son equivalentes.

### Definición de clase NP usando el concepto de verificador
Usar mTnD es problemático porque asume modelos de cómputo no disponibles en la realidad o mTD que consumen tiempo exponencial.

**Verificador** ($V$): algoritmo determinista para un lenguaje $A$ definido como $$A = \{w \mid V \text{ acepta } <w, c> \text{ para alguna cadena } c\}$$

### Ejemplos de problemas en NP
## Clase co-NP