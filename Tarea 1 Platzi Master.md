# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema
El problema nos pide que ordenemos los numeros ingresados en una lista y entonces saber en qué posición se encontraría el número a0 al final de este ordenamiento.

2. Define los datos de entrada
Los N números de la lista.

3. Haz tu análisis
Para resolver este problema tendremos que llevar a cabo dos procesos:
a) El uso de algun algoritmo de ordenamiento para ordenar los números de la lista (QuickSort).
b) Comparar a0 con los demás números. 

4. Resume tus conclusiones
Por un lado ejecutar el ordenamiento de la lista y por otro comparar cada número con a0 y crear

5. Elige el algoritmo
Primero ingresamos los N números que queramos en un array y entonces pasamos a la resolución del problema.
a)
Para la parte de ordenar podemos usar varios algoritmos, QuickSort es muy popular.
b)
1-Creamos un ciclo for: for( x=0; x <= array.length; x++)
2-Dentro del for metemos un if que en caso de que a0 sea mayor que x sume 1 a la variable contadora.
3-Al terminal el ciclo, la variable contadora contendrá la posicón de a0 una vez ya fuese ordenado el array.

6. Prueba
b)
var array = [5,4,2,6,8,3,1]
var a0 = array[0]
var contador = 0;
for(x=0; x<=array.length; x++)
{
    if(a0 > array[x])
    {
        contador++
    }
}

console.log(contador);

7. Obtén la complejidad computacional
a)Para el sort seria una complejidad de O(n^2).

b)En este caso se trataria de un problema de complejidad lineal, O(n)