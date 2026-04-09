import random

cities = ['A','B','C','D','E','F','G','H']

graph = [
[0,10,15,20,25,30,35,40],
[12,0,35,15,20,25,30,45],
[25,30,0,10,40,20,15,35],
[18,25,12,0,15,30,20,10],
[22,18,28,20,0,15,25,30],
[35,22,18,28,12,0,40,20],
[30,35,22,18,28,32,0,15],
[40,28,35,22,18,25,12,0]
]

def path_cost(path):
    cost = 0
    for i in range(len(path)-1):
        cost += graph[path[i]][path[i+1]]
    cost += graph[path[-1]][path[0]]
    return cost



# Local Beam Search
def local_beam_search(k, iterations=200):

    states = []
    for i in range(k):
        p = list(range(len(cities)))
        random.shuffle(p)
        states.append(p)

    best = None
    best_cost = float('inf')

    for i in range(iterations):

        all_neighbors = []

        for state in states:

            for i in range(len(state)):
                for j in range(i+1,len(state)):
                    neighbor = state.copy()
                    neighbor[i],neighbor[j] = neighbor[j],neighbor[i]
                    all_neighbors.append(neighbor)

        all_neighbors.sort(key=path_cost)

        states = all_neighbors[:k]

        c = path_cost(states[0])

        if c < best_cost:
            best_cost = c
            best = states[0]

    return best,best_cost


for k in [3,5,10]:
    path,cost = local_beam_search(k)
    print("Beam width:",k)
    print("Path:",[cities[i] for i in path])
    print("Cost:",cost)
    print()