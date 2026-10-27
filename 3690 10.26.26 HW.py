def minimax(depth, nodeIndex, isMax, scores, maxDepth):
    if depth == maxDepth:
        return scores[nodeIndex]
    if isMax:
        left = minimax(depth+1, nodeIndex*2, False, scores, maxDepth)
        right = minimax(depth+1, nodeIndex*2+1, False, scores, maxDepth)
        return max(left, right)
    else:
        left = minimax(depth+1, nodeIndex*2, True, scores, maxDepth)
        right = minimax(depth+1, nodeIndex*2+1, True, scores, maxDepth)
        return min(left, right)

scores = [3, 5, 14, 8, -2, 5, -1, 7]
maxDepth = 3

result = minimax(0, 0, True, scores, maxDepth)
print("The optimal value is:", result)
