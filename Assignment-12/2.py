from collections import deque

grid = [
[0,0,0,0,0,6,0,0,0],
[0,5,9,0,0,0,0,0,8],
[2,0,0,0,0,8,0,0,0],
[0,4,5,0,0,0,0,0,0],
[0,0,3,0,0,0,0,0,0],
[0,0,6,0,0,3,0,5,0],
[0,0,0,0,0,7,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,5,0,0,0,2]
]

cells = [(r,c) for r in range(9) for c in range(9)]

domains = {}
for r,c in cells:
    if grid[r][c] != 0:
        domains[(r,c)] = {grid[r][c]}
    else:
        domains[(r,c)] = set(range(1,10))

def neighbors(r,c):
    n = set()
    for i in range(9):
        n.add((r,i))
        n.add((i,c))
    br, bc = r//3*3, c//3*3
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            n.add((i,j))
    n.remove((r,c))
    return n

arcs = deque()
for r,c in cells:
    for nr,nc in neighbors(r,c):
        arcs.append(((r,c),(nr,nc)))

def revise(x,y):
    removed = 0
    for val in set(domains[x]):
        if all(val == v for v in domains[y]):
            domains[x].remove(val)
            removed += 1
    return removed

removed_total = 0

while arcs:
    x,y = arcs.popleft()
    removed = revise(x,y)
    removed_total += removed
    if removed > 0:
        if len(domains[x]) == 0:
            print("Failure: empty domain")
            break
        for n in neighbors(*x):
            arcs.append((n,x))

print("Total values removed:", removed_total)

for r in range(9):
    row = []
    for c in range(9):
        row.append(str(len(domains[(r,c)])))
    print(" ".join(row))