# preciso fazer um programa que converta uma temperatura de graus Celcius para Fahrenheit. Para isso, é só receber a temperatura em graus Celcius e utilizar a fórmula.

# (Conversor de Temperatura) Receba uma temperatura em graus Celsius e convertapara Fahrenheit usando a fórmula: F = C ∗ 1.8 + 32.

print("Bem-vindo ao conversor de temperatura!")
print("Faça a conversão utilizando ponto ao invés de vírgula \n") 

while True:
    celcius = float(input("Digite a temperatura em graus Celcius: \n"))
    r_farenheit = celcius * 1.8 + 32
    print(f"A temperatura em graus Farenheit é: {r_farenheit}")
    
    sair = input("Deseja sair? (s/n) \n")
    if sair == "s":
        print("Obrigado por usar o conversor de temperatura!")
        break
    
# não consegui limitar a quantidade de casas decimais :[ 