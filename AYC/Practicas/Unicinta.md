## 1. Descripción de alto nivel y complejidad

### 1.1. Máquina unicinta

**Marcas usadas.**

- $a$ representa un $0$ de $w$ ya comparado.
- $b$ representa un $1$ de $w$ ya comparado.
- $A$ representa un $0$ de $x_i$ ya comparado.
- $B$ representa un $1$ de $x_i$ ya comparado.
- $X$ se escribe sobre el $\#$ que precede a un candidato $x_i$ que ya se ha descartado.

**Funcionamiento.**

1. `q0` comprueba que la entrada empieza por $\#$. Si no, rechaza.
2. `qfind` está situado en el primer símbolo **no marcado** de $w$. Si lee $0$, lo cambia por $a$ y pasa a `qmarca0`; si lee $1$, lo cambia por $b$ y pasa a `qmarca1`. Si ya está en el $\#$ que cierra $w$, todos los bits de $w$ han sido comparados y pasa a comprobar el final del candidato.
3. `qmarca0`/`qmarca1` avanzan a la derecha por el resto de $w$, por los candidatos ya descartados (cuyos $\#$ iniciales son $X$ y cuyos bits pueden estar marcados $A/B$) y llegan al primer $\#$ no convertido en $X$. Ese $\#$ es el del candidato actual $x_i$. Al cruzarlo se entra en `q0xi` o `q1xi`.
4. `q0xi`/`q1xi` avanzan por el prefijo ya marcado $A/B$ del candidato actual y comparan su primer símbolo no marcado con el bit de $w$ que se acaba de marcar:
   - si coincide, escriben $A$ o $B$ y van a `qvolverw`;
   - si no coincide, o si el candidato se acaba antes, van a `qrechazarcadena`.
5. `qvolverw` retrocede a la izquierda hasta la última marca $a$ o $b$ de $w$ y se coloca en el siguiente símbolo no marcado de $w$, volviendo a `qfind`. Así se compara el siguiente bit.
6. Si un candidato falla, `qrechazarcadena` retrocede por su prefijo $A/B$, escribe $X$ sobre el $\#$ que lo precede y `qreset` borra las marcas $a/b$ de $w$ (las convierte otra vez en $0/1$) y vuelve al $\#$ inicial. Se empieza de nuevo con el siguiente candidato.
7. Cuando todos los bits de $w$ han coincidido con el candidato actual, `qfind` está en el $\#$ que cierra $w$ (o en una $X$ si ya había candidatos descartados). `qcheckend` salta los candidatos descartados y `qcheckxiend` recorre el prefijo marcado del candidato actual:
   - si encuentra $\#$, el candidato tiene exactamente la misma longitud que $w$, luego $x_i=w$;
   - si encuentra $0$ o $1$, el candidato es más largo y se descarta.
8. Si $x_i=w$, `qverifica` recorre el resto de la entrada y `qverifinal` comprueba que termina en $\#$. Si el resto es un sufijo válido, acepta en `qacc`.
9. Si se descartan todos los candidatos, `qmarca0`/`qmarca1` llegan al $\#$ final (el que cierra $x_k$) y al avanzar se encuentra el blanco; se rechaza en `qrej`.

**Complejidad.** Sea $n$ la longitud total de la entrada, $m=|w|$, $k$ el número de bloques $x_i$ y $S=\sum_i |x_i|$. Se tiene $n=m+S+k+2$.

- Tiempo: cada comparación con un candidato recorre como máximo $O(m)$ bits de $w$; el recorrido de ida y vuelta por la cinta y por los candidatos ya descartados cuesta $O(m+P_i)$ por bit comparado, donde $P_i$ es la longitud acumulada de los candidatos anteriores. Sumando sobre todos los candidatos y usando $m+S+k=O(n)$, el coste total es

$$
O\!\left(mS+S^2+kS+km+k^2\right)=O(n^2).
$$

- Espacio: solo se usan las celdas de la entrada y las marcas se escriben sobre esas mismas celdas. Como mucho se visita un número constante de celdas adicionales, luego

$$
O(n).
$$

### 2.1. Máquina unicinta $M_1$

$$
M_1=(Q,\Sigma,\Gamma,\delta,q_0,q_{acc},q_{rej})
$$

con

$$
\begin{aligned}
Q={}&\{q_0,q_{find},q_{marca0},q_{marca1},q_{0xi},q_{1xi},q_{volverw},\\
&q_{checkend},q_{checkxiend},q_{rechazarcadena},q_{reset},q_{verifica},q_{verifinal},q_{acc},q_{rej}\},\\
\Sigma={}&\{0,1,\#\},\\
\Gamma={}&\{0,1,\#,a,b,A,B,X,\sqcup\},\\
q_0={}&q_0,\\
q_{acc}={}&q_{acc},\\
q_{rej}={}&q_{rej}.
\end{aligned}
$$

La función de transición $\delta:Q\times\Gamma\rightharpoonup Q\times\Gamma\times\{L,R\}$ es parcial y viene dada por los siguientes grupos. En todos ellos, cuando se escribe «$\sigma$ recorre …» se entiende que la regla vale para cada símbolo del conjunto indicado.

**Estado $q_0$**

$$
\begin{aligned}
\delta(q_0,\#)&=(q_{find},\#,R),\\
\delta(q_0,\sigma)&=(q_{rej},\sigma,R), && \sigma\in\{0,1,\sqcup\}.
\end{aligned}
$$

**Estado $q_{find}$**

$$
\begin{aligned}
\delta(q_{find},a)&=(q_{find},a,R),\\
\delta(q_{find},b)&=(q_{find},b,R),\\
\delta(q_{find},0)&=(q_{marca0},a,R),\\
\delta(q_{find},1)&=(q_{marca1},b,R),\\
\delta(q_{find},X)&=(q_{checkend},X,R),\\
\delta(q_{find},\#)&=(q_{checkxiend},\#,R),\\
\delta(q_{find},\sqcup)&=(q_{rej},\sqcup,R).
\end{aligned}
$$

**Estados $q_{marca0}$ y $q_{marca1}$**

$$
\begin{aligned}
\delta(q_{marca0},\tau)&=(q_{marca0},\tau,R), && \tau\in\{X,0,1,A,B\},\\
\delta(q_{marca0},\#)&=(q_{0xi},\#,R),\\
\delta(q_{marca0},\sqcup)&=(q_{rej},\sqcup,R),\\
\delta(q_{marca1},\tau)&=(q_{marca1},\tau,R), && \tau\in\{X,0,1,A,B\},\\
\delta(q_{marca1},\#)&=(q_{1xi},\#,R),\\
\delta(q_{marca1},\sqcup)&=(q_{rej},\sqcup,R).
\end{aligned}
$$

**Estados $q_{0xi}$ y $q_{1xi}$ (comparación con el candidato actual)**

$$
\begin{aligned}
\delta(q_{0xi},A)&=(q_{0xi},A,R),\\
\delta(q_{0xi},B)&=(q_{0xi},B,R),\\
\delta(q_{0xi},0)&=(q_{volverw},A,L),\\
\delta(q_{0xi},1)&=(q_{rechazarcadena},1,L),\\
\delta(q_{0xi},\#)&=(q_{rechazarcadena},\#,L),\\
\delta(q_{0xi},\sqcup)&=(q_{rej},\sqcup,R),\\
\delta(q_{1xi},A)&=(q_{1xi},A,R),\\
\delta(q_{1xi},B)&=(q_{1xi},B,R),\\
\delta(q_{1xi},1)&=(q_{volverw},B,L),\\
\delta(q_{1xi},0)&=(q_{rechazarcadena},0,L),\\
\delta(q_{1xi},\#)&=(q_{rechazarcadena},\#,L),\\
\delta(q_{1xi},\sqcup)&=(q_{rej},\sqcup,R).
\end{aligned}
$$

**Estado $q_{rechazarcadena}$ (descartar el candidato actual)**

$$
\begin{aligned}
\delta(q_{rechazarcadena},A)&=(q_{rechazarcadena},A,L),\\
\delta(q_{rechazarcadena},B)&=(q_{rechazarcadena},B,L),\\
\delta(q_{rechazarcadena},\#)&=(q_{reset},X,L).
\end{aligned}
$$

**Estado $q_{reset}$ (borrar marcas de $w$ y volver al principio)**

$$
\begin{aligned}
\delta(q_{reset},\tau)&=(q_{reset},\tau,L), && \tau\in\{A,B,X,0,1\},\\
\delta(q_{reset},a)&=(q_{reset},0,L),\\
\delta(q_{reset},b)&=(q_{reset},1,L),\\
\delta(q_{reset},\#)&=(q_{find},\#,R).
\end{aligned}
$$

**Estado $q_{volverw}$ (volver al siguiente bit no marcado de $w$)**

$$
\begin{aligned}
\delta(q_{volverw},\tau)&=(q_{volverw},\tau,L), && \tau\in\{X,\#,0,1,A,B\},\\
\delta(q_{volverw},a)&=(q_{find},a,R),\\
\delta(q_{volverw},b)&=(q_{find},b,R).
\end{aligned}
$$

**Estado $q_{checkend}$ (saltar candidatos ya descartados)**

$$
\begin{aligned}
\delta(q_{checkend},\tau)&=(q_{checkend},\tau,R), && \tau\in\{0,1,A,B,X\},\\
\delta(q_{checkend},\#)&=(q_{checkxiend},\#,R),\\
\delta(q_{checkend},\sqcup)&=(q_{rej},\sqcup,R).
\end{aligned}
$$

**Estado $q_{checkxiend}$ (comprobar que el candidato no sea más largo que $w$)**

$$
\begin{aligned}
\delta(q_{checkxiend},A)&=(q_{checkxiend},A,R),\\
\delta(q_{checkxiend},B)&=(q_{checkxiend},B,R),\\
\delta(q_{checkxiend},0)&=(q_{rechazarcadena},0,L),\\
\delta(q_{checkxiend},1)&=(q_{rechazarcadena},1,L),\\
\delta(q_{checkxiend},\#)&=(q_{verifica},\#,R),\\
\delta(q_{checkxiend},\sqcup)&=(q_{rej},\sqcup,R).
\end{aligned}
$$

**Estados $q_{verifica}$ y $q_{verifinal}$ (validar el sufijo restante)**

$$
\begin{aligned}
\delta(q_{verifica},\tau)&=(q_{verifica},\tau,R), && \tau\in\{0,1,\#\},\\
\delta(q_{verifica},\sqcup)&=(q_{verifinal},\sqcup,L),\\
\delta(q_{verifinal},\#)&=(q_{acc},\#,R),\\
\delta(q_{verifinal},\tau)&=(q_{rej},\tau,R), && \tau\in\{0,1,\sqcup\}.
\end{aligned}
$$

Los estados $q_{acc}$ y $q_{rej}$ son estados de parada: no tienen transiciones de salida.

### 3.1. Correctitud de $M_1$ (unicinta)

Sea una entrada bien formada
$$
\#w\#x_1\#\cdots\#x_k\#
$$
con $w,x_i\in\{0,1\}^*$, $k\ge1$, y sea $m=|w|$.

**Definiciones auxiliares.** Diremos que un candidato $x_i$ está **descartado** si el $\#$ inmediatamente anterior a él ha sido sustituido por $X$. Diremos que una celda de $w$ está **marcada** si contiene $a$ o $b$ (con $a$ representando un $0$ y $b$ un $1$); análogamente, una celda de un candidato está marcada si contiene $A$ o $B$.

**Lema 1 (Invariante de comparación):** Demuestra por inducción sobre la cantidad $j$ de bits comparados entre $w$ y el candidato $x_i$ que $M_1$ mantiene un estado coherente de marcas:

- **Caso Base ($j = 0$):** Al inicio del proceso o tras un reinicio con `qreset`, $w$ no tiene marcas ($a/b$), el candidato $x_i$ no tiene marcas ($A/B$), la cabeza se sitúa al inicio de $w$ y los candidatos descartados previamente están marcados con $X$.
- **Paso Inductivo ($j \to j+1$):** Suponiendo cierto para $j$ bits comparados, en $q_{find}$ se marca el símbolo $j+1$ ($a$ o $b$) y se avanza hasta el candidato $x_i$ omitiendo los bloques descartados $X$. Los estados $q_{0xi}$ o $q_{1xi}$ verifican la coincidencia con el primer bit libre de $x_i$. Si coincide, se marca ($A$ o $B$) y $q_{volverw}$ regresa al siguiente símbolo libre de $w$, reestableciendo el invariante para $j+1$. Si no coincide o la longitud falla, $q_{rechazarcadena}$ marca el bloque con $X$, $q_{reset}$ restaura los bits de $w$ y se inicia un nuevo intento.

**Lema 2 (Fin de un candidato):** Evalúa el resultado tras procesar el candidato $x_i$:
1. Si $x_i = w$ y $\vert{}x_i\vert{} = m$, $q_{checkxiend}$ lee $\#$ y pasa a $q_{verifica}$ para recorrer el sufijo final y aceptar en $q_{acc}$.
2. Si $\vert{}x_i\vert{} > m$, $q_{checkxiend}$ lee $0$ o $1$ tras marcar $w$ y pasa a $q_{rechazarcadena}$ para descartar $x_i$.
3. Si $\vert{}x_i\vert{} < m$, $q_{0xi}$ o $q_{1xi}$ encuentra un $\#$ antes de tiempo y descarta $x_i$ en $q_{rechazarcadena}$.
4. Si los símbolos difieren en alguna posición, la falta de coincidencia transiciona a $q_{rechazarcadena}$ para descartar el candidato.

**Lema 3 (Terminación y rechazo):** Garantiza que si ningún $x_i = w$, tras $k$ descartes consecutivos todos los $\#$ iniciales quedan sustituidos por $X$. El recorrido de $q_{marca0}/q_{marca1}$ sobrepasa el $\#$ final de $x_k$, encuentra un blanco ($\sqcup$) y termina de forma finita en $q_{rej}$.

**Teorema 1:** $M_1$ decide el lenguaje $L$, ya que acepta únicamente si existe algún $x_i = w$ respetando el formato de la cadena, y rechaza en cualquier otro caso sin entrar en bucles infinitos.