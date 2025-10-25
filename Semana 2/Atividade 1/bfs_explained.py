# Curso: Inteligência Artificial - IFSP Pós Graduação
# Semana 2 - Atividade 1: Busca em Largura (BFS - Breadth-first search)
# ---------------------------------------------------------------
# Objetivo: Encontrar o caminho mais curto entre dois pontos em um grafo não ponderado
# usando o algoritmo de Busca em Largura (Breadth-First Search - BFS)
# ---------------------------------------------------------------
# Conceito:
# BFS é um algoritmo que explora todos os nós de um grafo "em camadas":
#   1ª camada: os vizinhos do nó inicial
#   2ª camada: os vizinhos dos vizinhos (não visitados)
#   3ª camada: e assim por diante...
#
# Essa abordagem garante que o primeiro caminho encontrado até o destino
# é o mais curto (em número de arestas).
# ---------------------------------------------------------------
# Enunciado:
# Imagine que você faz parte de uma equipe de logística e precisa planejar a rota mais eficiente entre dois centros de distribuição.
# A rede de rotas é um mapa complexo, onde os centros são os pontos e as estradas são as conexões.
#
# Sua tarefa é criar uma função que encontre o caminho mais curto entre um ponto de partida e um destino.
# Consideramos "o caminho mais curto" como aquele que passa pelo menor número de centros de distribuição intermediários.
#
# O algoritmo de Busca em Largura (BFS) é perfeito para isso, pois ele explora o mapa camada por camada a partir do ponto de início,
# garantindo que o primeiro caminho que ele encontrar até o destino será o mais curto.
#
# Requisitos da Função:
# - Crie uma função chamada encontrar_caminho_mais_curto.
# - A função receberá três argumentos:
#     mapa: Um dicionário que representa o mapa de conexões (um grafo).
#     inicio: Uma string com o nome do local de partida.
#     destino: Uma string com o nome do local final.
# - A função deve retornar uma lista de strings com a sequência de locais no caminho mais curto.
# - Se não for possível chegar ao destino, a função deve retornar uma lista vazia ([]).


from collections import deque
import json # Importando json para prints formatados e visuais


