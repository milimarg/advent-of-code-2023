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


def push_o_on_south(col_):
    lines = col_
    o_indices = [i for i, line in enumerate(lines) if 'O' in line]

    for i in range(len(o_indices) - 1, -1, -1):
        current_index = o_indices[i]
        while current_index < len(lines) - 1 and lines[current_index + 1] != '#':
            lines[current_index], lines[current_index + 1] = lines[current_index + 1], lines[current_index]
            current_index += 1
    return lines


#def push_o_on_west()


with open("./input.txt") as f:
    lines = f.readlines()
    for index, _ in enumerate(lines):
        lines[index] = lines[index].strip()

print(lines)

sum_ = 0

a = [[] for _ in lines]

#a = push_o_on_north(lines)

for index, _ in enumerate(lines):
    col = [row[index] for row in lines]
    for index2, e in enumerate(push_o_on_south(col)):
        a[index2].append(e)

#a = push_o_on_south(a)

for element in a:
    print("".join(element))

#print("\nEND...", sum_)
