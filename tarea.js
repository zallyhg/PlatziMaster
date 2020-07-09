// 1.- planteamineto del problema: se tiene una lista desordenada de numeros , 
// con diferentes valores que van del 0 al 13, para lo cual se busca ordenarlos con un algoritmo Quicksort
// , para lo cual tenemos en la lista un numero ya conocido el cual es 0.
// 2.- por tanto los datos de entrada, seran una cantidad N de numeros, qiue tienen valor ente 0 - 13, lo cual indica que pueden ser: [0,2,12,11,5,1,6,9,3,10,4,7,8,12,3,2,1,8].
// 3.- se tienen que hacer un comprativo entre numeros determinando cual es mayor a cual y ordenando de mayor a menor, ya que lo que se pide resolver en el problema es que la primera posicion sea a0,
//  a0 por tanto sera siempre el primer numero del array que hagamos 
// entonces se hara el ordenamiento, no importando que haya numeros repetidos.


const ordenarDeMenorAmayor = (a, b) => {
    if (a < b) {
      return -1;
    }
    if (a > b) {
      return 1;
    }
    return 0;
  };
  
  const quickSort = (
    arrayDesordenado,
    ordenamientoAlgoritmo = ordenarDeMenorAmayor
  ) => {

    const ordenarArray = [...arrayDesordenado];
  
    const cambiarDeLugar = (arrayAmover, i, j) => {
      const a = arrayAmover[i];
      arrayAmover[i] = arrayAmover[j];
      arrayAmover[j] = a;
    };
  
    const particion = (arrayDivision, start, end) => {
      const pivote = arrayDivision[end];
      let separarIndice = start;
      for (let j = start; j <= end - 1; j++) {
        const sortValue = ordenamientoAlgoritmo(arrayDivision[j], pivote);
        if (sortValue === -1) {
            cambiarDeLugar(arrayDivision, separarIndice, j);
          separarIndice++;
        }
      }
      cambiarDeLugar(arrayDivision, separarIndice, end);
      return separarIndice;
    };
  

    const recursiveSort = (arraytoSort, start, end) => {
     
      if (start < end) {
        const pivotePosition = particion(arraytoSort, start, end);
        recursiveSort(arraytoSort, start, pivotePosition - 1);
        recursiveSort(arraytoSort, pivotePosition + 1, end);
      }
    };
  
    //ordenar el array
    recursiveSort(ordenarArray, 0, arrayDesordenado.length - 1);
    return ordenarArray;
  };

const listaN = [45,2,12,11,5,1,6,9,3,100,4,7,8,12,3,2,1,8];
const ListNordenada = quickSort(listaN);
// console.log(ListNordenada);
document.getElementById('listaOrdenada').innerHTML = 
`Esta es la lista ordenada: <br> ${ListNordenada.join(', ')}<br> <br>
el resultado de a0 es =${ListNordenada[0]}`;