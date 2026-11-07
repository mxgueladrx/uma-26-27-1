## Introducción
En la teoría de la complejidad computacional, se demuestra si una clase de complejidad $C$ es cerrada bajo una operación formal de lenguajes analizando si, al aplicar dicha operación a cualquier par de lenguajes pertenecientes a $C$, el lenguaje resultante permanece dentro de $C$.

Se consideran dos lenguajes $L_1, L_2 \in NP$ sobre un alfabeto $\Sigma$. Las operaciones a evaluar se definen de la siguiente manera:
- **Unión:** $$L_1 \cup L_2 = \{ w \in \Sigma^* \mid w \in L_1 \lor w \in L_2 \}$$
- **Concatenación:** $$L_1 \circ L_2 = \{ w \in \Sigma^* \mid \exists u, v \in \Sigma^* \text{ tales que } w = uv, u \in L_1 \land v \in L_2 \}$$

Para demostrar que $L_1 \cup L_2 \in NP$ y $L_1 \circ L_2 \in NP$, se utiliza la caracterización formal de la clase NP:
1. **Definición por Máquina de Turing No Determinista (mTnD):** $NP = \bigcup_{k \ge 1} NTIME(n^k)$, la clase de lenguajes decididos por una mTnD en tiempo polinómico. Es como la ejecución en paralelo de múltiples hebras de cómputo o como un "adivino" que selecciona la rama de transición óptima hacia el estado de aceptación.
2. **Definición por Verificador Determinista (mTD):** un lenguaje $A \in NP$ si existe un verificador determinista $V$ que opera en tiempo polinómico tal que $w \in A$ si y solo si existe un certificado $c$ de longitud polinómica para el cual $V(w, c)$ acepta.

**Ejemplo:** si $L_1 = HAMPATH$ (el lenguaje de grafos que contienen un camino Hamiltoniano) y $L_2 = SAT$ (el lenguaje de fórmulas booleanas satisfacibles), ambos en NP, la unión $L_1 \cup L_2$ aceptará cualquier cadena que sea un grafo con camino hamiltoniano o bien una fórmula booleana satisfacible, mientras que la concatenación $L_1 \circ L_2$ aceptará cadenas compuestas por la representación de un grafo hamiltoniano seguida inmediatamente por una fórmula satisfacible.

## Cierre bajo Unión ($L_1 \cup L_2 \in NP$)
### Demostración mediante Máquinas de Turing No Deterministas (mTnD)
- **Hipótesis:** dado que $L_1 \in NP$ y $L_2 \in NP$, existen mTnD $N_1$ y $N_2$ que deciden $L_1$ y $L_2$ en tiempo polinómico $O(n^{k_1})$ y $O(n^{k_2})$ respectivamente.
- **Construcción de la mTnD** $N_{unión}$**:** ante una cadena de entrada $w$ de longitud $n$:
    1. De forma no determinista, $N_{unión}$ realiza una bifurcación inicial y elige simular $N_1(w)$ o $N_2(w)$.
    2. Si la máquina seleccionada acepta $w$, $N_{unión}$ acepta. Si esa rama rechaza, la rama se rechaza; la otra rama, que eligió la máquina alternativa, puede seguir aceptando.
- **Correctitud:**
    - Si $w \in L_1 \cup L_2$, entonces $w \in L_1$ o $w \in L_2$. Si $w \in L_1$, la rama que simula $N_1(w)$ alcanzará un estado de aceptación. Si $w \in L_2$, la rama de $N_2(w)$ aceptará. Por tanto, $N_{unión}$ cuenta con al menos una rama de aceptación.
    - Si $w \notin L_1 \cup L_2$, ni $N_1$ ni $N_2$ poseen ramas de aceptación sobre $w$, por lo que todas las hebras de $N_{unión}$ terminan en estado de rechazo.
- **Análisis de Complejidad Temporal:** la bifurcación inicial no determinista requiere $O(1)$ pasos. La simulación posterior ejecuta a lo sumo $\max(O(n^{k_1}), O(n^{k_2})) = O(n^k)$ pasos. Al ser una suma acotada polinómicamente, $N_{unión}$ decide $L_1 \cup L_2$ en tiempo polinómico no determinista.

