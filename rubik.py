import random
import numpy as np


Right = [[2, 18, 23, 7],[3, 10, 22, 15],[6, 14, 19, 11],[26, 37, 46, 35],[30, 34, 42, 38]]
Left = [[32, 36, 44, 40], [9, 8, 16, 17], [1, 12, 24, 13],[4, 20, 21, 5], [28, 39, 48, 33]]
Up = [[1, 2, 3, 4], [25, 26, 27, 28], [5, 6, 7, 8],[29, 30, 31, 32], [9, 10, 11, 12]]
Down = [[13, 16, 15, 14],[18, 17, 20, 19],[21, 24, 23, 22],[41, 44, 43, 42],[45, 48, 47, 46]]
Front = [[4, 11, 23, 16],[3, 19, 24, 8],[27, 38, 47, 36],[7, 15, 20, 12],[31, 35, 43, 39]]
Back = [[2, 9, 21, 14], [25, 40, 45, 34], [1, 17, 22, 6], [5, 13, 18, 10], [29, 33, 41, 37]]


"""
Esta función toma un movimiento específico representado por un producto de ciclos y un cubo representado por una lista y modifica el cubo para representar la rotación realizada
"""
def apply(move,cube):
    i = 3
    for orbit in move:
        temp1 = cube[orbit[i - 2]]
        temp2 = cube[orbit[i - 1]]
        temp3 = cube[orbit[i]]
        cube[orbit[i - 2]] = cube[orbit[i - 3]]
        cube[orbit[i - 3]] = temp3
        cube[orbit[i - 1]] = temp1
        cube[orbit[i]] = temp2


"""
Recibe una cadena que contiene movimientos del cubo
y una posición del cubo, y ejecuta esos movimientos en el cubo.
Una letra mayúscula es una rotación de la cara en el sentido de las agujas del reloj y una letra minúscula es una rotación de la cara en el sentido contrario a las agujas del reloj


"""
def execute(moves,cube):
    s = ""
    for move in moves:
        if move == 'F':
            apply(Front,cube)
            s += move
        elif move == 'B':
            apply(Back,cube)
            s += move
        elif move == 'R':
            apply(Right,cube)
            s += move
        elif move == 'L':
            apply(Left,cube)
            s += move
        elif move == 'U':
            apply(Up,cube)
            s += move
        elif move == 'D':
            apply(Down,cube)
            s += move
        elif move == 'f':
            for i in range(3):
                apply(Front,cube)
            s += move
        elif move == 'b':
            for i in range(3):
                apply(Back,cube)
            s += move
        elif move == 'r':
            for i in range(3):
                apply(Right,cube)
            s += move
        elif move == 'l':
            for i in range(3):
                apply(Left,cube)
            s += move
        elif move == 'u':
            for i in range(3):
                apply(Up,cube)
            s += move
        elif move == 'd':
            for i in range(3):
                apply(Down,cube)
            s += move
    return s


"""
Las funciones a continuación alinean los cubos en los siguientes índices 1,2,3,4,25,26,27,28
"""
def align25(cube):
    i = cube.index(25)
    move = ["25","u26","uu27","U28","BLU29","RB30","uRB31","lb32", "LU33", "B34", "Ru35", "FUU36", "ru37", "fUU38", "lU39", "b40", "Bru41", "rB42", "FlU43", "Lb44", "BB45", "RRu46", "FFUU47", "LLU48"][i-25]
    return execute(move,cube)


def align26(cube):
    i = cube.index(26)
    move = ["25", "26", "FFDRR27","LLDDRR28","29", "RRdfR30","FR31","LLDfR32", "BBrbb33", "RdfR34", "R35", "LDfR36", "r37", "rdfR38", "FFR39", "lDfR40", "DDfR41", "dfR42", "fR43", "DfR44", "dRR45", "RR46", "DRR47", "DDRR48"][i-25]
    return execute(move,cube)


