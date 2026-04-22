# Backward Chaining

def backward(goal, rules, facts, seen):

    print("Need to prove :", goal)

    if goal in facts:
        print(goal, "is a fact")
        return True

    if goal in seen:
        return False

    seen.add(goal)

    for left, right in rules:

        if right == goal:

            print("Using rule :", left, "->", right)

            ok = True

            for x in left:
                if not backward(x, rules, facts, seen):
                    ok = False

            if ok:
                print(goal, "proved")
                return True

    print(goal, "not proved")
    return False


print("2(a)")
rules = [
    (["P"], "Q"),
    (["R"], "Q"),
    (["A"], "P"),
    (["B"], "R")
]
facts = ["A", "B"]

if backward("Q", rules, facts, set()):
    print("Conclusion proved : Q")
else:
    print("Conclusion not proved")


print("\n2(b)")
rules = [
    (["A"], "B"),
    (["B", "C"], "D"),
    (["E"], "C")
]
facts = ["A", "E"]

if backward("D", rules, facts, set()):
    print("Conclusion proved : D")
else:
    print("Conclusion not proved")