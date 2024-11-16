# preciso fazer um programa que verifique se o usuário é maior de idade ou não para isso posso utilizar o if e o else.

# (Verificador de Maioridade) Peça a idade do usuário e informe se ele é maior de idade (18 anos ou mais) ou menor de idade.

def maioridade():
    print("Bem vindo ao verificador de maioridade")
    
    x = True
    while x:
        idade = int(input("Por favor insira a sua idade: \n"))
        
        if idade >= 18:
            print("Você é maior de idade")
        else:
            print("Você é menor de idade")
        
        sair = input("Deseja sair? (s/n) \n").lower()
        if sair == "s":
            print("Obrigado por usar o verificador de maioridade")
            x = False
maioridade()