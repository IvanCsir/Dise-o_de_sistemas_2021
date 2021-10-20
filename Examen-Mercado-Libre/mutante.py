import numpy as np 

matriz = np.array([ ["A","T","G","C","G","A"],
                    ["C","A","G","T","G","C"],
                    ["T","T","A","T","G","T"],
                    ["A","G","A","A","G","G"],
                    ["C","C","C","C","T","A"],
                    ["T","C","A","C","T","G"]])



diag = (np.diag(matriz))
diag1 = (np.diag(matriz, k = 1))
diag2 = (np.diag(matriz, k = 2))
diag_inferior1 = (np.diag(matriz, k = -1))
diag_inferior2 = (np.diag(matriz, k = -2))

secuencia = 0

lista_a = ['A','A','A','A']
lista_t = ['T','T','T','T']
lista_c = ['C','C','C','C']
lista_g = ['G','G','G','G']
def diagonales():
    

    global secuencia
    pos1_principal = list(diag[0:4])
    pos2_principal = list(diag[1:5])
    pos3_principal = list(diag[2:6])
    
    #Verifico las 3 posibilidades que tiene la diagonal principal para cumplir las 4 letras iguales
    if pos1_principal == lista_a or pos1_principal == lista_t or pos1_principal == lista_c or pos1_principal == lista_g:
        secuencia += 1
    elif pos2_principal == lista_a or pos2_principal == lista_t or pos2_principal == lista_c or pos2_principal == lista_g:
        secuencia += 1
    elif pos3_principal == lista_a or pos3_principal == lista_t or pos3_principal == lista_c or pos3_principal == lista_g:
        secuencia += 1
    else:
        secuencia += 0
    
    pos1_diag1 = list(diag1[0:4])
    pos2_diag1 = list(diag1[1:5])

    #Verifico las 2 posibilidades que tiene la diagonal superior1 para cumplir las 4 letras iguales
    if pos1_diag1 == lista_a or pos1_diag1 == lista_t or pos1_diag1 == lista_c or pos1_diag1 == lista_g:
        secuencia += 1
    elif pos2_diag1 == lista_a or pos2_diag1 == lista_t or pos2_diag1 == lista_c or pos2_diag1 == lista_g:
        secuencia += 1
    else:
        secuencia += 0

    pos1_diag2 = list(diag2[0:4])
    #Verifico la única posibilidad que tiene la diagonal principa2l para cumplir las 4 letras iguales
    if pos1_diag2 == lista_a or pos1_diag2 == lista_t or pos1_diag2 == lista_c or pos1_diag2 == lista_g:
        secuencia += 1
    else:
        secuencia += 0
    

    pos1_diag_inferior1 = list(diag_inferior1[0:4])
    pos2_diag_inferior1 = list(diag_inferior1[1:5])

    #Verifico las 2 posibilidades que tiene la diagonal inferior1 para cumplir las 4 letras iguales
    if pos1_diag_inferior1 == lista_a or pos1_diag_inferior1 == lista_t or pos1_diag_inferior1 == lista_c or pos1_diag_inferior1 == lista_g:
        secuencia += 1
    elif pos2_diag_inferior1 == lista_a or pos2_diag_inferior1 == lista_t or pos2_diag_inferior1 == lista_c or pos2_diag_inferior1 == lista_g:
        secuencia += 1
    else:
        secuencia += 0

    pos1_diag_inferior2 = list(diag_inferior2[0:4])
    
    #Verifico la única posibilidad que tiene la diagonal inferior2 para cumplir las 4 letras iguales
    if pos1_diag_inferior2 == lista_a or pos1_diag_inferior2 == lista_t or pos1_diag_inferior2 == lista_c or pos1_diag_inferior2 == lista_g:
        secuencia += 1

    else:
        secuencia += 0


matriz_transpuesta = np.transpose(matriz)
vertical1 = matriz_transpuesta[0]
vertical2 = matriz_transpuesta[1]
vertical3 = matriz_transpuesta[2]
vertical4 = matriz_transpuesta[3]
vertical5 = matriz_transpuesta[4]
vertical6 = matriz_transpuesta[5]

