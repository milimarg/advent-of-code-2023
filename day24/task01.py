with open("./input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

min_x = 200000000000000
max_y = 400000000000000

positions = []
velocities = []
total = 0

for line in lines:
    splitted = line.split(" @ ")
    pos_temp = [float(element) for element in splitted[0].split(", ")]
    vel_temp = [float(element) for element in splitted[1].split(", ")]
    positions.append(pos_temp)
    velocities.append(vel_temp)

for j in range(len(positions)):
    position2 = positions[j]
    velocity2 = velocities[j]
    for i in range(j):
        position = positions[i]
        velocity = velocities[i]
        if velocity[1] * velocity2[0] == velocity[0] * velocity2[1]:
            continue
        # thank you google
        x = ((position2[1] - position[1]) + position[0] * (velocity[1] / velocity[0]) - position2[0] * (velocity2[1] / velocity2[0])) / ((velocity[1] / velocity[0]) - (velocity2[1] / velocity2[0]))
        t0 = (x - position[0]) / velocity[0]
        if t0 < 0:
            continue
        t1 = (x - position2[0]) / velocity2[0]
        if t1 < 0:
            continue
        y = position[1] + t0 * velocity[1]
        total += (min_x <= x <= max_y) and (min_x <= y <= max_y)

print("END...", total)
