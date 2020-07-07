#-*- coding: utf-8 -*-

def run(lista_d):
    
    cont = 0
    for i in range(1,len(lista_d)):
        if 59 > lista_d[i]:
            cont+=1
                 
    
    print('El número a0 está en la posición {}'.format(cont))



if __name__ == "__main__":
    lista_d = [59,8,6,10,85,1,105,47,55,23,26,9,205]
    print('Esta es nuestra lista desordenada {}'.format(lista_d))
    print('En este caso nuestro numero a0 va a ser 59')
    run(lista_d)
