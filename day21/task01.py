with open("./input.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def get_complex_of_number(x_):
    return complex(x_.real % messed_up_variable, x_.imag % messed_up_variable)


def get_result(n, a, b, c):
    return a + n * (b - a + (n - 1) * (c - b - b + a) // 2)


data = {}
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "." or char == "S":
            data[i + j * 1j] = char

messed_up_variable = 131  # second part "26501365" -> 26501365 % x = step_to_reach + 1, x was bruteforced and is 131
total_steps_for_part_2 = 26501365
step_to_reach = 64
start = []
result = []

for x in data:
    if data[x] == "S":
        start = [x]

for step in range(3 * messed_up_variable):
    result_temp = len(start)
    if step == step_to_reach:
        print("part 1:", result_temp)
    if step % messed_up_variable == step_to_reach + 1:
        result.append(result_temp)
    start = {element + direction for direction in {1, -1, 1j, -1j} for element in start if get_complex_of_number(element + direction) in data}

print("part 2:", get_result(total_steps_for_part_2 // messed_up_variable, result[0], result[1], result[2]))
