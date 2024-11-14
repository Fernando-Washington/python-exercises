# Preciso realizar um cálculo de méida aritrimetrica entre 3 notas de um aluno e exibila para o usuário, para isso vamos utilizar as operações básicas de soma e divisão.

# (Cálculo de Média Aritmética) Peça três notas de um aluno e calcule a média aritmética delas.

print("Bem-vindo a calculadora de média aritimétrica!")

while True:
    nota_1 = int(input("Digite a primeira nota: \n"))
    nota_2 = int(input("Digite a segunda nota: \n"))
    nota_3 = int(input("Digite a terceira nota: \n"))

    media = round((nota_1 + nota_2 + nota_3) / 3, 2)
    print(f"A média aritimétrica é: {media}")
    
    sair = input("Deseja sair? (s/n) \n").lower()
    if sair == "s":
        print("Obrigado por usar a calculadora!")
        break
    
    
# A função round() recebe 2 argumentos. O primeiro é o número que deseja arredondar, e o segundo é a quantidade de casas decimais que você deseja.    