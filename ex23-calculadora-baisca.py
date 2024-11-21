# (Calculadora Básica com Estruturas Condicionais) Peça ao usuário dois números e uma operação (adição, subtração, multiplicação ou divisão) e execute a operação escolhida.

def calculadora_basica():
    print("Bem-vindo à calculadora básica!")
    print("Por favor, insira dois números e escolha uma operação:")

    x = True  # tudo certo só enviar, mas vale a pena tacar no gpt pra confirmar
    
    while x:
        operacao = input("Escolha uma operação (+, -, *, /): ")
        
        num1 = float(input("Digite o primeiro número: \n"))
        num2 = float(input("Digite o segundo número: \n"))
        
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
    
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Erro: Divisão por zero não é permitida.")
                continue
        else:
            print("Operação inválida. Por favor, escolha +, -, *, ou /.")
            continue
        
        print(f"O resultado da operação é: {resultado}")
        
        nova_operacao = input("Deseja fazer outra operação? (s/n) \n").lower()
        if nova_operacao == "n":
            print("Obrigado por usar a calculadora básica!")
            x = False   
        
calculadora_basica()