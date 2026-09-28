# Modelos de cómputo
Descripción matemática abstracta que explica sistemas formales para definir computaciones o cálculos.

## Máquina de Turing
### Determinista (mTD) unicinta
Define formalmente el concepto de algoritmo y estudiar límites teóricos de lo computable. Esta formada por:
- **Cinta**: infinita hacia la derecha, con celdas con infinitos espacios en blanco "\_" tras la entrada.
- **Cabeza lectora/escritora**: se mueve a izquierda o derecha, sin poder ir más a la izquierda del inicio.
- **Unidad de control**: decide el siguiente movimiento según el estado actual y el símbolo leído, incluyendo: inicio $q_0$, aceptación $q_{acc}$ y rechazo $q_{rej}$.

**Definición Formal (7-tupla)**: $M = (Q, \Sigma, \Gamma, \delta, q_0, q_{acc}, q_{rej})$
- $Q$: Conjunto finito de estados, con $q_{acc} \neq q_{rej}$.
- $\Sigma$: Alfabeto de entrada ("\_" $\notin \Sigma$).
- $\Gamma$: Alfabeto de cinta ($\Sigma \subseteq \Gamma$ y "\_" $\in \Gamma$).
- $\delta$: Función de transición $\delta: Q \times \Gamma \to Q \times \Gamma \times \{L, R\}$.
- $q_0, q_{acc}, q_{rej}$: Estados inicial, de aceptación y de rechazo.

**Lenguajes según su Resolubilidad**:
- **Turing-reconocible**: acepta cadenas pertenecientes al lenguaje, pero ante cadenas que no pertenecen puede rechazar o diverger. Calculabilidad.
- **Turing-decidible**: acepta cadenas del lenguaje y rechaza las que no pertenecen (converge). Complejidad.

**Complejidad en Tiempo y Espacio**:
- **Tiempo** $t(n)$: máximo número de pasos (veces que se ejecuta la función de transición $\delta$) sobre cualquier entrada de longitud $n$. Se ejecuta en tiempo $O(t(n))$.
- **Espacio** $s(n)$: máximo número de celdas ocupadas o visitadas en la cinta en algún momento para cualquier entrada de longitud $n$. Se cumple $s(n) = \max(|w|, t(n))$

**Configuración de una MT**: el número de configuraciones diferentes de una mTD que usa un máximo de $N$ celdas es $|\Gamma|^N \times N \times |Q|$. Si una mTD repite una configuración, estaría en un bucle infinito.

![[Pasted image 20260925115901.png]]

### Determinista (mTD) multicinta
Una cinta de entrada y $k$ cintas de trabajo con cabezas lectoras/escritoras independientes. Las cabezas se mueven de forma independiente y se pueden quedar paradas. $\delta: Q \times \Gamma^k \to Q \times (\Gamma \times \{L, R, S\})^k$, donde el movimiento $S$ permite dejar parada una cabeza.

**Complejidad en Tiempo y Espacio**:
- **Tiempo** $t(n)$: máximo número de pasos (veces que se ejecuta la función de transición $\delta$) sobre cualquier entrada de longitud $n$. Se ejecuta en tiempo $O(t(n))$.
- **Espacio** $s(n)$: máximo número de celdas ocupadas o visitadas en alguna cinta (sin contar la de entrada) en algún momento para cualquier entrada de longitud $n$.

**Teorema de Equivalencia**:
- Las mTD multicinta son equivalentes a las mTD unicintas.
- **Demostración**: se simulan las $k$ cintas en una única cinta separándolas mediante un delimitador "#" y expandiendo el alfabeto para marcar la posición de cada cabeza (el símbolo "^" indica la cabeza, $â$).
- **Sobrecarga**: aumento de tiempo polinómico (cuadrático $O(t(n)^2)$) debido a las pasadas consecutivas para leer/actualizar las cabezas codificadas.

![[Pasted image 20260925121341.png]]

### No determinista (mTnD)


## Tesis de Church-Turing
## Terminología para describir MT