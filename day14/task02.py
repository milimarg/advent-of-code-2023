def super_stringifier(dish):
    return "".join(["".join(row) for row in dish])


def push_o_on_north(dish):
    final = [[] for _ in dish]

    for i, line_ in enumerate(dish):
        col = [row[i] for row in dish]
        o_indices = [i for i, line in enumerate(col) if "O" in line]

        for j, _ in enumerate(o_indices):
            current_index = o_indices[j]
            while current_index > 0 and col[current_index - 1] != "#":
                col[current_index], col[current_index - 1] = col[current_index - 1], col[current_index]
                current_index -= 1
        for j, char in enumerate(col):
            final[j].append(char)
    return final


def push_o_on_west(dish):
    final = []

    for i, line_ in enumerate(dish):
        col = line_
        o_indices = [i for i, line in enumerate(col) if "O" in line]

        for j, _ in enumerate(o_indices):
            current_index = o_indices[j]
            while current_index > 0 and col[current_index - 1] != "#":
                col = list(col)
                col[current_index], col[current_index - 1] = col[current_index - 1], col[current_index]
                col = "".join(col)
                current_index -= 1
        final.append(col)
    return final


def push_o_on_south(dish):
    final = [[] for _ in dish]

    for i, _ in enumerate(dish):
        col = [row[i] for row in dish]
        o_indices = [i for i, line in enumerate(col) if 'O' in line]

        for j in range(len(o_indices) - 1, -1, -1):
            current_index = o_indices[j]
            while current_index < len(col) - 1 and col[current_index + 1] != '#':
                col[current_index], col[current_index + 1] = col[current_index + 1], col[current_index]
                current_index += 1
        for j, char in enumerate(col):
            final[j].append(char)
    return final


def push_o_on_east(dish):
    final = []

    for i, line_ in enumerate(dish):
        col = line_
        o_indices = [i for i, line in enumerate(col) if 'O' in line]

        for j in range(len(o_indices) - 1, -1, -1):
            current_index = o_indices[j]
            while current_index < len(col) - 1 and col[current_index + 1] != '#':
                col = list(col)
                col[current_index], col[current_index + 1] = col[current_index + 1], col[current_index]
                col = "".join(col)
                current_index += 1
        final.append(col)
    return final


def run_cycle(dish):
    temp_ = push_o_on_north(dish)
    temp_ = push_o_on_west(temp_)
    temp_ = push_o_on_south(temp_)
    return push_o_on_east(temp_)


with open("./input.txt") as f:
    lines = f.readlines()
    for index, _ in enumerate(lines):
        lines[index] = lines[index].strip()

sum_ = 0
cycles = []
temp = run_cycle(lines)

while super_stringifier(temp) not in cycles:
    cycles.append(super_stringifier(temp))
    temp = run_cycle(temp)

loop_length = len(cycles) - cycles.index(super_stringifier(temp))
not_in_loop = cycles.index(super_stringifier(temp))
cycles_left = (1000000000 - not_in_loop) % loop_length
for i in range(cycles_left - 1):
    temp = run_cycle(temp)

temp_len = len(temp)
for index, element in enumerate(temp):
    reversed_index = temp_len - index
    occurrence = element.count("O") * reversed_index
    sum_ += occurrence

print("END...", sum_)
