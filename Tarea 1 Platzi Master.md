# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema
Nos están pidiendo que se obtenga la posición en la que queda el número a0, después de ordenar la lista de N números, tomando en cuenta que es el primero en la lista
2. Define los datos de entrada
Nos darán como entrada valores entre 0 y M
3. Haz tu análisis
Solo se sabe que ao está en la posición 0 de la lista, y al ser a el coeficiente es un número conocido del principio,por lo que se puede hacer un un contador de las veces que se mueve a0 y tener su posición final, si se mueve a la derecha el contador se le sumara un entero y si se mueve a la izquierda se le restara. Para esto se le asiganará una variable a a0

4. Resume tus conclusiones
Al darle un valor a a0 será más identificable y se podrá proponer un algoritmo de ordenación
5. Elige el algoritmo
Tomando en cuenta que el número de datos puede ser N, pero que a0 debe pertenecer a los primeros lugares, propongo usar inserción
6. Prueba
  supongamos [10,9,8,7,6] y que a0 = 10
    contador = 0
    1.- iteración [7,10,9,8,6]
    contador = 1

    2.- iteración [6,7,10,9,8]
    contador = 2

    3.- iteración [6,7,9,10,8]
    contador = 3

    4.- iteración [6,7,8,9,10]
    contador = 4

    En este caso el programa llega a su fin, pero si fueran más datos seguiría haciendo iteraciones hasta que estuviera ordenada la lista

7. Obtén la complejidad computacional
O(n^2)
