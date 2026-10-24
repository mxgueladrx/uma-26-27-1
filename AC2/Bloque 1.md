# Redes Neuronales Artificiales
## Introducción
Son modelos computacionales inspirados en el cerebro humano. Muchos problemas son muy complejos para soluciones basadas en reglas. Aprende patrones de los datos para resolver problemas complejos.

## Machine Learning
Algoritmos que aprenden de la experiencia (datos), no con reglas. Su rendimiendo mejora con más datos. Datos malos provocan modelos malos.

Las funciones objetivo cuantifica que tan bueno es un modelo (mejor error mejor).

El algoritmo busca los mejores parámetros del modelo (optimización). Actualiza parámetros para minimizar el error. Es iterativo

### Deep Learning
Un subconjunto del ML basado en NN profundas. Las operaciones se aprender a partir de datos. Pasa de descripciones estadísticas paramétricas a modelos no paramétricos (con datos escasos se depende de suposiciones simplificadas; con abundancia los modelos no paramétricos se ajustan mejor).

## Aprendizaje Supervisado
Datos tienen características y etiquetas, y el modelo predice etiquetas a partir de las características.

Regresión, clasificación, ranking (sistemas de recomendación), sequence learning (las entradas/salidas son secuencias donde el contexto importa).

Las NN aproximan funciones complejas no lineales, jerarquías y se adaptan a nuevos datos y tareas.

## Redes Neuronales
Pasos de implementación:
- **Procesado de datos**: preprocesado, filtrado, normalización y división.
- **Diseño de la NN**: arquitectura, capas, tipo de neurona y funciones de activación.
- **Entrenamiento**: algoritmo de aprendizaje, tasa de aprendizaje, épocas y validación.
- **Evaluación**: test y métricas.

Capas de una NN:
- **Lineal**: suma ponderada de la entrada, junto con la función de activación.
- **Convolucional**: operaciones de convolución con kernels para capturar característas espaciales.
- **Recurrente**: mantiene el estado con pasos temporales para datos secuenciales temporales.
- **Dropout**: apaga un % de neuronas durante el entrenamiento para evitar el overfitting.
- **Pooling**: reduce dimensiones espaciales de la entrada.
- **Padding**: incrementa dimensiones espaciales de la entrada.
- **Normalization**: normaliza la entrada.
- **Transformaciones**: reestructuración.

Funciones de activación:
- Funciones sigmoides:
	- **Logística**: diferenciable en todo su dominio. $$f(x)=\frac{1}{1+e^{-x}}$$
	- **tanh**: versión desplazada y escalada de la logística. $$f(x)=\frac{e^x - e^{-x}}{e^x+e^{-x}}$$
- Funciones por tramos lineales:
	- **Lineal**: función identidad.
	- **ReLU**: diferenciable en todo su dominio menos 0. Presenta el problema de vanishing gradient. $$f(x)=\max (0,x)$$

Algoritmos de aprendizaje:
- **SGD** (stochastic gradient descent): actualiza pesos usando un gradiente de un lote de datos. Actualizaciones rápidas pero con alta varianza.
- **AdaGrad** (adaptive gradient algorithm): adapta la tasa de aprendizaje para cada parámetro, asignando tasas pequeñas a los pesos que más se actualizan.
- **RMSprop** (root mean square propagation): adapta la tasa de aprendizaje usando un promedio de los gradientes al cuadrado. Evita valores muy pequeños de tasa de aprendizaje.
- **Adam** (adaptive moment estimation): técnicas de momentum y RMSprop. Más equilibrado y eficiente para grandes conjuntos de datos.

Parámetros de entrenamiento:
- Ajustes:
	- **Tasa de aprendizaje**: define cuánto se ajustan los parámetros en cada iteración.
	- **Épocas**: una pasa completa a todos los datos.
	- **Batch size**: número de muestras usadas en cada iteración.
	- **Conjunto de validación**: subconjunto de entrenamiento para detener el entrenamiento.
- Variables aprendibles:
	- **Pesos**: cuánto influye una neurona en otra.
	- **Sesgos**: desplazan la salida de la función de activación. Es el valor añadido a la suma ponderada de las entradas.

# Redes Neuronales Convolucionales
## Introducción
Las CNNs son un tipo de NN para procesar y clasificar imágenes, audio y series temporales. Las operaciones de convolución se ejecutan de forma paralela.

Las capas densas no son invariantes a la traslación. La invarianza a traslaciones y distorsiones se logra con localidad, pesos compartidos y submuestreo dimensional.

