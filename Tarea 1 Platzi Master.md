# Tarea 1
Daniel Guecha

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema
    Dentro de una lista de N numeros aleatorios ordenar la lista y ver en que posicion queda a0, teniendo en cuenta que a0 es el valor que se encuentra en la posicion 0 de la lista
2. Define los datos de entrada
    lista de n numeros
3. Haz tu análisis
    Segun lo explicado en clase y teniendo en cuenta que no es nesesario ordenar la lista, debemos crear un contador y recorrer dicha lista una sola vez para ir verificando que numeros son mayores de a0 y asi ir aumentando nuestro contador para al final saber en que posicion quedaria a0.
4. Resume tus conclusiones
    no es necesario ordenar esta lista porq se elevaria nuestra complejidad computacional, solo vamos a recoorer una vez nuestro array y asi obtener la solucion.
5. Elige el algoritmo
    1. ingresamos un $array con n numeros aleatorios y un $contador = 0;
    2. recorremos el $array en sus n posiciones 
    3. por cada posiccion del $array verficamos si $array[0] > $array[n]:
        - si, entonces $contador++
        - si no, avanzamos a la sigiuiente posicion
    4. imprimir (posicion de a0 dentro de la lista es $contador)
    
6. Prueba
7. Obtén la complejidad computacional
La complejidad computacionl de este problema seria LINEAL O(N)