def encontrar_caminho_mais_curto(mapa, inicio, destino):
    """
    Esta função utiliza o algoritmo de Busca em Largura (BFS) para encontrar o caminho mais curto
    entre dois centros de distribuição em um grafo não ponderado (o menor número de conexões).

    Parâmetros:
    - mapa: dicionário representando o grafo (centros e suas conexões).
    - inicio: string representando o centro de partida.
    - destino: string representando o centro de destino.

    Retorna:
    - Lista com o caminho mais curto do 'inicio' ao 'destino'.
    - Lista vazia se não houver caminho possível.
    """

    print("=" * 60)
    print(f"🚀 INICIANDO BUSCA EM LARGURA (BFS) de '{inicio}' para '{destino}'")
    print("-" * 60)

    # Caso especial: se o ponto de partida for igual ao destino
    if inicio == destino:
        print(f"✅ Partida ('{inicio}') é igual ao Destino ('{destino}'). Caminho: [{inicio}]")
        return [inicio]

    # -----------------------------------------------------------------------------------------
    # ESTRUTURAS DE DADOS ESSENCIAIS PARA BFS
    # -----------------------------------------------------------------------------------------

    # Conjunto para armazenar os centros já visitados
    # @@TODO: Entender mais sobre uso de Conjunto e set e funcionamento neste contexto
    # CONCEITO: Um 'set' (conjunto) é uma coleção de itens desordenada, imutável (para seus elementos) e que NÃO permite duplicatas.
    # FUNÇÃO NO BFS: Usamos um 'set' (visitados) para ter O(1) (tempo constante) na checagem se um centro já foi visitado.
    # Isso impede que o algoritmo entre em loops infinitos em grafos com ciclos e garante que cada centro seja processado uma única vez
    # na camada correta (a mais próxima do início).
    visitados = set([inicio])
    print(f"🗺️  Centros Visitados (set): {visitados} (Começa com o 'inicio')")

    # Dicionário para armazenar o "pai" de cada nó visitado, usado para reconstruir o caminho
    # @@TODO: Entender mais sobre dicionário e funcionamento neste contexto
    # CONCEITO: Um 'dicionário' (dict) armazena pares de chave:valor. Acesso e inserção são O(1) (tempo constante).
    # FUNÇÃO NO BFS: O dicionário 'pais' armazena de onde viemos para chegar a um nó. Por exemplo, se 'B' foi visitado a partir de 'A',
    # teremos 'pais['B'] = 'A''. Isso nos permite, ao encontrar o destino, retroceder do destino ao início.
    pais = {}
    print(f"🌳 Relação Pai-Filho (dict): {pais} (Vazio, será preenchido durante a busca)")

    # Fila para controlar os centros a serem visitados (estrutura FIFO - First In, First Out)
    # CONCEITO: 'deque' (Double-Ended Queue) é uma fila eficiente para adicionar/remover elementos no início e fim.
    # FUNÇÃO NO BFS: A Fila garante a exploração por "camadas". O nó adicionado primeiro é explorado primeiro.
    # Isso é o que garante que o primeiro caminho encontrado será o mais curto (em número de passos).
    fila = deque([inicio])
    print(f"➡️  Fila de Exploração (deque): {list(fila)} (Começa com o 'inicio')")
    print("-" * 60)
    # -----------------------------------------------------------------------------------------

    # Loop principal do BFS
    passo = 0
    while fila:
        passo += 1
        print(f"\n===== PASSO {passo}: Explorando a Fila =====")
        print(f"FILA ATUAL: {list(fila)}")

        # Remove o primeiro elemento da fila (FIFO - Explorando a próxima camada)
        atual = fila.popleft()
        print(f"📍 Centro ATUAL explorado (popleft): '{atual}'")
        
        # O .get(atual, []) é uma maneira segura de buscar os vizinhos, retornando uma lista vazia se 'atual' não for uma chave.
        vizinhos_mapa = mapa.get(atual, [])
        print(f"🗺️  Vizinhos de '{atual}': {vizinhos_mapa}")

        # Itera sobre os vizinhos do centro atual
        for vizinho in vizinhos_mapa:
            print(f"  ↪️  Analisando Vizinho: '{vizinho}'")
            
            # Condição chave do BFS: Só visita se ainda não foi visitado
            if vizinho not in visitados:
                
                # Marca o vizinho como visitado
                visitados.add(vizinho)
                print(f"  ✅ '{vizinho}' NÃO VISITADO. Adicionado a 'visitados': {visitados}")

                # Armazena o centro atual como pai do vizinho (Para reconstrução do caminho)
                pais[vizinho] = atual
                print(f"  🔗 Definido PARENTESCO: '{vizinho}' tem pai '{atual}'. Pais atuais: {json.dumps(pais)}")

                # Se encontramos o destino, reconstruímos o caminho
                if vizinho == destino:
                    print(f"\n⭐ DESTINO ENCONTRADO: '{destino}'!")
                    
                    # --- RECONSTRUÇÃO DO CAMINHO ---
                    caminho = [destino]
                    
                    # Usa o dicionário 'pais' para retroceder do destino ao início
                    print(f"⏪ Iniciando Reconstrução do Caminho via 'pais':")
                    while caminho[-1] != inicio:
                        proximo_pai = pais[caminho[-1]]
                        caminho.append(proximo_pai)
                        print(f"   -> Adicionando Pai: '{proximo_pai}'. Caminho Temporário: {caminho}")
                        
                    caminho.reverse()  # Inverte a ordem para mostrar do início ao destino
                    print(f"🎉 Caminho Mais Curto (invertido): {caminho}")
                    print("=" * 60)
                    return caminho

                # Adiciona o vizinho à fila para continuar a busca na próxima "camada"
                fila.append(vizinho)
                print(f"  ➡️  '{vizinho}' adicionado à FILA para próxima camada. Nova Fila: {list(fila)}")
            else:
                print(f"  ❌ '{vizinho}' JÁ VISITADO. Ignorando.")


    # Se o loop terminar e o destino não foi encontrado
    print(f"\n❌ Fila vazia. O destino '{destino}' é inatingível a partir de '{inicio}'.")
    print("=" * 60)
    return []


# -----------------------------
# Dados de Teste
# -----------------------------


# Definindo um mapa de centros de distribuição como um grafo
mapa_exemplo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}


"""
Representação Visual do Grafo:

         A
       /   \
     B ----- C
    / \     /
   D   E -- F -- G
"""


# Testando a função com diferentes cenários

print("\n" * 2)
print("=" * 60)
print("RESULTADOS FINAIS DA BUSCA EM LARGURA (BFS)")
print("=" * 60)

# Caminho de A para G: ['A', 'C', 'F', 'G'] (Passa por C primeiro pois C é um vizinho antes de B ser processado completamente)
print("Caminho de A para G:", encontrar_caminho_mais_curto(mapa_exemplo, 'A', 'G'))

# Caminho de A para D: ['A', 'B', 'D']
#print("Caminho de A para D:", encontrar_caminho_mais_curto(mapa_exemplo, 'A', 'D'))

# Caminho de A para A: ['A']
#print("Caminho de A para A:", encontrar_caminho_mais_curto(mapa_exemplo, 'A', 'A'))

# Caminho de D para G: ['D', 'B', 'E', 'F', 'G']
#print("Caminho de D para G:", encontrar_caminho_mais_curto(mapa_exemplo, 'D', 'G'))

# Caminho de G para A: ['G', 'F', 'C', 'A']
#print("Caminho de G para A:", encontrar_caminho_mais_curto(mapa_exemplo, 'G', 'A'))

# Caminho de A para Z (inexistente): []
#print("Caminho de A para Z (inexistente):", encontrar_caminho_mais_curto(mapa_exemplo, 'A', 'Z'))