"""
    Reto de Julián Santos
    email: ingjuliansantos@gmail.com

"""

def list_input(number_quantity,number_lower_limit, number_upper_limit):
    numbers_list = []

    for i in range(number_quantity):
        mask = True
        while mask:
            number = float(input(f'Ingrese el numero {i} de la lista: '))  

            mask = (number<number_lower_limit) or (number>number_upper_limit)

            if mask:
                print(f'El numero debe ser entre {number_lower_limit} y {number_upper_limit}')
            
        numbers_list.append(number)

    return numbers_list

def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        
        # llamada recursiva en cada mitad
        merge_sort(izquierda)
        merge_sort(derecha)

        # iteradores
        i = 0
        j = 0
        # iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista    

def binary_search(lista, comienzo, final, objetivo):
    
    if comienzo > final:
        return False, -1

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True, medio
    elif lista[medio] < objetivo:
        return binary_search(lista, medio + 1, final, objetivo)
    else:
        return binary_search(lista, comienzo, medio -1, objetivo)

if __name__ == "__main__":

    M = int(input('Ingrese M: '))
    N = int(input('Ingrese N: '))

    numbers_list = list_input(N, 0, M)

    a0 = numbers_list[0]

    print('\nLista de numeros ingresada:\n')
    print(numbers_list)
    print(f'\nPrimer numero de la lista: {a0}')

    sorted_number_list = merge_sort(numbers_list)
    print('\nLista de numeros organizada:\n')
    print(sorted_number_list)

    found, a0_position = binary_search(sorted_number_list, 0, N-1, a0)

    print(f'\na0 {a0} se encuentra enla lista ordenada en la posicion: {a0_position}\n')


