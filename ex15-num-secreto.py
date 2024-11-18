from random import randint

def num_secreto():
    print("Beem-vindo ao jogo do número secreto!")
    num_secreto = randint(1, 100)
    
    x = True
    
    while x:
        chute = int(input("Digite um número entre 1 e 100: \n"))
        print(num_secreto)
        
        if chute > num_secreto:
            print("O número secreto é menor que", chute)
        elif chute < num_secreto:
            print("O número secreto é maior que", chute)
        else:
            print(f"Parabéns! Você acertou o número secreto era {num_secreto}!")
            
            sair = input("Deseja sair? (s/n): \n").lower()
            if sair == "s":
                x = False
                print("Obrigado por jogar!")
            else:
                num_secreto = randint(1, 100)
                continue
            
num_secreto()
