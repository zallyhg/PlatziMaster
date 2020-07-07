# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema: 
   - Tengo una lista desordenada a la que voy a llamar L = []. 
   - El valor mínimo de L es 0 y el valor máximo es M.
   - L tiene N posiciones que van desde 0 hasta N-1. 
   - Estando desordenada L[0] = a0.
   - La pregunta es en que posición queda a0.

2. Define los datos de entrada:
   - Todos los números son distintos.
   - L[0] = a0
   - L tiene N posiciones que van desde 0 hasta N-1. 


3. Haz tu análisis.
   Tengo un número finito de números dentro de una lista, lo que debo hacer es iterar dentro de los elementos de la lista para hallar la posición final de a0.
   
4. Resume tus conclusiones
   Puedo solucionar el problema de dos formas:
   - Ordenando la lista y comparando cada elemento de la lista con a0 para encontrar su posición.
   - Sin ordenar la lista comparar a0 con cada número en la lista y ver cuantas posiciones se corre a la derecha dependiendo de cuantos números sean menores que el.
5. Elige el algoritmo
6. Prueba
7. Obtén la complejidad computacional