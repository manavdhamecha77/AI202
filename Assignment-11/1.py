# District numbering
# 0 Kuchchh
# 1 Banaskantha
# 2 Patan
# 3 Mehsana
# 4 Sabarkantha
# 5 Gandhinagar
# 6 Ahmedabad
# 7 Surendranagar
# 8 Rajkot
# 9 Jamnagar
# 10 Devbhumi Dwarka
# 11 Porbandar
# 12 Junagadh
# 13 Gir Somnath
# 14 Amreli
# 15 Botad
# 16 Bhavnagar
# 17 Anand
# 18 Kheda
# 19 Panchmahal
# 20 Dahod
# 21 Vadodara
# 22 Chhota Udaipur
# 23 Bharuch
# 24 Narmada
# 25 Surat
# 26 Tapi
# 27 Dangs
# 28 Navsari
# 29 Valsad

N = 30

graph = [[0]*N for _ in range(N)]

edges = [
    (0,9),(0,8),(0,7),(0,2),(0,1),

    (1,2),(1,3),(1,4),
    (2,3),(2,7),

    (3,4),(3,5),(3,6),(3,7),

    (4,5),(4,18),(4,19),(4,20),

    (5,6),

    (6,7),(6,18),(6,17),(6,15),

    (7,15),(7,8),

    (8,15),(8,14),(8,9),

    (9,11),(9,10),

    (10,11),

    (11,12),

    (12,14),(12,13),(12,15),

    (13,14),

    (14,16),(14,15),

    (15,17),(15,16),

    (16,17),(16,23),

    (17,18),(17,21),(17,23),

    (18,21),(18,19),

    (19,21),(19,20),

    (21,23),(21,24),(21,22),

    (22,24),(22,20),

    (23,24),(23,25),

    (24,25),

    (25,26),(25,28),

    (26,27),(26,28),

    (27,28),

    (28,29)
]

for u, v in edges:
    graph[u][v] = 1
    graph[v][u] = 1


def select_unassigned(assignment, domains):
    unassigned = [i for i in range(N) if assignment[i] == -1]

    m = min(len(domains[i]) for i in unassigned)
    candidates = [i for i in unassigned if len(domains[i]) == m]

    return max(candidates, key=lambda x: sum(graph[x]))


def forward_check(node, color, domains):
    new_domains = [d.copy() for d in domains]

    for j in range(N):
        if graph[node][j] == 1 and color in new_domains[j]:
            new_domains[j].remove(color)
            if not new_domains[j]:
                return None

    return new_domains


def is_safe(node, color, assignment):
    for j in range(N):
        if graph[node][j] == 1 and assignment[j] == color:
            return False
    return True


def backtrack(assignment, domains):
    if -1 not in assignment:
        return assignment

    var = select_unassigned(assignment, domains)

    for color in domains[var]:
        if is_safe(var, color, assignment):
            assignment[var] = color

            new_domains = forward_check(var, color, domains)
            if new_domains:
                new_domains[var] = [color]
                res = backtrack(assignment, new_domains)
                if res:
                    return res

            assignment[var] = -1

    return None


def solve():
    for k in range(2, 7):
        print("Trying", k, "colors...")

        domains = [list(range(k)) for _ in range(N)]
        assignment = [-1]*N

        result = backtrack(assignment, domains)

        if result:
            return k, result


def verify(result):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 and result[i] == result[j]:
                return False
    return True


k, result = solve()

print("\nMinimum colors needed:", k)

if verify(result):
    print("Valid coloring\n")
else:
    print("Invalid coloring\n")

for i in range(N):
    print(i, "→ Color", result[i])