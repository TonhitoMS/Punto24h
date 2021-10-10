#Antonio Moscoso Sánchez
#TALF Grupo 2

import sys


estados_totais = []
estados_finais = []
simbolos = []
Transicions = []

#función que procesa o ficheiro e almacena en variables os distintos
#compoñentes da definición dun autómata
def ProcesarTexto():
    with open(sys.argv[1], 'r', encoding='utf-8') as mi_fichero:

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

#Método que realiza as transcións coa cadea baleira dun conxunto de estados dado
def Clausura(estadosE, Transicions, estados_totais, simbolos):
    estadosRes = []
    for j in range(0, len(estadosE)):
        e = Transicions[estados_totais.index(estadosE[j])][len(simbolos)]
        if not (e == " " or e == "" or e == "  "):
            if e.find(" ") >= 0:
                x = e.split(" ")
                for k in range(0, len(x)):
                    if not x[k] == "":
                        estadosRes.append(x[k])
            estadosRes.append(estadosE[j])
        else:
            estadosRes.append(estadosE[j])
    estadosRes = list(set(estadosRes))
    estadosRes.sort()
    return estadosRes

#función que comproba se algún estado do conxunto de estados
#é un estado final do autómata
def estadoFinal():
    for e in estadoAct:
        if e in estados_finais:
            print("Estado de aceptación: " + e)


estados_finais, estados_totais, simbolos = ProcesarTexto()
max = len(Transicions[0])
for j in Transicions:
    del j[max-1]

estadoAct = []
estadoC = []
estadoAct.append(estados_totais[0])

#clausura do estado inicial
while estadoAct != estadoC:
    estadoAct = Clausura(estadoAct, Transicions, estados_totais, simbolos)
    estadoC = Clausura(estadoAct, Transicions, estados_totais, simbolos)

print("Estados Clausura:")
print(estadoAct)

#bucle principal que procesa a cadea de entrada e os estados
#nos que se encontra o autómata en cada momento
for i in sys.argv[2]:
    print("\n********* Nova entrada *********")
    print("Entrada: " + i)
    v = []
    v.append(i)
    print(estadoAct)
    estadoAux = []

    for j in range(0, len(estadoAct)):
        e = Transicions[estados_totais.index(estadoAct[j])][simbolos.index(i)]
        if e.find(" ") >= 0:
            x = e.split(" ")
            for w in range(0, len(x)):
                if not x[w] == "":
                    estadoAux.append(x[w])
        else:
            if not e == "":
                estadoAux.append(e)
    estadoAct = estadoAux
    while estadoAct != estadoC:
        estadoAct = Clausura(estadoAct, Transicions, estados_totais, simbolos)
        estadoC = Clausura(estadoAct, Transicions, estados_totais, simbolos)
    print("Estado final da iteracción")
    print(estadoAct)
    estadoFinal()
    print("********************************\n")

estadoAct = list(set(estadoAct))
estadoAct.sort()

print("Estado final:")
print(estadoAct)
estadoFinal()
print()





























