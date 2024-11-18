# Preciso criar um programa que calcule a área de um retangulo e exiba o resultado, utilizando a seguinte fórmula: area = base ∗ altura.

# (Calculadora de Área de Retângulo) Receba a base e a altura de um retângulo e exiba a área dele usando a fórmula: area = base ∗ altura 2 (2) area = base × altura.

def retangulo():
    print("Bem-vindo à calculadora de área de retângulo!")
    
    x = True
    while x:
        base = float(input("Digite a base do retângulo: \n"))
        altura = float(input("Digite a altura do retângulo: \n"))
        area =  (base * altura) / 2

        print(f"A área do retângulo é: {area}m²")
        
        sair = input("Deseja sair? (s/n): \n").lower()
        if sair == "s":
            x = False
retangulo()
