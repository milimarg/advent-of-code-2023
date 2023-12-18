with open("./input.txt") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
direction = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}


def shoelace(points_):
    area = 0
    for (y1, x1), (y2, x2) in zip(points_, points_[1:] + [points_[0]]):
        area += x1 * y2 - x2 * y1
    return area / 2


for index, line in enumerate(lines):
    split = line.split(" ")
    split[1] = int(split[1])
    lines[index] = split

sum_ = 0
points = []
x = y = 0

for (current_direction, range, _) in lines:
    dy, dx = direction[current_direction]
    y += dy * range
    x += dx * range
    points.append((y, x))
    temp = sum(range_ for (current_direction, range_, _) in lines)
    sum_ = int(shoelace(points) + temp / 2 + 1)

print("END...", sum_)