def align27(cube):
    i = cube.index(27)
    move = ["27", "LLDFF28", "29", "30", "fLLULu31", "LF32", "lDFF33",  "bDDBff34",  "rdRFF35", "F36", "RdrFF37", "f38", "Ulu39", "UUbUU40", "DlF41", "Rfr42", "fuRU43", "lFL44",  "DDFF45", "dFF46", "FF47", "DFF48"][i-27]
    return execute(move,cube)


def align28(cube):
    i = cube.index(28)
    move = ["25", "26", "27", "28", "29", "30", "31", "LLdbLB32", "L33", "RDbLBr34", "fflff35",  "LdbLB36", "BBLBB37", "ufU38", "l39", "lDFlf40", "bLB41", "DbLB42", "Flf43", "dbLB44!!", "UBBu45", "DDLL46" , "dLL47", "LL48"][i-25]
    return execute(move,cube)


def align1(cube):
    i = cube.index(1)
    move = ["1", "RDDrBdb2", "lrDDLR3", "fddFlDL4", "dlDLdlDL5", "RDrdlDL6", "rdRdlDLdBdb7", "LDlddBDb8", "ldLddBdb9", "RDrBdbDlDL10", "rdRBdb11", "fdFDBdb12", "dlDL13", "lDL14", "lDDL15","DlDDL16", "DBdb17", "DDBdb18", "Bddb19", "BDbddldL20", "BdbDlDL21", "RdrDlDDL22", "DRdrDlDDL23", "DDRdrDlDDL24"][i-1]
    return execute(move,cube)


def align2(cube):
    i = cube.index(2)
    move = ["1", "2", "rdRbDDB3", "fbDDFB4", "5", "bDBdbDB6", "FbDfB7", "LbDDBl8", "9", "RdrDRdr10", "rdRDDbdB11", "fdFRdr12", "DbDDB13", "dbDB14", "bDB15","bDDB16", "Rdr17", "DRdr18", "dRDDr19", "RDDr20", "dbDBRDDr21", "bDBRDDr22", "DbDBRDDr23", "DDbDBRDDr24"][i-1]
    return execute(move,cube)


def align3(cube):
    i = cube.index(3)
    move = ["1", "2", "3", "LDlrdR4", "5", "6", "rDRdrDR7", "LrDlR8", "9", "10", "FdfDFdf11", "fDDFFdf12", "ddFDf13", "dFDf14", "FDf15", "rDR16", "FDDf17", "Fdf18", "DFdf19", "DDFdf20", "DfDFFdf21", "DDfDFFdf22", "dfDFFdf23", "fDFFdf24"][i-1]
    return execute(move,cube)


def align4(cube):
    i = cube.index(4)
    move = ["1", "2", "3", "4", "5", "6", "7", "LDlDDfDF8", "9", "10", "11", "fDDFLDDl12", "fDF13", "fDDF14", "dLDl15", "dfDF16", "DfdF17", "dLdl18!!", "Ldl19", "fdF20", "DfDFLDDl21", "DDfDFLDDl22", "dfDFLDDl23", "fDFLDDl24"][i-1]
    return execute(move,cube)


"""
Toma un cubo y resuelve la parte superior usando las funciones de alineación definidas anteriormente
"""
def solvetop(cube):
    sequence  = ''
    sequence += align25(cube)
    sequence += align26(cube)
    sequence += align27(cube)
    sequence += align28(cube)
    sequence += align1(cube)
    sequence += align2(cube)
    sequence += align3(cube)
    sequence += align4(cube)
    return sequence


"""
Toma una representación vectorial de un cubo y un número entero opcional n. A continuación, aplica n movimientos aleatorios al cubo para desordenarlo.
"""
def scramble(cube,n=50):
    possible_moves = "RLUDFBrludfb"
    sequence = ''
    for _ in range(n):
        s = possible_moves[random.randint(0,11)]
        sequence += s
    return execute(sequence,cube)


"""
Esta función traduce una serie de movimientos en 90 grados.
"""
def toprotate(moves):
    translation = str.maketrans("RFLBrflb","FLBRflbr")
    return moves.translate(translation)


