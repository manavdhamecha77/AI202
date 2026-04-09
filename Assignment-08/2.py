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

# Initial population
def initial_population(size):
    pop = []
    for i in range(size):
        p = list(range(len(cities)))
        random.shuffle(p)
        pop.append(p)
    return pop

# Selection
def selection(pop):
    pop.sort(key=path_cost)
    return pop[:len(pop)//2]

# 1-point crossover
def crossover_one(p1,p2):

    point = random.randint(1,len(p1)-2)

    child = p1[:point]

    for gene in p2:
        if gene not in child:
            child.append(gene)

    return child

# 2-point crossover
def crossover_two(p1,p2):

    a,b = sorted(random.sample(range(len(p1)),2))

    child = [None]*len(p1)

    child[a:b] = p1[a:b]

    fill = [g for g in p2 if g not in child]

    idx = 0

    for i in range(len(child)):
        if child[i] is None:
            child[i] = fill[idx]
            idx += 1

    return child

# Mutation
def mutate(path,rate=0.1):

    if random.random() < rate:
        i,j = random.sample(range(len(path)),2)
        path[i],path[j] = path[j],path[i]

    return path

# Genetic Algorithm
def genetic_algorithm(pop_size=50,generations=300,crossover="one"):

    pop = initial_population(pop_size)

    for i in range(generations):

        parents = selection(pop)

        children = []

        while len(children) < pop_size:

            p1,p2 = random.sample(parents,2)

            if crossover=="one":
                child = crossover_one(p1,p2)
            else:
                child = crossover_two(p1,p2)

            child = mutate(child)

            children.append(child)

        pop = children

    best = min(pop,key=path_cost)

    return best,path_cost(best)

path,cost = genetic_algorithm(crossover="one")
print("Genetic Algorithm (1-point crossover)")
print("Path:",[cities[i] for i in path])
print("Cost:",cost)

print()

path,cost = genetic_algorithm(crossover="two")
print("Genetic Algorithm (2-point crossover)")
print("Path:",[cities[i] for i in path])
print("Cost:",cost)



abcde
vwxyz

a|b|cde
ab|c|de
abc|d|e
a|bc|de
ab|cd|e
a|bcd|e












