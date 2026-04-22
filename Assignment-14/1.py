# Forward Chaining

def forward_chain(rules, facts, goal):

    known = set(facts)

    print("Initial Facts :", facts)
    print()

    changed = True

    while changed:

        changed = False

        for left, right in rules:

            ok = True

            for x in left:
                if x not in known:
                    ok = False

            if ok and right not in known:

                print(left, "->", right, " so derive ", right)
                known.add(right)
                changed = True

    print()
    print("All Facts :", list(known))

    if goal in known:
        print("Conclusion proved :", goal)
    else:
        print("Conclusion not proved")


print("1(a)")
rules = [
    (["P"], "Q"),
    (["L", "M"], "P"),
    (["A", "B"], "L")
]
facts = ["A", "B", "M"]
forward_chain(rules, facts, "Q")

print("\n1(b)")
rules = [
    (["A"], "B"),
    (["B"], "C"),
    (["C"], "D"),
    (["D", "E"], "F")
]
facts = ["A", "E"]
forward_chain(rules, facts, "F")