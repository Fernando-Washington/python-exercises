def palindromo():
    print("Bem vindo ao verificador de palíndromo!")    
    
    x = True
    while x:
        palavra = input("Digite uma palavra ex: Arara  \n").lower()
        palavra_invertida = palavra[::-1]
        
        if palavra == palavra_invertida:
            print(f"A palavra {palavra} é um palíndromo!")
        else:
            print(f"A palavra {palavra} não é um palíndromo!")
            
        sair = input("Deseja sair? (s/n) \n").lower()
        if sair == "s":
            print("Obrigado por usar o verificador de palíndromo!")
            x = False
        
palindromo()