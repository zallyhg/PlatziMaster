# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema
Dada una lista desordenada imprimir en que posición quedaría el elemnto a0 si la lista estuviera ordenada
2. Define los datos de entrada
Input: Lista desordenada
Output: posición a0
3. Haz tu análisis
En primera instancia pensé en ordenarla pero la solución que reduce O (el tiempo de ejecución The big O) es:
- Contar las veces que un número de la lista es mayor que a0 y empezar esta cuenta en 0
4. Resume tus conclusiones
Antes de programar o pensar en la mejor manera de hacer este código debo revisar que esperan obtener con la 
solución de la solicitud y no tanto en la descripción de la solucitud.
5. Elige el algoritmo
Propio/expuesto en clase programado por mi.
vector = input
output = 0
for i in vector:
    if vector[0] > vector[i]:
        output = output + 1
print(output)
6. Prueba
vector = [5,2,4,9]
output = 0
for i in vector:
    if vector[0] > vector[i]: #2 y 4 son menores
        output = output + 1 #se suma 1, 2 veces 
print(output) #sera 2 que indicaría la tercera posición en vector.
7. Obtén la complejidad computacional
O(N) porque solo tiene un for.
