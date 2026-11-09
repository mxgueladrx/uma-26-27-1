---
marp: true
theme: default
paginate: true
math: katex
size: 16:9
header: "Práctica 3 · Sipser"
footer: "Teoría de la Computación · Complejidad"
---

<style>
section { font-size: 22px; }
section h1 { font-size: 42px; }
section h2 { font-size: 32px; }
section h3 { font-size: 24px; }
section table { font-size: 18px; }
section li { margin-bottom: 0.3em; }
</style>

<!-- _class: lead -->
<!-- _paginate: false -->

# Demostraciones de Complejidad Computacional

## Cierre de NP y el problema TRIANGLE en P

**Práctica 3 · Sipser**

### Objetivos
- Demostrar formalmente que NP es cerrada bajo unión y concatenación.
- Construir las máquinas de Turing y los verificadores deterministas asociados.
- Probar que TRIANGLE ∈ P mediante una mTD y un análisis temporal O(n³).

<!-- _footer: "1:00 min · Práctica 3 · Sipser" -->

<!--
NOTAS DEL ORADOR (1:00)
Buenos días. En esta exposición resolvemos formalmente dos ejercicios de la Práctica 3. El ejercicio 7 demuestra que NP es cerrada bajo unión y concatenación. El ejercicio 9 demuestra que TRIANGLE pertenece a P. No nos limitaremos a enunciar los resultados: construiremos explícitamente las máquinas de Turing y los verificadores, probaremos su correctitud y acotaremos su tiempo. Al final presentaremos una tabla comparativa con los modelos utilizados.
-->

---

## Ejercicio 7 · Introducción y caracterización de NP

### Operaciones formales

$$L_1 \cup L_2 = \{\, w \in \Sigma^* \mid w \in L_1 \lor w \in L_2 \,\}$$

$$L_1 \circ L_2 = \{\, w \in \Sigma^* \mid \exists u,v \in \Sigma^*:\ w = uv,\ u \in L_1,\ v \in L_2 \,\}$$

### Dos caracterizaciones equivalentes de NP

1. **Máquina de Turing no determinista (mTnD):**
   $NP = \bigcup_{k \ge 1} NTIME(n^k)$. La máquina “adivina” la rama correcta y acepta si alguna rama acepta en tiempo polinómico.
2. **Verificador determinista:**
   $A \in NP$ si existe un verificador $V$ determinista en tiempo polinómico y un certificado $c$ de longitud polinómica tales que $w \in A \iff \exists c:\ V(w,c)$ acepta.

**Ejemplo:** $HAMPATH$ (grafos con camino hamiltoniano) y $SAT$ (fórmulas satisfacibles) pertenecen a NP; su unión y concatenación seguirán en NP, como se demuestra a continuación.

<!-- _footer: "1:00 min · Práctica 3 · Sipser" -->

<!--
NOTAS DEL ORADOR (1:00)
Partimos de dos lenguajes L1 y L2 en NP sobre un alfabeto Sigma. La unión acepta las cadenas que están en L1 o en L2; la concatenación acepta cadenas que se pueden partir en u en L1 y v en L2. Usaremos dos caracterizaciones equivalentes de NP. La primera: una máquina de Turing no determinista decide el lenguaje en tiempo polinómico; podemos imaginarla como un adivino que elige la rama correcta. La segunda: un verificador determinista polinómico comprueba la pertenencia a partir de un certificado de longitud polinómica. Ejemplos típicos son HAMPATH y SAT; su unión y concatenación seguirán siendo problemas en NP, como vamos a demostrar.
-->

---

## Cierre de NP bajo unión ($L_1 \cup L_2 \in NP$)

**Hipótesis:** $N_1$ y $N_2$ deciden $L_1$ y $L_2$ en tiempo $O(n^{k_1})$ y $O(n^{k_2})$.

### Construcción de la mTnD $N_{unión}$

