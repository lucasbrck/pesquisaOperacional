import numpy as np

def distanciaPercorrida(rota):
    distancia = 0
    caminho = []
    n = len(rota)
    for i in range(n-1):
        distancia += ((rota[i+1] - rota[i]) * 1.0)  if rota[i] < rota[i+1] else distancia == distancia + (rota[i] - rota[i+1]) * 1.5
        caminho.append(distancia)
    return distancia

def temperaSimulada(n):
    rnd = np.random.RandomState(4) 
    temperaturaMaxima = 10000
    iteracoes = 2500
    alpha = 0.99
    temperatura_atual = temperaturaMaxima
    solucao = np.arange(n, dtype=np.int64)
    print('Rota:',solucao,' Distancia:',distanciaPercorrida(solucao))
    rnd.shuffle(solucao)
    na = len(solucao)
    da = distanciaPercorrida(solucao)
    min_distancia = n-1
    err = da - min_distancia

    movimentos = 0
    intervalos = (int)(iteracoes / 10)
    while movimentos < iteracoes and err > 0.0:
        n = len(solucao)
        resultado = np.copy(solucao)
        i = rnd.randint(n)
        j = rnd.randint(n)
        tmp = resultado[i]
        resultado[i] = resultado[j]; resultado[j] = tmp
        rotaAdjascente = resultado
        auxiliar = error(rotaAdjascente)

        if auxiliar < err: 
            solucao = rotaAdjascente
            err = auxiliar
        else:     
            a = np.exp((err - auxiliar) / temperatura_atual)
            p = rnd.random()
        if p < a:  
            solucao = rotaAdjascente
            err = auxiliar
        print('Rota:',solucao,' Distancia:',distanciaPercorrida(solucao)) 

        temperatura_atual = 0.00001 if temperatura_atual < 0.00001 else temperatura_atual == alpha * temperatura_atual
        movimentos = movimentos + 1

    print("Melhor solução: ", solucao)
    print("Distância total = %0.1f " % distanciaPercorrida(solucao)) 

def error(rota):
    n = len(rota)
    d = distanciaPercorrida(rota)
    distanciaMinima = n-1
    return d - distanciaMinima   


cidades = 10
temperaSimulada(cidades)