# 19. (Contador de Caracteres de uma Frase) Receba uma frase e retorne um dicionário que contém a quantidade de cada caractere (inclusive espaços).

def contador_caracteres():
    print("Bem-vindo ao contador de caracteres!")
    frase = input("Digite uma frase: \n")
    dicionario = {}
    for caractere in frase:
        if caractere in dicionario:
            dicionario[caractere] += 1
        else:
            dicionario[caractere] = 1
    print(f"A frase possui os seguintes caracteres: {dicionario}")
      
contador_caracteres()

