def alphaBeta(tree, alpha, beta, isMax):
    if isinstance(tree, int):
        print("Evaluating:", tree)
        return tree

    if isMax:
        bestValue = float("-inf")

        for i, child in enumerate(tree):
            value = alphaBeta(child, alpha, beta, False)
            bestValue = max(bestValue, value)
            alpha = max(alpha, bestValue)

            if alpha >= beta:
                print("Pruning:", tree[i + 1:])
                break

        return bestValue

    else:
        bestValue = float("inf")

        for i, child in enumerate(tree):
            value = alphaBeta(child, alpha, beta, True)
            bestValue = min(bestValue, value)
            beta = min(beta, bestValue)

            if alpha >= beta:
                print("Pruning:", tree[i + 1:])
                break

        return bestValue
gameTree =\
    [
    [[3, 5],[17, 8]],
    [[-2, 5],[-1, 7]]
    ]

result = alphaBeta(gameTree, float("-inf"), float("inf"), True)

print("Final MAX value:", result)