### Demostración equivalente por Verificador Determinista
Sean $V_1$ y $V_2$ los verificadores deterministas de $L_1$ y $L_2$ en tiempo polinómico con certificados $c_1$ y $c_2$. Se construye el verificador $V_{unión}(w, c)$ asignando al certificado el formato $c = (i, c')$, donde $i \in \{1, 2\}$. Si $i=1$, se ejecuta $V_1(w, c')$; si $i=2$, se ejecuta $V_2(w, c')$. $V_{unión}$ acepta en tiempo polinómico determinista si y solo si la verificación individual es satisfactoria.

## Cierre bajo Concatenación ($L_1 \circ L_2 \in NP$)
### Demostración mediante Máquinas de Turing No Deterministas (mTnD)
- **Hipótesis:** sean $N_1$ y $N_2$ mTnD que deciden $L_1$ y $L_2$ en tiempo polinómico $p_1(n)$ y $p_2(n)$ respectivamente.
- **Construcción de la mTnD** $N_{concat}$**:** ante una cadena de entrada $w$ de longitud $n$:
    1. De forma no determinista, $N_{concat}$ "adivina" una partición de la cadena $w$ en dos subcadenas $u$ y $v$ tales que $w = uv$ (probando no deterministamente la posición del punto de corte $i \in \{0, 1, \dots, n\}$).
    2. Ejecuta la mTnD $N_1$ sobre $u$ y la mTnD $N_2$ sobre $v$.
    3. Si tanto $N_1(u)$ como $N_2(v)$ aceptan en sus respectivas ramas, $N_{concat}$ acepta. En caso contrario, esa rama rechaza.
- **Correctitud:**
    - Si $w \in L_1 \circ L_2$, existe al menos una división válida $w = uv$ con $u \in L_1$ y $v \in L_2$. La rama no determinista que elija dicho punto de corte encontrará la aceptación de $N_1(u)$ y de $N_2(v)$, aceptando la entrada.
    - Si $w \notin L_1 \circ L_2$, para cualquier partición $w = uv$, o bien $u \notin L_1$ o bien $v \notin L_2$, por lo que ninguna rama de $N_{concat}$ podrá aceptar.
- **Análisis de Complejidad Temporal:**
    - La elección no determinista de la partición requiere $O(n)$ pasos.
    - Puesto que $|u| \le n$ y $|v| \le n$, la simulación de $N_1(u)$ requiere $p_1(|u|) \le p_1(n)$ pasos y la de $N_2(v)$ requiere $p_2(|v|) \le p_2(n)$ pasos.
    - El tiempo total de cualquier rama de $N_{concat}$ es $O(n) + p_1(n) + p_2(n)$, el cual es un polinomio $O(n^k)$.

### Demostración equivalente por Verificador Determinista
Sean $V_1$ y $V_2$ los verificadores deterministas de $L_1$ y $L_2$ en tiempo polinómico con certificados $c_1$ y $c_2$. Se construye el verificador $V_{concat}(w, c)$ definiendo el certificado como $c = (i, c_1, c_2)$, donde $i \in \{0, \dots, |w|\}$ representa el punto de corte para dividir la entrada en $w = uv$ (con $|u|=i$). El verificador extrae $u$ y $v$, ejecuta $V_1(u, c_1)$ y $V_2(v, c_2)$, y acepta en tiempo polinómico determinista si y solo si ambas verificaciones resultan satisfactorias.

## Contextualización más allá del ejercicio
- **Estabilidad de la clase NP:** demostrar el cierre bajo unión y concatenación confirma que NP es una clase computacionalmente estable: combinar dos problemas en NP mediante estas operaciones produce un nuevo problema que permanece dentro de la misma clase.
- **Comparación con la clase P:** la clase P también es cerrada bajo unión y concatenación (y además bajo intersección y complemento, ya que $P = co-P$).
- **El contraste con el complemento (**$co-NP$**):**
    - En la unión y la concatenación basta con adivinar un certificado o rama de éxito entre las opciones.
    - En el complemento ($co-NP$), se exige verificar la ausencia de soluciones en todas las ramas de cómputo. La asimetría entre encontrar una solución y certificar que no existe ninguna mantiene abierto si $NP = co-NP$.
- **Cierre bajo reducciones:** de forma análoga a los lenguajes, NP es cerrada bajo reducciones polinómicas ($\le_p$**)**, propiedad fundamental para definir y estructurar la clase de los problemas NP-completos (NPC).

## Referencias
- **Modelos de cómputo** (`02-Modelos de cómputo.pdf`): Máquinas de Turing No Deterministas (mTnD), modelo de cómputo en paralelo (hebras) y adivino no determinista.
- **Jerarquía de Chomsky** (`03-Jerarquía de Chomsky.pdf`): Clasificación de lenguajes formales y modelos de autómatas.
- **Reducción y Cierre** (`05-Reducción.pdf`): Concepto de reducibilidad $\le_p$, propiedades de estabilidad y cierre de clases bajo reducción en tiempo polinómico.
- **Complejidad en Tiempo: Clase P** (`07-Complejidad Tiempo--P.pdf`): Definición de la clase P y cierre bajo complementación ($P = co-P$).
- **Complejidad en Tiempo: Clase NP** (`08-Complejidad Tiempo--NP.pdf`): Caracterización de NP mediante mTnD en poli-tiempo, verificadores deterministas, certificados y análisis de la clase co-NP.

### Uso de IA Generativa
1. **Herramienta utilizada**: Gemini Notebook
2. **Propósito del uso**:
	- Asistencia en la resolución formal y estructuración adaptándolo estrictamente a los apartados de la rúbrica solicitada.
3. **Prompts o instrucciones proporcionadas**:
	- "Explícame que significa que NP sea cerrado bajo unión y concatenación y ponme un ejemplo para entenderlo"
	- "Añade alguna reflexión adicional sobre el problema, conectándolo con conceptos conocidos o próximos a los conocidos"
4. **Uso del contenido generado**: el contenido se empleó como borrador base para desarrollar la demostración matemática e interrelacionar las definiciones formales de Máquinas de Turing No Deterministas (mTnD) y Verificadores Deterministas en tiempo polinómico.
5. **Revisión y edición**: se realizó una revisión del material generado, solicitando adaptaciones de formato, corrección/ampliación de secciones específicas y aclaración de dudas.