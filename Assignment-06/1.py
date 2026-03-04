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

# heuristic h(n) to Boston
h = {
    0:860, 1:610, 2:550, 3:780, 4:640,
    5:470, 6:400, 7:260, 8:215, 9:270,
    10:360, 11:0, 12:50, 13:107
}


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


# Greedy Best First Search
# f(n) = h(n)

def GREEDY(start, goal):

    def f(node):
        return h[node.state]

    frontier = PriorityQueue(f)
    frontier.add(Node(start, None, 0))

    lookup = {}
    explored = 0

    while not frontier.empty():

        node = frontier.pop()
        explored += 1

        if node.state == goal:
            return node, explored

        lookup[node.state] = True

        for i in range(n):
            if adj[node.state][i] != 0 and i not in lookup:
                new_cost = node.path_cost + adj[node.state][i]
                frontier.add(Node(i, node, new_cost))

    return None, explored


# A* Search
# f(n) = g(n) + h(n)

def ASTAR(start, goal):

    def f(node):
        return node.path_cost + h[node.state]

    frontier = PriorityQueue(f)
    frontier.add(Node(start, None, 0))

    lookup = {start:0}
    explored = 0

    while not frontier.empty():

        node = frontier.pop()
        explored += 1

        if node.state == goal:
            return node, explored

        for i in range(n):

            if adj[node.state][i] != 0:

                new_cost = node.path_cost + adj[node.state][i]

                if i not in lookup or new_cost < lookup[i]:
                    lookup[i] = new_cost
                    frontier.add(Node(i, node, new_cost))

    return None, explored


def get_path(node):
    path = []
    while node:
        path.append(cities[node.state])
        node = node.parent
    return path[::-1]

#

start = 0      # Chicago
goal = 11      # Boston

g_sol, g_exp = GREEDY(start, goal)
a_sol, a_exp = ASTAR(start, goal)

print("Greedy Path:", get_path(g_sol))
print("Cost:", g_sol.path_cost)
print("Explored:", g_exp)

print("\nA* Path:", get_path(a_sol))
print("Cost:", a_sol.path_cost)
print("Explored:", a_exp)
