# 29. (Remoção de Elementos Duplicados de uma Lista Aninhada) Receba uma lista de listas (uma lista aninhada) com valores duplicados e crie uma nova lista de listas onde cada sublista contenha apenas valores únicos.

def remocao_duplicados(lista_aninhada):
    resultado = []  
    for sublista in lista_aninhada:
        sublista_sem_duplicados = list(set(sublista))
        resultado.append(sublista_sem_duplicados)
    return resultado
    
lista_aninhada = [[11, 12, 12, 11, 13, 15, 13], [1, 1, 2, 2, 3, 3, 4, 5]]
resultado = remocao_duplicados(lista_aninhada)
print(resultado)

    