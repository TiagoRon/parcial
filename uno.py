def imprimir_lista_inversa(lista):
    if lista:
        imprimir_lista_inversa(lista[1:])
        print(lista[0])

mi_lista = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15]
imprimir_lista_inversa(mi_lista)
