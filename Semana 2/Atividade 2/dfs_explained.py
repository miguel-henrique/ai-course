# Curso: Inteligência Artificial - IFSP
# Semana 2 - Atividade 2: Busca em Profundidade (DFS - Depth-first search)
# ---------------------------------------------------------------
# Objetivo: Encontrar um caminho (qualquer caminho) entre dois pontos em um grafo
# usando o algoritmo de Busca em Profundidade (Depth-First Search - DFS).
# ---------------------------------------------------------------
# Conceito:
# DFS explora o grafo o mais profundamente possível ao longo de cada ramo antes
# de fazer o 'backtracking' (retorno). É como explorar um labirinto: você segue
# um corredor até o fim, e se for um beco sem saída, você volta e tenta outro.
#
# A implementação recursiva simula a pilha de chamadas (LIFO - Last In, First Out)
# característica do DFS, onde o último nó a ser entrado é o primeiro a ser explorado.
# ---------------------------------------------------------------
# Enunciado:
# Imagine que você está programando um robô para encontrar a saída de um labirinto.
# O labirinto é representado como um mapa de salas interconectadas, onde cada sala é um ponto e os corredores são as conexões.
#
# Sua tarefa é implementar uma função que encontre um caminho — qualquer caminho — da entrada até a saída do labirinto.
# O algoritmo de Busca em Profundidade (DFS) é uma ótima estratégia para este problema.
# Ele funciona de maneira similar a como uma pessoa exploraria um labirinto: escolhe um corredor, segue-o até o fim,
# e se não encontrar a saída, volta (backtracking) e tenta o próximo corredor disponível.
#
# Requisitos da Função:
# - Crie uma função principal chamada encontrar_caminho_labirinto.
# - A função receberá três argumentos:
#     labirinto: Um dicionário que representa o mapa de conexões (um grafo).
#     inicio: Uma string com o nome da sala de entrada.
#     fim: Uma string com o nome da sala de saída.
# - A função deve retornar uma lista de strings com a sequência de salas do caminho encontrado.
# - Se não houver nenhum caminho até a saída, a função deve retornar uma lista vazia ([]).

import json # Importando json para prints formatados e visuais

# Variável global (ou poderíamos passar como parâmetro) para controlar o nível de recursão/indentação do print
NIVEL_RECURSAO = 0

def encontrar_caminho_labirinto(labirinto, inicio, fim):
    """
    Função principal que inicia o processo de busca em profundidade (DFS).

    Parâmetros:
    - labirinto: dicionário representando o grafo do labirinto.
    - inicio: sala de entrada.
    - fim: sala de saída.

    Retorna:
    - Lista com o caminho encontrado ou lista vazia se não houver caminho.
    """
    global NIVEL_RECURSAO
    NIVEL_RECURSAO = 0 # Reinicia o contador de recursão
    print("=" * 60)
    print(f"🕵️ INICIANDO BUSCA EM PROFUNDIDADE (DFS) de '{inicio}' para '{fim}'")
    print("-" * 60)

    # -----------------------------------------------------------------------------------------
    # ESTRUTURAS DE DADOS ESSENCIAIS PARA DFS
    # -----------------------------------------------------------------------------------------

    # Conjunto para armazenar as salas já visitadas. Essencial para evitar que o algoritmo
    # entre em loops infinitos em grafos com ciclos. A checagem é O(1) (tempo constante).
    visitados = set()
    print(f"🗺️ Salas Visitadas (set): {visitados} (Vazio no início)")
    print("-" * 60)

    # Inicia a busca recursiva
    caminho = dfs_recursivo(labirinto, inicio, fim, visitados)

    print("\n" + "=" * 60)
    if caminho is not None:
        print(f"🎉 CAMINHO ENCONTRADO: {caminho}")
        print("=" * 60)
        return caminho
    else:
        print(f"❌ Não foi possível encontrar um caminho de '{inicio}' para '{fim}'.")
        print("=" * 60)
        return []

