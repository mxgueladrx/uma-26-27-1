## Diagonalización
Recorrer la diagonal caemos en una operación más compleja.
- **Construir la tabla (universo)**: todas las posibilidades de máquinas/entradas.
- **Definir un elemento sobre la diagonal (autorreferencia negativa)**: construir una función $D$ que consulte la celda diagonal $(j, j)$ y modifique o invierta su resultado.
- **Identificar que el supuesto a rechazar está en el universo**: si la hipótesis que se quiere refutar fuese cierta, el elemento $D$ debería pertenecer a la tabla.
- **Detectar el punto crítico que lleva a contradicción**: evaluar el elemento $D$ en la posición diagonal $m$, derivando en un resultado contradictorio

![[Pasted image 20261006174915.png]]

## Máquina de Turing Universal
Existe una mT $U$ que para cada mT $M$ y cada entrada $x$ se cumple que $U(M, x) = M(x)$.

Para representar cualquier máquina $M = (Q, \Sigma, \Gamma, \delta, q_0, q_{acc}, q_{rej})$ en un alfabeto binario estándar:
- Los estados de $M$ se asocian a enteros: $q_0 = 0$, $q_{acc} = 1$, $q_{rej} = 2$, hasta $|Q|-1$.
- Los símbolos del alfabeto $\Gamma$ se asocian a enteros del $|Q|$ al $|Q|+|\Gamma|-1$.
- Los movimientos $L$ y $R$ se codifican como $|Q|+|\Gamma|$ y $|Q|+|\Gamma|+1$.
- Cada símbolo/estado requiere $\lceil \log_2(|Q| + |\Gamma| + 2) \rceil$ bits.
- La función de transición $\delta$ se codifica como una secuencia de pares: $((estado, símbolo), (estado, símbolo, movimiento))$, separados por `;`

![[Pasted image 20261006180219.png]]

### Intérprete para lenguaje LOOP
Solo se usan bucles for y siempre se detienen. Los niveles de anidamiento $L_i$: $L_0$ son programas sin bucles; $L_1$ programas con bucles sin anidar; $L_2$ anidamiento máximo de 2 niveles...

Para cada nivel $i$, existe una máquina universal $U_i$ que simula los programas de $L_i$, pero dicho intérprete NO puede pertenecer al propio nivel $L_i$ ($U_i \notin L_i$), aunque SÍ pertenece al nivel inmediatamente superior $L_{i+1}$ ($U_i \in L_{i+1}$). 

$\forall i, \exists U_i : \big(\forall x, \forall P \in L_i, U_i(P, x) = P(x)\big) \land (U_i \notin L_i) \land (U_i \in L_{i+1})$

### Diagonalización
- Supongamos que existe $U_i \in L_i$.
- Construimos el programa diagonal $D(x) = U_i(P_x, x) + 1 = P_x(x) + 1$.
- Dado que $U_i \in L_i$ y la operación de sumar $1$ no añade bucles, $D \in L_i$. Por tanto, debe ocupar alguna posición $m$ en la lista de programas ($D = P_m$).
- Evaluando en la entrada $m$: $D(m) = P_m(m) + 1 \implies P_m(m) = P_m(m) + 1$, lo que resulta en una contradicción.
- Conclusión: No existe $U_i \in L_i$. Sin embargo, implementar la lógica del intérprete añade un bucle externo adicional para recorrer las líneas de código, por lo que $U_i \in L_{i+1}$

## Problema de la parada ($HALT$) no es decidible
$HALT = \{<M, x> \mid M(x) \downarrow \}$.

![[Pasted image 20261010143622.png]]

## Relación entre $P$ y $EXP$ ($P \subsetneq EXP$)
Para demostrar que la inclusión es estricta ($P \subseteq EXP$ y $P \neq EXP$), se usa diagonalización definiendo un lenguaje $L$ con autorreferencia negativa:

$L = \{ x \mid x = \langle M \rangle \# 1^c \# 1^e \text{ tal que } M \text{ no acepta } x \text{ en tiempo } c \cdot |x|^e \}$

**Lema 1**: $L \in EXP$
Existe una mT $M_L$ que decide $L$ simulando el comportamiento de $M$ sobre $x$ durante un número de pasos acotado por $c \cdot |x|^e$.
- $M_L$ cuenta los pasos ejecutados usando un contador en binario.
- Como la simulación del límite de tiempo $c \cdot |x|^e$ puede realizarse dentro de una cota exponencial $2^{O(n^k)}$, la máquina $M_L$ siempre se detiene y decide el lenguaje en tiempo exponencial, lo que prueba que $L \in EXP$.

**Lema 2:** $L \notin P$
Suponiendo que $L \in P$:
- Si $L \in P$, debería existir una mT $M_p$ que decida $L$ en tiempo polinómico $c_p \cdot |x|^{e_p}$.
- Si evaluamos la máquina $M_p$ sobre la cadena diagonal $x_p = \langle M_p \rangle \# 1^{c_p} \# 1^{e_p}$:
    - Si $x_p \in L$**:** $M_p$ acepta $x_p$ en tiempo $c_p \cdot |x_p|^{e_p}$, lo que por definición de $L$ significa que $x_p \notin L$.
    - Si $x_p \notin L$**:** $M_p$ rechaza $x_p$ en tiempo $c_p \cdot |x_p|^{e_p}$, lo que por definición de $L$ significa que $x_p \in L$.
- Ambas situaciones generan una contradicción, por lo que es imposible que exista $M_p$ y se concluye que $L \notin P$.