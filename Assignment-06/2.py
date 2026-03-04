maze = [
    [2,0,0,1,3],
    [1,1,0,1,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [3,0,0,0,0]
]

rows = 5
cols = 5


class Node:
    def __init__(self, pos, parent=None, path_cost=0, goals=None):
        self.pos = pos
        self.parent = parent
        self.path_cost = path_cost
        self.goals = goals[:]       # remaining rewards


class PriorityQueue:
    def __init__(self, f):
        self.data = []
        self.f = f

    def add(self, node):
        self.data.append(node)
        self.data.sort(key=self.f)

    def pop(self):
        return self.data.pop(0)

    def empty(self):
        return len(self.data) == 0


# find start and rewards
start = None
rewards = []

for r in range(rows):
    for c in range(cols):
        if maze[r][c] == 2:
            start = (r,c)
        if maze[r][c] == 3:
            rewards.append((r,c))


# Manhattan distance
def heuristic(pos, goals):

    if len(goals) == 0:
        return 0

    best = 999999
    for g in goals:
        d = abs(pos[0]-g[0]) + abs(pos[1]-g[1])
        if d < best:
            best = d
    return best

def ASTAR(start, goals):

    def f(node):
        return node.path_cost + heuristic(node.pos, node.goals)

    frontier = PriorityQueue(f)
    frontier.add(Node(start, None, 0, goals))

    lookup = {}
    visited_tiles = []
    explored = 0

    while not frontier.empty():

        node = frontier.pop()
        explored += 1

        visited_tiles.append(node.pos)

        if node.pos in node.goals:
            new_goals = []
            for g in node.goals:
                if g != node.pos:
                    new_goals.append(g)
            node.goals = new_goals

        if len(node.goals) == 0:
            return node, visited_tiles, explored

        lookup[(node.pos, tuple(node.goals))] = node.path_cost

        r, c = node.pos

        moves = [ (0,-1), (0,1), (-1,0), (1,0) ] 

        for dr, dc in moves:

            nr = r + dr
            nc = c + dc

            if nr>=0 and nr<rows and nc>=0 and nc<cols:

                if maze[nr][nc] != 1:

                    new_cost = node.path_cost + 1
                    state_key = ((nr,nc), tuple(node.goals))

                    if state_key not in lookup or new_cost < lookup[state_key]:

                        frontier.add(Node((nr,nc), node, new_cost, node.goals))

    return None, visited_tiles, explored


def get_path(node):
    path = []
    while node:
        path.append(node.pos)
        node = node.parent
    return path[::-1]


#

solution, visited, explored = ASTAR(start, rewards)

print("Path:", get_path(solution))
print("Visited tiles:", visited)
print("Total cost:", solution.path_cost)
print("Explored nodes:", explored)
