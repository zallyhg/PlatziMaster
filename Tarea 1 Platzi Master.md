# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema
De la lista con n números hay que ubicar la posición de a0 una vez ordenada.
2. Define los datos de entrada
n es la cantidad de números y a0 como valor inicial hasta n
3. Haz tu análisis
Ubicar posición de a0   
4. Resume tus conclusiones
Se pueden tener distintas formas de resolver el ordenamiento buscando la forma más eficiente
5. Elige el algoritmo
ubicar/conocer N
aumentar posición de a0 por cada valor menor en la lista 
imprimir contador hasta llegar a la ubicación
6. Prueba
leer a0 
a0 = 2 

2|8|1|5|0

for (leer arreglo)
if (x<a0)
cont ++;

x=8 c=0
x=1 c=1
x=5 c=1 
x=0 c=2

7. Obtén la complejidad computacional
O(n)