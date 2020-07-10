# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema
2. Define los datos de entrada
Rta: * Cantidad de numeros distintos: 10
     * Lista desordenada: [7,17,0,20,9,1,-5,28,12,15,29,13,23,4,-1]
     * Valor a0: 7
3. Haz tu análisis
Rta: Dado que la cantidad de elementos que he escogido para el ejercicio, considero que una función que vaya evaluando en grupos de 2 los elementos de la lista sera mas efectivo que dividir la lista en 2.
4. Resume tus conclusiones
Rta: Luego de que el proceso de evaluación se haya completado al recorrer las n veces necesarias para ordenar la lista, la finalidad es identificar en posición quedo el numero que se definio como a0. Adicional, será beneficioso reconocer cuantos ciclos le tomará al algoritmo ordenarlo por completo.
5. Elige el algoritmo
Rta: El algoritmo que facilitará el proceso de ordenamiento para este listado será Bubble Sort
6. Prueba
Rta:
int ordenar_burbuja(int* array, int elementos)
{
 int i;
 int j;
 int aux_elem;
 int movimientos;

 movimientos = 0;

 for (int i = 0; i < elementos - 1; i++)
 {
     for (j = 1; j < elementos; j++)
     {
         if (array[j] < array[j-1])
         {   // si el elemento anterior es mayor, hacemos el cambio
             aux_elem = array[j];
             array[j] = array[j-1];
             array[j-1] = aux_elem;
             movimientos++;
         }
     }
 }

 return movimientos;
}
7. Obtén la complejidad computacional:
Rta: Al depender de 2 for para su procesamiento, la complejidad computacional es O(n^2).
