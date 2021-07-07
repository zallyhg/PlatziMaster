# Tarea 1

Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.

### Pasos a seguir que debes incluir en tu solución

1. Entiende la descripción del problema
    El problema nos pide que dentro de una lista de n números de m valores saber donde se encuntra a0 (el primer elemento del programa)
2. Define los datos de entrada
    Datos entranada n.. con valor m hasta n - 1
3. Haz tu análisis
    Sabiendo que existen n elementos lo único que tenemos seguro es a0 y que puede y de a0 hasta an, podemos tener un contador de cuantas veces se mueve a0 asi sabremos su posición final, el contaodr inicia en 0 esto quiere decir que a0 está en la posición inicial si se mueve a la derecha el contador se le sumara un enterp y si se mueve a la izquierda se le restara otro entero.
4. Resume tus conclusiones
    En conclusión con una variable auxiliar puede ser x en este caso sabemos en todo momento en que posición se encuentra a0 independientemente cuantas veces cambie de lugar
5. Elige el algoritmo
    1-Ingresamos un array
    2-ordenamos comparando
    3-si 5 se mueve a la derecha sumamos uno a nuestro contador, si se mueve a la izquierda restamos
    4- observamos la posición del contador
6. Prueba
    ejemplo: [5,3,4,2,1]
    contador = 0
    1 iteración [3,5,4,2,1]
    contador = 1

    2 iteración [3,4,5,2,1]
    contador = 2
    
    3 iteración [3,4,2,5,1]
    contador = 3

     1 iteración [3,4,6,1,5]
    contador = 4         

    el programa sigue son sus iteraciones hasta obtener la siguiente salida:

    iteracion n [1,3,4,5,6]
    contador = 3  
7. Obtén la complejidad computacional
    De acuerdo a las laminas de la presentación su comlejidad sería O(N) o sea lineal