# (Verificação de Anagrama) Receba duas palavras e determine se elas são anagramas (ou seja, possuem as mesmas letras em qualquer ordem).

def anagrama():
    print("Bem-vindo ao Verificador de Anagramas!")
    
    palavra1 = input("Digite a primeira palavra: \n").lower()
    palavra2 = input("Digite a segunda palavra: \n").lower()
    
    if sorted(palavra1) == sorted(palavra2):
        print("São anagramas") 
    else:
        print("Não são anagramas")
anagrama()
    
# sorted organiza os elementos de acordo com a ordem natural, str de A a Z.
    