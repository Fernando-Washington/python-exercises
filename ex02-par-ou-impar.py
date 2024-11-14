# preciso fazer um programa que receba um número inteiro e exiba ao usuário se ele é par ou impar. Sabemos o numero for dividido por 2 e o resto da divisão for igual a 0, o número é par, caso contrário é impar.

# (Verificador de Número Par ou Ímpar) Peça ao usuário um número inteiro e informe se ele é par ou ímpar

print("Bem-vindo ao verificadir de numeros pares e impares!")

while True:
    num = int(input("Digite um número inteiro: \n"))
    if num % 2 == 0:
        print(f"O numero {num} é par")
    else:
        print(f"O numero {num} é impar")
    
    sair = input("Deseja sair? (s/n) \n").lower()
    if sair == "s":
        print("Obrigado por usar o verificador de numeros pares e impares!")
        break