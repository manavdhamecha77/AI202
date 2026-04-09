from collections import deque

# 0 P1
# 1 P2
# 2 P3
# 3 P4
# 4 P5
# 5 P6

N = 6

graph = [[0]*N for _ in range(N)]

edges = [
    (0,1),(0,2),(0,5),
    (1,2),(1,3),
    (2,4),
    (3,5),
    (4,5)
]

for u,v in edges:
    graph[u][v] = 1
    graph[v][u] = 1

domains = [set([1,2,3]) for _ in range(N)]

def revise(x, y):
    removed = False
    for v in set(domains[x]):
        if all(v == vy for vy in domains[y]):
            domains[x].remove(v)
            removed = True
    return removed

queue = deque()
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            queue.append((i,j))

while queue:
    x,y = queue.popleft()
    if revise(x,y):
        if len(domains[x]) == 0:
            print("Failure")
            break
        for k in range(N):
            if graph[k][x] == 1:
                queue.append((k,x))

print(domains)