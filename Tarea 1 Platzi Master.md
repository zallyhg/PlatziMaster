# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema
  a) ordenar N números
  b) ver en que posición esta el número = a0
  
2. Define los datos de entrada
  a) N números
  
3. Haz tu análisis
  a) usar un algoritmo de ordenamiento como bubble Sort para ordenar (no dice si de mayor a menor o no)
  b) usar un for que compare a0 con el valor de cada indice y retornar el valor con el indice
  
4. Resume tus conclusiones
  a) comparar cada par de numeros, e ir colocando el menor en el indice-1 del numero con el que lo comparo (suponiendo que es de menor a mayor) e ir aumentando el indice en +1 N veces
5. Elige el algoritmo
  a) Bubble Sort
  
6. Prueba

  a) ordenar (suponiendo que los numero en orden los voy agregando a un array O)
  for(i=0; i<N.length;i++){
    for(j=0; j<N.length-i;j++){
      N[j]>N[j+1] = N[j+1],N[j]
    }
  }
  b) Comparar      
      for(i=0; i< O.length; i++){
        if (O[i]===a0){
          return i
          }
      
7. Obtén la complejidad computacional
  a) O(n^2) Por los 2 for para ordenar, si son muchos datos se puede usar un merge sort que en O(n log n)
