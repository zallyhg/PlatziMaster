# Tarea 1 Julián Cubillos [C5]

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema
Respuesta:  La lista que se da tiene una cantidad de numeros de N estos pueden ser muchos datos  o en su defecto pocos datos desde 2 hasta infinito, hay que ordenar un número dado en este caso es el primer de la lista y colocarlo en el lugar correspondiente a su ordenamiento.

2. Define los datos de entrada
Respuesta: Asi como se indica en la respuesta 1 los datos pueden variar segun la lista que se especifique, pueden ser numeros negativos o positivos, enteros o decimales.

3. Haz tu análisis
Respuesta: El elemento a0 quedara ordenado en la posicion aN despues de realizar la verificacion de N-1 elementos por ejemplo si es una lista de 10 elemento como: (8, 4, 0, 2, 6, 9, 3, 1, 7, 5) el elemento a0 seria 8 pero quedaria ordenado despues de iterar N-1 veces cada vuelta a la lista y N-1 veces cada vuelta y asi el algoritmo da su posicion final y asi con todos los elementos hasta completar la lista.


4. Resume tus conclusiones
Respuesta: Para usar un algoritmo u otro depende de la cantidad de datos que se den en lista, la efectividad de ellos depende de factores como la cantidad mencionada y el metodo de desarrollo, para asi usar algoritmos lineales (sin necesidad de ciclos repetitivos), logaritmicos (llamando a funciones) o exponenciales (anidando ciclos uno dentro de otro).

5. Elige el algoritmo
Respuesta: Si la cantidad de los datos son menores a 50 puedo usar insertionsort (ordenamiento uno a uno).
Si la cantidad de datos es menor a 100 puedo usar bubblesort o selectionsort
Si la cantidad es mayor de 100 datos puedo usar algoritmos tipo quicksort o mergesort.

