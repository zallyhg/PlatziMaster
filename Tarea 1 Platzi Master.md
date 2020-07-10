# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema
>El problema consiste en ordenar una lista desordenada, pero previamiente, se identificará el primer elemento de la lista, de manera que se le pueda hacer un tracking durante el proceso de ordenamiento, y al final >del algoritmo saber en que posición ha quedado el primer elemento de la lista original. La lista contiene N elementos [0, N-1].

2. Define los datos de entrada
>Lista de N números aleatorios

3. Haz tu análisis
>Es necesario primero generar los datos de entrada, para esto se utilizará la función randint en python para generar una lista de números enteros de tamaño l.

>Los datos de entrada se pasan a una función, en la cuál primeramente se establece una variable a0 a 0, lo que nos indica la posición actual del elemento original.

>Esta lista será iterará a través de dos for loops, el primero de los índices 1 hasta la longitud de la lista, y el segundo de 0 a length-i, esto es para que en la primer iteración se itere en el rango 0, ... , length-1, es decir, no tome en cuenta el elemento final, ya para que en las posteriores vaya disminuyendo el rango, dado que en cada iteración el valor más alto va quedando en el extremo derecho, ya no tiene sentido tomarlo en cuenta en futuras iteraciones.

>Dentro de los for loops, se hará un intercambio en el caso en el que el elemento más a la izquierda sea menor, y si resulta que el índice j es igual a nuestra variable a0, esto indica que nuestro primer elemento original ha sido víctima de un swap, por lo que se aumentará en una unidad.

>Adicionalmente, se integra una variable que contará el número de intercambios en cada iteración, de manera que si en una iteración hay cero intercambios, termina el algoritmo, puesto que se considera que al no haber intercambios la lista ya se encuentra ordenada.

4. Resume tus conclusiones
>El algoritmo elegido para este problema fue el método de la burbuja, aunque presenta algunas adaptaciones para evitar utilizar cómputo innecesario.
>Para esto se utilizaron algunas variables adicionales, y así mismo una variable que va monitoreando los intercambios del elemento original, esto para poder identificar su posición final al completar el ordenamiento.

5. Elige el algoritmo
>El algoritmo es el método de la burbuja adaptado.


6. Prueba
>Lista original: [4, 11, 12, 12, 11, 19, 11, 18, 2, 7]
>a0 = 0

>Swaps in iteration 1: 5 | Cumulative swaps: 5   |   a0 = 0

>Swaps in iteration 2: 4 | Cumulative swaps: 9   |   a0 = 0

>Swaps in iteration 3: 3 | Cumulative swaps: 12  |   a0 = 0

>Swaps in iteration 4: 2 | Cumulative swaps: 14  |   a0 = 0

>Swaps in iteration 5: 2 | Cumulative swaps: 16  |   a0 = 0

>Swaps in iteration 6: 2 | Cumulative swaps: 18  |   a0 = 0

>Swaps in iteration 7: 2 | Cumulative swaps: 20  |   a0 = 1

>Swaps in iteration 8: 1 | Cumulative swaps: 21  |   a0 = 1

>Swaps in iteration 9: 0 | Cumulative swaps: 21  |   a0 = 1

>Lista ordenada: [2, 4, 7, 11, 11, 11, 12, 12, 18, 19]

>a0 = 1


7. Obtén la complejidad computacional
>Para el primer for:

>Complejidad temporal: n-1

>Para el segundo for:

>Complejidad temporal: n-1 + n-2 + n-3 + ... + n-n -> <img src="https://latex.codecogs.com/svg.latex?\Large&space;\sum_{i=0}^{n} n-i" title="second for loop complexity" />

>Complejidad: <img src="https://latex.codecogs.com/svg.latex?\Large&space;(n-1) \sum_{i=0}^{n} n-i" title="second for loop complexity" />

><img src="https://latex.codecogs.com/svg.latex?\Large&space;O(\sum_{i=0}^{n} n^{2}-in-n+1)" title="second for loop complexity" />

