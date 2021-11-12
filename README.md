# Documento de arranque:

## Equipo:

- Eduardo Galindo Rojas Loa- A01028846 
* Rafael Ríos García- A01028722

----
## Propuesta formal del reto:

La actividad integradora que se nos plantea en esta unidad de formación consiste
en idear una solución para reducir los problemas de tráfico que enfrenta nuestra
ciudad. Para fundamentar dicha solución será necesario simular el comportamiento
de múltiples agentes en un ambiente controlado. Mismos agentes que deberán de 
ser capaces de interactuar entre sí para evitar que ocurran colisones.

---
## Identificación de los agentes:

1. Vehículos. Estos agentes serán los más importantes para la simulación, pues 
su movimiento a través de la glorieta es el que ilustrará la propuesta de solución.
   * Deberán ser capaces de:
     - Mantenerse en el carril correcto e identificar a otros agentes que se encuentren cercanos para evitar colisiones
     - Identificar la ruta más efectiva para trasladarse de un punto a otro
     - Encender la direccional cuando tenga que dar vuelta, otros agentes deben ser capaces de identificar cuando esto ocurra para disminuir la velocidad

2. Terreno inaccesible. Estos agentes representarán los bordes de la carretera.
   * Otros agentes no serán capaces de acceder a esta área

3. Carriles. Serán las líneas que los vehículos deben de seguir para transitar por la avenida.
   * Cuando un vehículo tenga que cambiar de un carril a otro, será necesario que encienda las intermitentes
   
----

##Plan de trabajo:

 | Id | Actividad | Tiempo |
| --: | -- | -- |
| 1 | [ ] Programar el comportamiento individual de cada agente | 1 semana |
| 2 | [ ] Probar el funcionamiento individual | 2 días |
| 3 | [ ] Implementar la relación adecuada | 2 semanas |


