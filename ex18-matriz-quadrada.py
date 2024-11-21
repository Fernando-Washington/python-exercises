#(Soma de Diagonais de uma Matriz Quadrada) Receba uma matriz quadrada de inteiros e calcule a soma dos elementos das diagonais principal e secundária.
def soma_matriz():
    print("Bem-vindo ao programa de soma de matrizes!")
    print("Por favor, insira os valores da matriz 2x2 sendo 'a' e 'b' a primeira linha e 'c' e 'd' a segunda linha:")
    
    a = int(input("Digite o valor da matriz do superior esquerdo: \n"))
    b = int(input("Digite o valor da matriz do superior direito: \n"))
    c = int(input("Digite o valor da matriz do inferior esquerdo: \n"))
    d = int(input("Digite o valor da matriz do inferior direito: \n"))
    
    matriz = [
        [a, b],
        [c, d]
    ]
    
    print(f"Sua matriz é: {matriz} \n")

    diagonal_principal = 0
    diagonal_secundaria = 0
    
    for i in range(len(matriz)):
        diagonal_principal +=  matriz[i][i]
        diagonal_secundaria += matriz[i][len(matriz) - i - 1]
        
    print(f" A soma da diagonal principal é: {diagonal_principal}")
    print(f" A soma da diagonal secundaria é: {diagonal_secundaria}")
    
soma_matriz()

# somar o index 0 com 1 e o 1 com 2
# para acessar elementos individuais em uma matriz eu preciso de um i duplo