"""
Esta función se llama bajo la suposición de que la cara superior del cubo está resuelta. Verifica las piezas en las posiciones 41-44. Si alguna cara numerada entre 33-40 está en una de estas posiciones, la colocará en su ubicación correcta. Saldrá cuando todas las superficies en las posiciones 41-44 tengan números mayores que 40.
"""
def edgesfrombottom(cube):
    result = ""
    middle_sides = [33,34,35,36,37,38,39,40]
    up_right = [33,34,35,36]
    move = ""
    for i in range(41,45):
        s = cube[i]
        if s in middle_sides:
            if ((i-s)%4) == 3:
                execute('d',cube)
                result += 'd'
            elif ((i-s)%4) == 2:
                execute('dd',cube)
                result += 'dd'
            elif ((i-s)%4) == 1:
                execute('D',cube)
                result += 'D'
            if s in up_right:
                move = "drDRDFdf"
            else:
                move = "DLdldfDF"


            for _ in range((s+1)%4):
                move = toprotate(move)
            result += move
            execute(move,cube)
    if len(result) == 0:
        return result
    return result+edgesfrombottom(cube)


"""
Esta función analiza las superficies en las posiciones 33-36. Si una pieza está fuera de lugar
mueve la cara hasta el borde inferior y luego coloca la cara en el lugar correcto
llamando a los bordes desde la función inferior (edgesfrombottom)
"""
def edgesfromsides(cube):
    result = ""
    for i in range(33,37):
        s = cube[i]
        if s != i:
            move = "drDRDFdf"
            for _ in range((i+1)%4):
                move = toprotate(move)
            result += move
            execute(move,cube)
            result += edgesfrombottom(cube)
    return result


"""
Esta función coloca las superficies numeradas 45-48 en la parte inferior del cubo.
Muchos manuales de instrucciones para resolver el cubo llaman a esto "crear una cruz amarilla", ya que normalmente hacen que la cara inferior sea amarilla, y cuando las cuatro aristas inferiores están en la parte inferior, forman la forma de una cruz.
"""
def flipbottomedges(cube):
    bottom_edges = [45,46,47,48]
    num_on_bottom = 0
    result = ""
    for i in bottom_edges:
        if cube[i] in bottom_edges:
            num_on_bottom += 1
    if num_on_bottom == 0:
        move = "FLDldfBRDrdRDrdb"
        result += move
        execute(move,cube)
    elif num_on_bottom == 2:
        while cube[48] < 45 or cube[47] > 44:
            move = "d"
            result += move
            execute(move,cube)
        if cube[45] > 44:
            move = "RDFdfr"
            result += move
            execute(move,cube)
        else:
            move = "FLDldf"
            result += move
            execute(move,cube)
    return result


"""
Esta función alinea los bordes inferiores en la posición correcta.
"""
def positionbottomedges(cube):
    result = ""
    bottom_edges = [45,46,47,48]
    count = 0
    for i in bottom_edges:
        s = cube[i]
        if s == i:
            count += 1
    while count < 2:
        count = 0
        result += 'D'
        execute('D',cube)
        for i in bottom_edges:
            s = cube[i]
            if s == i:
                count += 1
    if count == 2:
        if cube[46] == 46:
            if cube[48] == 48:
                move = 'FDfDFDDfRDrDRDDrD'
                result += move
                execute(move,cube)
            elif cube[45] == 45:
                move = 'LDlDLDDlD'
                move = toprotate(move)
                result += move
                execute(move,cube)
            elif cube[47] == 47:
                move = 'LDlDLDDlD'
                for i in range(2):
                    move = toprotate(move)
                result += move
                execute(move,cube)


        elif cube[45] == 45:
            if cube[47] == 47:
                move = toprotate('FDfDFDDfRDrDRDDrD')
                result += move
                execute(move,cube)
            elif cube[48] == 48:
                move = 'LDlDLDDlD'
                result += move
                execute(move,cube)
        elif cube[47] == 47:
            if cube[48] == 48:
                move = 'LDlDLDDlD'
                for i in range(3):
                    move = toprotate(move)
                result += move
                execute(move,cube)
    return result


