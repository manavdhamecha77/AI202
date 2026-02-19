TOTAL_G = 3
TOTAL_B = 3

# Node format (G,B,Boat)
# Boat Left = 0
# Boat Right = 1

# build state space
states = []
index_map = {}
k = 0
for gl in range(4):
    for bl in range(4):
        for boat in range(2):
            states.append((gl, bl, boat))
            index_map[(gl, bl, boat)] = k
            k += 1

N = len(states)

def valid(gl, bl):
    gr = TOTAL_G - gl
    br = TOTAL_B - bl

    if gl < 0 or bl < 0 or gr < 0 or br < 0:
        return False

    if gl > 0 and bl > gl:
        return False
    if gr > 0 and br > gr:
        return False

    return True


# adjacency matrix
adj = [[0]*N for i in range(N)]

# possible moves
moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

for i in range(N):
    gl, bl, boat = states[i]

    if not valid(gl, bl):
        continue

    for dg, db in moves:
        if boat == 0:
            ng, nb, nbp = gl-dg, bl-db, 1
        else:
            ng, nb, nbp = gl+dg, bl+db, 0

        if valid(ng, nb) and (ng,nb,nbp) in index_map:
            j = index_map[(ng,nb,nbp)]
            adj[i][j] = 1


class Node:
    def __init__(self, state, parent, depth):
        self.state = state
        self.parent = parent
        self.depth = depth


def depth_limited_search(start, goal, limit):

    frontier = [None]*1000
    top = -1
    explored = 0

    top += 1
    frontier[top] = Node(start, None, 0)

    result = "failure"

    while top >= 0:

        node = frontier[top]
        top -= 1
        explored += 1

        if node.state == goal:
            return node, explored

        if node.depth >= limit:
            result = "cutoff"
        else:
            for j in range(N):

                if adj[node.state][j] == 1:

                    temp = node
                    cycle = False
                    while temp:
                        if temp.state == j:
                            cycle = True
                            break
                        temp = temp.parent

                    if not cycle:
                        child = Node(j, node, node.depth+1)
                        top += 1
                        frontier[top] = child

    return result, explored


def iterative_deepening_search(start, goal):
    depth = 0
    total_explored = 0

    while True:

        result, explored = depth_limited_search(start, goal, depth)
        total_explored += explored

        if result != "cutoff":
            return result, total_explored, depth

        depth += 1


def print_path(node):
    path = []
    while node:
        path.append(states[node.state])
        node = node.parent

    path.reverse()

    for p in path:
        print(p)


start = index_map[(3,3,0)]
goal = index_map[(0,0,1)]

print("Depth Limited Search (limit=3)")
res, explored_dls = depth_limited_search(start, goal, 3)

if isinstance(res, Node):
    print_path(res)
else:
    print("No solution within depth limit")

print("States explored:", explored_dls)


print("\nIterative Deepening Search")
res2, explored_ids, final_depth = iterative_deepening_search(start, goal)

if isinstance(res2, Node):
    print_path(res2)

print("States explored:", explored_ids)
print("Solution depth:", final_depth)