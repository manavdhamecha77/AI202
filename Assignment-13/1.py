# symbol class
class Symbol:
    def __init__(self, name):
        self.name = name


# priority
def prec(op):
    if op == "~":
        return 4
    if op == "&":
        return 3
    if op == "|":
        return 2
    if op == "->":
        return 1
    if op == "<->":
        return 0
    return -1


# associativity
def assoc(op):
    if op == "~" or op == "->":
        return "R"
    return "L"


# tokenize
def tokens(exp):
    arr = []
    i = 0

    while i < len(exp):

        if exp[i] == " ":
            i += 1

        elif exp[i].isalpha():
            arr.append(exp[i])
            i += 1

        elif exp[i] in "()&|~":
            arr.append(exp[i])
            i += 1

        elif exp[i:i+2] == "->":
            arr.append("->")
            i += 2

        elif exp[i:i+3] == "<->":
            arr.append("<->")
            i += 3

    return arr


# infix to postfix
def to_postfix(exp):

    arr = tokens(exp)
    st = []
    out = []

    for x in arr:

        if x.isalpha():
            out.append(x)

        elif x == "(":
            st.append(x)

        elif x == ")":

            while st and st[-1] != "(":
                out.append(st.pop())

            st.pop()

        else:

            while st and st[-1] != "(":

                top = st[-1]

                if assoc(x) == "L" and prec(top) >= prec(x):
                    out.append(st.pop())

                elif assoc(x) == "R" and prec(top) > prec(x):
                    out.append(st.pop())

                else:
                    break

            st.append(x)

    while st:
        out.append(st.pop())

    return out


# solve postfix
def solve(exp, data):

    post = to_postfix(exp)
    st = []

    for x in post:

        if x in data:
            st.append(data[x])

        elif x == "~":
            a = st.pop()
            st.append(not a)

        else:
            b = st.pop()
            a = st.pop()

            if x == "&":
                st.append(a and b)

            elif x == "|":
                st.append(a or b)

            elif x == "->":
                st.append((not a) or b)

            elif x == "<->":
                st.append(a == b)

    return st.pop()


# print truth table
def show_table(n, exp):

    vars = []

    for i in range(n):
        vars.append(chr(97 + i))

    print("\nExpression =", exp)
    print()

    for x in vars:
        print(x, end="  ")
    print("exp")

    total = 2 ** n

    for num in range(total):

        data = {}

        bits = bin(num)[2:].zfill(n)

        for i in range(n):
            if bits[i] == "1":
                data[vars[i]] = True
            else:
                data[vars[i]] = False

        for x in vars:
            print("T" if data[x] else "F", end="  ")

        ans = solve(exp, data)

        print("T" if ans else "F")


# main
n = int(input("Enter number of variables: "))
exp = input("Enter expression: ")
show_table(n, exp)