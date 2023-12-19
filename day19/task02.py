from copy import deepcopy

with open("./input.txt") as f:
    lines = [line.strip().replace("}", "") for line in f.readlines()]

conditions = {}
variables = []
is_variable = False
total_of_total = 0
chars = [">", "<"]

for line in lines:
    if len(line) == 0:
        is_variable = True
        continue
    if is_variable:
        line = line.replace("{", "")
        variables.append(line.split(","))
    else:
        key, values = line.split("{")
        a = [value for value in values.split(",")]
        conditions[key] = a


def recall(condition, r, data):
    if condition == "A":
        temp = 1
        for condition in data.values():
            temp *= condition[1] - condition[0] + 1
        r += temp
    elif condition != "R":
        r += run(data, condition)
    return r


def run(data, next_condition):
    r = 0
    for condition in conditions[next_condition]:
        if ":" in condition:
            condition_part, action = condition.split(":")
            new_rng = 0
            a = b = 0
            for char in chars:
                if char in condition_part:
                    new_rng = deepcopy(data)
                    a, b = condition_part.split(char)
                    b = int(b)
                    break
            if ">" in condition_part and new_rng[a][1] > b:
                new_rng[a][0] = max(new_rng[a][0], b + 1)
                r = recall(action, r, new_rng)
                data[a][1] = min(data[a][1], b)
            if "<" in condition_part and new_rng[a][0] < b:
                new_rng[a][1] = min(new_rng[a][1], b - 1)
                r = recall(action, r, new_rng)
                data[a][0] = max(data[a][0], b)
        else:
            r = recall(condition, r, data)
    return r


list_ = [1, 4000]
print(run({"x": list_.copy(), "m": list_.copy(), "a": list_.copy(), "s": list_.copy()}, "in"))
