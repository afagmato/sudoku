def crear_taulell():
    return [[0] * 9 for _ in range(9)]

def mostrar_taulell(taulell):
    for i, fila in enumerate(taulell):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        fila_str = ""
        for j, num in enumerate(fila):
            if j % 3 == 0 and j != 0:
                fila_str += "| "
            fila_str += str(num) if num != 0 else "." 
            fila_str += " "
        print(fila_str)

def es_valid(taulell, fila, col, num):
    # Comprovar fila
    if num in taulell[fila]:
        return False
    
    # Comprovar columna
    if num in [taulell[i][col] for i in range(9)]:
        return False
    
    # Comprovar caixa 3x3
    inici_fila = (fila // 3) * 3
    inici_col = (col // 3) * 3
    for i in range(inici_fila, inici_fila + 3):
        for j in range(inici_col, inici_col + 3):
            if taulell[i][j] == num:
                return False
    
    return True

import random

def omplir_taulell(taulell):
    for fila in range(9):
        for col in range(9):
            if taulell[fila][col] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if es_valid(taulell, fila, col, num):
                        taulell[fila][col] = num
                        if omplir_taulell(taulell):
                            return True
                        taulell[fila][col] = 0
                return False
    return True

def amagar_caselles(taulell, nivell):
    caselles = {"facil": 30, "mitja": 45, "dificil": 55}
    quantes = caselles.get(nivell, 40)
    
    posicions = [(f, c) for f in range(9) for c in range(9)]
    random.shuffle(posicions)
    
    for fila, col in posicions[:quantes]:
        taulell[fila][col] = 0

def jugar(taulell):
    while True:
        mostrar_taulell(taulell)
        
        if all(taulell[f][c] != 0 for f in range(9) for c in range(9)):
            print("\nEnhorabona! Has completat el sudoku!")
            break
        
        try:
            fila = int(input("\nFila (1-9): ")) - 1
            col = int(input("Columna (1-9): ")) - 1
            num = int(input("Número (1-9): "))
        except ValueError:
            print("Introdueix números vàlids.")
            continue
        
        if not (0 <= fila <= 8 and 0 <= col <= 8 and 1 <= num <= 9):
            print("Valors fora de rang.")
            continue
        
        if not es_valid(taulell, fila, col, num):
            print("Moviment no vàlid!")
            continue
        
        taulell[fila][col] = num

if __name__ == "__main__":
    taulell = crear_taulell()
    omplir_taulell(taulell)
    
    nivell = input("Nivell (facil / mitja / dificil): ")
    amagar_caselles(taulell, nivell)
    jugar(taulell)
