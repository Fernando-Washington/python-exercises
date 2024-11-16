# preciso fazer um contador de caracteres aonde conte os caracteres de uma palavra levando em consideração espaços em branco. para isso podemos utilizar a propriedade len()

# (Contador de Caracteres em uma Palavra) Solicite uma palavra do usuário e exiba quantos caracteres ela possui.
def contador():
    print("Bem vindo ao contador de caracteres!")

    x = True
    while x:
        caractere = input("Digite seu texto para descobrir o número de caracteres: \n")
        print(f"O texto possui {len(caractere)} caracteres")
        sair = input("Deseja sair? (s/n): \n").lower()
        if sair == "s":
            print("Obrigado por usar o contador de caracteres!")
            x = False
contador()
            