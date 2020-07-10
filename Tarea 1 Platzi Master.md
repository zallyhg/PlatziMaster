# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema
Hay una lista L (lista) desordenada con una variable N (números) con valores entre 0 y M

Nos comenta que el primer número de la lista es el a0, y necesitamos saber  dónde queda dicho numero

La primera posición de la lista es 0 y la última N-1 
L = [0,… N-1]

2. Define los datos de entrada
Lista = l
Números de la lista = n
Valores = v
Primer Número = l[a0,…]
Primera posición = l [0,1,2,3,4,…]
Ultima posición = l[0,1,2,3,4,…. N-1]

3. Haz tu análisis
El problema me indica que debo hallar donde queda a0 que corresponde al primer valor de la lista, para eso debería comparar el valor a0 que esta en la posición 0 con el valor de la siguiente posición:

Valor de posición 0 > Valor posición 1

Si esto es cierto, el valor de la posición 0 osea a0 pasa a la posición 1.
Luego a0 se encuentra en la posición 1, por lo tanto se compara el valor de la posición 1 con la posición 2 y así se ejecuta el ciclo hasta que el valor a0 deje de ser mayor que el siguiente valor. Puedo crear una Variable que me cuente la posición en la que se encuentra el número para así tener un registro de donde se encuentra a0.

4. Resume tus conclusiones
El problema para solucionarlo de manera simple, es comparar a0 en la posición actual con el valor siguiente, cada que a0 sea mayor al siguiente, se correrá una casilla y el próximo valor bajara una casilla, ese ciclo se ejecutara hasta que a0 sea menor al siguiente número.

5. Elige el algoritmo
Array = [N]
N = cantidad de valores en array
A0 = el valor iniciara en 0

Función ejecuta el orden de a0 al ser invocada
Ciclo que incremente se encarga de contar la posición
Variable que es igual a la posición actual valueComp = array[i]

Variable j = a0 (Para asignar el valor en el que se desea empezar y comparar, en este caso la posición 0)

Ciclo while que comparara la que a0 es mayor que el siguiente numero
Si es cierto, j se le sumara 1

A0 tomara el valor de la posición actual

6. Prueba
Se implementa un algoritmo tipo Insertion Sort en Javascript

var array = [10,4,20,6,9,8,25,640,456,521,698,411,105,145,14];
//n count the values in the array
var n = array.length;
var a0 = array[0];

function order(arr,size){
    //var i is for the whole cycle
    for (let i = 1; i < size; i++) {
        let valueComp = arr[i]
        let j = i-1;
        //This second cycle compare the value a0 with the next one
        while (j >= 0 && arr[j] > valueComp) {
            arr[j+1] = arr[j];
            j--
        }
        arr[j+1] = valueComp;
    }
}

order(array,n);
console.log(array);
console.log("a0 ended in position: " + array.indexOf(a0));

7. Obtén la complejidad computacional

Este problema tiene una complejidad computacional O(N^2)