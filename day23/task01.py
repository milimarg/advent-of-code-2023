with open("./input.txt") as f:
    data = [line.strip() for line in f.readlines()]

directions = {(0, -1): "^", (0, 1): "v", (-1, 0): "<", (1, 0): ">"}
start = data[0].find(".")
end = data[-1].find(".")


def check_path(point_, direction_):
    temp = directions.copy()
    output = []
    to_remove = (direction_[0] * -1, direction_[1] * -1)
    temp.pop(to_remove)
    for element in temp:
        output.append(((point_[0] + element[0], point_[1] + element[1]), element))
    output = [x for x in output if data[x[0][1]][x[0][0]] != "#"]
    return output


def new_path_helper(positions):
    r = []
    for i_ in positions:
        point_, direction_ = i_
        if data[point_[1]][point_[0]] == directions[direction_] or \
                data[point_[1]][point_[0]] == '.':
            r.append(i_)
    return r


def fucking_path_finder():
    queue = []
    output = []
    queue.append([1, maze[(start, 0)]])
    while len(queue) != 0:
        length_, nodes = queue.pop(0)
        for node in nodes:
            line, point_ = node
            aye = maze[point_] if point_ in maze else []
            queue.append([length_ + line, aye])
        if len(nodes) == 0:
            output.append(length_)
    return output


def get_longest_path_through_each_wall(start_, length_, visited):
    next_visited = visited.copy()
    next_visited.append(start_)
    initial = maze[start_]
    current_data = []
    for line, node in initial:
        if node not in visited:
            current_data.append((line, node))
        if node == (end, len(data) - 1):
            ahah.append(line + length_)
            return
    for line, node in current_data:
        get_longest_path_through_each_wall(node, length_ + line, next_visited)


for part in [1, 2]:
    maze = {}
    pos = [[(start, 0), (0, 1), (start, 1)]]
    ahah = []
    for i in pos:
        origin, direction, point = i
        length = 0
        while True:
            if point == (end, len(data) - 1):
                if origin not in maze:
                    maze[origin] = []
                maze[origin].append((length, point))
                break
            new_path = check_path(point, direction)
            length += 1
            if len(new_path) == 1:
                point, direction = new_path[0]
                continue
            if origin not in maze:
                maze[origin] = []
            maze[origin].append((length, point))
            if part == 1:
                new_path = new_path_helper(new_path)
            for j in new_path:
                if [point, j[1], j[0]] not in pos:
                    pos.append([point, j[1], j[0]])
                    continue
                if part == 1:
                    break
            break
    if part == 2:
        get_longest_path_through_each_wall((start, 0), 1, [])
    value = fucking_path_finder() if part == 1 else ahah
    print(f"part {part}:", max(value))
