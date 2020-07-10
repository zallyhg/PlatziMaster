# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema
tenemos una lista desordenada y al primer numero se le conocera como a0, al ordenar la lista tenemos que saber en que posición quedara a0
2. Define los datos de entrada
N -1 de numeros
3. Haz tu análisis
tenemos que ordenar la lista con algun algoritmo de ordenamiento 
se puede usar un for loop para recorre el arreglo y despues un if que compare a0 es menor a un numero y aumentar un contador y al econtrar un numero mayor finalizar restar
4. Resume tus conclusiones
con un for loop es suficiente ya que lo mas importante es saber donde quedara a0 
5. Elige el algoritmo
for loop
6. Prueba

def find_position(arr):

    position = 0
    a = arr[0]

    for number in arr:

        if number < a :
            position += 1

    return position



if __name__ == "__main__":
    
    print(find_position([9,1,5,-10,12]))

7. Obtén la complejidad computacional

seria una complejida O(n)