from copy import deepcopy


def manhattan_distance(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])


with open("./input.txt") as f:
    lines = f.readlines()

galaxies = []
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == "#":
            galaxies.append([row, col])

all_rows = []
all_cols = []

for galaxy in galaxies:
    all_rows.append(galaxy[0])
    all_cols.append(galaxy[1])

row = len(lines)
col = len(lines[0])

empty_rows = sorted(set(range(row)).difference(set(all_rows)))
empty_cols = sorted(set(range(col)).difference(set(all_cols)))

for part_index, part in enumerate([2, 1000000]):
    galaxies_expanded = deepcopy(galaxies)

    for i, galaxy in enumerate(galaxies):
        for empty_row in empty_rows:
            if galaxy[0] > empty_row:
                galaxies_expanded[i][0] += part - 1
        for empty_col in empty_cols:
            if galaxy[1] > empty_col:
                galaxies_expanded[i][1] += part - 1

    sum_ = 0

    for index, element in enumerate(galaxies_expanded):
        for index2, element2 in enumerate(galaxies_expanded):
            if index == index2:
                continue
            sum_ += manhattan_distance(element, element2)

    print(f"Part {part_index + 1} =", sum_ // 2)
