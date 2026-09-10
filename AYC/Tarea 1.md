![[Pasted image 20260910113003.png]]![[Pasted image 20260910113012.png]]![[Pasted image 20260910113021.png]]![[Pasted image 20260910113029.png]]![[Pasted image 20260910113036.png]]

## 1.
- **P**: problemas que se pueden resolver en tiempo polinómico y se encuentra solución. Un ejemplo es ordenar una lista.
- **NP**: problemas cuya solución se verifica en tiempo polinómico pero encontrar la solución se tarda más que un tiempo polinómico (o no, problema P vs NP). Un ejemplo es el Sudoku, es difícil de resolver pero muy rápido de comprobar la solución.
Sé de ellos por el famoso problema de P vs NP y me informé de él un poco.
## 2.
- **P (Tiempo Plolinomial)**: problemas que se pueden resolver mediante una máquina de Turing determinista y esta acotado por un polinomio $O(n^k)$. Son problemas que consideramos eficientes o tratables. 
	- UN ejemplo es el algoritmo de Dijkstra, que tiene una cota $O(|E|+|V|\log|V|)$.
- **NP (Tiempo Polinomial No Determinista)**: problemas cuya solución se verifica en tiempo polinómico por una máquina de Turing determinista, pero su solución se alcanza mediante una máquina de Turing no determinista. 
	- Un ejemplo es el problema de la Satisfacibilidad Booleana (SAT), que consiste en estudiar si existe alguna combinación de valores de verdad que hagan una fórmula proposicional satisfacible (verdadera).
- **REC (Lenguajes Recursivos / Problemas Decidibles)**: problemas en los que existe un algoritmo (máquina de Turing) capaz de responder "Si" o "No" de manera matemática y en un número finito de pasos. 
	- Un ejemplo es analizar si una cadena de texto pertenece a un lenguaje.
- **RE (Recursivamente Enumerables / Problemas Semidecidibles)**: problemas en los que existe un algoritmo capaz de confirmar las respuestas afirmativas ("Si") deteniéndose en tiempo finito. Si la respuesta es "No", el algoritmo podría entrar en un bucle infinito. 
	- Un ejemplo es estudiar la validez de la lógica de primer orden (LP1). LP1 es semidecidible, si un conjunto de fórmulas es insatisfacible, existe un algoritmo capaz de certificar dicha insatisfacibilidad en un número finito de pasos. Si el conjunto es satisfacible, el procedimiento matemático podría entrar en un bucle infinito.

| **Clase** | **Ámbito**           | **Tipo de algoritmo**    | **Propiedades**                             | **Ejemplos**                    |
| --------- | -------------------- | ------------------------ | ------------------------------------------- | ------------------------------- |
| **P**     | Complejidad temporal | Determinista y eficiente | Cota $O(n^k)$                               | Camino más corto (Dijkstra)     |
| **NP**    | Complejidad temporal | Verificación polinómica  | Verificable en $O(n^k)$                     | Satisfacibilidad booleana (SAT) |
| **REC**   | Computabilidad       | Decidible                | Respuesta "Si" o "No" sin bucles            | Comprobación sintáctica         |
| **RE**    | Computabilidad       | Semidecidible            | Puede entrar en bucle infinito ante el "No" | Semidecibilidad de LP1          |
