def push_o_on_north(dish):
    final = []#[[] for _ in dish]
    for i, line_ in enumerate(dish):
        #col = [row[i] for row in dish]
        col = line_
        o_indices = [i for i, line in enumerate(col) if "O" in line]

        for j, _ in enumerate(o_indices):
            current_index = o_indices[j]
            while current_index > 0 and col[current_index - 1] != "#":
                col[current_index], col[current_index - 1] = col[current_index - 1], col[current_index]
                current_index -= 1
        #for j, char in enumerate(col):
        #    final[j].append(char)
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


with open("./input.txt") as f:
    lines = f.readlines()
    for index, _ in enumerate(lines):
        lines[index] = lines[index].strip()

sum_ = 0

#a = push_o_on_south(lines)
#
#for element in a:
#    print("".join(element))

#print("\nEND...", sum_)
