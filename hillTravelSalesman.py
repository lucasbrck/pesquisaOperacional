import random
import time

def SubidaEncosta(n):
    start = time.time()
    pesos = []
    tempo = {}
    for i in range(n):
        pontos = []
        for j in range(n):
            if j == i:
                pontos.append(0)
            pontos.append(pesos[j][i]) if j < i else pontos.append(random.randint(5, 100))
        pesos.append(pontos)
    pontos = list(range(len(pesos)))
    subida = []
    rotas = []
    vizinhos = []
    caminhoVizinho = []
    distancia = 0
    for i in range(len(pesos)):
        cidade = pontos[random.randint(0, len(pontos) - 1)]
        subida.append(cidade)
        pontos.remove(cidade)
    for i in range(len(subida)):
        distancia = distancia + pesos[subida[i - 1]][subida[i]]
        rotas.append(distancia)
    for i in range(len(subida)):
        for j in range(i + 1, len(subida)):
            vizinho = subida.copy()
            vizinhoPassado = vizinho.copy()
            caminhoVizinho.append(vizinhoPassado)
            vizinho[i] = subida[j]
            vizinho[j] = subida[i]
            vizinhos.append(vizinho)
    vizinhoEscolhido, vizinhoDistancia = melhorSubida(pesos, vizinhos, subida, start, rotas, pontos)

def distanciasPercorridas(pesos, subida):
    distancia = 0
    for i in range(len(subida)):
        distancia += pesos[subida[i - 1]][subida[i]]
    return distancia

def melhorSubida(pesos, vizinhos, subida, start, rotas, pontos):
    rota = distanciasPercorridas(pesos, vizinhos[0])
    vizinhoEscolgido = vizinhos[0]
    for vizinho in vizinhos:
        atual = distanciasPercorridas(pesos, vizinho)
        if atual < rota:
            vizinhoEscolgido = vizinho
            rota = atual
    print("Pesos:", pesos)
    print("Subida:", subida)
    print("Vizinhos:", vizinhos)
    print("Melhor caminho:", vizinhoEscolgido)
    print("Melhor valor da rota: ", rota)
    end = time.time()
    print("Tempo de execução: ", end - start)
    return vizinhoEscolgido, rota

SubidaEncosta(10)