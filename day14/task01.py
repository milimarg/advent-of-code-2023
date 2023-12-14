def push_o_on_north(dish):
    final = [[] for _ in dish]
    for i, _ in enumerate(dish):
        col = [row[i] for row in dish]
        o_indices = [i for i, line in enumerate(col) if "O" in line]

        for j, a in enumerate(o_indices):
            current_index = o_indices[j]
            while current_index > 0 and col[current_index - 1] != "#":
                col[current_index], col[current_index - 1] = col[current_index - 1], col[current_index]
                current_index -= 1
        for j, char in enumerate(col):
            final[j].append(char)
    return final


with open("./input.txt") as f:
    lines = f.readlines()
    for index, _ in enumerate(lines):
        lines[index] = lines[index].strip()

sum_ = 0

a = push_o_on_north(lines)

for index, element in enumerate(a):
    reversed_index = len(a) - index
    occurrence = element.count("O") * reversed_index
    sum_ += occurrence

print("\nEND...", sum_)
