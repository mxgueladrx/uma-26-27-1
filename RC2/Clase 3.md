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
Una red bayesiana es un conjunto de variables proposicionales $V$, conjunto de relaciones binarias sobre $V$, $E$ y una distribución de probabilidad conjunta $P$ sobre $V$. $(V,E)$ forman un grafo acíclico, conexo y dirigido $G$ y $(G,P)$ cumplen las hipótesis de Independencia incondicional.

Se dibujan siempre las fechas hacia abajo

**Variable proposicional**: variable aleatoria que toma un conjunto exhaustivos (cumple todos los rangos o estados posibles de la variable) y excluyentes (pertenece solo a una clase) de valores.

Hipótesis de independencia incondicional: sea $pa(x)$ padre de $x$, $de(x)$ descendientes de $x$, $s(x)$ hijos de $x$ y $as(x)$ ascendientes de $x$. Si $\forall X \in V, \forall Y \in V - \{X \cup de(x) \cup pa(x)\}$, $x$ es independiente de $y$ dado $pa(x)$.

![[Pasted image 20260923180916.png]]

---
![[Pasted image 20260923181343.png]]

hacer

---
![[Pasted image 20260923181948.png]]

$\forall X \in V y Y \in V - \{X \cup de(X) \cup pa(X) \}, X \ ind\ Y$ dado $pa(x)$ 

- $X=SL$ ind $Y \in \{I, SA \}$ a priori
- $X=SE$ ind $Y \in \{SA\}$ dados $pa(SE)=\{SL,I\}$
- $X=I$ ind $\{SL, SA\}$ a priori
- $X=SA$ ind $\{SL, I, SE, DO\}$ a priori
- $X=DO$ ind $\{SL, I, FE, SA\}$ dados $\{SE\}$
- $X=FE$ ind $\{DO, SL, I\}$ dados $\{SE, SA\}$

---
![[Pasted image 20260923182935.png]]

- $X=A$ ind $\{L, S, B\}$ a priori
- $X=T$ ind $\{L, S, B\}$ dados $\{A\}$
- $X=E$ ind $\{A, S, B\}$ dados $\{T, L\}$
- $X=S$ ind $\{A, T\}$ a priori
- $X=L$ ind $\{A, T, B\}$ dados $\{S\}$
- $X=B$ ind $\{A, T, L, E, X\}$ dados $\{S\}$
- $X=X$ ind $\{A, T, L, S, B, D\}$ dados $\{E\}$
- $X=D$ ind $\{A, T, L, S, X\}$ dados $\{E, B\}$

---

Comunicación abierta = dependencia. Comunicación cerrada = independencia

- La comunicación entre B y C está abierta pero se cierra al conocer el valor del padre común
- La comunicación entre B y C está cerrada pero se abre al conocer el valor de hijo común
- La comunicación entre A y C está abierta pero se cierrra al conocer el valor el valor intermedio

## Teorema fundamental (Factorización de la probabilidad)
Dada una red bayesiana, su distribución de probabilidad se puede expresar como $P(x_1, ..., x_n) = \prod P(x_i / pa(x_i))$. Permite describir una red bayesiana a partir de las probabilidades condicionadas de cada nodo dados sus padres en lugar de la probabilidad conjunta. 

$P(t_1 \mid c_1)+P(t_2 \mid c_1)=1,\ P(t_1 \mid c_1)+P(t_1 \mid c_2)$ no tiene por qué dar 1.

![[Pasted image 20260925154727.png]]

---
![[Pasted image 20260925155136.png]]

$P(C,T,G,R,F,D)=P(C)·P(T\mid C)·P(R\mid T)·P(F\mid T,G)·P(D\mid T,G)·P(G)$

| nº de valores a pedir si no es red bayesiana | si sí es red bayesiana |
| -------------------------------------------- | ---------------------- |
| $2^6 - 1=63$                                 | $1+2+2+4+4+1=14$       |

---
![[Pasted image 20260925160058.png]]

$P(C,W,D,P,I,T,M)=P(C)·P(W)·P(D \mid C,W)·P(P\mid W)·P(I\mid D,P,T)·P(M\mid T)·P(T)$

| nº de valores a pedir si no es red bayesiana | si sí es red bayesiana |
| -------------------------------------------- | ---------------------- |
| $2^7 - 1=127$                                | $1+1+4+2+8+2+1=19$     |

---
![[Pasted image 20260925160831.png]]

$P(M=si\mid Co=si)=\frac{P(M=si,Co=si)}{P(Co=si)}=\frac{\sum_{T,J,Ca} P(M=si,Co=si,T,J,Ca)}{\sum_{Co,T,J,Ca}P(M=si,Co,T,J,Ca)}=\frac{8 \ \text{sumandos}\ · 4\ \text{multiplicaciones}}{16\ \text{sumandos}\ · 4\ \text{multiplicaciones}}$

$P(M,T,Ca,J,Co)=P(M)·P(T\mid M)·P(J \mid T)·P(Co\mid T,Ca)·P(Ca\mid M)$

---
## Modelado con redes bayesianas
Un modelo es una representación selectiva de la realidad.
- **Modelado cualitativo**: se definen los nodos (conjunto exhaustivo y excluyente de variables) y las relaciones (influencia causal-efecto).
- **Modelado cuantitativo**: se especifican parámetros, distribuciones de probabilidad condicionada de cada nodo dados sus padres (y la probabilidad a priori de los nodos sin padre).

![[Pasted image 20260925164823.png]]

![[Pasted image 20260925164837.png]]

---
![[Pasted image 20260925165404.png]]


## Algoritmo de propagación de probabilidades en árboles