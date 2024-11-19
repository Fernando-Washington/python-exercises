# 17. (Ordenação de Lista com Números Negativos e Positivos) Dada uma lista de números inteiros que incluem positivos e negativos, ordene-os de forma que os negativos fiquem antes dos positivos, mantendo a ordem original relativa entre eles.

# forma n1
def ordernar_lista():
    lista = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
    lista_negativos = []
    lista_positivos = []
    for i in lista:
        if i < 0:
            lista_negativos.append(i)
        else:
            lista_positivos.append(i)
    lista_negativos.reverse()
    print(lista_negativos + lista_positivos)
        
ordernar_lista()    

# forma n2
def ordernar_lista():
    lista = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
    sorted_lista = sorted(lista)
    print(sorted_lista)
ordernar_lista()

# forma n3
def ordernar_lista():
    lista = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
    lista.sort()
    print(lista)
ordernar_lista()    