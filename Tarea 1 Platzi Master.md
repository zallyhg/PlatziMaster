# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema
Tenemos un array N, el primer numero es a0,
necesitamos identificar la posicion de a0 despues de haber ordenado el array


2. Define los datos de entrada
Datos de entrada es el array N


3. Haz tu análisis
N= [5,6,8,3,1,10,4]
a0= 5 N[0]
N arrglado= [1,3,4,5,6,8,10]
a0= N[3]
Se movio 3 posiciones a la derecha, como?
En el array hay 3 numeros menores de 5, es decir 3 numeros que deben estar a la izquierda, las 3 posiciones que se movio a0.


4. Resume tus conclusiones
Necesitamos la posicion de a0,
sabemos que la posicion es la cantidad de numeros menores a a0,
podemos simplemente contar la cantidad de numeros menores a a0 para hallar su posicion final   


5. Elige el algoritmo
funcion buscarPosicion (array){
	for (i=1 hasta que  i<array.lenght){			n
	if (array[0]>array[i]){					1
		contarPosicion ++				1
		}
	}
	return array[contarPosicion]				1
}


6. Prueba
N= [5,6,8,3,1,10,4]
          + +    +
contarPosicion= 3
posicion a0= N[3]
Tenemos 3 numeros menores a 5 en el array


Array ordenado
N= [1,3,4,5,6,8,10]
          +
posicion de a0= N[3]


7. Obtén la complejidad computacional
Complejidad computacional O(n)


