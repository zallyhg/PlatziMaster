# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema
   El problema planteado muestra una lista desordena de numeros diferentes de varios numeros(no indica cuantos), los cuales deb en ordenarse y determinar en que posicion (indice), queda el primer numero (a0) de esa lista desordenada.
   
2. Define los datos de entrada
  Cada uno de los valores de la lista desordenada.
3. Haz tu análisis
  Se debe ordenar la lista e ir comparando en que lugar queda guardado, el indice del primer numero de esa lista inicial.
4. Resume tus conclusiones
  Se debe ir guardando la ubicacion del primer numero, que tantas posiciones se desplaza
5. Elige el algoritmo
  Se ordenaran los numeros de menor a mayor, iniciando con el primer numero (a0) y comparandolo con el adyacente, si el numero es menor se desplaza a la izquierda de este y si es mayor, se coloca a la derecha.
6. Prueba
7. Obtén la complejidad computacional
  La complejidad es del tipo O(n^2)
