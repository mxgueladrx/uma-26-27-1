## Apartado 1.1
$$n \lt n\log n \lt n \log^k n \lt n^2$$
Para demostrarlo vamos a ver las relaciones de dominación mediante cálculo de límites de cada par de funciones, para los $k \gt 1$, vamos a suponer que $k=2$:
- Relación entre $n$ y $n \log n$:  $$\lim_{n \to \infty} \frac{n \log n}{n}=\lim_{n \to \infty} \log n = \infty$$
	Luego, $n \in o(n\log n)$.
- Relación entre $n\log n$ y $n \log^2 n$: $$\lim_{n \to \infty} \frac{n \log^2 n}{n \log n}=\lim_{n \to \infty} \log n = \infty$$
	Luego, $n \log n \in o(n \log^k n)$.
- Relación entre $n\log^2 n$ y $n^2$: $$\lim_{n \to \infty} \frac{n^2}{n \log^2 n}=\lim_{n \to \infty} \frac{n}{\log^2 n} = \infty$$
	Dado que cualquier función polinómica domina a cualquier función logarítmica cuando $n \to \infty$, $n \log^k n \in o(n^2)$.

## Apartado 1.2
### 1. Relación con respecto a $n^{1+\epsilon}$ (con $0 \lt \epsilon \ll 1$)
Para determinar dónde se sitúan $n \log n$ y $n\log^k n$ entre $n$ y $n^2$, vamos a compararlas con una función polinómica intermedia $n^{1+\epsilon}$, como por ejemplo $n^{1.001}$ (donde $\epsilon = 0.001$).
- Comparación de $n\log n$ y $n^{1+\epsilon}$:
	Calculamos el límite: $$\lim_{n \to \infty} \frac{n \log n}{n^{1+\epsilon}}=\lim_{n \to \infty} \frac{\log n}{n^{\epsilon}}$$
	Aplicando L'Hôpital: $$\lim_{n \to \infty} \frac{\frac{1}{n}}{\epsilon n^{\epsilon-1}}=\lim_{n \to \infty} \frac{1}{\epsilon n^{\epsilon}}=0$$
	Como el límite es 0, $n^{1+\epsilon}$ crece asintóticamente más rápido que $n \log n$, independientemente de lo pequeño que sea $\epsilon$ (siempre que $\epsilon \gt 0$). Por tanto $n\log n \in o(n^{1+\epsilon})$.

- Comparación de $n\log^k n$ y $n^{1+\epsilon}$:
	De la misma forma, comparamos la función con el logaritmo elevado a $k$ (asumimos $k \gt 1$) calculando el límite: $$\lim_{n \to \infty} \frac{n\log^k n}{n^{1+\epsilon}}=\lim_{n\to \infty} \frac{\log^k n}{n^\epsilon}$$
	Sabemos que cualquier función polinómica $n^\epsilon$ crece asintóticamente más rápido que cualquier función polilogarítmica $\log^k n$. Si aplicamos L'Hôpital $k$ veces, veríamos que el numerador acabaría siendo constante o tendiendo a 0, mientras que el denominador seguiría creciendo. Por tanto el límite es 0: $$\lim_{n\to \infty} \frac{\log^k n}{n^\epsilon}=0$$
	Esto demuestra que $n^{1+\epsilon}$ también crece más rápido que $n\log^k n$. Por tanto $n\log^k n \in o(n^{1+\epsilon})$.

### 2. Conclusión expresada con palabras sencillas
Teniendo en cuenta que hemos demostrado que tanto $n\log n$ como $n \log^k n$ están acotadas superiormente por $n^{1+\epsilon}$ (para cualquier $\epsilon \gt 0$), y dado que $\epsilon$ puede ser un valor infinitamente pequeño (haciendo que $n^{1+\epsilon}$ esté casi pegado a $n$), podemos concluir que:
- La función $n\log n$ está muy cerca de $n$: el factor $\log n$ crece tan despacio que no logra acercar la función a $n^2$. Cualquier exponente apenas mayor a 1 (como $n^{1.001}$) ya la supera rápidamente.
- La función $n\log^k n$ está muy cerca de $n$: ocurre exactamente lo mismo. Aunque elevemos el logaritmo a una potencia $k$, ese crecimiento extra sigue siendo demasiado débil para alcanzar a $n^2$, quedándose estancada cerca del comportamiento de $n$.

## Apartado 1.3
$$n^{\log n} \lt 2^n \lt n! \lt n^n$$
Demostramos cada relación calculando el $\lim_{n \to \infty} \frac{f(n)}{g(n)}$.
- $n^{\log n} \lt 2^n$: 
	Reescribimos las funciones usando la misma base para que resulte más fácil compararlas. Asumimos un $\log$ en base 2, aunque el resultado es el mismo para cualquier constante. $$n^{\log_2 n} = (2^{\log_2 n})^{\log_2 n}=2^{(\log_2 n)^2}$$
	Calculamos el límite: $$\lim_{n \to \infty} \frac{n^{\log_2 n}}{2^n}=\lim_{n \to \infty} \frac{2^{(\log_2 n)^2}}{2^n}=\lim_{n \to \infty} 2^{(\log_2 n)^2 - n}$$
	Para resolver el límite del exponente, sabemos que la función lineal crece más rápido que la logarítmica. Por tanto: $$\lim_{n \to \infty} ((\log_2 n)^2 -n)=-\infty$$
	Elevando la base al resultado: $2^{-\infty}=0$. Por tanto $n^{\log n} \in o(2^n)$.

