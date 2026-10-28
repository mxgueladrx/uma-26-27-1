## Ejercicio 1
Sea la siguiente red:

![[Pasted image 20261028182121.png]]

Y tenemos la evidencia de que el resultado de los rayos X es anormal y que el paciente fuma:

![[Pasted image 20261028181414.png]]

La enfermedad más probable que puede tener es bronquitis (con un 60%) y cáncer de pulmón (64.6%). 

## Ejercicio 2
### Apartado a
Nodos objetivo:

![[Pasted image 20261028183240.png]]

Nodos auxiliares no hay, puesto que no hay ningún nodo de tipo "Auxiliary".

Todos los nodos son de subtipo "Ranked".

Estos nodos etiquetados como "Ranked" son objetivos:

![[Pasted image 20261028183700.png]]

### Apartado b
Tenemos la evidencia de que el paciente tiene alto el colesterol total (a999_350) y los triglicéridos totales (a17_4).
- Si es hombre:
	![[Pasted image 20261028184218.png]]

	La enfermedad más probable que puede tener el paciente es "Hepatic steatosis", con un 75% de probabilidad.

- Si es mujer:
	![[Pasted image 20261028184236.png]]

	La enfermedad más probable que puede tener el paciente es "PBC", con un 85.9% de probabilidad.

A ambos pacientes les conviene hacer una prueba de "Antimytochondrial antibodies", ya que son los que más afinan el diagnóstico. Si damos como evidencia que tiene presente "Antimytochondrial antibodies", entonces:
- Hombre:
	![[Pasted image 20261028185106.png]]

- Mujer:
	![[Pasted image 20261028185123.png]]

Vemos que el diagnóstico del hombre ha cambiado a "PBC", igual que tuvo la mujer al inicio. Además, la probabilidad de ambos superan el 95% de tener "PBC".

## Ejercicio 2
### Apartado a
Sean los siguientes pacientes con las siguientes evidencias:

![[Pasted image 20261028215911.png]]

- Juan Pérez: 
	![[Pasted image 20261028220145.png]]

	La enfermedad más probable que padezca es "Cirrhosis", con una probabilidad del 92.1%.

- María Serrano:
	![[Pasted image 20261028220431.png]]

	La enfermedad más probable que padezca es "PBC", con una probabilidad del 99.3%.

- Iván García:
	![[Pasted image 20261028220645.png]]

	La enfermedad más probable que padezca es "Hepatic steatosis", con una probabilidad del 91.8%.

### Apartado b
- Juana Pérez: 
	![[Pasted image 20261028221323.png]]

	Podemos ver que la probabilidad es casi la misma, ha bajado solo una décima, 91.7%, con el mismo diagnóstico de "Hepatic steatosis".