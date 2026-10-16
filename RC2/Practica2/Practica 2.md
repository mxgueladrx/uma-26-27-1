## Ejercicio 1

![[Pasted image 20261009165841.png]]

Sea el nodo D (daño cerebral), E (edad avanzada) y B (bajo nivel de estudios) los tres nodos padres del nodo T (test MMSE).

Vamos a construir las probabilidades necesarias para el modelo dando las probabilidades de que cada una de las causas provoque el efecto por separado (lo denotamos por $c_x$). También vamos a calcular la probabilidad complementaria ($q_x = 1 - c_x$):
- **D (daño cerebral)**: $c_D = P(T \mid D)=0.9 \implies q_D = 1-0.9=0.1$
- **E (edad avanzada)**: $c_E = P(T\mid E)=0.6 \implies q_E = 1-0.6=0.4$
- **B (bajo nivel de estudios)**: $c_B = P(T\mid B)=0.5 \implies q_B = 1-0.5=0.5$
- **R (ruido)**: $c_R =P(T\mid R)=0.01 \implies q_R = 1-0.01=0.99$

La probabilidad de que no suspenda el test MMSE (aprueba): $$P(\lnot T \mid D, E, B)=q_R · \prod_{i \in T_u} q_i$$
Por tanto, la probabilidad de suspender es $$1-(q_R · \prod_{i \in T_u} q_i)$$

![[Pasted image 20261014182229.png]]

![[Pasted image 20261014182237.png]]

![[Pasted image 20261014182256.png]]

Para comprobar que los resultados de estas fórmulas son idénticos a los que aparecen en la tabla de las CPT:
- **Caso 1 (D = si, E = si, B = si)**:
$$P(T \mid D, E, B)=1-(q_R·q_D·q_E·q_B)=1-(0.99·0.1·0.4·0.5)=98.02$$
- **Caso 2 (D = si, E = no, B = no)**:
$$P(T\mid D, \lnot E, \lnot B)=1-(q_R·q_D)=1-(0.99*0.1)=0.901$$
- **Caso 3 (D = no, E = no, B = no)**:
$$P(T\mid \lnot D, \lnot E, \lnot B)=1-(q_R)=1-(0.99)=0.01$$

## Ejercicio 2

![[Pasted image 20261014190554.png]]

Primero vamos a asignar a cada nodo un identificador:
- **Temperatura adecuada**: T
- **Humedad adecuada**: H
- **Crecimiento bacteria**: C

Como el modelo NoisyMax usa relaciones OR, y la red que tenemos presenta una relación AND, usando las leyes de Morgan obtenemos lo siguiente: $A \land B \equiv \lnot(\lnot A \lor \lnot B)$.

Traducido a la red: $C(si) \equiv T(si) \land H(si) \equiv \lnot(T(no) \lor H(no)) \implies C(no) \equiv T(no) \lor H(no)$

La bacteria no crece si no hay una temperatura adecuada o no hay una humedad adecuada.

Vamos a construir las probabilidades necesarias para el modelo dando las probabilidades de que cada una de las causas provoque el efecto por separado (lo denotamos por $c_x$). También vamos a calcular la probabilidad complementaria ($q_x = 1 - c_x$):