- $2^n \lt n!$:
	Para calcular el límite con el factorial, aplicaremos la aproximación de Stirling ($n! \approx \sqrt{2\pi n}\left(\frac{n}{e}\right)^n$). $$\lim_{n \to \infty} \frac{2^n}{n!}=\lim_{n \to \infty} \frac{2^n}{\sqrt{2\pi n}\left(\frac{n}{e}\right)^n}$$
	Agrupamos los términos elevados a n: $$\lim_{n \to \infty} \frac{1}{\sqrt{2\pi n}}\left(\frac{2}{\frac{n}{e}}\right)^n=\lim_{n \to \infty} \frac{1}{\sqrt{2\pi n}} \left(\frac{2e}{n}\right)^n$$
	Evaluamos cada parte: $$\lim_{n \to \infty} \frac{1}{\sqrt{2\pi n}} = 0$$ $$\lim_{n \to \infty} \left(\frac{2e}{n}\right)^n = 0$$porque la base se hace menor que 1 para $n \gt 2e \approx 5.43$. Por tanto: $$\lim_{n \to \infty} \frac{1}{\sqrt{2\pi n}} \left(\frac{2e}{n}\right)^n=0·0=0$$
	Es decir, $2^n \in o(n!)$.

- $n! \lt n^n$:
	Utilizamos de nuevo la aproximación de Stirling para poder trabajar con el factorial. $$\lim_{n \to \infty} \frac{n!}{n^n}=\lim_{n \to \infty} \frac{\sqrt{2\pi n} \left(\frac{n}{e}\right)^n}{n^n}$$
	Simplificamos: $$\lim_{n \to \infty} \sqrt{2\pi n} \frac{\not{n^n}}{e^n · \not{n^n}} = \lim_{n\to \infty}\frac{\sqrt{2\pi n}}{e^n}$$
	Resolvemos: $$\lim_{n\to \infty} \frac{\sqrt{2\pi n}}{e^n}=\frac{\infty}{\infty}$$
	Llegamos a una indeterminación, que resolveremos aplicando la regla de L'Hôpital: $$f(n) = \sqrt{2\pi n}=\sqrt{2\pi}·n^{1/2} \\ f'(n) = \sqrt{2\pi}· \frac{1}{2}n^{-1/2} = \frac{\sqrt{2\pi}}{2\sqrt{n}} \\ g(n) = e^n \\ g'(n)=e^n \\ \lim_{n \to \infty} \frac{\frac{\sqrt{2\pi}}{2\sqrt{n}}}{e^n} = \lim_{n \to \infty} \frac{\sqrt{2\pi}}{2\sqrt{n}·e^n}=\frac{\sqrt{2\pi}}{\infty}=0$$
	Por tanto $n! \in o(n^n)$.

## Apartado 1.4
Nos pide analizar si existe algún $k$ tal que cuando $n\to \infty$, $n^{\log n} \in O(n^k)$. Para ello vamos a evaluar el límite: $$\lim_{n \to \infty} \frac{n^{\log n}}{n^k}$$
Usando como idea la toma de logaritmos (en base 2) del apartado anterior. $$f(n) = \frac{n^{\log_2 n}}{n^k} \\ \log_2(f(n))=\log_2\left(\frac{n^{\log_2 n}}{n^k}\right)$$
Aplicando propiedades de logaritmos: $$\log_2(f(n)) = \log_2(n^{\log_2 n}) - \log_2(n^k) = (\log_2 n · \log_2 n) - (k \log_2 n)$$
Factorizamos $\log_2 n$: $$\log_2(f(n)) = \log_2 n · (\log_2 n - k)$$
Calculamos el límite: $$\lim_{n \to \infty} \log_2(f(n)) = \lim_{n \to \infty} \log_2 n · \log_2(n - k) = \infty · \infty = \infty$$
Como $\log_2(f(n))$ tiende a $\infty$, entonces $f(n)$ también tiende a $\infty$: $$\lim_{n \to \infty} \frac{n^{\log n}}{n^k} = 2^{\infty} = \infty$$
Por tanto $n^k \in o(n^{\log n})$. No es posible encontrar un $k$ para que $n^{\log n}$ quede acotada superiormente por $n^k$. Siempre existirá un valor de $n$ a partir del cuál $n^{\log n}$ superará estrictamente a $n^k$.

Buscando información adicional, la función $n^{\log n}$ es una función superpolinómica (crece estrictamente más rápido que cualquier polinomio de grado $k$) y además subexponencial (crece más despacio que cualquier función exponencial).

## Referencias
### Uso de IA Generativa
1. **Herramienta utilizada**: Gemini (Google)
2. **Propósito del uso**: 
	- Asistencia para la resolución de ciertos límites.
	- Información sobre la aproximación de Stirling y toma de logaritmos.
	- Comprobación de nuestros resultados obtenidos.
3. **Prompts o instrucciones proporcionadas**: 
	- "Que es la aproximación de Stirling para n!".
	- "Que es la toma de logaritmos".
	- "Corrige el ejercicio y comprueba que esté correcto".
4. **Uso del contenido generado**: 
	- Respuesta de ejemplos e información extra sobre lo preguntado anteriormente.
	- Las explicaciones redactadas por la IA fueron reescritas por nosotros para comprenderlo mejor con nuestras palabras.
5. **Revisión y edición**:
	- Comprobación paso a paso de las operaciones matemáticas de los límites calculados son correctos y no hay alucinaciones.
	- Comprobación de que los resultados obtenidos por la IA sean coherentes y no haya contradicciones.