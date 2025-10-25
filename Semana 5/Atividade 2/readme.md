Otimizando o Minimax com Poda Alfa-Beta
O algoritmo Minimax explora toda a árvore de jogo, o que é ineficiente ($O(b^m)$). A Poda Alfa-Beta é uma otimização crucial que "poda" (não explora) ramos da árvore que garantidamente não influenciarão a decisão final, sem alterar o resultado. Isso pode reduzir drasticamente o tempo de busca, no melhor caso para $O(b^{m/2})$.

A poda funciona mantendo dois valores durante a busca:

Alfa ($\alpha$): O melhor valor (máximo) garantido para o jogador MAX até agora no caminho atual. Inicializado com $-\infty$.
Beta ($\beta$): O melhor valor (mínimo) garantido para o jogador MIN até agora no caminho atual. Inicializado com $+\infty$.
Problema Alvo: Implementando a Lógica de MAX com Poda
Sua tarefa é implementar apenas a função max_value_alfa_beta(node, alfa, beta). Esta função representa a lógica do jogador MAX ao decidir seu movimento, incorporando a Poda Alfa-Beta.

A função min_value_alfa_beta (lógica do MIN) já está fornecida no template.

Sua função max_value_alfa_beta deve seguir a lógica apresentada no material:

Caso Base: Se o node for um terminal (int), retorne seu valor.
Caso Recursivo (MAX):
Inicialize um valor v = -infinito.
Para cada filho na lista node:
Chame recursivamente min_value_alfa_beta(filho, alfa, beta) para obter o valor do filho (pois o próximo turno é do MIN).
Atualize v = max(v, valor_do_filho).
Implemente a Condição de Poda Beta: Se v >= beta, o jogador MIN (ancestral) nunca escolherá este ramo. Retorne v imediatamente (poda!).
Atualize alfa = max(alfa, v).
Retorne v.
A árvore de jogo usa a mesma representação da atividade anterior: int para terminais, list para galhos. Use float('inf') e float('-inf').

Restrições:

Não utilize nenhuma biblioteca externa (ex: math, random). O numpy está disponível no template, mas não é necessário para esta solução.
AVISO IMPORTANTE: O objetivo desta atividade é avaliar sua capacidade de implementar a lógica de otimização da Poda Alfa-Beta. O uso de Inteligência Artificial Generativa (Gemini, ChatGPT, Copilot, etc.) para escrever o código desta questão é estritamente proibido e acarretará na sua anulação.



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