1. Sobre $w$, realizar una **bifurcación inicial no determinista**: elegir la rama 1 o la rama 2. Coste: $O(1)$.
2. En la rama 1, simular $N_1(w)$; en la rama 2, simular $N_2(w)$.
3. Aceptar si la máquina simulada acepta; si esa rama rechaza, la otra rama puede seguir aceptando.

### Correctitud

- Si $w \in L_1 \cup L_2$, entonces $w \in L_1$ o $w \in L_2$: al menos una rama alcanza la aceptación.
- Si $w \notin L_1 \cup L_2$, ni $N_1$ ni $N_2$ aceptan $w$: todas las ramas rechazan.

### Complejidad temporal

$$T(n) = O(1) + \max\bigl(O(n^{k_1}), O(n^{k_2})\bigr) = O(n^k)$$

Por tanto, $L_1 \cup L_2 \in NP$.

<!-- _footer: "1:30 min · Práctica 3 · Sipser" -->

<!--
NOTAS DEL ORADOR (1:30)
Supongamos que N1 y N2 deciden L1 y L2 en tiempos O(n^k1) y O(n^k2). Construimos N_unión así: sobre la entrada w, primero hace una bifurcación no determinista y elige qué máquina simular; después ejecuta N1(w) o N2(w) según la rama. La elección cuesta O(1). Para la correctitud: si w está en la unión, al menos una rama acepta; si no está, ninguna de las dos máquinas acepta, luego todas las ramas rechazan. El tiempo de cualquier rama es el máximo de los dos tiempos más la bifurcación: O(1) + max(O(n^k1), O(n^k2)), que es un polinomio O(n^k). Conclusión: la unión está en NP.
-->

---

## Cierre de NP bajo concatenación ($L_1 \circ L_2 \in NP$)

**Hipótesis:** $N_1$ y $N_2$ deciden $L_1$ y $L_2$ en tiempo polinómico $p_1(n)$ y $p_2(n)$.

### Construcción de la mTnD $N_{concat}$

1. Sobre $w$ de longitud $n$, **adivinar no deterministamente** un punto de corte $i \in \{0,1,\dots,n\}$.
2. Dividir $w = uv$, con $|u| = i$ y $|v| = n-i$.
3. Simular $N_1(u)$ y $N_2(v)$; aceptar si **ambas** aceptan.

### Correctitud

- Si $w \in L_1 \circ L_2$, existe una división válida $w = uv$ con $u \in L_1$ y $v \in L_2$; la rama que elige ese corte acepta.
- Si $w \notin L_1 \circ L_2$, para todo corte $u \notin L_1$ o $v \notin L_2$; ninguna rama acepta.

### Complejidad temporal

$$T(n) = O(n) + p_1(n) + p_2(n) = O(n^k)$$

Por tanto, $L_1 \circ L_2 \in NP$.

<!-- _footer: "1:30 min · Práctica 3 · Sipser" -->

<!--
NOTAS DEL ORADOR (1:30)
Para la concatenación, la idea es adivinar dónde termina la primera palabra. N_concat elige de forma no determinista un punto de corte i entre 0 y n, divide w en u, de longitud i, y v, el resto. Luego simula N1 sobre u y N2 sobre v en la misma rama, y acepta solo si ambas aceptan. Correctitud: si w es concatenación de una palabra de L1 y una de L2, la rama que acierta el corte acepta; si w no lo es, para todo corte al menos una de las dos simulaciones rechaza, así que ninguna rama acepta. En tiempo, elegir el corte cuesta O(n), y como las longitudes de u y v no superan n, las simulaciones cuestan a lo sumo p1(n) y p2(n). El total O(n) + p1(n) + p2(n) es polinómico. Luego la concatenación está en NP.
-->

---

## Demostración equivalente por verificadores deterministas

### Verificador para la unión

