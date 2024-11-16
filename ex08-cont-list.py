# preciso fazer um programa que conte quantos números tem em uma lista, para isso posso utilizar o len() para contar o tamanho da lista.
# vamos adicionar algumas funcionalidades extras, como o usuário poder montar sua própria lista, e o usuário poder sair do programa.


# 8. (Contagem de Números em uma Lista) Dada uma lista de números, exiba quantos números ela contém.
print("Bem-vindo a lista 2 em 1! Ela cria e conta os itens da lista.")
nome_lista = input("Digite o nome da sua lista: \n")
print(f"Sua lista é: {nome_lista}")
# confirmar se o nome da lista está correto ou se o usuário quer mudar o nome da lista.
lista_usuario = []  
print(f"Essa é a sua lista atualmente: {lista_usuario} ela possui {len(lista_usuario)} itens.")
print("Para sair basta digitar 'sair' a qualquer momento.")
x = True
while x:
    valor = input("Digite o nome do item para adicionar a lista: \n").lower()
    lista_usuario.append(valor)
    print(lista_usuario)
    
    if valor == "sair":
        lista_usuario.remove("sair") # remove sair antes de imprimir a lista
        print(f"Sua lista tem {len(lista_usuario)} itens.")
        x = False

'''
append é um método embutido na linguagem de programação Python que permite adicionar elementos a uma lista existente um a um.

def contador():
    print("Bem-vindo ao contador de números!")
    x = True
    lista = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]
    while x:
        print(f"A lista tem {len(lista)} números.")
        sair = input("Deseja sair? (s/n) \n").lower()
        if sair == "s":
            print("Obrigado por usar o contador de números!")
            x = False
contador()

'''