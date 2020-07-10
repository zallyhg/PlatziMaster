import UIKit

/*Tienes una lista desordenada con N números distintos los cuales tienen valores entre 0 y M. Llamemos al primer número de esta lista a0 . Debes ordenar los números de la lista y ver en qué posición queda el número a0 . En este problema la primera posición de la lista es la posición 0 y la última es la posición N – 1.*/

//1.Entiende la descripción del problema: -Ordenar la lista y devolver la posicion de a0

//2.Define los datos de entrada: -Un lista desordenada de N numeros distintos.

//3.Haz tu análisis: -Tengo que ordenar y devolver la posicion donde quedaria a0, Tengo que devolver tambien toda la lista ordenada?. El punto de ordenar es devolver la posicion de a0, asi que basta con saber donde estaria a0 en la lista ordenada, No tengo que devolver toda la lista ordenada.

//4.Resume tus conclusiones: Lo importante es devolver la posicion de a0 en una lista ya ordenada, no es necesario ordenar la lista en su totalidad.

//5.Elige el algoritmo
/* variable lista = [0...m]
   constate a0 = lista[0]
   variable posicion = 0
    Para (auxiliar) en (lista) { //1n instrucciones
        si a0 > auxiliar
            posicion = posicion+1 //1 instruccion
    }
    Escribir "a0 se encuentra en la posicion: \(posicion)"
 
 */

/*De esta manera esoty obteninedo la posicion que tendria a0 si ordenara toda la lista, pero sin ordenarla, lo que en realidad hago es comparar el valor de a0 con cada uno de los otros elementos de la lista y obtener el numero de elemetos que son menores al a0, de esa manera yo puedo suponer la posicion que tendria si la lista estuviera ordenada.*/

//6.Prueba
var lista = [4,13,5,18,7,19,12,3,17,1,16,2,20,9,11,8,14,6,15,]
let a0 = lista[0]
var posicion = 0
for aX in lista { //1n
    if a0>aX {
        posicion+=1 //1
    }
}
print("a0 se encuentra en la posicion: \(posicion)") //a0 se encuentra en la posicion: 3

//7.Obtén la complejidad computacional
//Orden(n+1): Orden lineal