- Certificado: $c = (i, c')$, con $i \in \{1,2\}$.
- $V_{unión}(w,c)$ ejecuta $V_i(w,c')$ y acepta si esta verificación acepta.
- $|c|$ es polinómica y la verificación es determinista en tiempo polinómico.

### Verificador para la concatenación

- Certificado: $c = (i, c_1, c_2)$, donde $i \in \{0,\dots,|w|\}$ es el punto de corte.
- $V_{concat}(w,c)$ divide $w = uv$ con $|u| = i$ y ejecuta $V_1(u,c_1)$ y $V_2(v,c_2)$.
- Acepta si y solo si **ambas** verificaciones aceptan.

| Operación | Certificado | Verificación determinista |
|:--|:--|:--|
| Unión | $(i,c')$ | $V_i(w,c')$ |
| Concatenación | $(i,c_1,c_2)$ | $V_1(u,c_1) \land V_2(v,c_2)$ |

En ambos casos se obtiene un verificador determinista polinómico; luego la clase NP es cerrada bajo las dos operaciones.

<!-- _footer: "1:00 min · Práctica 3 · Sipser" -->

<!--
NOTAS DEL ORADOR (1:00)
La segunda vía es equivalente y a veces más intuitiva: verificadores deterministas. Para la unión, el certificado es un par (i, c prima), donde i indica cuál de los dos verificadores usar y c prima es el certificado correspondiente. El verificador ejecuta V_i sobre w y c prima. Para la concatenación, el certificado es (i, c1, c2): i es el punto de corte y c1, c2 son los certificados de cada parte. El verificador divide w con el corte, ejecuta V1 sobre u y V2 sobre v, y acepta si ambos aceptan. En los dos casos el certificado tiene longitud polinómica y la verificación es determinista polinómica, lo que confirma la pertenencia a NP.
-->

---

## Ejercicio 9 · El problema TRIANGLE

### Definición formal

Un **triángulo** (3-clique) en un grafo no dirigido $G=(V,E)$ es un conjunto de tres vértices distintos $\{u,v,w\} \subseteq V$ tal que:

$$\{(u,v), (v,w), (w,u)\} \subseteq E$$

El lenguaje de decisión es:

$$TRIANGLE = \{\, \langle G \rangle \mid G \text{ es un grafo no dirigido con al menos un triángulo} \,\}$$

### Ejemplo

En $G_1$ con $V_1=\{A,B,C,D\}$ y $E_1=\{(A,B),(B,C),(C,A),(C,D)\}$, el conjunto $\{A,B,C\}$ forma un triángulo; $D$ no participa en ningún triángulo.

```text
    A ----- B
     \     /
      \   /
        C ----- D
```

<!-- _footer: "1:00 min · Práctica 3 · Sipser" -->

<!--
NOTAS DEL ORADOR (1:00)
Pasamos al ejercicio 9. Un triángulo, o 3-clique, es un conjunto de tres vértices distintos de un grafo no dirigido G igual a V, E, tales que las tres aristas entre ellos están en E. El lenguaje de decisión TRIANGLE contiene las codificaciones de grafos que tienen al menos un triángulo. En el ejemplo, el grafo con vértices A, B, C y D y las aristas AB, BC, CA y CD contiene el triángulo A, B, C; el vértice D cuelga de C y no forma parte de ningún triángulo. La pregunta es si podemos decidir esto en tiempo polinómico determinista.
-->

---

## Demostración de $TRIANGLE \in P$ mediante una mTD

Sea $M$ una máquina de Turing determinista. Sobre la entrada $\langle G \rangle$, con $G=(V,E)$ y $n=|V|$:

1. **Validar** que $\langle G \rangle$ es una codificación válida de un grafo no dirigido. Si no lo es, **rechazar**.
2. Para cada conjunto no ordenado de tres vértices distintos $\{u,v,w\} \subseteq V$:
   - Consultar si $(u,v) \in E$, $(v,w) \in E$ y $(w,u) \in E$.
   - Si las tres aristas existen, **aceptar**.
3. Si se examinan todos los $\binom{n}{3}$ tríos sin encontrarlas, **rechazar**.

### Criterios de decisión

- **Aceptación:** existe al menos un trío $\{u,v,w\}$ con sus tres aristas presentes.
- **Rechazo:** la entrada no es válida o ningún trío cumple la condición anterior.

<!-- _footer: "1:30 min · Práctica 3 · Sipser" -->

<!--
NOTAS DEL ORADOR (1:30)
Construimos una máquina de Turing determinista M. Primero valida que la entrada sea una codificación correcta de un grafo no dirigido; si no lo es, rechaza. Después recorre todos los tríos no ordenados de vértices distintos. Para cada trío consulta si existen las tres aristas: u con v, v con w y w con u. Si las tres existen, acepta inmediatamente. Si termina de revisar todos los tríos sin encontrarlas, rechaza. La clave es que no hay adivinación: el recorrido es exhaustivo y determinista. Lo único que falta es comprobar que el número de tríos y el coste de cada comprobación son polinómicos.
-->

---

## Correctitud y análisis de complejidad temporal de TRIANGLE

### Correctitud

- Si $G \in TRIANGLE$, existe un trío mutuamente conectado; el recorrido exhaustivo lo evalúa y $M$ acepta.
- Si $G \notin TRIANGLE$, ningún trío posee las tres aristas; tras agotar los tríos, $M$ rechaza.

### Complejidad temporal (matriz de adyacencia $n \times n$)

| Etapa | Coste |
|:--|:--|
| Comprobación del formato | $O(n^2)$ |
| Enumeración de tríos: $\binom{n}{3} = \frac{n(n-1)(n-2)}{6}$ | $O(n^3)$ |
| 3 consultas de aristas por trío, cada una en $O(1)$ | $O(1)$ por trío |
| Rechazo final | $O(1)$ |

$$T(n) = O(n^2) + O(n^3) + O(1) = O(n^3)$$

**Conclusión:** $M$ decide $TRIANGLE$ en tiempo polinómico, por lo que **$TRIANGLE \in P$**.

<!-- _footer: "1:00 min · Práctica 3 · Sipser" -->

<!--
NOTAS DEL ORADOR (1:00)
Veamos correctitud y tiempo con una matriz de adyacencia de n por n. Si el grafo tiene un triángulo, ese trío aparecerá en el recorrido y la máquina aceptará. Si no lo tiene, ningún trío cumplirá las tres aristas y la máquina rechazará al agotarlos. En tiempo: validar la codificación cuesta O(n²); hay C(n,3) = n(n−1)(n−2)/6 tríos, que es O(n³); y cada trío hace tres consultas en O(1). Por tanto el total es O(n²) + O(n³) + O(1) = O(n³). Al estar acotada por un polinomio, M decide TRIANGLE en tiempo polinómico y TRIANGLE pertenece a P.
-->

---

## Resumen de resultados

| Resultado | Modelo utilizado | Complejidad |
|:--|:--|:--|
| $L_1 \cup L_2 \in NP$ | mTnD $N_{unión}$ / Verificador $V_{unión}$ | $O(n^k)$ |
| $L_1 \circ L_2 \in NP$ | mTnD $N_{concat}$ / Verificador $V_{concat}$ | $O(n^k)$ |
| $TRIANGLE \in P$ | mTD $M$ | $O(n^3)$ |

### Ideas clave

- **Unión:** bifurcación no determinista; basta con que una rama acepte.
- **Concatenación:** elección no determinista del punto de corte; ambas partes deben aceptar.
- **TRIANGLE:** verificación exhaustiva de los $\binom{n}{3}$ tríos con consultas $O(1)$.

Todas las demostraciones son **constructivas** y sus tiempos quedan acotados por un polinomio.

<!-- _footer: "0:30 min · Práctica 3 · Sipser" -->

<!--
NOTAS DEL ORADOR (0:30)
En resumen: la unión y la concatenación de dos lenguajes en NP siguen en NP, con máquinas no deterministas que bifurcan o adivinan el corte, y con verificadores que reciben el índice y los certificados. TRIANGLE está en P, con una máquina determinista que examina los O(n³) tríos. Los tres resultados son constructivos y sus tiempos son polinómicos. Con esto cerramos los dos ejercicios.
-->
