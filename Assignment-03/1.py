import random

# Envirenment Side
rooms = ["A", "B", "C"]

env = {
    "A": random.randint(0, 1),
    "B": random.randint(0, 1),
    "C": random.randint(0, 1)
}

location = random.choice(rooms)
dir = 1
percepts = []

print("Initial Environment:", env)
print("Initial Location:", location)
print("\n",end="")

for i in range(10):
    percepts.append((location, env[location]))

    if env[location] == 1:
        env[location] = 0
    else:
        room_index = rooms.index(location)
        next_index = room_index + dir

        if next_index < 0 or next_index > 2:
            dir *= -1
            next_index = room_index + dir

        location = rooms[next_index]

print("Generated percepts:")
print(percepts)
print("\n",end="")


# Rule Table
rule_table = {
    ("A", 1): "Remove",
    ("A", 0): "Move Right",
    ("B", 1): "Remove",
    ("B", 0): "Move Left",
    ("C", 1): "Remove",
    ("C", 0): "Move Left"
}


# Agent Side
total_cost = 0
step = 1

for room, condition in percepts:
    state = "Dirty" if condition else "Clean"
    action = rule_table[(room, condition)]

    print("Step", step)
    print("Percept : Room", room, "-", state)
    print("Action  :", action)

    # clean
    if action == "Remove":
        env[room] = 0

    total_cost += 1
    print("Cost:", total_cost)
    print("\n",end="")

    step += 1
