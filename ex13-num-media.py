# preciso fazer um programa que peça uma lista de notas de alunos e que a divide-a pela média, em seguida retornar uma lista com as notas que são maiores do que a média, da pra fazer utilizando um loop for e condicionais if e else.

# 13. (Média com Notas Maiores que a Média) Peça uma lista de notas de alunos e calcule a média. Em seguida, retorne uma lista com as notas que são maiores do que a média.

def media():
    print("Bem vindo ao programa média de notas")
    notas = []
    print("Digite as notas uma por vez e digite 'pronto' para realizar o cálculo: ")
    while True:
        lista_nota = input("Insira as notas: \n").lower()
        if lista_nota == "pronto":
            if notas: # 1 ou + elemento = True, 0 elementos = False
                media = sum(notas) / len(notas)
                print(f"Suas notas são: {lista_nota}")
                notas_maiores = [nota for nota in notas if nota > media] 
            print(f"Notas maiores que a média: {notas_maiores}")
            break
        else:
            notas.append(float(lista_nota))
            
        
media()

# sum - soma todos os elementos de uma lista
# len - retorna o tamanho de uma lista
    