## Operación de convolución
Mide el solapamiento entre dos funciones cuando una de ellas se invierte y se desplaza. $$(f·g)(x)=\int f(z)g(x-z)dz$$
Para el espacio 2D: $$(f · g)(x, y) = \sum_i \sum_j f(i, j) g(x-i, y-j)$$
Ejemplos: 
$$\begin{bmatrix}1&2&3\\4&5&6\\7&8&9\end{bmatrix} \times \begin{bmatrix}1&2&1\\0&0&0\\-1&-2&-1\end{bmatrix} = -24$$
$$\begin{bmatrix}1&2&3\\4&5&6\\7&8&9\end{bmatrix} \times \begin{bmatrix}1&2\\2&1\end{bmatrix} = \begin{bmatrix}18&24\\36&42\end{bmatrix}$$
$$\begin{bmatrix}0&0&0&0&0\\0&1&2&3&0\\0&4&5&6&0\\0&7&8&9&0\\0&0&0&0&0\end{bmatrix} \times \begin{bmatrix}1&2&1\\0&0&0\\-1&-2&-1\end{bmatrix} = 
\begin{bmatrix} -13 & -20 & -17 \\ -18 & -24 & -18 \\ 13 & 20 & 17 \end{bmatrix}$$
$$\begin{bmatrix}1&2&1\\0&0&0\\-1&-2&-1\end{bmatrix} \times \begin{bmatrix}0&0&0&0&0\\0&1&2&3&0\\0&4&5&6&0\\0&7&8&9&0\\0&0&0&0&0\end{bmatrix} = 
\begin{bmatrix} -13 & -20 & -17 \\ -18 & -24 & -18 \\ 13 & 20 & 17 \end{bmatrix}$$

## Capas convolucionales
Tamaño de kernel:
- **Grandes**: patrones amplios y complejos, mapas de características pequeños.
- **Pequeños**: detalles finos, mapas de características grandes.

Stride: determina cuantas posiciones se desplaza el kernel. 
- **Alto**: mapa de características reducido, perdiendo resolución espacial.
- **Bajo**: preserva detalles, mapas de características densos.

Padding: añade valores adicionales (0s) alrededor de la entrada antes de la convolución. 
- **Same padding**: garantiza las mismas dimensiones en la entrada y salida.
- **Valid padding**: salida más pequeña y descarta información de los bordes.

El tamaño de la salida es: $$output\_size = \left\lfloor \frac{input\_size - kernel\_size + 2·padding}{stride}\right\rfloor + 1$$

## Capas de pooling
**Reducción de dimensionalidad**: reduce las dimensiones espaciales aplicando una función sobre el mapa de características con una ventana móvil.

**Invarianza a la traslación**: incrementa robustez frente a pequeños desplazamientos y distorsiones en la entrada.

**Preservación de características**: retiene características importantes detectadas por los kernels mientras quita ruido.

Ejemplos:

![[Pasted image 20261022120534.png]]

1) $$\left\lfloor \frac{200-3+2·0}{1} \right\rfloor +1=198 \\
\left\lfloor \frac{198-3+2·0}{1} \right\rfloor +1=196$$$196\times196$
2) $$\left\lfloor \frac{200-3+2·1}{2} \right\rfloor +1=100 \\
\left\lfloor \frac{100-3+2·0}{1} \right\rfloor +1=98$$$98\times 98$
3) $$\left\lfloor \frac{200-5+2·1}{1} \right\rfloor +1=198 \\
\left\lfloor \frac{198-5+2·0}{2} \right\rfloor +1=97$$$97\times 97$

## Otras capas
**Función de activación**: captura características no lineales y jerarquías espaciales complejas. 

**Batch normalization**: normaliza las activaciones, acelerando y estabilizando el aprendizaje. Va después de la convolución ya antes de la función de activación.

**Dropout**: reduce la correlación de los mapas de características espaciales. Va tras las capas de pooling. Se aplican dropout más bajos en CNNs que en densas.

## Modelos preentrenados
**LeNet**: viabilidad de entrenar mediante retropropagación en imágenes. 2 convolucionales con sigmoide o tanh (6 kernels 5x5 y 16 kernels 10x10), 2 average pooling (2x2 con stride 2), 3 dense (120, 84, 10). Entrada de 32x32.

**AlexNet**: usó ReLU para acelerar el entrenamiento, overlapping max pooling, local response normalization tras convoluciones y dropout en dense. Filtros grandes al inicio con muchos canales. Usó doble GPU con data agumentation, weight decay y SGD con momentum. 5 convolucionales y 3 dense.

**VGG**: aumentar la profundidad con kernels pequeños uniformes mejora el rendimiento. 16 o 19 convolucionales (kernels 3x3) y 3 dense.

