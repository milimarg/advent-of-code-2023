with open("./input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

data = {}

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        data[complex(j, i)] = char


def contraception_run(element):
    done = []
    while element:
        position_, direction_ = element.pop()
        while not (position_, direction_) in done:
            value = (position_, direction_)
            if value not in done:
                done.append(value)
            position_ += direction_

            char_ = data.get(position_)
            if char_ == "|" or char_ == "-":
                direction_ = 1j if char_ == "|" else -1
                element.append((position_, -direction_))
            if char_ == "/" or char_ == "\\":
                direction_ = complex(direction_.imag, direction_.real) * (-1 if char_ == "/" else 1)
            if char_ is None:
                break

    result_len = []
    for pos, _ in done:
        if pos not in result_len:
            result_len.append(pos)
    return len(result_len) - 1


result = contraception_run([(-1, 1)])

print("part 1:", result)

temp = []

for direction in (1, 1j, -1, -1j):
    for position in data:
        if position - direction not in data:
            temp.append([(position - direction, direction)])

for index, _ in enumerate(temp):
    temp[index] = contraception_run(temp[index])

print("part 2:", max(temp))
