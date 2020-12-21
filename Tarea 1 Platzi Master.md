# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema

El problema nos esta indicando que se va a tener un arreglo al cual le vamos a ingresar hasta un total de M numeros, que van a irse ordenando conforme sean ingresados. El primer numero sera a0 y sera nuestro dato relevante, al cual le hallaremos la posicion luego de la entrada de todos los datos del arreglo.

2. Define los datos de entrada

Los datos de entrada seran cada uno de los valores de las posiciones del arreglo.

3. Haz tu análisis

El primer dato en ingresar al arreglo, lo llamaremos a0. En el momento en que este dato es ingresado nuestro objetivo sera llevar la cuenta de la posicion en que se encuentra en cada instante, ya que esto al final nos daria su posicion final.

4. Resume tus conclusiones

Para dar con la posicion final de a0 es necesario marcar el numero de veces que es movido en el arreglo.

5. Elige el algoritmo

Para este problema podemos implementar un algoritmo que valide cada dato que entra al arreglo, que nos indique si a0 debe trasladarse o si ese valor debe ser ingresado a la derecha de este. En este caso los numeros los ordenaremos de mayor a menor por lo tanto si el dato nuevo ingresado es mayor a nuestra constante a0 entonces a0 sera trasladado a la derecha para dar entrada al nuevo ingreso, de lo contrario la nueva informacion digitada sera situada a la derecha de este.

6. Prueba

Para este problema implementamos un ordenamiento tipo Bubble Sort en Python que nos ayuda a ordenar el arreglo a medida que ingresamos datos al arreglo:

def sort(arr):
    if (len(arr) > 1):
        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1):
                if(arr[j] > arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":
    arr = []

    for i in range(10):
        arr.append(input('Ingrese un valor: '))
        if (i == 0):
            a0 = arr[i]
        sort(arr)
    
    print('El valor a0 quedo en la posicion: ', format(arr.index(a0)))

Al final obtenemos el indice del dato ya que guardamos inicialmente su valor.

7. Obtén la complejidad computacional

Este algoritmo tiene una complejidad computacional del tipo O(n^3).
