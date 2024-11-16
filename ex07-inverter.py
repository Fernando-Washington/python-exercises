# preciso fazer um programa que inverta uma string para isso posso utilizar

# (Inversor de String) Receba uma palavra e exiba-a invertida (exemplo: "Python-> "nohtyP"). 

def inversor():
    print("Bem-vindo ao inversor de string!")
    
    x = True
    while x:
        print(input("Digite o texto que deseja inverter: \n")[::-1])
        sair = input("Deseja sair? (s/n) \n").lower()
        
        if sair == "s":
            print("Obrigado por usar o inversor de string!")
            
            x = False
inversor()