# vou fazer uma calculadora simples, que receba dois números do usuário e exiba a soma deles, para isso será necessário utilizar a função input para receber os números do usuário e a função print para exibir o resultado.

# (Calculadora de Soma Simples) Receba dois números do usuário e exiba a soma deles.

print("Bem-vindo à calculadora de soma simples!")

while True:
    valor1 = int(input("Digite o primeiro valor: \n"))
    valor2 = int(input("Digite o segundo valor: \n"))

    resultado = valor1 + valor2
    print(f"O resultado da soma é: {resultado}")
    
    sair = input("Deseja sair? (s/n) \n").lower()
    if sair == "s":
        print("Obrigado por usar a calculadora!")
        break

# isso ficou bom, antes eu estava fazendo assim até pensar nas novas funcionalidades:

'''valor1 = int(input("Digite o primeiro valor: \n"))
valor2 = int(input("Digite o segundo valor: \n"))

resultado = valor1 + valor2
print(f"O resultado da soma é: {resultado}")'''