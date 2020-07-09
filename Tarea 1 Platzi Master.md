# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema
    Implementar un algoritmo de ordenamiento para ordenar (valga la redundancia) de menor a mayor una cantidad de N números entre 0 hasta M, determinando su posición en la lista.

2. Define los datos de entrada

    los datos de entrada serían:
     2.1. Definir lista de números.
     2.2. Insertar en la lista la N cantidad de números a ordenar.
    
3. Haz tu análisis
    Una vez determinada la lista y la cantidad de valores a ordenar, realizar comparación. Esta se realizará por pares de números.
    Si a es menor que b, estos intercambiaran posición, mientras que el número mayor se comparará con el resto de valores hasta que se obtenga la lista ordenada hasta el final de cada iteración.
    ejemplo.
    
    lista [4 , 7, 9, 3, 5, 2, 1, 6]
    
    Comparar los valores 4 y 7, en la posición 0 y 1 (respectivamente).
    4 < 7, al cumplirse la condición, 4 mantendría su posición, mientras que en la siguiente iteración 7 se va a comparar con 9... así sucesivamente hasta el fina de cada iteración de la lista.


4. Resume tus conclusiones

    Ordenar de menor a mayor una lista de N cantidad de números.

5. Elige el algoritmo

    El algoritmo con el cual se resolverá este reto es bubble sort, el cual, revisa cada elemento de la lista que va a ser ordenada con el siguiente, intercambiándolos de posición si están en el orden equivocado. Es necesario revisar varias veces toda la lista hasta que no se necesiten más intercambios, lo cual significa que la lista está ordenada.

6. Prueba

    ```javascript
    function bubbleSort(lista) {
        for (let i = 0; i < lista.length; i++) {
            for (let j = 0; j < lista.length; j++) {
                if (lista[j] > lista[j + 1]) {
                    let temp = lista[j];
                    lista[j] = lista[j + 1];
                    lista[j + 1] = temp;
                };
            };
        };
        console.log(lista);
        };
        const listNumbers = [4 , 7, 9, 3, 5, 2, 1, 6];
        console.log(bubbleSort(listNumbers)); //mostrará la lista ordenada.
```

7. Obtén la complejidad computacional