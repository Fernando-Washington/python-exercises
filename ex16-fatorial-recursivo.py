# preciso fazer um programa que calcule o fatorial de um número usando recursão. recursao é quando uma função chama a si mesma. e um fatoorial é o produto de todos os números inteiros positivos de 1 até um número dado. por exemplo o fatorial de 5 é 5 * 4 * 3 * 2 * 1 = 120.

# 16. (Calculadora de Fatorial Recursiva) Crie uma função recursiva que calcula o fatorial de um número dado pelo usuário.

print("Bem-vindo a calculadora de fatorial!") 
n = int(input("Digite um número para calcular o fatorial: "))
def fatorial(n):  
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(n))

       