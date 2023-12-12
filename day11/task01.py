f = open("./input.txt")

lines = f.readlines()

shift = 0
shift_max = 1000000

lines_new = lines.copy()

line_len = len(lines[0])

for i, line in enumerate(lines):
    if len(set(line)) == 2:
        str_test = ("." * (line_len - 1)) + "\n"
        for j in range(shift_max):
            lines_new.insert(i + 1 + j, str_test)

lines = lines_new.copy()

for i in range(len(lines[0])):
    if 0 < shift < shift_max + 1:
        shift += 1
        continue
    if shift == shift_max + 1:
        shift = 0
    col = [line[i] for line in lines]
    test = set(col)
    if len(test) == 1 and test != {'\n'}:
        for j in range(shift_max):
            lines = [line[:(i + j)] + "." + line[(i + j):] for line in lines]
            shift = 1

f.close()

positions = []

for i, y in enumerate(lines):
    for j, x in enumerate(y):
        if x == "#":
            positions.append({"x": j, "y": i})

sum_ = 0

for i, galaxy in enumerate(positions):
    for j, galaxy2 in enumerate(positions):
        if i == j:
            continue
        distance = abs(galaxy2["x"] - galaxy["x"]) + abs(galaxy2["y"] - galaxy["y"])
        sum_ += distance

print("END...", sum_ / 2)
