# preciso fazer um programa que receba um numero inteiro e gere e exiba a tabuada dele de 1 a 10. para isso podemos utilizar um laço de repetição. acho melhor o for pois podemos limitar o laço de repetição.

# (Gerador de Tabuada) Receba um número inteiro e exiba a tabuada dele (multiplicações de 1 a 10).
def tabuada():
    print("Bem vindo ao super gerador de tabuada 2.0!")
    
    x = True
    while x:
        num = int(input("Digite um número inteiro: \n"))
        print(f"Tabuada do {num}:")
        
        for i in range(1, 10 + 1):
            print(f"{num} x {i} = {num * i}")  
                      
        sair = input("Deseja sair? (s/n): \n").lower()
        if sair == "s":
            print("Obrigado por usar o super gerador de tabuada 2.0!")
            x = False
tabuada()