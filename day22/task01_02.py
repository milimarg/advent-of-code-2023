def drop(bricks_, index_to_skip):
    peaks = {}
    falls = 0

    for i_, (a1, a2, a3, b1, b2, b3) in enumerate(bricks_):
        if i_ == index_to_skip:
            continue
        area = []
        for a in range(a1, b1 + 1):
            for b in range(a2, b2 + 1):
                area.append((a, b))
        temp_ = []
        for a in area:
            temp_.append(peaks[a] if a in peaks else 0)
        peak = max(temp_) + 1
        for a in area:
            peaks[a] = peak + b3 - a3
        bricks_[i_] = (a1, a2, peak, b1, b2, peak + b3 - a3)
        falls += peak < a3
    return falls


with open("./input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

bricks = []

for element in lines:
    split = element.split("~")
    temp = [int(element) for a1 in split for element in a1.split(",")]
    bricks.append(temp)

drop(bricks, None)

results = [[], []]
for i in range(len(bricks)):
    value = drop(bricks.copy(), i)
    results[0].append(not value)
    results[1].append(value)

temp = []

for element in results:
    temp.append(sum([element for element in element]))

for part in [1, 2]:
    print(f"part {part}:", temp[part - 1])
