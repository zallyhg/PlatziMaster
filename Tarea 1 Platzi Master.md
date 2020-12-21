# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema

El problema muestra una situación, donde contamos con números desordenados dentro de una lista, hay un numero el cual nombraremos como a0, este se encuentra al inicio de la lista que actualmente está desordenada, lo que se requiere es ordenar esta lista e identificar la posición de a0 dentro de la lista ya ordenada, cabe mencionar que en este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

2. Define los datos de entrada

Los datos de entrada pueden ser n con valores entre 0 y m

3. Haz tu análisis

Dentro de los datos que tenemos hasta el momento sabemos lo siguiente, que nuestro numero a0 esta al inicio de la lista y que la lista esta desordenada, tenemos que tener en cuenta que lo que se requiere es saber donde queda a0 al final del ordenamiento de la lista, pueden haber varias soluciones, en este caso se pretende utilizar el algoritmo de ordenamiento BubbleSort dado que la metodología que utiliza el mismo puede ser de ayuda para lo requerido dado que este va comparando la lista en pares y se va repitiendo de 1 a 1 hasta que queda totalmente ordenada.
En este caso sabiendo el funcionamiento de este algoritmo, Bubble sort, podemos definir una variable “piloto” que pueda ir contando las iteraciones del índice 0 que es donde se encuentra a0, cada vuelta que haga sabremos donde esta a0 y al final únicamente sumamos todos los movimientos que tuvo para verificar donde quedo a0.

4. Resume tus conclusiones

Utilizaremos una variable que este registrando los movimientos que hay desde el inicio del algoritmo en el índice 0 de la lista que es donde esta a0, al final sumando los movimientos sabremos en que índice de la lista esta a0

5. Elige el algoritmo

El algoritmo de ordenamiento Bubble Sort

6. Prueba

Array = [3,1,6,5,8]

Primer recorrido

	Iteracion #1: Index0 con Index1
		3 < 1 = False, hacemos cambio entre 3 y 1
		Array = [1,3,6,5,8]

	Iteracion #2: Index1 con Index2
		3 < 6 = True, no hacemos ningun cambio 3 y 6
		Array = [1,3,6,5,8]

	Iteracion #3: Index2 con Index3
		6 < 5 = False, hacemos cambio entre 6 y 5
		Array = [1,3,5,6,8]

	Iteracion #4: Index3 con Index4
		6 < 8 = True, no hacemos ningun cambio 5 y 8
		Array = [3,1,6,5,8]

7. Obtén la complejidad computacional

void cambiar_pos(int *n1, int *n2)
{
    int temp = *n1;
    *n1 = *n2;
    *n2 = temp;
}

void bubbleSort(int vector_entrada[], int n)
{
    int i, j;
    for(i=0; i < n-1; i++)
    {
        for(j=0; j < n-i-1; j++)
        {
            //[3,1,6,5,8]
            if(vector_entrada[j]>vector_entrada[j+1])
            cambiar_pos(&vector_entrada[j],&vector_entrada[j+1]);
        }
    }
}

int print_array(int vector_entrada[], int n)
{
    int i;
    for(i=0; i<n-1; i++)
        printf("%d ,", vector_entrada[i]);
    printf("\n fin del ordenamiento");
}

main(int argc, char const *argv[])
{
    int vector_entrada[]={3,1,6,5,8};
    int n = sizeof(vector_entrada)/sizeof(vector_entrada[0]);
    bubbleSort(vector_entrada, n);
    print_array(vector_entrada, n);
    printf("\n");
    return 0;
}