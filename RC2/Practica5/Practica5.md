# Práctica 5 - Aprendizaje con GeNIe
## Pregunta 1

![[Screenshot from 2026-11-23 14-23-12.png|377]]

## Pregunta 2

![[Pasted image 20261123180802.png]]

Obtenemos una probabilidad de 0.57 de que el porcentaje de retención (no abandona la carrera) sea de entre un 39% y 59%.

## Pregunta 3

![[Pasted image 20261123181238.png]]

En este caso cambia, obtenemos una probabilidad de 0.62 de que el porcentaje de retención (no abandona la carrera) sea de entre un 59% y 82%.

## Pregunta 4
### Redes bayesianas

![[Pasted image 20261123195540.png]]

![[Pasted image 20261123195156.png]]   ![[Pasted image 20261123195206.png]]

![[Pasted image 20261123195202.png|367]]

- **Capacidad discriminativa:** Obtiene un AUC = 0.803915, lo que refleja una buena capacidad global para distinguir clientes.
    
- **Sesgo hacia la clase positiva:** Aunque logra una exactitud total del 71.7%, su rendimiento está descompensado entre clases. Identifica con gran eficacia los casos positivos (86.84%, con solo 140 falsos negativos), pero presenta una tasa de error elevada en los casos negativos (54.49% de acierto), clasificando erróneamente a 426 clientes.

### Naive Bayes

![[Pasted image 20261123195118.png]]

![[Pasted image 20261123195400.png]]   ![[Pasted image 20261123195410.png|281]]

![[Pasted image 20261123195424.png|345]]

- **Capacidad discriminativa:** Registra un AUC = 0.77549, situándose en un nivel de discriminación aceptable, pero inferior al de la Red Bayesiana debido a la pérdida de información que supone ignorar las dependencias entre atributos.
    
- **Mayor equilibrio entre clases:** Con una exactitud global del 71.1% (apenas 0,6 puntos por debajo de la Red Bayesiana), ofrece un comportamiento mucho más balanceado. Mejora casi en 10 puntos porcentuales la detección de perfiles negativos (64.32%, reduciendo los falsos positivos a 334), a costa de perder sensibilidad en los positivos (77.07%, elevando los falsos negativos a 244).

### Conclusión

| Métrica de evaluación                 | Red bayesiana            | Naive Bayes             |
| ------------------------------------- | ------------------------ | ----------------------- |
| Accuracy                              | **71.70% (1434 / 2000)** | 71.10 % (1422 / 2000)   |
| Sensibilidad (acierto clase positiva) | **86.84% (924 / 1064)**  | 77.07 % (820 / 1064)    |
| Especifidad (acierto clase negativa)  | 54.49% (510 / 936)       | **64.32 % (602 / 936)** |
| AUC                                   | **0.803915**             | 0,775490                |

Desde un punto de vista estadístico y de capacidad predictiva global, la Red Bayesiana es mejor modelo. Supera a Naive Bayes tanto en exactitud global (71.7% frente a 71.1%) como en el área bajo la curva ROC (0.803915 frente a 0.77549). No obstante, Naive Bayes reduce los falsos positivos de 426 a 334.

## Pregunta 5
### Redes bayesianas

![[Pasted image 20261123200855.png|318]]   ![[Pasted image 20261123200921.png|338]]

![[Pasted image 20261123201031.png|342]]   ![[Pasted image 20261123201040.png|335]]

![[Pasted image 20261123201047.png|338]]   ![[Pasted image 20261123201054.png|342]]

- **Rendimiento global bajo:** Obtiene una exactitud del 35.88% (61 aciertos de 170), quedando ligeramente por debajo de un clasificador trivial que predijera siempre la clase mayoritaria (`s2_39_59`, que supone el 36.47% de la muestra).
    
- **Sesgo hacia los tramos inferiores y errores graves:** Concentra la mayoría de sus predicciones en `s1_below_39` (69) y `s2_39_59` (68), fallando casi el 80% de los casos de `s3_59_82` (12/58). Además, clasifica 8 estudiantes del tramo de máxima retención (`s4_82_up`) en el tramo mínimo (`s1_below_39`), señal de sobreajuste (_overfitting_) ante el reducido tamaño muestral.
    
- **Capacidad discriminativa (AUC):** Presenta valores modestos en las tres primeras clases (0.685910, 0.579376 y 0.676185) y solo alcanza una separación sólida en `s4_82_up` (`0,906959`), situando su AUC promedio en 0.712108.

### Naive Bayes

![[Pasted image 20261123201211.png]]   ![[Pasted image 20261123201221.png|311]]

![[Pasted image 20261123201232.png|343]]   ![[Pasted image 20261123201239.png|335]]

![[Pasted image 20261123202125.png|337]]   ![[Pasted image 20261123201248.png|347]]

- **Mejora notable en exactitud:** Alcanza un 53.53 % de acierto global (91 de 170), superando en 17.65 puntos porcentuales a la Red Bayesiana y destacando en los extremos (`s1_below_39` con 60.61% y `s4_82_up` con 88.24%).
    
