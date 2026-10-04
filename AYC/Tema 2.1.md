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
La función de transición mapea a un conjunto de posibles acciones $\delta: Q \times \Gamma \to \mathcal{P}(Q \times \Gamma \times \{L, R\})$

![[Pasted image 20261003123711.png]]

Tiene dos perspectivas:
- **Paralelismo ilimitado**: en cada decisión no determinista se clonan hebras de ejecución. Acepta si al menos una hebra llega a $q_{acc}$ y rechaza si TODAS las hebras llegan a $q_{rej}$.
- **Adivino / Verificador**: elige mágicamente la rama correcta que lleva a $q_{acc}$.

**Teorema de equivalencia**: Las mTnD son equivalentes a las mTD. Se simula la mTnD con una mTD determinista de 3 cintas: cinta 1 (entrada original de solo lectura), cinta 2 (simulación donde se copia la entrada y se trabaja simulando las transiciones) y cinta 3 (progreso/exploración de alternativas del árbol de configuraciones).

Se utiliza un recorrido en anchura (BFS) sobre el árbol de configuraciones para encontrar la rama de aceptación (fijar $t(n)$).

| Paso | Función                                                                                                                                                                                                                                                                                       |
| ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.   | Escribimos la lista de transiciones en la cinta de progreso (longitud $t(n)$)                                                                                                                                                                                                                 |
| 2.   | Copiamos la entrada en la cinta de simulación                                                                                                                                                                                                                                                 |
| 3.   | Simulamos eligiendo la transición según la cinta de progreso: rechaza la rama si llega a $q_{rej}$ (paso 4). Rechaza la rama si alguna transición es inválida (paso 4). Rechaza la rama si completa $t(n)$ pasos sin aceptar (paso 4). Acepta la entrada si llega a $q_{acc}$ (acepta y para) |
| 4.   | Se prepara la siguiente lista de transiciones: si no hemos probado todas las opciones (paso 2). Si hemos probado todas (rechaza y para, nº de ramas $h^{t(n)})$                                                                                                                               |

Sea $h$ el factor de ramificación, supone un esfuerzo de cómputo de $O(h^{t(n)})$. El espacio máximo ocupado es lo que supone la alternativa con más memoria.

En caso de no acotar el tiempo $t(n)$, se acota $(s(n))$: $t(n)\le |\Gamma|^{s(n)} \times s(n) \times |Q|$

## Tesis de Church-Turing
Cualquier función efectivamente calculable puede ser computada por una máquina de Turing (o equivalente)

## Terminología para describir MT
Niveles de descripción de una MT:
- **Descripción Formal (bajo nivel):** definición detallada mediante la 7-tupla, alfabetos, estados y la función de transición.
- **Descripción de Implementación (nivel intermedio):** lenguaje natural que explica cómo la cabeza se mueve y organiza la información en la cinta sin listar la tabla de estados. Permite calcular el orden de magnitud de la complejidad.
- **Descripción Algorítmica (alto nivel):** prosa estructurada en etapas/bloques que destaca la lógica del algoritmo omitiendo detalles de bajo nivel sobre la cinta o movimientos de la cabeza.