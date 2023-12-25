import z3

with open("./input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

min_x = 200000000000000
max_y = 400000000000000

positions = []
velocities = []

x_real = z3.Real("x")
y_real = z3.Real("y")
z_real = z3.Real("z")
vx_real = z3.Real("vx")
vy_real = z3.Real("vy")
vz_real = z3.Real("vz")
solver = z3.Solver()

for line in lines:
    splitted = line.split(" @ ")
    pos_temp = [float(element) for element in splitted[0].split(", ")]
    vel_temp = [float(element) for element in splitted[1].split(", ")]
    positions.append(pos_temp)
    velocities.append(vel_temp)

for part in [1, 2]:
    result = 0
    for j in range(len(positions)):
        position2 = positions[j]
        velocity2 = velocities[j]
        if part == 1:
            for i in range(j):
                position = positions[i]
                velocity = velocities[i]
                if velocity[1] * velocity2[0] == velocity[0] * velocity2[1]:
                    continue
                x = ((position2[1] - position[1]) + position[0] * (velocity[1] / velocity[0]) - position2[0] * (
                            velocity2[1] / velocity2[0])) / (
                                (velocity[1] / velocity[0]) - (velocity2[1] / velocity2[0]))
                t0 = (x - position[0]) / velocity[0]
                if t0 < 0:
                    continue
                t1 = (x - position2[0]) / velocity2[0]
                if t1 < 0:
                    continue
                y = position[1] + t0 * velocity[1]
                result += (min_x <= x <= max_y) and (min_x <= y <= max_y)
        else:
            px, py, pz = positions[j]
            vx, vy, vz = velocities[j]
            time_i_second = z3.Real(f"t_{j}")
            solver.add(px + vx * time_i_second == x_real + vx_real * time_i_second)
            solver.add(py + vy * time_i_second == y_real + vy_real * time_i_second)
            solver.add(pz + vz * time_i_second == z_real + vz_real * time_i_second)
    if part == 2:
        solver.check()
        model = solver.model()
        result = (model.eval(x_real).as_long() +
                  model.eval(y_real).as_long() +
                  model.eval(z_real).as_long())
    print(f"part {part}:", result)
