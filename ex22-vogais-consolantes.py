# 22. (Contagem de Vogais e Consoantes) Peça ao usuário uma frase e conte o número devogais e consoantes. Ignore espaços e caracteres especiais.

def cont_vogais_consoantes():
    print("Bem vindo ao contador de vogais e consoantes")
    frase = input("Digite sua frase:").lower()
    vogais = "aeiou"
    num_vogais = 0
    num_consoantes = 0
    for letra in frase:
        if letra.isalpha():
            if letra in vogais:
                num_vogais += 1
            else:
                num_consoantes += 1
    print(f"A sua frase possui: {num_vogais} vogais e {num_consoantes} consoantes")
cont_vogais_consoantes()

# isalpha() faz com que apenas letras sejam consideradas
  
            
    
