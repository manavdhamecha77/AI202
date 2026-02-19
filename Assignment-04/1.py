# city mapping
cities = {
    0: "Chicago",
    1: "Detroit",
    2: "Cleveland",
    3: "Indianapolis",
    4: "Columbus",
    5: "Pittsburgh",
    6: "Buffalo",
    7: "Syracuse",
    8: "New York",
    9: "Philadelphia",
    10: "Baltimore",
    11: "Boston",
    12: "Providence",
    13: "Portland"
}

n = 14

adj = [
 [0,283,345,182,0,0,0,0,0,0,0,0,0,0],
 [283,0,169,0,0,0,256,0,0,0,0,0,0,0],
 [345,169,0,0,144,134,189,0,0,0,0,0,0,0],
 [182,0,0,0,176,0,0,0,0,0,0,0,0,0],
 [0,0,144,176,0,185,0,0,0,0,0,0,0,0],
 [0,0,134,0,185,0,215,0,0,305,247,0,0,0],
 [0,256,189,0,0,215,0,150,0,0,0,0,0,0],
 [0,0,0,0,0,0,150,0,254,0,0,312,0,0],
 [0,0,0,0,0,0,0,254,0,97,0,0,181,0],
 [0,0,0,0,0,305,0,0,97,0,101,215,0,0],
 [0,0,0,0,0,247,0,0,0,101,0,0,0,0],
 [0,0,0,0,0,0,0,312,0,215,0,0,50,107],
 [0,0,0,0,0,0,0,0,181,0,0,50,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,107,0,0]
]


class Node:
    def __init__(self, state, parent=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost


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


def f(node):
    return node.path_cost   # Uniform Cost Search


def BEST_FIRST_SEARCH(start, goal):

    frontier = PriorityQueue(f)
    frontier.add(Node(start, None, 0))

    lookup = {start: 0}   # lookup table storing best cost so far

    while not frontier.empty():

        node = frontier.pop()

        if node.state == goal:
            return node

        for i in range(n):
            if adj[node.state][i] != 0:

                new_cost = node.path_cost + adj[node.state][i]

                if i not in lookup or new_cost < lookup[i]:
                    lookup[i] = new_cost
                    frontier.add(Node(i, node, new_cost))

    return None


def get_path(node):
    path = []
    while node:
        path.append(cities[node.state])
        node = node.parent
    return path[::-1]

# main
start = 7   # Syracuse
goal = 0    # Chicago

solution = BEST_FIRST_SEARCH(start, goal)

print("Path:", get_path(solution))
print("Total Cost:", solution.path_cost)
