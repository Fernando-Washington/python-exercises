# preciso criar um programa que peça uma frase e conte quantas palavrás únicas essa frase possui, isso sem considerar maiúsculas e minúsculas.

# (Contador de Palavras Únicas) Peça ao usuário uma frase e, em seguida, conte quantas palavras únicas ela possui (sem considerar maiúsculas e minúsculas).

def palavras_unicas():
    print("Bem-vindo ao contador de palavras únicas!")
    x = True
    while x:
        frase = input("Digite uma frase: \n").lower()
        palavras = frase.split() 
        unicas = set(palavras) 
        if len(unicas) == 1:
            print(f"A frase possui {len(unicas)} palavra única.")
        else:
            print(f"A frase possui {len(unicas)} palavras únicas.")
        
        sair = input("Deseja sair? (s/n): \n").lower()
        if sair == "s":
            print("Obrigado por usar o contador de palavras únicas!")
            x = False
palavras_unicas()
        
        
        
        
        
        
# o slit separa as palavras da frase        
# o set elimina repetições em uma lista