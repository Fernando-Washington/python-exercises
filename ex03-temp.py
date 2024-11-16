# preciso fazer um programa que converta uma temperatura de graus Celcius para Fahrenheit. Para isso, é só receber a temperatura em graus Celcius e utilizar a fórmula.

# (Conversor de Temperatura) Receba uma temperatura em graus Celsius e convertapara Fahrenheit usando a fórmula: F = C ∗ 1.8 + 32.
def conversor_temperatura():
    print("Bem-vindo ao conversor de temperatura!")
    print("Faça a conversão utilizando ponto ao invés de vírgula \n") 
    
    x = True # round((nota_1 + nota_2 + nota_3) / 3, 2)
    while x:
        celcius = float(input("Digite a temperatura em graus Celcius: \n"))
        r_farenheit = celcius * 1.8 + 32
        print(f"A temperatura em graus Farenheit é: {r_farenheit}")
        sair = input("Deseja sair? (s/n) \n").lower()
        
        if sair == "s":
            print("Obrigado por usar o conversor de temperatura!")
            x = False
            
conversor_temperatura()

# não consegui limitar a quantidade de casas decimais :[ 