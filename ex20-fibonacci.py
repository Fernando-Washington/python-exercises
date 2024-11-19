# 20. (Gerador de Números da Sequência de Fibonacci) Peça ao usuário um número n e gere uma lista com os n primeiros números da sequência de Fibonacci.

# a formula da sequencia de fibonacci é: # f(n) = f(n-1) + f(n-2)

def fibonacci():
    print("Bem vindo ao gerador de números da Sequência de Fibonacci")
    n = int(input("Digite a quantidade de sequências que deseja obter: \n"))
    sequencia = [0, 1]

    for i in range(2, n):
         n_fibonacci = sequencia[-1] + sequencia[-2]
         sequencia.append(n_fibonacci)
    print(f"Os primeiros {n} números da Sequência de Fibonnacci são: {sequencia}")
fibonacci()
    