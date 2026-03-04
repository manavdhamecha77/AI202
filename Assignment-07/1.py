import random
import math

N = 8


class Node:
    def __init__(self, board):
        self.board = board[:]
        self.h = heuristic(board)


def heuristic(board):
    attacks = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j]:
                attacks += 1
            if abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks


def random_board():
    return [random.randint(0, 7) for i in range(N)]


def neighbors(board):
    neigh = []
    for r in range(N):
        for c in range(N):
            if board[r] != c:
                new_board = board[:]
                new_board[r] = c
                neigh.append(new_board)
    return neigh


def steepest_ascent(start):
    current = Node(start)
    steps = 0

    while True:
        if current.h == 0:
            return current, steps, True

        neigh = neighbors(current.board)
        best = current

        for b in neigh:
            n = Node(b)
            if n.h < best.h:
                best = n

        if best.h >= current.h:
            return current, steps, False

        current = best
        steps += 1


def first_choice(start):
    current = Node(start)
    steps = 0

    while True:
        if current.h == 0:
            return current, steps, True

        neigh = neighbors(current.board)
        random.shuffle(neigh)

        improved = False
        for b in neigh:
            n = Node(b)
            if n.h < current.h:
                current = n
                steps += 1
                improved = True
                break

        if not improved:
            return current, steps, False


def random_restart():
    total_steps = 0
    restarts = 0

    while True:
        start = random_board()
        result, steps, solved = steepest_ascent(start)
        total_steps += steps
        restarts += 1
        if solved:
            return result, total_steps, True, restarts


def simulated_annealing(start):
    current = Node(start)
    T = 100
    steps = 0

    while T > 0.01:
        if current.h == 0:
            return current, steps, True

        neigh = neighbors(current.board)
        next_node = Node(random.choice(neigh))

        delta = current.h - next_node.h

        if delta > 0:
            current = next_node
        else:
            prob = math.exp(delta / T)
            if random.random() < prob:
                current = next_node

        T *= 0.95
        steps += 1

    return current, steps, False


def summarize(name, data):
    solved = sum(1 for r in data if r[3])
    avg_steps = sum(r[2] for r in data) / len(data)
    avg_final_h = sum(r[1] for r in data) / len(data)

    print(name)
    print("Solved:", solved, "/ 50")
    print("Average steps:", round(avg_steps, 2))
    print("Average final heuristic:", round(avg_final_h, 2))
    print()


def main():

    steepest_results = []
    first_results = []
    anneal_results = []

    local_minima_steepest = 0
    local_minima_first = 0
    local_minima_anneal = 0

    for _ in range(50):

        start = random_board()
        init_h = heuristic(start)

        r1 = steepest_ascent(start)
        steepest_results.append((init_h, r1[0].h, r1[1], r1[2]))
        if r1[0].h != 0 and not r1[2]:
            local_minima_steepest += 1

        r2 = first_choice(start)
        first_results.append((init_h, r2[0].h, r2[1], r2[2]))
        if r2[0].h != 0 and not r2[2]:
            local_minima_first += 1

        r3 = simulated_annealing(start)
        anneal_results.append((init_h, r3[0].h, r3[1], r3[2]))
        if r3[0].h != 0 and not r3[2]:
            local_minima_anneal += 1

    print("Local minima encountered:")
    print("Steepest Ascent:", local_minima_steepest)
    print("First Choice:", local_minima_first)
    print("Simulated Annealing:", local_minima_anneal)
    print()

    summarize("Steepest Ascent", steepest_results)
    summarize("First Choice Hill Climbing", first_results)
    summarize("Simulated Annealing", anneal_results)

    rr = random_restart()
    print("Random Restart")
    print("Solved with total steps:", rr[1])
    print("Number of restarts:", rr[3])


main()