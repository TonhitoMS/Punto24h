import sys

from tabulate import tabulate

estados_totais = []
estados_finais = []
simbolos = []
Transicions = []

def ProcesarTexto():
    with open(sys.argv[2], 'r', encoding='utf-8') as mi_fichero:

        estados_totais = mi_fichero.readline().replace('\n', '').split(' ')[1:]
        estados_finais = mi_fichero.readline().replace('\n', '').split(' ')[1:]
        simbolos = mi_fichero.readline().replace('\n', '').split(' ')[1:]

        mi_fichero.readline()

        while True:
            linea = mi_fichero.readline()
            if not linea:
                break
            else:
                Transicions.append(linea.replace('\n', '').split("#"))
    return estados_finais, estados_totais, simbolos

def Clausura(estadosE, Transicions, estados_totais, simbolos):
    estadosRes = []
    #print("Clausura")
    #print(estadosE)
    #print(len(estadosE))
    for j in range(0, len(estadosE)):
        #print("Clausura de")
        #print(estadosE[j])
        e = Transicions[estados_totais.index(estadosE[j])][len(simbolos)]
        #print(e == "  ")
        if not (e == " " or e == "" or e == "  "):
            if e.find(" ") >= 0:
                x = e.split(" ")
                #print(x)
                #print(len(x))
                for k in range(0, len(x)):
                    if not x[k] == "":
                        estadosRes.append(x[k])
                        #print(x[k])
            estadosRes.append(estadosE[j])
            #print(e)
        else:
            #print("Non ten clausura")
            estadosRes.append(estadosE[j])
    estadosRes = list(set(estadosRes))
    estadosRes.sort()
    return estadosRes

def estadoFinal():
    for e in estadoAct:
        if e in estados_finais:
            print("Estado de aceptación: " + e)


estados_finais, estados_totais, simbolos = ProcesarTexto()
print(tabulate(Transicions))
print(estados_finais)
print(estados_totais)
print(simbolos)
#print(len(Transicions[0]))
max = len(Transicions[0])
#print(max)
for j in Transicions:
    del j[max-1]
print(Transicions[0])


estadoAct = []
estadoC = []
estadoAct.append(estados_totais[0])
# estadoAct = ['A', 'B']
# print(estadoAct)
# estadoAct = Clausura(estadoAct, Transicions, estados_totais, simbolos)
# print(estadoAct)
#estadoAct = Clausura(estadoAct, Transicions, estados_totais, simbolos)
while estadoAct != estadoC:
    estadoAct = Clausura(estadoAct, Transicions, estados_totais, simbolos)
    estadoC = Clausura(estadoAct, Transicions, estados_totais, simbolos)

print("Estados Clausura:")
print(estadoAct)

for i in sys.argv[1]:
    print("\n********* Nova entrada *********")
    print("Entrada: " + i)
    v = []
    v.append(i)
    print(estadoAct)
    estadoAux = []
    while estadoAct != estadoC:
        estadoAct = Clausura(estadoAct, Transicions, estados_totais, simbolos)
        estadoC = Clausura(estadoAct, Transicions, estados_totais, simbolos)
    print("Estados Clausura:")
    print(estadoAct)

    for j in range(0, len(estadoAct)):
        #print("j = " + str(j))
        #print("Estado actual " + estadoAct[j])
        e = Transicions[estados_totais.index(estadoAct[j])][simbolos.index(i)]
        if e.find(" ") >= 0:
            #print("varios estados")
            x = e.split(" ")
            #print("Estados: ")
            #print(x)
            for w in range(0, len(x)):
                if not x[w] == "":
                    estadoAux.append(x[w])
        else:
            if not e == "":
                estadoAux.append(e)
        #print("Estado actual")
        #print(estadoAct)
    estadoAct = estadoAux
    #estadoAct = Clausura(estadoAct, Transicions, estados_totais, simbolos)
    print("Estado final da iteracción")
    print(estadoAct)
    estadoFinal()
    print("********************************\n")

estadoAct = Clausura(estadoAct, Transicions, estados_totais, simbolos)
estadoAct = list(set(estadoAct))
estadoAct.sort()

print("Estado final:")
print(estadoAct)
estadoFinal()
print()





























