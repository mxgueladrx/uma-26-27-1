## NP-completitud (definición y características)
**C-completo y NP-completo**: un lenguaje $L$ es NP-completo respecto a $\le_p$ si cumple dos condiciones:
1. **Condición de pertenencia**: $L \in NP$.
2. **Condición de ser difícil (hard)**: $\forall L' \in NP, L' \le_p L$

**NP-difícil (NP-hard)**: un problema cumple la condición de ser difícil, sin tener obligatoriamente pertenecer a NP.

La clase NPC constituye un grado de equivalencia respecto a $\leq_p$. Para demostrar que dos problemas están en el mismo grado de equivalencia:
- **En la clase P**: para probar $L_1 \leq_p L_2$, el transductor ejecuta la mTD $M_1(w)$ en tiempo polinómico $O(n^k)$ y escribe una cadena fija $u \in L_2$ o $v \notin L_2$. El tiempo total de reducción es polinómico.
- **Intento fallido en NPC**: si se intenta simular la mTnD $M_1$ que decide $L_1 \in NP$, la máquina $M_1$ opera en tiempo no determinista $O(n^k)$, el transductor requiere un número exponencial de pasos $2^{O(n^k)}$. Por tanto, no sirve.

La demostración requiere un enfoque distinto:
- Una reducción $f$ que no simula la mTnD $M_1$ sobre la entrada $w$.
- Una reducción $f$ que traduce la estructura de la mTnD $M_1$ sobre la entrada $w$ en una fórmula booleana $\phi$ en tiempo polinómico $O(|w|^k)$.
- **Equivalencia lógica**:
    - $\Rightarrow$ **(Si** $w \in L_1$**)**: existe al menos una secuencia válida de transiciones que lleva a $M_1$ a un estado de aceptación (hacen $\phi = TRUE$).
    - $\Leftarrow$ **(Si** $w \notin L_1$**)**: ninguna secuencia de $M_1$ alcanza un estado de aceptación ($\phi$ es insatisfacible).

![[Pasted image 20261108122908.png]]

Usos de NPC:
1. **Demostrar que** $P \neq NP$: un investigador puede centrarse en los problemas NPC (más difíciles dentro de NP).
2. **Demostrar que** $P = NP$: encontrar un algoritmo en tiempo polinómico para un único problema NPC.
    - Si $A \in NPC$ y $A \in \text{P}$, entonces $P = NP$.
3. **Justificar la falta de un algoritmo polinómico**:
    - Si $A \in NPC$ y $A \leq_p B$, entonces $B$ es NP-difícil.
    - Si $A \in NPC$, $B \in NP$ y $A \leq_p B$, entonces $B$ es NPC.

## SAT es NP-completo (NPC)
Cook y Levin demostraron que SAT es NPC (demostrar que $SAT \in NPC$ y $\forall L \in NP, L \le_p SAT$): $$SAT = \{\langle \phi \rangle \mid \phi \text{ es una fórmula booleana satisfacible}\}$$
### $SAT \in NP$
- **Decidir con mTnD en poli-tiempo (**$N_{\text{SAT}}$**)**:
    1. Para cada variable elegir de forma no determinista si toma el valor 0 (FALSE) o 1 (TRUE) ($O(n)$).
    2. Sustituir en la fórmula $\phi$ los literales por sus valores ($O(n)$).
    3. Si el resultado es TRUE, aceptar; en otro caso, rechazar ($O(n)$).
- **Verificar con mTD en poli-tiempo (**$V_{\text{SAT}}$**)**:
    1. Dada la entrada $\langle \phi, c \rangle$, verificar que $c$ es un certificado válido (una asignación booleana) ($O(n)$).
    2. Sustituir en $\phi$ y comprobar en tiempo $O(n)$ que la fórmula evalúa a TRUE

### $\forall L \in NP, L \leq_p SAT$ (Teorema de Cook-Levin)
Para cualquier $L \in NP$ decidido por una mTnD $M$ en poli-tiempo, se construye la función de reducción $f$ que transforma en poli-tiempo la cadena $w$ en una fórmula booleana $\phi$ que simula $M$ sobre $w$.

