from collection import queue

# 0 P1
# 1 P2
# 2 P3
# 3 P4
# 4 P5
# 5 P6

N = 6

names = ["P1", "P2", "P3", "P4", "P5", "P6"]

graph = [[0]*N for i in range(N)]

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


# initial domains
domains = [
    set(["R1","R2","R3"]) for i in range(N)
]


def show_domains(title):
    print("\n" + title)
    for i in range(N):
        print(names[i], ":", sorted(domains[i]))


def revise(x, y):

    removed = False

    for val in list(domains[x]):

        ok = False

        for v in domains[y]:
            if val != v:
                ok = True
                break

        if not ok:
            domains[x].remove(val)
            removed = True

    return removed


def ac3(trace=False):

    q = queue(200)

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                q.push((i,j))

    step = 1

    while len(q.container) != 0:

        pair = q.pop()

        x = pair[0]
        y = pair[1]

        changed = revise(x,y)

        if trace and step <= 5:

            print("Step", step, ": Arc (" + names[x] + "," + names[y] + ") checked")

            if changed:
                print("  Domain updated")
            else:
                print("  No change")

            step += 1

        if changed:

            if len(domains[x]) == 0:
                print("Failure")
                return False

            for k in range(N):
                if graph[k][x] == 1 and k != y:
                    q.push((k,x))

    return True

# RUN 1
show_domains("Initial Domains:")

print("\nRunning AC-3 (Trace first 5 steps):")
ac3(True)

show_domains("Domains after AC-3:")

print("\nArc-consistent: YES")


# RUN 2
domains[0] = set(["R1"])

show_domains("After assigning P1 = R1:")

print("\nRunning AC-3 again:")
ans = ac3(False)

show_domains("Final Domains:")

if ans:
    print("\nResult: No failure, CSP still solvable")
else:
    print("\nResult: Failure detected")