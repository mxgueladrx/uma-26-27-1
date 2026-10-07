## Ejercicio 1
**Nodos**:
- Polen de Plantas (PP):
	- hay_polen
	- no_hay_polen
- Síndrome del Ojo Seco (SOS):
	- si
	- no
- Picazón de Ojos (PO):
	- si_pica
	- no_pica

El problema se modela con los nodos anteriores. PP y SOS causan PO. Ese comportamiento condicional se modela con un OR, si PP o SOS tiene alguna probabilidad alta, PO también tendrá una probabilidad alta. 

![[Pasted image 20261005195440.png]]

![[Pasted image 20261005194759.png]]

## Ejercicio 2
**Nodos**:
- Antecedente del Gen Rosaceia (GEN):
	- si
	- no
- Rosacea Hereditaria (RH):
	- si
	- no
- Contacto con el Sol (SOL):
	- si
	- no
- Crema con Retinol (CR):
	- si
	- no
- Irritación en la Piel (IP):
	- si
	- no

El problema se modela con los nodos anteriores. Los nodos GEN, SOL y CR no tienen padres, por lo que tendrán probabilidad a priori equiprobables. RH tiene como padre GEN, ya que si posee ese gen aumenta la probabilidad, GEN causa RH. IP es provocado por una de las 3 causas: RH, SOL o CR. Ese comportamiento condicional se modela con un OR. Si al menos una de ellas está presente, la probabilidad de IP aumenta.

![[Pasted image 20261005200119.png]]

![[Pasted image 20261005200153.png]]

![[Pasted image 20261005200214.png]]

## Ejercicio 3
**Nodos**:
- Planta (P):
	- floralis
	- petalis
	- ramosis
- Hoja (H):
	- rugosa
	- lisa
- Flor (F):
	- blanca
	- rosa
	- roja
- Rama (R):
	- n4
	- n5
	- n6
- Tipo de Rama (TR):
	- robusta
	- fragil
- Diametro de la Rama Principal (DR):
	- grande
	- pequeño

El nodo raíz es P, asignando una distribución equiprobable a las tres clases. F, H y R son causa (hijos) de la P observada. DR depende de R ya que el diametro depende del número de ramas. Además, TR se determina por el número de ramas R y DR. 

![[Pasted image 20261005203413.png]]

![[Pasted image 20261005203427.png]]

![[Pasted image 20261005203435.png]]

![[Pasted image 20261005203445.png]]

![[Pasted image 20261005203458.png]]

![[Pasted image 20261005203522.png]]

## Ejercicio 4
**Nodos**:
- Puerta Abierta (PA):
	- si
	- no
- Robo (R):
	- si
	- no
- Coche de su hija aparcado en la calle (C):
	- si
	- no
- Muebles desordenados (M):
	- si
	- no

Los nodos raíz son R y C, al que se le asigna una distribución equiprobabe. PA se modela con un OR entre R y C. Si ocurre un R o C, o ambos, la probabilidad de PA aumenta. M depende de solo si ha habido R, por lo que es solo causa de eso.

![[Pasted image 20261005205138.png]]

![[Pasted image 20261005205154.png]]

![[Pasted image 20261005205214.png]]

## Ejercicio 5
**Nodos**:
- Retraso del autobús (RA):
	- si
	- no
- Retención de tráfico (RT):
	- si
	- no
- Avería (A):
	- si
	- no
- Servicio Suspendido (SS):
	- si
	- no
- Obras (O):
	- si
	- no
- Otras Líneas en Servicio (LS):
	- si
	- no

Los nodos raíz son RT, A, O y LS con distribuciones equiprobables. SS depende de que hayan O y LS. La probabilidad de SS es del 100% solo si sucede O y LS. Esto se representa con un AND. RA es causa de una de las siguientes: RT, A y SS. Si ocurre una de ellas la probabilidad de RA aumenta. Además, por sentido común, si SS, la probabilidad de RA es del 100% ya que no hay línea de ese bus.

![[Pasted image 20261007113603.png]]

![[Pasted image 20261007113636.png]]

![[Pasted image 20261007113702.png]]

## Ejercicio 6
**Nodos**:
- Accidente de Tráfico (AT):
	- si
	- no
- Pérdida de Control del Vehículo (PCD):
	- si
	- no
- Error humano (H):
	- si
	- no
- Carretera Resbaladiza (CR):
	- si
	- no
- Fallo Mecánico (FM):
	- si
	- no
- Exceso de Velocidad (EV):
	- si
	- no
- Distracción del Conductor (DC):
	- si
	- no
- Capacidad de Reacción Mermada (CRM):
	- si
	- no
- Consumo de Sustancias (CS):
	- si
	- no
- Cansancio (C):
	- si
	- no
- Vertido de Sustancias (VS):
	- si
	- no
- Condiciones Atmosféricas (CA):
	- si
	- no

Los nodos raíz son CS, C, DC, VS, CA, FM y EV, todos con probabilidad equiprobable. CRM es causada por CS o C (compuerta OR). H es causado por DC y CRM (compuerta AND). CR por VS o CA (compuerta OR). PCD es causado si ocurre al menos una de H, CR, FM o EV (compuerta OR). AT depende de PCD, aumentando la probabilidad si la hay.

![[Pasted image 20261007122209.png]]

![[Pasted image 20261007121148.png]]

![[Pasted image 20261007122644.png]]

![[Pasted image 20261007121637.png]]

![[Pasted image 20261007121946.png|700]]

![[Pasted image 20261007122151.png]]

## Ejercicio 7
**Nodos**:
- Coche (C):
	- puerta1
	- puerta2
	- puerta3
- Participante (P):
	- puerta1
	- puerta2
	- puerta3
- Monty (M):
	- puerta1
	- puerta2
	- puerta3

Los nodos raíz son C y P, con probabilidad equiprobable. M depende de C y P. Si C == P, M abre cualquiera de las otras dos puertas con igual probabilidad. Si C != P, M abre la única puerta disponible (sin el premio) con probabilidad 1.

![[Pasted image 20261007123842.png]]

![[Pasted image 20261007123830.png]]