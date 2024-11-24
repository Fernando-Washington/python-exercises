# 28. (Verificador de Sudoku) Dado um tabuleiro de Sudoku (9x9), verifique se ele é válido, ou seja, se cada linha, coluna e subgrade 3x3 contém números únicos de 1 a 9.

# não consegui fazer, mas vou deixar o que eu fiz até agora

def verificador_sudoku():
    valores = 0
    for i in valores:
        if i != 1 or i != 2 or i != 3 or i != 4 or i != 5 or i != 6 or i != 7 or i != 8 or i != 9:
            return False
        else:
            return True
verificador_sudoku()

# o or é um operador lógico que retorna True se pelo menos uma das condições for verdadeira.
    