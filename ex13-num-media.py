# preciso fazer um programa que peça uma lista de notas de alunos e que a divide-a pela média, em seguida retornar uma lista com as notas que são maiores do que a média, da pra fazer utilizando um loop for e condicionais if e else.

# 13. (Média com Notas Maiores que a Média) Peça uma lista de notas de alunos e calcule a média. Em seguida, retorne uma lista com as notas que são maiores do que a média.

def media():
    print("Bem vindo ao programa média de notas")
    notas = []
    
    while True:
        nota = input("Digite uma nota ou digite 'pronto' para sair: ").lower()
        if nota == "pronto":
            print(f"Notas maiores que a média: {notas_maiores}")
            break
        else:
            notas.append(float(nota))
            print(f"Suas notas são: {notas}")
        if notas:
            media = sum(notas) / len(notas)
            notas_maiores = [nota for nota in notas if nota > media] 
media()
    