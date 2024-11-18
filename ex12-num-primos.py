# Preciso fazer um programa que peça um intervalo de números e retorne uma lista com todos os números primos dentro desse mesmo, sabemos que um número primo é aquele que só é divisível por 1 e por ele mesmo.

# (Números Primos em um Intervalo) Receba um intervalo de números do usuário (por exemplo, entre 10 e 50) e retorne uma lista com todos os números primos dentro desse intervalo.

# o resto da divisão tem que ser igual a 0 para ser um número primo

def primos():
    print("Bem-vindo ao contador de números primos!")
    
    x = True
    while x:
        inicio = int(input("Digite o número inicial do intervalo: \n"))
        fim = int(input("Digite o número final do intervalo: \n"))
        
        print("Números primos no intervalo:")
        for num in range(inicio, fim + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(num, end=" ") 
                        
        print("\n")
        sair = input("Deseja sair? (s/n): \n").lower()
        if sair == "s":
            print("Obrigado por usar o contador de números primos!")
            x = False
primos()