import sys

from tabulate import tabulate

estados_totais = []
estados_finais = []
simbolos = []
Transiciones = []

def ProcesarTexto():
    with open('machine.txt', 'r', encoding='utf-8') as mi_fichero:

        estados_totais = mi_fichero.readline().replace('\n', '').split(' ')[1:]
        estados_finais = mi_fichero.readline().replace('\n', '').split(' ')[1:]
        simbolos = mi_fichero.readline().replace('\n', '').split(' ')[1:]

        mi_fichero.readline()

        while True:
            linea = mi_fichero.readline()
            if not linea:
                break
            else:
                Transiciones.append(linea.replace('\n', '').split("#"))
    return estados_finais, estados_totais, simbolos

estados_finais, estados_totais, simbolos = ProcesarTexto()
print(tabulate(Transiciones))
print(estados_finais)
print(estados_totais)
print(simbolos)


#tran = Transiciones[0][0]
estadoAct = []
estadoAct.append(estados_totais[0])
for i in sys.argv[1]:
    print()
    print(i)
    v = []
    v.append(i)
    #print(i)
    print(estadoAct)
    estadoAux = []
    #print(simbolos.index(i))
    #print(estados_totais.index(estadoAct[0]))
    for j in range(0, len(estadoAct)):
        print("j = " + str(j))
        print("Estado actual " + estadoAct[j])
        #print(estadoAct)
        #estadoAct[j] = Transiciones[estados_totais.index(estadoAct[j])][simbolos.index(i)]
        e = Transiciones[estados_totais.index(estadoAct[j])][simbolos.index(i)]
        if e.find(" ") >= 0:
            print("varios estados")
            #estadoAct.append(e.split(" "))
            x = e.split(" ")
            print("Estados: ")
            print(x)
            for w in range(0, len(x)):
                if not x[w] == "":
                    estadoAux.append(x[w])
        else:
            if not e == "":
                estadoAux.append(e)
        #print(estadoAct[j])
        #estadoAct.remove(estadoAct[j])
        print("Estado actual")
        print(estadoAct)
    estadoAct = estadoAux
    #for t in range(0, len(tran)):
    #tran[t] = Transiciones[estados_totais.index(tran)][simbolos.index(i)]
    #tran[t] = tran[t].split(" ")
    print("Estado final da iteracción")
    print(estadoAct)
print("\nEstado final:")
print(estadoAct)





























