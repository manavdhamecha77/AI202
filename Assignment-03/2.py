import random

# Environment Side
percepts = []

for i in range(20):
    train_detect = random.randint(0, 1)
    obstacle = random.randint(0, 1)
    emergency = random.choice(["Neutral", "Active"])

    percepts.append((train_detect, obstacle, emergency))

print("Generated percepts:")
print(percepts)
print("\n",end="")


# Rule Tbale
rule_table = {
    (1, 0, "Neutral"): ("Lower", "On", "Red"),
    (1, 1, "Neutral"): ("Lower", "On", "Red"),
    (0, 1, "Neutral"): ("Lower", "On", "Red"),
    (0, 0, "Neutral"): ("Raise", "Off", "Green"),

    (0, 0, "Active"): ("Lower", "On", "Red"),
    (1, 0, "Active"): ("Lower", "On", "Red"),
    (0, 1, "Active"): ("Lower", "On", "Red"),
    (1, 1, "Active"): ("Lower", "On", "Red")
}


# Agent Side
cost = 0
step = 1

for percept in percepts:
    train, obstacle, emergency = percept
    gate, siren, signal = rule_table[(train, obstacle, emergency)]

    print("Step", step)
    print("Percept : Train", train, ", Obstacle", obstacle, ", Emergency", emergency)
    print("Action  : Gate", gate, ", Siren", siren, ", Train Signal", signal)

    cost += 1
    print("Cost:", cost)
    print("\n",end="")

    step += 1