**GoogLeNet**: filtros 1x1, 3x3 y 5x5 con convoluciones 1x1 para reducir dimensionalidad. 22 capas y sustituyendo dense por global average pooling.

**ResNet**: usa bloques residuales, añaden la entrada a la salida para aprender funciones residuales. Las conexiones de salto facilitan el flujo del gradiente. Variantes de 34, 50, 101 y 152 capas con bloques bottleneck.

**DenseNet**: bloques densos, capas de transición que unen bloques densos (batch normalization, convolución 1x1 y average pooling). Evita el gradient vanishing con rutas directas de gradientes y reuso de características. Variantes de 121, 169, 201 y 264 capas.

# Redes Generativas Adversarias
## Introducción
Modelos DL para generar datos nuevos mediante el aprendizaje de datos. Formado por dos NN que compiten entre sí de forma adversarial: generator y discriminator.

Es aprendizaje no supervisado (no requiere datos etiquetados). Generan salidas diversas y realistas (imágenes, vídeo, texto, audio...). 

Requiere mucho coste computacional y un ajuste cuidadoso para evitar inestabilidades en el entrenamiento.

## Arquitectura
**Generator**: produce muestras a partir de ruido y patrones aprendidos. Maximiza la entropía cruzada cuando el discriminator falla.

**Discriminator**: clasifica las muestras en reales o falsas. Minimiza la entropía cruzada.

Función de perdida: $$loss = -\frac{1}{n} \sum^{n}_{i} \log(D(x_i)) + \log(1-D(G(z_i)))$$
$\log(D(x_i))$ evalúa como rinde discriminator ante un dato real $x_i$.
$\log(1-D(G(z_i)))$ evalúa como rinde el discriminator ante datos falsos creados por el generator ante una entrada de ruido $z_i$.

## Entrenamiento
**Juego Minimax**: juego suma cero en el que el generator engaña a discriminator, mientra que éste intenta identificar los datos correctos. $$\min_D \max_G -\mathbb{E}_x \log D(x) - \mathbb{E}_z \log(1 - D(G(z)))$$
Evolución continua de calidad de generación hasta que generator produzca datos realistas. El equilibrio se alcanza cuando discriminator no distingue lo real de lo falso.

**Inception Score (IS)**: calidad y diversidad de las imágenes generadas usando un clasificador preentrenado (Inception). Valores altos indican mayor cantidad de objetos reconocibles y variedad de clases.

**Fréchet Inception Score (FID)**: compara estadísticas de las imágenes generadas con las reales. Valores bajos indica mayor similitud.

**Mode Score y detección de Mode Collapse**: cuantifica la diversidad y detecta modos faltantes en datos generados.

## Variantes
**Vanilla GAN**: original y básico usado como fundamento.

**Conditional GANs**: generación controlada de datos añadiendo variables o etiquetas de condiciones.

**Deep Convolutional GANs**: generación realista de imágenes con convoluciones.

**Cycle GANs**: traducción de imagen a imagen sin necesidad de datos emparejados. 

**Style GANs**: síntesis de imágenes de alta calidad y controlables.

# Aplicaciones de las Redes Neuronales en Visión por Computador 
## Transfer Learning
Reutiliza un modelo preentrenado en una tarea para mejorar el rendimiento en otra similar. Reduce el tiempo de entrenamiento y coste computacional, y mejora la precisión en conjuntos de datos pequeños.

Se carga el modelo, se congelan las capas iniciales para mantener las características genéricas aprendidas y se ajustan las finales para adaptarlo a nuestros datos.

## Clasificación de imágenes
Usa NN para categorizar imágenes basándose en datos etiquetados aprendidos. En salud, comercio y redes sociales. AlexNet, VGG y ResNet.

## Detección de objetos
Identifica objetos y ubicaciones en imágenes, devolviendo un bounding box y etiqueta de clase. Sistemas de tiempo real (conducción, videovigilancia, robótica). YOLO, SS y Faster R-CNN.

## Segmentación de imágenes
Clasifica cada píxel de una imagen para mejorar los detalles y definir límites de objetos. Imágenes médicas, conducción y monitoreo. U-Net y DeepLab.

## Reconocimiento facial
Analiza puntos de referencia faciales y únicos y los codifica. Aborda problemas de iluminación, pose, oclusión... Seguridad, experiencia de usuario y redes sociales. FaceNet y DeepFace.

## Generación de imágenes
Modelos generativos para crear imágenes o mejorarlas. Superresolución, transferencia de estilo y aumentado de datos.

## Análisis de vídeos
Entiende tareas de visión con CNN + RNN o transformers. Reconocimiento de acciones, vigilancia y conducción.