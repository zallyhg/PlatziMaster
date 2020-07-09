# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema

    El problema nos pide que que resolvamos en cuál posición quedará
    el elemento a0 una vez la lista se haya ordenado

2. Define los datos de entrada

    Los datos de entrada son:

    N - Cantidad de elementos en el conjunto lista
    M - Valor máximo que pueden tomar los elementos
    a0 - será la etiqueta que llevará el elemento que se encuentre primero en la lista
    pos - varibale que indica la posición del elemento a0, por defecto, al comenzar, pos = 1
    lista[N] - arreglo del conjunto

3. Haz tu análisis

    El problema solicita sólo la posición (pos) en la que quedará el elemento a0, por lo tanto, no será necesario que los demás elementos queden ordenados siempre y cuando tu algoritmo pueda detectar la posición final de a0

    Para esto se usará el siguiente algoritmo

    pos = 1;

    for (int i=0; i < N; i++)
    {
        if (a0 > lista[i])
        {
            pos++;
        }
    }

    return pos;

4. Resume tus conclusiones

    El algoritmo utilizado encuentra la cantidad de elementos que sean menores al valor de a0, lo hace recorriendo todo el conjutno, por ende, no importa si este está ordenado o no, ya que de esta manera podremos saber cuántos elementos quedarán detrás de a0 una vez que el conjunto sea ordenado

5. Elige el algoritmo
6. Prueba
7. Obtén la complejidad computacional