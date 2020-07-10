1.	Nos dan una lista de números de tamaño n, con sus elementos en desorden. Se requiere usar un algoritmo de ordenamiento para ordenar de menor a mayor los elementos de la lista.
2.	Un arreglo de tamaño n con números ordenados al azar.
3.	Tenemos el valor inicial a0 si en la lista es de tamaño 1 la posición de a0 seria 0, entonces se procede a comparar con el numero contiguo y si a0 es mayor que dicho número, se aumentaría un contador que se encargaría de indicar la posición del elemento a0 por el contrario si es menor le restaría una unidad de ese contador indicando que se movió hacia la izquierda.
4.	Dependiendo del algoritmo que se use y con la ayuda de una variable auxiliar podemos saber la posición del elemento a0 a medida que el algoritmo de ordenamiento va cambiándolo de posición.
5.	 PROCEDIMIENTO bubble_sort ( arreglo a[1:n])
iteración ← 0
REPETIR
    Bandera ← FALSO //indicador de finalización del ciclo
    PARA i VARIANDO DE 1 HASTA n - 1 - iteración HACER
        SI a[i] > a[i+1] ENTONCES
            Mover a[i] Y a[i+1]
            Bandera ← VERDADERO
        FIN SI
    FIN PARA
    iteración ← iteración + 1
MIENTRAS QUE Bandera = VERDADERO
6.	  
[8, 1, 6, 5, 2, 4]

[1, 8, 6, 5, 2, 4]

[1, 6, 8, 5, 2, 4]

[1, 6, 5, 8, 2, 4]

[1, 5, 6, 2, 8, 4]

[1, 5, 2, 6, 4, 8] = Bandera = Verdadero

[1, 5, 2, 6, 4, 8]

[1, 2, 5, 6, 4, 8]

[1, 2, 5, 4, 6, 8] = Bandera = Verdadero

[1, 2, 5, 4, 6, 8]
[1, 2, 5, 4, 6, 8]

[1, 2, 4, 5, 6, 8] = Bandera = Falso

7.	En caso optimo:
complejidad Θ(n).
En caso medio y desfavorable:
complejidad Θ(n2)
