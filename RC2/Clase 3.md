problema de modelado
relaciones de Independencia
algoritmo de aprendizaje
predecir evaluacion de probabilidades

## Sistemas basados en el conocimiento (SBC)
Software que soluciona problemas que exigen conocimientosobre un tema.

**Motor de inferencia**: parte de un sistema de IA que usa conocimientos o modelos para obtener una conclusión a partir de unos datos.

![[Pasted image 20260918154951.png]]

En un sistema basado en reyes bayesianas, el motor de inferencias calcula y actualiza las probabilidades de variables cuando recibe nueva información (evidencia).

![[Pasted image 20260918155434.png]]

## Método probabilístico clásico
**Diagnóstico**: inferencia abdutiva. Determinar las causas que mejor explican lo sucedido.
**Predicción**: inferencia predictiva. Predecir algo que va a pasar.

## Presentación intuitiva
En una red bayesiana, cada nodo corresponde a una variable que a su vez representa una entidad del mundo real. Los arcos que unen los nodos son relaciones de influencia causal.

![[Pasted image 20260918161704.png]]

![[Pasted image 20260918162340.png]]

![[Pasted image 20260918162823.png]]

![[Pasted image 20260918163000.png]]

Probabilidad a priori: $P(x)$, prevalencia.
Conjunto de observaciones o evidencias: $e=\{ ... \}$
Probabilidad a posteriori: $P^*(x)=P(x\mid e)$

Se puede reescribir como: $P^*(x) = \alpha · P(x) · \lambda(x)$ donde $\alpha=\frac{1}{P(y)}$ (constante de normalización) y $\lambda(x)=P(y\mid x)$ (que tan bueno es el test). 

![[Pasted image 20260918163120.png]]

## Definición formal de red bayesiana

## Teorema fundamental

## Modelado con redes bayesianas

## Algoritmo de propagación de probabilidades en árboles