# Função auxiliar recursiva que realiza a busca em profundidade
def dfs_recursivo(labirinto, atual, fim, visitados):
    """
    Função recursiva que explora o labirinto em profundidade (DFS).
    O conceito de Pilha (LIFO) é implementado implicitamente pela Pilha de Chamadas da Recursão.

    Parâmetros:
    - labirinto: grafo representando o labirinto.
    - atual: sala atual sendo explorada.
    - fim: sala de destino.
    - visitados: conjunto de salas já visitadas.

    Retorna:
    - Lista com o caminho encontrado ou None se não houver caminho (ocorre o Backtracking).
    """
    global NIVEL_RECURSAO
    indent = "  " * NIVEL_RECURSAO
    NIVEL_RECURSAO += 1

    print(f"\n{indent}⬇️ RECURSÃO (Profundidade {NIVEL_RECURSAO}): Sala ATUAL: '{atual}'")
    print(f"{indent}   Visitados Atuais: {visitados}")

    # Condição de Parada 1: Saída Encontrada
    if atual == fim:
        NIVEL_RECURSAO -= 1
        print(f"{indent}   ⭐ SAÍDA ENCONTRADA! Retornando o caminho: ['{atual}']")
        return [atual] # Retorna a sala atual, que é o destino

    # Marca a sala atual como visitada ANTES de explorar seus vizinhos
    if atual in visitados:
        # Se for um grafo não-direcionado, este caso não deve ocorrer se a chamada for correta,
        # mas é uma salvaguarda para evitar re-processamento.
        print(f"{indent}   ❌ Sala '{atual}' JÁ VISITADA. Voltando (Backtracking).")
        NIVEL_RECURSAO -= 1
        return None

    visitados.add(atual)  # Marca a sala como visitada

    # Explora cada vizinho da sala atual
    vizinhos = labirinto.get(atual, [])
    print(f"{indent}   Vizinhos de '{atual}': {vizinhos}")

    for vizinho in vizinhos:
        # Verifica se o vizinho ainda não foi visitado
        if vizinho not in visitados:
            print(f"{indent}   ➡️ Indo para VIZINHO: '{vizinho}'")
            # Chamada recursiva: aprofunda a busca no vizinho
            resultado = dfs_recursivo(labirinto, vizinho, fim, visitados)

            # Se a chamada recursiva encontrou um caminho (não retornou None)
            if resultado is not None:
                # Concatena a sala atual no INÍCIO do caminho retornado pelo vizinho
                NIVEL_RECURSAO -= 1
                caminho_completo = [atual] + resultado
                print(f"{indent}   ⤴️ Retorno BEM-SUCEDIDO: Caminho reconstruído: {caminho_completo}")
                return caminho_completo

        else:
            print(f"{indent}   🚫 Vizinho '{vizinho}' JÁ VISITADO. Pulando.")

    # Condição de Parada 2: Backtracking
    # Se o loop terminar sem encontrar o destino, significa que a partir desta sala
    # não há caminho para o destino ou todos os caminhos levam a salas já visitadas.
    NIVEL_RECURSAO -= 1
    print(f"{indent}   ↩️ BACKTRACKING: Nenhum caminho encontrado a partir de '{atual}'. Retornando None.")
    return None  # Indica que não há caminho a partir deste ponto

# -----------------------------
# Dados de Teste
# -----------------------------

# Definindo um labirinto como um grafo
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


"""
Representação Visual do Grafo/Labirinto:

              Entrada
             /       \
            A  -----> B
           / \       / \
          C --\     /   D
         /     \   /     \
        Saida   \|/       E
                 |        |
                 |        F
                 \       /
                  \----- Saida
    (O DFS encontrará o primeiro caminho que aparecer na ordem dos vizinhos,
     que, neste caso, é geralmente via 'A' e 'C').
"""


# Testando a função com diferentes cenários

print("\n" * 2)
print("=" * 60)
print("INÍCIO DOS TESTES DA BUSCA EM PROFUNDIDADE (DFS)")
print("=" * 60)

# TESTE 1: Caminho da Entrada até Saida (esperado: ['Entrada', 'A', 'C', 'Saida'] ou ['Entrada', 'B', 'D', 'E', 'F', 'Saida'])
print("\n" * 3)
print("--- TESTE 1: Entrada -> Saida ---")
caminho1 = encontrar_caminho_labirinto(labirinto_exemplo, 'Entrada', 'Saida')
print(f"RESULTADO FINAL (Entrada -> Saida): {caminho1}")


# TESTE 2: Caminho de B até C (esperado: ['B', 'Entrada', 'A', 'C'])
print("\n" * 3)
print("--- TESTE 2: B -> C ---")
caminho2 = encontrar_caminho_labirinto(labirinto_exemplo, 'B', 'C')
print(f"RESULTADO FINAL (B -> C): {caminho2}")


# TESTE 3: Caminho de Entrada até Z (sala inexistente/inalcançável)
print("\n" * 3)
print("--- TESTE 3: Entrada -> Z (Inexistente) ---")
caminho3 = encontrar_caminho_labirinto(labirinto_exemplo, 'Entrada', 'Z')
print(f"RESULTADO FINAL (Entrada -> Z): {caminho3}")


# TESTE 4: Caminho de A para F (esperado: ['A', 'Entrada', 'B', 'D', 'E', 'F'] )
print("\n" * 3)
print("--- TESTE 4: A -> F ---")
caminho4 = encontrar_caminho_labirinto(labirinto_exemplo, 'A', 'F')
print(f"RESULTADO FINAL (A -> F): {caminho4}")