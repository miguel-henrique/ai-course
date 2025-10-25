import numpy as np

# --- Constantes (NÃO MODIFICAR) ---
# Usamos True/False para legibilidade
JOGADOR_MAX = True
JOGADOR_MIN = False

#---------------------------------------------------
# SUA IMPLEMENTAÇÃO COMEÇA AQUI
#---------------------------------------------------

def minimax_aditivo(node, is_max_turn):
    """
    Implementa o algoritmo "Minimax Aditivo" de forma recursiva.
    
    Parâmetros:
    - node: O nó atual da árvore. Pode ser um 'int' (terminal) ou 'list' (galho).
    - is_max_turn: True se for o turno do MAX, False se for o turno do MIN.
    
    Retorna:
    - O valor (utilidade) ótimo deste nó, seguindo as regras "Aditivas".
    """
    
    # 1. Caso Base: O nó é terminal?
    # Verifique se 'node' é um 'int'. Se for, retorne seu valor.
    # (Dica: use 'isinstance(node, int)')
    
    # SEU CÓDIGO AQUI
    if isinstance(node, int):
        return node
    
    
    # 2. Caso Recursivo: Turno do MAX
    if is_max_turn == JOGADOR_MAX:
        # MAX quer maximizar o valor.
        # Inicialize o 'melhor_valor' com o menor valor possível ( -infinito )
        # Itere por cada 'filho' na lista 'node'
        #   Chame 'minimax_aditivo' recursivamente para o 'filho'
        #   Lembre-se: o próximo turno será do MIN (JOGADOR_MIN)
        #   Atualize o 'melhor_valor' usando max()
        
        # No final, retorne o 'melhor_valor' + 1 (conforme a regra do MAX)
        
        # SEU CÓDIGO AQUI
        melhor_valor = float('-inf')
        for filho in node:
            valor_filho = minimax_aditivo(filho, JOGADOR_MIN)
            melhor_valor = max(melhor_valor, valor_filho)
        return melhor_valor + 1  # Regra do MAX (+1)

    # 3. Caso Recursivo: Turno do MIN
    else: # is_max_turn == JOGADOR_MIN
        # MIN quer minimizar o valor.
        # Inicialize o 'pior_valor' com o maior valor possível ( +infinito )
        # Itere por cada 'filho' na lista 'node'
        #   Chame 'minimax_aditivo' recursivamente para o 'filho'
        #   Lembre-se: o próximo turno será do MAX (JOGADOR_MAX)
        #   Atualize o 'pior_valor' usando min()
        
        # No final, retorne o 'pior_valor' - 2 (conforme a regra do MIN)
        
        # SEU CÓDIGO AQUI
        pior_valor = float('inf')
        for filho in node:
            valor_filho = minimax_aditivo(filho, JOGADOR_MAX)
            pior_valor = min(pior_valor, valor_filho)
        return pior_valor - 2  # Regra do MIN (-2)

#---------------------------------------------------
# SUA IMPLEMENTAÇÃO TERMINA AQUI
#---------------------------------------------------

# O Coderunner usará esta função para testar seu código.
# Exemplo de árvore:
# tree_exemplo = [ [1, 5], [10, 3] ]
# O nó raiz é MAX, então a chamada inicial seria:
# valor_final = minimax_aditivo(tree_exemplo, JOGADOR_MAX)
#
# Cálculo esperado:
# Filho 1 (MIN): min(1, 5) - 2 = -1
# Filho 2 (MIN): min(10, 3) - 2 = 1
# Raiz (MAX): max(-1, 1) + 1 = 2
#
# print(f"O valor Minimax Aditivo da árvore é: {valor_final}") # Deve imprimir 2