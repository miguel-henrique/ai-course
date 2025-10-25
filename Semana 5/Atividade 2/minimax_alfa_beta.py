import numpy as np

# --- Constantes (NÃO MODIFICAR) ---
JOGADOR_MAX = True
JOGADOR_MIN = False

# --- Função MIN (FORNECIDA - NÃO MODIFICAR) ---
# Esta função implementa a lógica do jogador MIN com Poda Alfa-Beta.
# Você a usará na sua implementação de max_value_alfa_beta.
def min_value_alfa_beta(node, alfa, beta):
    """
    Calcula o valor Minimax com poda para um nó MIN.
    (Função fornecida, não modificar)
    """
    # Caso Base: Terminal
    if isinstance(node, int):
        return node

    v = float('inf')
    # Para cada filho (que será um nó MAX)
    for filho in node:
        # Chama max_value recursivamente
        # É ESSENCIAL que a função max_value_alfa_beta esteja definida
        # para que esta recursão mútua funcione.
        valor_filho = max_value_alfa_beta(filho, alfa, beta) 
        v = min(v, valor_filho)
        
        # Condição de Poda Alfa (MIN poda se v <= alfa)
        if v <= alfa:
            return v # Poda!
            
        # Atualiza Beta
        beta = min(beta, v)
        
    return v

#---------------------------------------------------
# SUA IMPLEMENTAÇÃO COMEÇA AQUI
# Implemente apenas a função max_value_alfa_beta
#---------------------------------------------------

def max_value_alfa_beta(node, alfa, beta):
    """
    Implementa a lógica do jogador MAX com Poda Alfa-Beta.
    
    Parâmetros:
    - node: O nó atual da árvore ('int' ou 'list').
    - alfa: O melhor valor garantido para MAX até agora.
    - beta: O melhor valor garantido para MIN até agora.
    
    Retorna:
    - O valor (utilidade) ótimo deste nó MAX, com poda.
    """
    
    # 1. Caso Base: O nó é terminal?
    # Se 'node' for um 'int', retorne seu valor.
    # (Dica: use isinstance(node, int))
    
    # SEU CÓDIGO AQUI
    if isinstance(node, int):
        return node
    
    
    # 2. Caso Recursivo: Turno do MAX
    # Inicialize v com -infinito
    v = float('-inf')
    
    # SEU CÓDIGO AQUI (inicialização de v)
    
    # Itere por cada 'filho' na lista 'node'
    
    # SEU CÓDIGO AQUI (início do loop for)
    for filho in node:
        
        # Chame a função MIN fornecida recursivamente para o filho.
        # Passe alfa e beta atuais para a chamada recursiva.
        valor_filho = min_value_alfa_beta(filho, alfa, beta)
        
        # SEU CÓDIGO AQUI (chamada recursiva a min_value_alfa_beta)
        
        # Atualize v com o máximo entre v e o valor do filho.
        v = max(v, valor_filho)
        
        # SEU CÓDIGO AQUI (atualização de v)
        
        # IMPLEMENTE A CONDIÇÃO DE PODA BETA AQUI:
        # Se v for maior ou igual a beta, retorne v imediatamente.
        
        # SEU CÓDIGO AQUI (condição if v >= beta)
        if v >= beta:
            return v
            
        # ATUALIZE ALFA AQUI:
        # alfa deve ser o máximo entre o alfa atual e v.
        
        # SEU CÓDIGO AQUI (atualização de alfa)
        alfa = max(alfa, v)
        
    # Retorne o valor final v
    return v
    # SEU CÓDIGO AQUI (retorno final de v)
    #pass # Remova esta linha quando implementar

#---------------------------------------------------
# SUA IMPLEMENTAÇÃO TERMINA AQUI
#---------------------------------------------------

# O Coderunner usará esta função para testar seu código.
# Exemplo de árvore do material da aula:
# tree_exemplo = [ [3, 12, 8], [2, 4, 6], [14, 5, 2] ]
# A chamada inicial seria:
# valor_final = max_value_alfa_beta(tree_exemplo, float('-inf'), float('inf'))
# print(f"O valor Alfa-Beta da árvore é: {valor_final}") # Deve imprimir 3


#---------------------------------------------------
# CASOS DE TESTE
#---------------------------------------------------

# 1. Árvore Clássica de Exemplo (Deve podar alguns nós e retornar 3)
tree_exemplo_classico = [
    [3, 12, 8],      # Galho 1: MIN escolhe 3
    [2, 4, 6],       # Galho 2: MIN escolhe 2
    [14, 5, 2]       # Galho 3: MIN escolheria 2, mas o 14/5/2 deve ser podado
]
print("--- Teste 1: Exemplo Clássico ---")
# MAX começa com alfa = -inf e beta = +inf
valor_final_1 = max_value_alfa_beta(tree_exemplo_classico, float('-inf'), float('inf'))
print(f"Valor Minimax esperado: 3")
print(f"Valor Minimax retornado: {valor_final_1}\n")


# 2. Árvore Simples (Não deve haver poda)
tree_simples = [
    [10, 5],
    [2, 8]
]
# MIN(10, 5) = 5
# MIN(2, 8) = 2
# MAX(5, 2) = 5
print("--- Teste 2: Árvore Simples ---")
valor_final_2 = max_value_alfa_beta(tree_simples, float('-inf'), float('inf'))
print(f"Valor Minimax esperado: 5")
print(f"Valor Minimax retornado: {valor_final_2}\n")


# 3. Árvore com Poda Profunda (Para forçar a poda de um galho inteiro)
tree_poda_profunda = [
    [1, 99],        # MIN escolhe 1. Alfa = 1.
    [10, 20],       # MIN escolhe 10. v=10. beta é atualizado para 10. Alfa=1. Sem poda.
    [0, 100],       # MIN escolhe 0. v=0. Como 0 <= Alfa (1), deve haver poda aqui.
    [30, 40]        # Não deve ser explorado devido à poda.
]
# MIN(Galho 1) = 1
# MIN(Galho 2) = 10
# MIN(Galho 3) = 0.
# MAX(1, 10, 0) = 10.
print("--- Teste 3: Poda de Galho Inteiro ---")
valor_final_3 = max_value_alfa_beta(tree_poda_profunda, float('-inf'), float('inf'))
print(f"Valor Minimax esperado: 10")
print(f"Valor Minimax retornado: {valor_final_3}\n")