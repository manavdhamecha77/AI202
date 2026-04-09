board = [" "]*9

def print_board(b):
    for i in range(0, 9, 3):
        print(b[i], "|", b[i+1], "|", b[i+2])
    print()

def is_winner(b, p):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(b[a]==b[c]==b[d]==p for a,c,d in wins)

def is_full(b):
    return " " not in b

def minimax(b, is_max, depth=0):
    if is_winner(b, "X"): return 1, []
    if is_winner(b, "O"): return -1, []
    if is_full(b): return 0, []

    best = -float("inf") if is_max else float("inf")
    best_tree = []

    for i in range(9):
        if b[i] == " ":
            b[i] = "X" if is_max else "O"
            score, subtree = minimax(b, not is_max, depth+1)
            b[i] = " "

            node = (i, score, subtree)

            if is_max:
                if score > best:
                    best = score
                    best_tree = [node]
                else:
                    best_tree.append(node)
            else:
                if score < best:
                    best = score
                    best_tree = [node]
                else:
                    best_tree.append(node)

    return best, best_tree

def best_move(b):
    best_score = -float("inf")
    move = -1

    for i in range(9):
        if b[i] == " ":
            b[i] = "X"
            score, _ = minimax(b, False)
            b[i] = " "
            if score > best_score:
                best_score = score
                move = i

    return move

def print_tree(tree, depth=0):
    for move, score, subtree in tree:
        print("  "*depth + f"Move:{move} Score:{score}")
        print_tree(subtree, depth+1)


score, tree = minimax(board, True)
print("Best Score:", score)
print("Best Move:", best_move(board))
print("\nSearch Tree:")
print_tree(tree)

def alphabeta(b, is_max, alpha, beta, depth=0):
    if is_winner(b, "X"): return 1, []
    if is_winner(b, "O"): return -1, []
    if is_full(b): return 0, []

    best_tree = []

    if is_max:
        best = -float("inf")
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score, subtree = alphabeta(b, False, alpha, beta, depth+1)
                b[i] = " "

                best = max(best, score)
                alpha = max(alpha, best)

                best_tree.append((i, score, subtree))

                if beta <= alpha:
                    break

        return best, best_tree

    else:
        best = float("inf")
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score, subtree = alphabeta(b, True, alpha, beta, depth+1)
                b[i] = " "

                best = min(best, score)
                beta = min(beta, best)

                best_tree.append((i, score, subtree))

                if beta <= alpha:
                    break

        return best, best_tree


def best_move_ab(b):
    best_score = -float("inf")
    move = -1

    for i in range(9):
        if b[i] == " ":
            b[i] = "X"
            score, _ = alphabeta(b, False, -float("inf"), float("inf"))
            b[i] = " "
            if score > best_score:
                best_score = score
                move = i

    return move



score_ab, tree_ab = alphabeta(board, True, -float("inf"), float("inf"))
print("Best Score (AB):", score_ab)
print("Best Move (AB):", best_move_ab(board))
print("\nPruned Tree:")
print_tree(tree_ab)

minimax_nodes = 0
alphabeta_nodes = 0

def minimax_count(b, is_max):
    global minimax_nodes
    minimax_nodes += 1

    if is_winner(b, "X"): return 1
    if is_winner(b, "O"): return -1
    if is_full(b): return 0

    if is_max:
        best = -float("inf")
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = max(best, minimax_count(b, False))
                b[i] = " "
        return best
    else:
        best = float("inf")
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = min(best, minimax_count(b, True))
                b[i] = " "
        return best

 
def alphabeta_count(b, is_max, alpha, beta):
    global alphabeta_nodes
    alphabeta_nodes += 1

    if is_winner(b, "X"): return 1
    if is_winner(b, "O"): return -1
    if is_full(b): return 0

    if is_max:
        best = -float("inf")
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = max(best, alphabeta_count(b, False, alpha, beta))
                b[i] = " "
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = float("inf")
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = min(best, alphabeta_count(b, True, alpha, beta))
                b[i] = " "
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best


# Compare
minimax_count(board, True)
alphabeta_count(board, True, -float("inf"), float("inf"))

print("\nNodes explored:")
print("Minimax:", minimax_nodes)
print("Alpha-Beta:", alphabeta_nodes)