- **Coherencia ordinal en los fallos:** Sus errores se limitan prácticamente a categorías contiguas (confunde `s1` con `s2` o `s4` únicamente con `s3`), sin producir saltos extremos entre `s1_below_39` y `s4_82_up`.
    
- **Alta capacidad discriminativa (AUC):** Supera a la Red Bayesiana en las cuatro clases, alcanzando 0.847158 en `s1_below_39`, 0.642622 en `s2_39_59`, 0.774015 en `s3_59_82` y 0.983468 en `s4_82_up` (AUC promedio de 0.811816).

### Conclusión

| Métrica de evaluación            | Red bayesiana        | Naive Bayes           |
| -------------------------------- | -------------------- | --------------------- |
| Accuracy                         | 35.88% (61 / 170)    | **53.53% (91 / 170)** |
| Acierto `s1_below_39` (33 casos) | 39.39% (13 / 33)     | **60.61% (20 / 33)**  |
| Acierto `s2_39_59` (62 casos)    | **46.77% (29 / 62)** | 45.16% (28 / 62)      |
| Acierto `s3_59_82` (58 casos)    | 20.69% (12 / 58)     | **48.28% (28 / 58)**  |
| Acierto `s4_82_up` (17 casos)    | 48.28% (28 / 58)     | **88.24% (15 / 17)**  |
| AUC - `s1_below_39`              | 0.685910             | **0.847158**          |
| AUC - `s2_39_59`                 | 0.579376             | **0.642622**          |
| AUC - `s3_59_82`                 | 0.676185             | **0.774015**          |
| AUC — `s4_82_up`                 | 0.906959             | **0.983468**          |
| AUC promedio                     | 0.712108             | **0,811816**          |

Naive Bayes es claramente mejor modelo para este conjunto de datos, ya que supera a la Red Bayesiana tanto en exactitud global (53.53% frente a 35.88%) como en el área bajo la curva ROC de cada una de las cuatro categorías.

## Pregunta 6
### Red bayesiana
![[Pasted image 20261123203458.png]]   ![[Pasted image 20261123203715.png]]   ![[Pasted image 20261123203725.png|226]]

![[Pasted image 20261123203753.png|315]]   ![[Pasted image 20261123203759.png|314]]

![[Pasted image 20261123203804.png|308]]

### Naive Bayes

![[Pasted image 20261123203855.png|224]]   ![[Pasted image 20261123203913.png|242]]   ![[Pasted image 20261123203921.png|207]]

![[Pasted image 20261123203934.png|322]]   ![[Pasted image 20261123203939.png|335]] 

![[Pasted image 20261123203944.png|320]]

### Conclusión

Atendiendo a la exactitud global (Accuracy), la Red Bayesiana es ligeramente mejor modelo, alcanzando un 83.05% de acierto (1661/2000) frente al 82.55% de Naive Bayes (1651/2000), apenas 0.5 puntos porcentuales (10 instancias) de diferencia.

En la práctica, ambos modelos ofrecen un rendimiento casi equivalente. Los dos clasifican perfectamente la clase `Wurro` (100% de acierto y AUC de 0.993164) y reparten de forma inversa sus aciertos en las otras dos categorías: la Red Bayesiana destaca en `Wacka` (82.77% frente a 64.18%) mientras que Naive Bayes lo hace en `Hobexa` (82.62% frente a 65.55%). Sin embargo, Naive Bayes obtiene un área bajo la curva ROC un poco superior tanto en `Hobexa` (0.940266 frente a 0.937170) como en `Wacka` (0.912992 frente a 0.909896), por lo que, aunque la Red Bayesiana gana por la mínima en exactitud con el umbral por defecto, Naive Bayes presenta una capacidad discriminativa (AUC) ligeramente mayor con una estructura mucho más simple.

## Pregunta 7

- **Solvencia crediticia - Gana Red Bayesiana (71.70% / AUC 0.804 vs. 71.10% / AUC 0.775):** Al contar con 10 000 datos, la red estima bien sus parámetros y aprovecha las dependencias reales entre atributos, mientras que Naive Bayes pierde información al asumir independencia.
    
- **Retención universitaria - Gana Naive Bayes (53.53% / AUC 0.812 vs. 35.88% / AUC 0.712):** Con solo 170 instancias, la Red Bayesiana sufre un fuerte sobreajuste al tener que calcular demasiadas probabilidades condicionadas; la simplicidad de Naive Bayes evita este problema y generaliza mucho mejor.
    
- **Planeta Zyx - Empate técnico (83.05% / AUC 0.947 vs. 82.55 % / AUC 0.949):** Con 10 000 registros y rasgos morfológicos que dependen directamente de la especie sin apenas relación entre sí, se cumple el supuesto de independencia condicional de Naive Bayes, igualando el rendimiento de ambos modelos.

Las Redes Bayesianas aprenden mejor cuando abundan los datos y existen relaciones causales entre variables; Naive Bayes resulta más eficaz cuando la muestra es pequeña o los atributos son independientes dada la clase.
