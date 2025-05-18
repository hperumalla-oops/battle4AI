import math

# Alpha-Beta Pruning implementation
def minimax(node_index, depth, max_depth, alpha, beta, maximizingPlayer, values):
    if depth == max_depth:
        return values[node_index]

    if maximizingPlayer:
        maxEva = -math.inf
        for i in range(2):  # left and right child
            eva = minimax(node_index * 2 + i, depth + 1, max_depth, alpha, beta, False, values)
            maxEva = max(maxEva, eva)
            alpha = max(alpha, maxEva)
            if beta <= alpha:
                break
        return maxEva
    else:
        minEva = math.inf
        for i in range(2):  # left and right child
            eva = minimax(node_index * 2 + i, depth + 1, max_depth, alpha, beta, True, values)
            minEva = min(minEva, eva)
            beta = min(beta, minEva)
            if beta <= alpha:
                break
        return minEva

#need to be power of 2
values = [30, 1, 6, 5, 1, 2, 10, 20]  

max_depth = int(math.log2(len(values)))

evaluated_value = minimax(0, 0, max_depth, -math.inf, math.inf, True, values)

print("Evaluated Value:", evaluated_value)