def verticales():
    global secuencia
    pos1_vertical1 = list(vertical1[0:4])
    pos2_vertical1 = list(vertical1[1:5])
    pos3_vertical1 = list(vertical1[2:6])

    if pos1_vertical1 == lista_a or pos1_vertical1 == lista_t or pos1_vertical1 == lista_c or pos1_vertical1 == lista_g:
        secuencia += 1
    elif pos2_vertical1 == lista_a or pos2_vertical1 == lista_t or pos2_vertical1 == lista_c or pos2_vertical1 == lista_g:
        secuencia += 1
    elif pos3_vertical1 == lista_a or pos3_vertical1 == lista_t or pos3_vertical1 == lista_c or pos3_vertical1 == lista_g:
        secuencia += 1
    else:
        secuencia += 0
    
    pos1_vertical2 = list(vertical2[0:4])
    pos2_vertical2 = list(vertical2[1:5])
    pos3_vertical2 = list(vertical2[2:6])

    if pos1_vertical2 == lista_a or pos1_vertical2 == lista_t or pos1_vertical2 == lista_c or pos1_vertical2 == lista_g:
        secuencia += 1
    elif pos2_vertical2 == lista_a or pos2_vertical2 == lista_t or pos2_vertical2 == lista_c or pos2_vertical2 == lista_g:
        secuencia += 1
    elif pos3_vertical2 == lista_a or pos3_vertical2 == lista_t or pos3_vertical2 == lista_c or pos3_vertical2 == lista_g:
        secuencia += 1
    else:
        secuencia += 0

    pos1_vertical3 = list(vertical3[0:4])
    pos2_vertical3 = list(vertical3[1:5])
    pos3_vertical3 = list(vertical3[2:6])

    if pos1_vertical3 == lista_a or pos1_vertical3 == lista_t or pos1_vertical3 == lista_c or pos1_vertical3 == lista_g:
        secuencia += 1
    elif pos2_vertical3 == lista_a or pos2_vertical3 == lista_t or pos2_vertical3 == lista_c or pos2_vertical3 == lista_g:
        secuencia += 1
    elif pos3_vertical3 == lista_a or pos3_vertical3 == lista_t or pos3_vertical3 == lista_c or pos3_vertical3 == lista_g:
        secuencia += 1
    else:
        secuencia += 0

    pos1_vertical4 = list(vertical4[0:4])
    pos2_vertical4 = list(vertical4[1:5])
    pos3_vertical4 = list(vertical4[2:6])

    if pos1_vertical4 == lista_a or pos1_vertical4 == lista_t or pos1_vertical4 == lista_c or pos1_vertical4 == lista_g:
        secuencia += 1
    elif pos2_vertical4 == lista_a or pos2_vertical4 == lista_t or pos2_vertical4 == lista_c or pos2_vertical4 == lista_g:
        secuencia += 1
    elif pos3_vertical4 == lista_a or pos3_vertical4 == lista_t or pos3_vertical4 == lista_c or pos3_vertical4 == lista_g:
        secuencia += 1
    else:
        secuencia += 0

    pos1_vertical5 = list(vertical5[0:4])
    pos2_vertical5 = list(vertical5[1:5])
    pos3_vertical5 = list(vertical5[2:6])

    if pos1_vertical5 == lista_a or pos1_vertical5 == lista_t or pos1_vertical5 == lista_c or pos1_vertical5 == lista_g:
        secuencia += 1
    elif pos2_vertical5 == lista_a or pos2_vertical5 == lista_t or pos2_vertical5 == lista_c or pos2_vertical5 == lista_g:
        secuencia += 1
    elif pos3_vertical5 == lista_a or pos3_vertical5 == lista_t or pos3_vertical5 == lista_c or pos3_vertical5 == lista_g:
        secuencia += 1
    else:
        secuencia += 0
    
    pos1_vertical6 = list(vertical6[0:4])
    pos2_vertical6 = list(vertical6[1:5])
    pos3_vertical6 = list(vertical6[2:6])

    if pos1_vertical6 == lista_a or pos1_vertical6 == lista_t or pos1_vertical6 == lista_c or pos1_vertical6 == lista_g:
        secuencia += 1
    elif pos2_vertical6 == lista_a or pos2_vertical6 == lista_t or pos2_vertical6 == lista_c or pos2_vertical6 == lista_g:
        secuencia += 1
    elif pos3_vertical6 == lista_a or pos3_vertical6 == lista_t or pos3_vertical6 == lista_c or pos3_vertical6 == lista_g:
        secuencia += 1
    else:
        secuencia += 0
    

horizontal1 = list(matriz[0])
horizontal2 = list(matriz[1])
horizontal3 = list(matriz[2])
horizontal4 = list(matriz[3])
horizontal5 = list(matriz[4])
horizontal6 = list(matriz[5])

