# Tarea 1 - Omar Montoya

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema
    -Tengo una lista de N cantidad de números desordenada de la cual debo ser capaz de ubicar a0 una vez ordenada la lista.

2. Define los datos de entrada
    - N (Cantidad de números de la lista)
    - La lista de números tan larga como N
    - a0 (El primer valor de la lista)

3. Haz tu análisis
    - Debo poder ubicar la posición de a0 (El primer valor de la lista) una vez se hayan ordenado los valores.

4. Resume tus conclusiones
    - Existen varias maneras de obtener el resultado, incluso métodos que podrían facilitar este algoritmo dependiendo el lenguaje en el que se desarrolle.

5. Elige el algoritmo
    - Obtener valor de N
    - Capturar el valor a0 de la lista
    - Aumentar la posición de a0 por cada valor menor en la lista.
    - Imprimir el contador para obtener la ubicación

6. Prueba
    -Función en JavaScript reto1();

7. Obtén la complejidad computacional
    -function reto1() {
        var List = [];
        var a0, x, N;
        var counter = 0;

        N = prompt("Ingrese el valor para N: ");

        for (i = 0; i < N; i++) {
            x = prompt("Ingrese un número:", "");
            a0 = List[0];
            if(x < a0){counter++;}
            List.push(x);
        }

        document.write("El valor a0 se encuentra en la posición: ", counter);
    }