# Resolution

def negate(x):

    if x[0] == "~":
        return x[1:]

    return "~" + x


def resolve(c1, c2):

    out = []

    for a in c1:
        for b in c2:

            if a == negate(b):

                temp = set(c1 + c2)
                temp.remove(a)
                temp.remove(b)
                out.append(list(temp))

    return out


def resolution(kb, goal):

    clauses = []

    for x in kb:
        clauses.append(x)

    clauses.append([negate(goal)])

    print("Clauses :")
    for x in clauses:
        print(x)

    print()

    new = []

    while True:

        n = len(clauses)

        for i in range(n):
            for j in range(i + 1, n):

                res = resolve(clauses[i], clauses[j])

                for x in res:

                    print(clauses[i], "and", clauses[j], "=>", x)

                    if x == []:
                        print("Empty Clause found")
                        print("Conclusion proved :", goal)
                        return

                    if x not in clauses and x not in new:
                        new.append(x)

        if not new:
            print("Conclusion not proved")
            return

        for x in new:
            clauses.append(x)

        new = []


print("3(a)")
kb = [
    ["P", "Q"],
    ["~P", "R"],
    ["~Q", "S"],
    ["~R", "S"]
]
resolution(kb, "S")

print("\n3(b)")
kb = [
    ["~P", "Q"],
    ["~Q", "R"],
    ["S", "~R"],
    ["P"]
]
resolution(kb, "S")