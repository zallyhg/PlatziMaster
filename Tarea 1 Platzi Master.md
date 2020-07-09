# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema
    Dentro de una lista con N numeros, tengo que encontrar que posicion tendria a0 luego de ser ordenada dicha lista

2. Define los datos de entrada
    Lista de N numeros entre 0 y m
3. Haz tu análisis
    Al principio creia que era necesario ordenar la lista, pero gracias a la explicacion de zally (gracias zally) entendi que no es necesario, ya que solo se requiere conocer la posicion donde se encontraria a0
4. Resume tus conclusiones
    Necesito saber donde estara a0
5. Elige el algoritmo
    Usare un algoritmo muy sencillo con solo un for que itere por todo el largo de un array
6. Prueba
    Probe con una lista definida, pero ya que use para el for 'len' funcionara con una lista de cualquier tamaño 
7. Obtén la complejidad computacional
    Ya que es un for que procesa cada uno de los datos es lineal: 
    O(N)