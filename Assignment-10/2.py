# Symbols:
# S = SUCK, L = LEFT, R = RIGHT
# D = Dirty, C = Clean

def is_goal(state):
    return state[1] == 'Clean' and state[2] == 'Clean'


def results(state, action):
    loc, A, B = state
    out = []

    if action == 'Suck':
        if loc == 'A':
            if A == 'Dirty':
                out.append(('A', 'Clean', B))
                out.append(('A', 'Clean', 'Clean'))
            else:
                out.append(('A', 'Dirty', B))

        if loc == 'B':
            if B == 'Dirty':
                out.append(('B', A, 'Clean'))
                out.append(('B', 'Clean', 'Clean'))
            else:
                out.append(('B', A, 'Dirty'))

    elif action == 'Move Left':
        out.append(('A', A, B))

    elif action == 'Move Right':
        out.append(('B', A, B))

    return out


def format_state(s):
    return f"({s[0]},{s[1]},{s[2]})"


def build_plan(state, visited):
    if is_goal(state):
        return ["→ Goal"]

    if state in visited:
        return None

    actions = ['Suck', 'Move Left', 'Move Right']

    for a in actions:
        res = results(state, a)

        branches = []
        ok = True

        for r in res:
            sub = build_plan(r, visited + [state])
            if sub is None:
                ok = False
                break
            branches.append((r, sub))

        if ok:
            output = []
            output.append(format_state(state))
            output.append(f"→ {a}")
            output.append("AND {")

            for (r, sub) in branches:
                output.append(f"  {format_state(r)}")
                for line in sub[1:]:
                    output.append("    " + line)

            output.append("}")
            return output

    return None


# Run
initial = ('B', 'Dirty', 'Dirty')
plan = build_plan(initial, [])

# Print
for line in plan:
    print(line)