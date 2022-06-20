from itertools import count
import random as rd


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


def hillClimb(arr,obj,cnj):
    arrInicial = arr.copy()
    print('Estado Inicial: ',arr)
    result = False
    while True:
        somaAtual = valorSoma(arr,cnj)
        if(somaAtual == obj):
            result = True
            break
        somaVizinho = 0
        for i in range(0,len(arr)):
            arrVizinho = arr.copy()
            arrVizinho[i] = 1 if arrVizinho[i] == 0 else 0
            somaVizinho = valorSoma(arrVizinho,cnj)
            print('Novo Vizinho', arrVizinho,' Soma:',somaVizinho)
            if somaVizinho == obj:
                arr = arrVizinho.copy()
                result = True
                break
            else:
                somaAtual = somaVizinho
                arr = arrVizinho.copy()
        if result:
            break
        if arrVizinho == arrInicial:
            break
    if result:
        for i in range(len(arr)):
            if arr[i] == 1:
                subSet.append(cnj[i])
        if len(subSet) > 0: print(f'Subconjunto cuja soma seja {obj} encontrado: {subSet}')
        else: print(f'Não foi encontrado subconjunto cuja soma seja {obj}')
    else:
        print(f'Não foi encontrado subconjunto cuja soma seja {obj}')


print('TESTE 1')     
conjunto = [3, 34, 4, 12, 5, 2]
objetivo = 9
subSet = []
hillClimb(convBin(conjunto),objetivo,conjunto)
print('#########')
# print('TESTE 2')    
# conjunto2 = [30, 40, 10, 15, 10, 60, 54]
# objetivo2 = 55
# subSet = []
# hillClimb(convBin(conjunto2),objetivo2,conjunto2)
# print('########')  
# print('TESTE 3')  
# conjunto3 = [-7, -3, -2, 5, 8]
# objetivo3 = 0
# subSet = []
# hillClimb(convBin(conjunto3),objetivo3,conjunto3)