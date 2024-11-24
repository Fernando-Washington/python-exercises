# 27. (Contador de Palavras Frequentes) Peça ao usuário um texto longo e exiba as 5 palavras mais frequentes no texto, ignorando maiúsculas e minúsculas

def contador_palavras():
    texto = input("Digite um texto: \n")
    palavras = texto.lower().split()
    palavras_frequentes = {}
    
    for palavra in palavras:
        if palavra in palavras_frequentes:
            palavras_frequentes[palavra] += 1
        else:
            palavras_frequentes[palavra] = 1
    
    palavras_frequentes = sorted(palavras_frequentes.items(), key=lambda x: x[1], reverse=True)
    
    lista_final = palavras_frequentes[:5]
    for palavra, frequencia in lista_final:
        print(f"{palavra}: {frequencia}")
contador_palavras()

# palavras_frequentes = sorted(palavras_frequentes.items(), key=lambda x: x[1], reverse=True)
# aqui estou atribuindo a lista palavras_frequentes a uma lista de tuplas com com .items (que são listas imutáveis) e ordenada com pela frequencia das palavras em labda em ordem decrescente graças ao sorted e reverse=True, depois é só pegar os 5 primeiros elementos da lista com [:5]
# Para usar o lamda primeiro eu passo o argumento x que é a declaração do que eu quero ordenar, e depois a ação que quero que ele faça com o argumento, no caso o x[1] que é a frequencia das palavras, e depois o reverse=True que é para ordenar em ordem decrescente.
    
    
            