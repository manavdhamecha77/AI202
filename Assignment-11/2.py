# SEND + MORE = MONEY

letters = ['S','E','N','D','M','O','R','Y']


def is_valid(assign):
    # All values must be unique
    if len(set(assign.values())) < len(assign):
        return False

    # Leading digits cannot be zero
    if ('S' in assign and assign['S'] == 0) or ('M' in assign and assign['M'] == 0):
        return False

    # If all assigned, check full equation
    if len(assign) == 8:
        S,E,N,D = assign['S'],assign['E'],assign['N'],assign['D']
        M,O,R,Y = assign['M'],assign['O'],assign['R'],assign['Y']

        SEND  = 1000*S + 100*E + 10*N + D
        MORE  = 1000*M + 100*O + 10*R + E
        MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

        return SEND + MORE == MONEY

    return True


def backtrack(assign):
    # If all assigned → solution
    if len(assign) == 8:
        return assign

    # Pick next variable
    for l in letters:
        if l not in assign:
            var = l
            break

    for digit in range(10):
        assign[var] = digit

        if is_valid(assign):
            result = backtrack(assign)
            if result:
                return result

        del assign[var]

    return None


solution = backtrack({})

print("\nSolution:\n")
for k in letters:
    print(k, "→", solution[k])

S,E,N,D = solution['S'],solution['E'],solution['N'],solution['D']
M,O,R,Y = solution['M'],solution['O'],solution['R'],solution['Y']

print("\nSEND =", 1000*S + 100*E + 10*N + D)
print("MORE =", 1000*M + 100*O + 10*R + E)
print("MONEY =", 10000*M + 1000*O + 100*N + 10*E + Y)