#### Tableau
Matriz $n^k \times n^k$ donde las filas son configuraciones alcanzadas por $M$ (empieza y acaba por #), la primera es $q_0$, cada una sigue a la anterior según $\delta$, y al llegar a $q_{accept}$ se repite la fila.

Para cada celda en la fila $i$ y columna $j$ ($1 \leq (i,j) \leq n^k$), y para cada símbolo $s \in C$ ($C = Q \cup \Gamma \cup \{\#\}$ es el alfabeto del recuadro), se define la variable booleana $x_{i,j,s}$:
- $x_{i,j,s} = TRUE$ si la celda ($i,j$) contiene el símbolo $s$.
- $x_{i,j,s} = FALSE$ en caso contrario.

![[Pasted image 20261108124941.png]]

#### Fórmula $\phi$
$$\phi = \phi_{celda} \land \phi_{inicio}\land \phi_{mueve}\land \phi_{acepta}$$
##### $\phi_{inicio}$
Garantiza que la primera fila del recuadro sea la configuración inicial de $M$ sobre $w$ (empieza y acaba en #, empieza en $q_0$, entrada $w$ y resto en blanco "\_"): $$\phi_{inicio} = x_{1,1,\#} \wedge x_{1,2,q_0} \wedge x_{1,3,w_1} \wedge x_{1,4,w_2} \wedge \dots \wedge x_{1,n+2,w_n} \wedge x_{1,n+3,\_} \wedge \dots \wedge x_{1,n^k,\#}$$
##### $\phi_{acepta}$
Garantiza que la rama alcanza el estado $q_{acc}$ en alguna posición: $$\phi_{acepta} = \bigvee_{1 \leq i, j \leq n^k} x_{i,j,q_{acc}}$$
##### $\phi_{celda}$
Garantiza que las celdas contienen un único símbolo del alfabeto $C$: $$\phi_{celda} = \bigwedge_{1 \leq (i,j) \leq n^k} \left[ \bigvee_{s \in C} \left( x_ {i,j,s} \land \bigwedge_{t \in C, s \neq t} \overline{x_{i,j,t}} \right) \right]$$
##### $\phi_{mueve}$
Garantiza que las transiciones entre filas consecutivas respetan $\delta$ de $M$.

**Ventana legal**: ventana 2x3 que no viola las acciones especificadas por una $\delta$. Llamaremos $ventana\_legal(i,j)$ a la fórmula sobre los 6 campos de la ventana cuya celda central superior es $(i,j$): $$ventana\_legal(i,j) = \bigvee_{a_1, \dots, a_6 \text{ es legal}} (x_{i,j-1,a_1} \wedge x_{i,j,a_2} \wedge x_{i,j+1,a_3} \wedge x_{i+1,j-1,a_4} \wedge x_{i+1,j,a_5} \wedge x_{i+1,j+1,a_6})$$
![[Pasted image 20261108133314.png]]

![[Pasted image 20261108133354.png]]

![[Pasted image 20261108133400.png]]

**Afirmación**: si la fila superior es la configuración inicial y cada ventana del recuadro es legal, entonces cada fila es una configuración que sigue legalmente a la precedente.
- Celdas no adyacentes al estado no cambian entre la fila superior e inferior.
- La ventana centrada sobre la cabeza de lectura garantiza que las 3 posiciones afectadas se actualizan conforme a $\delta$.

$$\phi_{mueve} = \bigwedge_{1 \leq i \leq n^k-1 \\ 2 \leq j \leq n^k-1} ventana\_legal(i,j)$$

#### Complejidad de reducción
- **Número de variables**: Ocupa $n^k \times n^k = n^{2k}$ celdas. El número de variables es $O(n^{2k})$.
- **Tamaño de las subfórmulas**:
    - $\phi_{celda}$: fragmentos de tamaño fijo por celda $\rightarrow O(n^{2k})$.
    - $\phi_{inicio}$: tamaño acotado por la primera fila $\rightarrow O(n^k)$.
    - $\phi_{acepta}$: disyunción sobre todas las celdas $\rightarrow O(n^{2k})$.
    - $\phi_{mueve}$: fragmento fijo por cada ventana $2 \times 3 \rightarrow O(n^{2k})$.
- **Tamaño total de** $\phi$: $O(n^{2k})$ (o considerando la representación de índices en símbolos, $O(n^{2k} \log n)$).
- **Conclusión**: Como el tamaño de $\phi$ es polinómico en $n$, la reducción $f$ se puede construir en tiempo polinómico. Queda probado el Teorema de Cook-Levin: SAT es NPC.

## 3SAT es NP-completo (NPC)
Caso especial de SAT donde la fórmula booleana está en Forma Normal Conjuntiva (FNC) y cada cláusula contiene 3 literales. Ejemplo: $(x \vee y \vee \neg z) \wedge (a \vee \neg y \vee b) \wedge \dots$.

**Demostración**:
1. $3SAT \in NP$: mismo razonamiento que para $\text{SAT}$.
2. $SAT \leq_p 3SAT$: transformar cualquier fórmula $\phi$ de $\text{SAT}$ a una fórmula equivalente $\phi'$ en 3SAT.

**Paso 1**: Convertir la fórmula a FNC:
- $\phi_{celda}$: es un AND de subfórmulas, donde cada una es un AND de ORs. Ya está en FNC.
- $\phi_{inicio}$: es un gran AND de variables aisladas (cláusulas de 1 literal). Ya está en FNC.
- $\phi_{acepta}$: es un gran OR de variables (una única cláusula grande). Ya está en FNC.
- $\phi_{mueve}$: se convierte a FNC usando equivalencias booleanas estándar.

**Paso 2**: Convertir cláusulas a exactamente 3 literales por cláusula:
- **Cláusulas de 1 o 2 literales**: se repite uno de los literales hasta completar 3 (ej. $(a)$ pasa a $(a \vee a \vee a)$; $(a \vee b)$ pasa a $(a \vee b \vee b)$).
- **Cláusulas de 3 literales**: se mantienen iguales.
- **Cláusulas con más de 3 literales**:
    - **Caso 4 literales**: la cláusula $(a_1 \vee a_2 \vee a_3 \vee a_4)$ se sustituye por: $$(a_1 \vee a_2 \vee z_1) \wedge (\neg z_1 \vee a_3 \vee a_4)$$
    - **Caso general** $M$ **literales**: La cláusula $(a_1 \vee a_2 \vee \dots \vee a_M)$ se descompone en $M-2$ cláusulas con $M-3$ variables nuevas $z_1, z_2, \dots, z_{M-3}$: $$(a_1 \vee a_2 \vee z_1) \wedge (\neg z_1 \vee a_3 \vee z_2) \wedge (\neg z_2 \vee a_4 \vee z_3) \wedge \dots \wedge (\neg z_{M-3} \vee a_{M-1} \vee a_M)$$
Preserva la satisfactibilidad de la fórmula original y se ejecuta en poli-tiempo, demostrando que·SAT es NP-completo.