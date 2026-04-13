# Cryptarithmetic Puzzle: SEND + MORE = MONEY

symbols = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']


def find_solution():
    available_digits = set(range(10))

    M = 1   # Since carry can only be 1

    for S in range(1, 10):
        if S == M:
            continue

        for O in available_digits - {M, S}:
            for E in available_digits - {M, S, O}:
                for N in available_digits - {M, S, O, E}:
                    for D in available_digits - {M, S, O, E, N}:
                        for R in available_digits - {M, S, O, E, N, D}:

                            Y = (D + E) % 10
                            carry1 = (D + E) // 10

                            used = {M, S, O, E, N, D, R}
                            if Y in used:
                                continue

                            if (N + R + carry1) % 10 != E:
                                continue
                            carry2 = (N + R + carry1) // 10

                            if (E + O + carry2) % 10 != N:
                                continue
                            carry3 = (E + O + carry2) // 10

                            if (S + M + carry3) % 10 != O:
                                continue
                            carry4 = (S + M + carry3) // 10

                            if carry4 == M:
                                return {
                                    'S': S, 'E': E, 'N': N, 'D': D,
                                    'M': M, 'O': O, 'R': R, 'Y': Y
                                }


answer = find_solution()

print("Solution:\n")

for ch in symbols:
    print(ch, "=", answer[ch])

S = answer['S']
E = answer['E']
N = answer['N']
D = answer['D']
M = answer['M']
O = answer['O']
R = answer['R']
Y = answer['Y']

SEND = 1000 * S + 100 * E + 10 * N + D
MORE = 1000 * M + 100 * O + 10 * R + E
MONEY = 10000 * M + 1000 * O + 100 * N + 10 * E + Y

print("\nSEND  = ", SEND)
print("MORE  = ", MORE)
print("MONEY =", MONEY)