# 25. (Filtro de Números Pares em uma Lista) Receba uma lista de inteiros e filtre apenas os números pares.

def filtro_pares():
    print("Bem-vindo ao filtro de números pares!")
    num = input("Por favor, insira uma lista de números inteiros separados por espaço: \n")
    # funciona
    numeros = num.split()
    
    lista_num = []
    pares = []

    lista_num = [int(i) for i in numeros]
    pares = [i for i in lista_num if i % 2 == 0]
    
    print(f"Os números pares são: {pares}")
filtro_pares()

# Não estava conseguindo converter num para int, então utilizei o split para separar os números por exemplo: "1" "2" "3" já que ele divide uma string em uma lista de substrings usando um espaço como delimitador.