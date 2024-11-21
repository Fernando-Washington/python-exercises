# 21. (Remoção de Elementos Duplicados) Receba uma lista de inteiros e retorne uma nova lista sem elementos duplicados, mantendo a ordem original.

print("Bem vindo ao removedor de Elementos Duplicados")
print("Ao terminar digite 'pronto' para o programa calcular o resultado")
lista_duplicados = []
lista_sem_duplicados = []

def remocao_elementos():
    x = True
    while x:
        num_inteiros = input("Digite uma lista de inteiros com elementos duplicados: \n")
        if num_inteiros.lower() == 'pronto':
            print(lista_sem_duplicados) 
            x = False
        elif num_inteiros:
            lista_duplicados.append(num_inteiros)
        else: 
            print("Insira um valor válido")
            
        for num in lista_duplicados:
            if num not in lista_sem_duplicados:
                lista_sem_duplicados.append(num)
             
remocao_elementos()

'''
for num in lista_duplicados:
            if num not in lista_sem_duplicados:
                lista_sem_duplicados.append(num)
                
# No loop for o (num) que é o index percorre cada elemento dentro da lista e realiza algo, neste caso é uma comparação verificando se o num atual do loop não está na lista, caso ele não esteja irá retornar True e executar a linha subsequente, caso o contrário não, e neste caso a próxima linha adiciona este mesmo num atual do loop para uma nova lista que é a lista_sem_duplicados

'''

    