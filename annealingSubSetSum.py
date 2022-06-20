import random as rd
import math
def convBin(arr):
    fState = rd.randint(1,2**len(arr)-1)
    fState = format(fState,'b')
    fState = str(fState).rjust(5,'0')
    arrState = []
    for i in range(len(fState)):
        arrState.append(int(fState[i]))
    return arrState


def valorSoma(arr,cnj):
    soma = 0
    for i in range(0,len(arr)):
        if arr[i] == 1:
            soma += cnj[i]
    return soma

def newState(arrAt,tempAt,tempI):
    size = len(arrAt)
    nb = tempAt * size // tempI
    newState = arrAt.copy()
    for i in range(0,nb):
        pt = rd.randint(0, (size-1))
        newState[pt] = 0 if newState[pt] == 1 else 1
    return newState

def genAgenda(tempAt, size):
    Agenda = []
    for i in range(tempAt,0,-1):
        x = i*size//tempAt
        x = x if x > 0 else 1
        Agenda.append(x)
    Agenda.append(0)
    return Agenda

def simAnnealing(cnj,obj,tempAt):
    n = len(cnj)
    T = genAgenda(tempAt,n)
    result = False
    estadoAtual = convBin(cnj)
    somaAtual = valorSoma(estadoAtual,cnj)
    print(f'Agenda: {T}\nEstado Inicial: {estadoAtual}')
    Tmax= T[0]
    for t in T:
        if somaAtual == obj:
            result = True
        if t == 0:
            break
        estadoProx = newState(estadoAtual,t,Tmax)
        somaProx = valorSoma(estadoProx,cnj)
        print(f'Novo Estado: {estadoProx} - Soma: {somaProx}')
        if somaProx == obj:
            estadoAtual,somaAtual = estadoProx, somaProx
            result = True
            break
        deltaE = somaProx - somaAtual
        if deltaE > 0:
            estadoAtual,somaAtual = estadoProx, somaProx
        else: 
            sort = rd.uniform(0,1)
            if math.exp(deltaE/t)-int(math.exp(deltaE/t)) > sort:
                estadoAtual,somaAtual = estadoProx, somaProx
    if result:
        for i in range(len(estadoAtual)):
            if estadoAtual[i] == 1:
                subSet.append(cnj[i])
        if len(subSet) > 0: print(f'Subconjunto cuja soma seja {obj} encontrado: {subSet}')
        else: print(f'Não foi encontrado subconjunto cuja soma seja {obj}')
    else:
        print(f'Não foi encontrado subconjunto cuja soma seja {obj}')
         


conjunto = [30,40,10,15,10,60,54]
objetivo = 55
subSet = []
simAnnealing(conjunto,objetivo,100)
