with open("./input.txt") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]


def count_differences(a, b):
    su = 0
    a = "".join(a)
    b = "".join(b)
    for i in range(len(a)):
        su += a[i] != b[i]
    return su


def find_reflection(layout_, is_horizontal, difference, part):
    height = len(layout_ if is_horizontal else layout_[0])
    for x in range(1, height):
        num_rows = min(x, height - x)
        if is_horizontal:
            top = layout_[x - num_rows:x]
            bottom = list(reversed(layout_[x:x + num_rows]))
        else:
            top = [row[x - num_rows:x] for row in layout_]
            bottom = ["".join(reversed(row[x:x + num_rows])) for row in layout_]
        if part == 1 and top == bottom:
            return x
        if part == 2 and count_differences(top, bottom) == difference:
            return x
    return 0


empty_rows = [y for y, row in enumerate(lines) if row == ""]

for part in [1, 2]:
    result = 0
    for start, end in zip([-1] + empty_rows, empty_rows + [len(lines)]):
        layout = lines[start + 1:end]
        result += find_reflection(layout, 0, 1, part)
        result += 100 * find_reflection(layout, 1, 1, part)
    print(f"Part {part} = {result}")
