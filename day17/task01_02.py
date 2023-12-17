from heapq import heappop, heappush

with open("./input.txt") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
lines = [[int(digit) for digit in x] for x in lines]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
directions_len = len(directions)
row_len = len(lines)
col_len = len(lines[0])

biggest_number = float("inf")


def inr(pos, arr):
    return pos[0] in range(len(arr)) and pos[1] in range(len(arr[0]))  # optimize


def check_for_distance(result, x, y, start_distance, end_distance, direction, results, current):
    result_increase = 0
    for distance in range(0, end_distance):
        temp_x = x + directions[direction][0] * (distance + 1)
        temp_y = y + directions[direction][1] * (distance + 1)
        if not inr((temp_x, temp_y), lines):
            continue
        result_increase += lines[temp_x][temp_y]
        if (distance + 1) < start_distance:
            continue
        temp_ah = result + result_increase
        if results.get((temp_x, temp_y, direction), biggest_number) <= temp_ah:
            continue
        results[(temp_x, temp_y, direction)] = temp_ah
        heappush(current, (temp_ah, temp_x, temp_y, direction))


for index, element in enumerate([(1, 3), (4, 10)]):
    start_distance = element[0]
    end_distance = element[1]
    visited = []
    results = {}
    current = [(0, 0, 0, -1)]
    while current:
        result, x, y, current_direction = heappop(current)
        if x == row_len - 1 and y == col_len - 1:
            break
        if (x, y, current_direction) in visited:
            continue
        visited.append((x, y, current_direction))
        for direction in range(directions_len):
            if direction == current_direction or (direction + 2) % directions_len == current_direction:
                continue
            check_for_distance(result, x, y, start_distance, end_distance, direction, results, current)
    print(f"part {index + 1}:", result)
