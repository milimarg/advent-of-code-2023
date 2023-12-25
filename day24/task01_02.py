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
        px2, py2, pz2 = positions[j]
        vx2, vy2, vz2 = velocities[j]
        if part == 1:
            for i in range(j):
                px, py, pz = positions[i]
                vx, vy, vz = velocities[i]
                if vy * vx2 == vx * vy2:
                    continue
                x = (((py2 - py) + px * (vy / vx) - px2 * (vy2 / vx2)) /
                     ((vy / vx) - (vy2 / vx2)))
                t0 = (x - px) / vx
                if t0 < 0:
                    continue
                t1 = (x - px2) / vx2
                if t1 < 0:
                    continue
                y = py + vy * t0
                result += (min_x <= x <= max_y) and (min_x <= y <= max_y)
        else:
            time_i_second = z3.Real(f"t_{j}")
            solver.add(px2 + vx2 * time_i_second == x_real + vx_real * time_i_second)
            solver.add(py2 + vy2 * time_i_second == y_real + vy_real * time_i_second)
            solver.add(pz2 + vz2 * time_i_second == z_real + vz_real * time_i_second)
    if part == 2:
        solver.check()
        model = solver.model()
        result = (model.eval(x_real).as_long() +
                  model.eval(y_real).as_long() +
                  model.eval(z_real).as_long())
    print(f"part {part}:", result)
