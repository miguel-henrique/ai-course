from collections import deque

def encontrar_caminho_mais_curto(mapa, inicio, destino):
    if inicio == destino:
        return [inicio]
    visitados = set([inicio])
    pais = {}
    fila = deque([inicio])
    while fila:
        atual = fila.popleft()
        for vizinho in mapa.get(atual, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                pais[vizinho] = atual
                if vizinho == destino:
                    caminho = [destino]
                    while caminho[-1] != inicio:
                        caminho.append(pais[caminho[-1]])
                    caminho.reverse()
                    return caminho
                fila.append(vizinho)
    return []

mapa_exemplo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}

print(encontrar_caminho_mais_curto(mapa_exemplo, 'A', 'G'))
