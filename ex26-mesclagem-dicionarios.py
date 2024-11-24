# 26. (Mesclagem de Dois Dicionários) Dado dois dicionários, mescle-os em um terceiro. Caso eles tenham chaves em comum, some os valores das chaves correspondentes.

def estoque_lojas():
    
    loja1 = {'Arroz': 10, 'Feijão': 5, 'Macarrão': 8, 'Leite': 12}
    loja2 = {'Arroz': 5, 'Feijão': 3, 'Macarrão': 2, 'Carne': 3}
    estoque = {}
    
    for chave, valor in loja1.items():
        estoque[chave] = valor
    for item, quantidade in loja2.items():
        if item in estoque:
            estoque[item] += quantidade
        else:
            estoque[item] = quantidade
            
    print(f"O estoque combinado entre as lojas é: ")    
   
    for item, quantidade in estoque.items():
        print(f"{item}: {quantidade}")
estoque_lojas() 
    
        

    