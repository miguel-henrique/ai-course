def encontrar_caminho_labirinto(labirinto, inicio, fim):
    visitados = set()
    caminho = dfs_recursivo(labirinto, inicio, fim, visitados)
    return caminho if caminho is not None else []

def dfs_recursivo(labirinto, atual, fim, visitados):
    if atual == fim:
        return [atual]
    visitados.add(atual)
    for vizinho in labirinto.get(atual, []):
        if vizinho not in visitados:
            resultado = dfs_recursivo(labirinto, vizinho, fim, visitados)
            if resultado is not None:
                return [atual] + resultado
    return None

labirinto_exemplo = {
    'Entrada': ['A', 'B'],
    'A': ['Entrada', 'C'],
    'B': ['Entrada', 'D'],
    'C': ['A', 'Saida'],
    'D': ['B', 'E'],
    'E': ['D', 'F'],
    'F': ['E', 'Saida'],
    'Saida': []
}

print(encontrar_caminho_labirinto(labirinto_exemplo, 'Entrada', 'Saida'))
print(encontrar_caminho_labirinto(labirinto_exemplo, 'A', 'F'))
print(encontrar_caminho_labirinto(labirinto_exemplo, 'B', 'C'))
print(encontrar_caminho_labirinto(labirinto_exemplo, 'Entrada', 'Z'))
