with open("./input.txt") as f:
    lines = [line.strip().replace("}", "") for line in f.readlines()]

conditions = {}
variables = []
is_variable = False
total_of_total = 0

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
        for index, element in enumerate(a):
            a[index] = a[index].split(":")
        conditions[key] = a

for index, variable in enumerate(variables):
    for definition in variable:
        exec(definition)

    next_key = "in"
    result = 0

    while 1:
        temp = True
        for value in conditions[next_key]:
            if temp:
                try:
                    result = eval(value[0])
                except:
                    result = -1
            if temp and result == True:
                next_key = value[1]
                temp = False
            if temp and result == -1:
                next_key = value[0]
                temp = False
        if next_key == "A" or next_key == "R":
            break

    total = sum([int(a.split("=")[1]) for a in variables[index]])
    total_of_total += total if next_key == "A" else 0

print("END...", total_of_total)