6. Prueba Usando un metodo 1 a 1
Vuelta 1
(*8, *4, 0, 2, 6, 9, 3, 1, 7, 5)  Iteraccion 0  Lista original
(4, *8, *0, 2, 6, 9, 3, 1, 7, 5)  Iteraccion 1
(4, 0, *8, *2, 6, 9, 3, 1, 7, 5)  Iteraccion 2
(4, 0, 2, *8, *6, 9, 3, 1, 7, 5)  Iteraccion 3
(4, 0, 2, 6, *8, *9, 3, 1, 7, 5)  Iteraccion 4
(4, 0, 2, 6, 8, *3, *9, 1, 7, 5)  Iteraccion 5
(4, 0, 2, 6, 8, 3, *1, *9, 7, 5)  Iteraccion 6
(4, 0, 2, 6, 8, 3, 1, *7, *9, 5)  Iteraccion 7
(4, 0, 2, 6, 8, 3, 1, 7, *5, *9)  Iteraccion 8  Ordenado 9; N-1 = 9
Vuelta 2
(*0, *4, 2, 6, 8, 3, 1, 7, 5, 9)  Iteraccion 9
(0, *2, *4, 6, 8, 3, 1, 7, 5, 9)  Iteraccion 10
(0, 2, *4, *6, 3, 8, 1, 7, 5, 9)  Iteraccion 11
(0, 2, 4, *6, *8, 3, 1, 7, 5, 9)  Iteraccion 12
(0, 2, 4, 6, *3, *8, 1, 7, 5, 9)  Iteraccion 13
(0, 2, 4, 6, 3, *1, *8, 7, 5, 9)  Iteraccion 14
(0, 2, 4, 6, 3, 1, *7, *8, 5, 9)  Iteraccion 15
(0, 2, 4, 6, 3, 1, 7, *5, *8, 9)  Iteraccion 16 Ordenado 8, 9; N-1 = 8
Vuelta 3
(*0, *2, 4, 6, 3, 1, 7, 5, 8, 9)  Iteraccion 17
(0, *2, *4, 6, 3, 1, 7, 5, 8, 9)  Iteraccion 18
(0, 2, *4, *6, 3, 1, 7, 5, 8, 9)  Iteraccion 19
(0, 2, 4, *3, *6, 1, 7, 5, 8, 9)  Iteraccion 20
(0, 2, 4, 3, *1, *6, 7, 5, 8, 9)  Iteraccion 21
(0, 2, 4, 3, 1, *6, *7, 5, 8, 9)  Iteraccion 22
(0, 2, 4, 3, 1, 6, *5, *7, 8, 9)  Iteraccion 23 Ordenado 7, 8, 9; N-1 = 7
Vuelta 4
(*0, *2, 4, 3, 1, 6, 5, 7, 8, 9)  Iteraccion 24
(0, *2, *4, 3, 1, 6, 5, 7, 8, 9)  Iteraccion 25
(0, 2, *3, *4, 1, 6, 5, 7, 8, 9)  Iteraccion 26
(0, 2, 3, *1, *4, 6, 5, 7, 8, 9)  Iteraccion 27
(0, 2, 3, 1, *4, *6, 5, 7, 8, 9)  Iteraccion 28
(0, 2, 3, 1, 4, *5, *6, 7, 8, 9)  Iteraccion 29 Ordenado 6, 7, 8, 9; N-1 = 6
Vuelta 5
(*0, *2, 3, 1, 4, 5, 6, 7, 8, 9)  Iteraccion 30
(0, *2, *3, 1, 4, 5, 6, 7, 8, 9)  Iteraccion 31
(0, 2, *1, *3, 4, 5, 6, 7, 8, 9)  Iteraccion 32
(0, 2, 1, *3, *4, 5, 6, 7, 8, 9)  Iteraccion 33
(0, 2, 1, 3, *4, *5, 6, 7, 8, 9)  Iteraccion 34 Ordenado 5, 6, 7, 8, 9; N-1 = 5
Vuelta 6
(*0, *2, 1, 3, 4, 5, 6, 7, 8, 9)  Iteraccion 35
(0, *1, *2, 3, 4, 5, 6, 7, 8, 9)  Iteraccion 36
(0, 1, *2, *3, 4, 5, 6, 7, 8, 9)  Iteraccion 37
(0, 1, 2, *3, *4, 5, 6, 7, 8, 9)  Iteraccion 38 Ordenado 4, 5, 6, 7, 8, 9; N-1 = 4
Vuelta 7
(*0, *1, 2, 3, 4, 5, 6, 7, 8, 9)  Iteraccion 39
(0, *1, *2, 3, 4, 5, 6, 7, 8, 9)  Iteraccion 40
(0, 1, *2, *3, 4, 5, 6, 7, 8, 9)  Iteraccion 41 Ordenado 3, 4, 5, 6, 7, 8, 9; N-1 = 3
Vuelta 8
(*0, *1, 2, 3, 4, 5, 6, 7, 8, 9)  Iteraccion 41
(0, *1, *2, 3, 4, 5, 6, 7, 8, 9)  Iteraccion 42 Ordenado 2, 3, 4, 5, 6, 7, 8, 9; N-1 = 2
Vuelta 9
(*0, *1, 2, 3, 4, 5, 6, 7, 8, 9)  Iteraccion 43 Ordenado 0, 1, 2, 3, 4, 5, 6, 7, 8, 9; N-1 = 2

7. Obtén la complejidad computacional
Respuesta: Si los cantidad de datos dados son pocas el algoritmo de ordenamiento puede tener una complejidad de crecimiento exponencial donde pueda anidar varias ciclos repetitivos, esto porque la cantidad de datos no va a ser un problema sencillo de calculo para la computadora, no me va generar un retraso en tiempo y la resolucion va a ser muy rapida.
Sin embargo si la cantidad de datos es mayor o igual a por ejemplo 100 datos debo buscar soluciones con procedimientos lineales o lagaritmicas donde el gran numero de datos no afecte el tiempo de resolucion y no se vea afectado el calculo