"""
Esta función alinea las esquinas inferiores en las posiciones correctas
"""
def positionbottomcorners(cube):
    result = ''
    bottom_corners = [21,22,23,24]
    count = 0
    while count < 4:
        count = 0
        correct = 0
        for i in bottom_corners:
            if (cube[i]-i) % 4 == 0:
                count += 1
                correct = i
        if count == 4:
            return result
        if count  == 0:
            move = 'rDLdRDld'
            result += move
            execute(move,cube)
        if count == 1:
            move = 'rDLdRDld'
            for j in range(correct % 4):
                move = toprotate(move)
            result += move
            execute(move,cube)
    return result


"""
Esta función rota cada esquina del cubo en la orientación correcta
"""
def rotatebottomcorners(cube):
    result = ''
    bottom_corners = [21,22,23,24]
    for i in bottom_corners:
        while cube[21] < 21:
            move = 'buBUbuBU'
            result += move
            execute(move,cube)
        result += 'D'
        execute('D',cube)
    return result


"""
Esta función resuelve un cubo mezclado y devuelve la secuencia de
movimientos utilizados para resolver el cubo
"""
def solvecube(cube):
    result=""
    result+=solvetop(cube)


    result+=edgesfrombottom(cube)


    result+=edgesfromsides(cube)


    result+=flipbottomedges(cube)


    result+=positionbottomedges(cube)


    result+=positionbottomcorners(cube)


    result+=rotatebottomcorners(cube)
    return result


def test(n):
    flag=True
    for i in range(n): #Testea la funcion en n cubos
        cube=list(range(49)) #Inicializa un cubo resuelto
        t=scramble(cube) #Lo mezcla
        t=solvetop(cube) #Resuelve la cara superior
        t=edgesfrombottom(cube) #Desplaza los bordes laterales del fondo
        for position in range(41,45): #Se fija en locaciones 41 a 44
            if cube[position]<41: #Si hay cara lateral
                flag=False #Reporta un problema
                print("Tu función tiene un problema")
        if flag:
                print("Tu función parece estar bien")


def test2(n):
   flag=True
   for i in range(n):                        #Prueba tu función en n cubos
      cube=list(range(49))                   #Inicializa un cubo resuelto
      t=scramble(cube)                       #Mezcla el cubo
      t=solvetop(cube)                       #Resuelve la cara superior del cubo
      t=edgesfrombottom(cube)                #Mueve cualquier borde lateral fuera de la parte inferior.
      t=edgesfromsides(cube)                 #Corrige la posición de los lados laterales.
      if cube[33:41]!=list(range(33,41)):    #Chequea los bordes latelares
            flag=False
            print("Tu función tiene un problema")
            print(cube[33:41])
   if flag:
      print("Tu función parece estar bien.")


def testall(n):
    flag=True
    for i in range(n):                        #Función de prueba en n cubos
        cube=list(range(49))                  #Inicializa un cubo resuelto
        t=scramble(cube)                      #Aletoriza el cubo
        t=solvetop(cube)                      #Resuelve la cara superior del cubo
        t=edgesfrombottom(cube)               #Mueve los bordes laterales del fondo
        t=edgesfromsides(cube)                #Coloca los bordes laterales en los lugares correctos
        t=flipbottomedges(cube)               #Voltea los bordes inferiores hacia abajo
        if cube[1:13]!=list(range(1,13)):     #Pruebas en la cara superior
            flag=False
        if cube[25:41]!=list(range(25,41)):   #Prueba la segunda cara
            flag=False
        if min(cube[45:])<45:                 #Testea los bordes de la cara inferior
            flag=False
    if flag:
        print("Tu codigo parece funcionar.")


if __name__ == '__main__':


    cube = list(range(49))
    scramble(cube)
    print("\nCubo mezclado:\n {}".format(cube))
    solution = solvecube(cube)
    print("\n Cubo resuelto y solución: \n {} \n {}".format(cube,solution))