def horizontales():
    global secuencia
    pos1_horizontal1 = list(horizontal1[0:4])
    pos2_horizontal1 = list(horizontal1[1:5])
    pos3_horizontal1 = list(horizontal1[2:6])

    if pos1_horizontal1 == lista_a or pos1_horizontal1 == lista_t or pos1_horizontal1 == lista_c or pos1_horizontal1 == lista_g:
        secuencia += 1
    elif pos2_horizontal1 == lista_a or pos2_horizontal1 == lista_t or pos2_horizontal1 == lista_c or pos2_horizontal1 == lista_g:
        secuencia += 1
    elif pos3_horizontal1 == lista_a or pos3_horizontal1 == lista_t or pos3_horizontal1 == lista_c or pos3_horizontal1 == lista_g:
        secuencia += 1
    else:
        secuencia += 0

    pos1_horizontal2 = list(horizontal2[0:4])
    pos2_horizontal2 = list(horizontal2[1:5])
    pos3_horizontal2 = list(horizontal2[2:6])

    if pos1_horizontal2 == lista_a or pos1_horizontal2 == lista_t or pos1_horizontal2 == lista_c or pos1_horizontal2 == lista_g:
        secuencia += 1
    elif pos2_horizontal2 == lista_a or pos2_horizontal2 == lista_t or pos2_horizontal2 == lista_c or pos2_horizontal2 == lista_g:
        secuencia += 1
    elif pos3_horizontal2 == lista_a or pos3_horizontal2 == lista_t or pos3_horizontal2 == lista_c or pos3_horizontal2 == lista_g:
        secuencia += 1
    else:
        secuencia += 0

    pos1_horizontal3 = list(horizontal3[0:4])
    pos2_horizontal3 = list(horizontal3[1:5])
    pos3_horizontal3 = list(horizontal3[2:6])

    if pos1_horizontal3 == lista_a or pos1_horizontal3 == lista_t or pos1_horizontal3 == lista_c or pos1_horizontal3 == lista_g:
        secuencia += 1
    elif pos2_horizontal3 == lista_a or pos2_horizontal3 == lista_t or pos2_horizontal3 == lista_c or pos2_horizontal3 == lista_g:
        secuencia += 1
    elif pos3_horizontal3 == lista_a or pos3_horizontal3 == lista_t or pos3_horizontal3 == lista_c or pos3_horizontal3 == lista_g:
        secuencia += 1
    else:
        secuencia += 0

    pos1_horizontal4 = list(horizontal4[0:4])
    pos2_horizontal4 = list(horizontal4[1:5])
    pos3_horizontal4 = list(horizontal4[2:6])

    if pos1_horizontal4 == lista_a or pos1_horizontal4 == lista_t or pos1_horizontal4 == lista_c or pos1_horizontal4 == lista_g:
        secuencia += 1
    elif pos2_horizontal4 == lista_a or pos2_horizontal4 == lista_t or pos2_horizontal4 == lista_c or pos2_horizontal4 == lista_g:
        secuencia += 1
    elif pos3_horizontal4 == lista_a or pos3_horizontal4 == lista_t or pos3_horizontal4 == lista_c or pos3_horizontal4 == lista_g:
        secuencia += 1
    else:
        secuencia += 0

    pos1_horizontal5 = list(horizontal5[0:4])
    pos2_horizontal5 = list(horizontal5[1:5])
    pos3_horizontal5 = list(horizontal5[2:6])

    if pos1_horizontal5 == lista_a or pos1_horizontal5 == lista_t or pos1_horizontal5 == lista_c or pos1_horizontal5 == lista_g:
        secuencia += 1
    elif pos2_horizontal5 == lista_a or pos2_horizontal5 == lista_t or pos2_horizontal5 == lista_c or pos2_horizontal5 == lista_g:
        secuencia += 1
    elif pos3_horizontal5 == lista_a or pos3_horizontal5 == lista_t or pos3_horizontal5 == lista_c or pos3_horizontal5 == lista_g:
        secuencia += 1
    else:
        secuencia += 0

    pos1_horizontal6 = list(horizontal6[0:4])
    pos2_horizontal6 = list(horizontal6[1:5])
    pos3_horizontal6 = list(horizontal6[2:6])

    if pos1_horizontal6 == lista_a or pos1_horizontal6 == lista_t or pos1_horizontal6 == lista_c or pos1_horizontal6 == lista_g:
        secuencia += 1
    elif pos2_horizontal6 == lista_a or pos2_horizontal6 == lista_t or pos2_horizontal6 == lista_c or pos2_horizontal6 == lista_g:
        secuencia += 1
    elif pos3_horizontal6 == lista_a or pos3_horizontal6 == lista_t or pos3_horizontal6 == lista_c or pos3_horizontal6 == lista_g:
        secuencia += 1
    else:
        secuencia += 0

def is_mutant():
    global secuencia
    if secuencia >= 2:
        print("--Es mutante--")
    else:
        print("--Es humano--")

if __name__ == "__main__":
    diagonales()
    verticales()
    horizontales()
    is_mutant()


















