"""
Find the number of states explored before reaching the goal state using the BFS algorithm.

7 2 4        _ 1 2 
5 _ 6   ->   3 4 5
8 3 1        6 7 8
"""

from collection import queue

q = queue(200000)

start = (7,2,4,
         5,0,6,
         8,3,1)

goal = (0,1,2,
        3,4,5,
        6,7,8)

moves = {
    0: [1,3],
    1: [0,2,4],
    2: [1,5],
    3: [0,4,6],
    4: [1,3,5,7],
    5: [2,4,8],
    6: [3,7],
    7: [4,6,8],
    8: [5,7]
}

def bfs(start, goal):
    visited = set()
    explored = 0

    q.push(start)
    visited.add(start)

    while not q.empty():
        state = q.pop()
        explored += 1

        if state == goal:
            return explored

        zero = state.index(0)

        for m in moves[zero]:
            new_state = list(state)
            new_state[zero], new_state[m] = new_state[m], new_state[zero]
            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                q.push(new_state)

    return -1

print(f"Number of states explored in bfs: {bfs(start, goal)}")
