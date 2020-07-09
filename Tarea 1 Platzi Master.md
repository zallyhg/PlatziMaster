# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema

1. Nos piden tener una lista de elementos de manera desordenada y de esa lista, el primer elemento le llamaremos a0, la lista tiene M elementos, en el siguiente paso nos pide ordenar la lista y asimismo tener presento el primero elementos y que nos diga en qué posición quedó

2. Define los datos de entrada

2. Lista desordenada, quien será a0. 

3. Haz tu análisis
3. Necesitamos una lista o array definir el elemento al que haré seguimiento y a su vez asignarle un fin a la lista que será M o n-1

4. Resume tus conclusiones
4. Necesitamos un algoritmo que recorra el array y al finalizar me indique en qué posición quedó el elemento que escogí para hacerle seguimiento

5. Elige el algoritmo
5. let arrayM = [a0, 1, ,2 ,3, M];
let quicksort = (arrayN) => {
let index = a0;
for(i = 0; i< arrayN; i++){
    for j = 0; j< arrayN; j++{
        if(arrayN[j] < arrayN[j+1])
        let pi = arrayN[j];
        arrayN[j] = arrayN[j+1];
        arrayN[j+1] = pi;
    }
}
let searchIndex = arrayN.indexOf(index);
console.log(`La variable ${index} está en la posición ${searchIndex}`);
return arrayN
}
