import collections, math

with open("./input.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def put_in_rx_mess(source_):
    for p_ in inputs[source_]:
        if data[p_][0] == "%" and p_ not in rxMess:
            rxMess.append(p_)
        elif p_ in inputs["rx"]:
            put_in_rx_mess(p_)
        else:
            if p_ not in rxMess:
                rxMess.append(p_)


data = {"rx": ("!", [], False)}
inputs = {}
inputs_memory = {}
rxMess = []

for i, line in enumerate(lines):
    source, dest = line.split("->")
    source = source.strip()
    destinations = dest.strip().split(", ")
    if source == "broadcaster":
        start_sources = destinations
        continue
    temp = source[0]
    source = source[1:]
    data[source] = (temp, destinations, False)
    for d in destinations:
        if d not in inputs:
            inputs[d] = []
        inputs[d].append(source)

put_in_rx_mess("rx")

count = [0, 0]
q = collections.deque()
ah = collections.defaultdict(set)
lcms = []
found = False
found_value = 0
i = -1


def call_flipflop(memory, source, destinations):
    outgoing = not memory
    if outgoing:
        ah[source].add(i)
    data[source] = (category, destinations, not memory)
    for d in destinations:
        q.append((outgoing, d))
        count[outgoing] += 1


def call_conjunction(source, category, destinations):
    outgoing = False
    for p in inputs[source]:
        if not data[p][2]:
            outgoing = True
            break
    data[source] = (category, destinations, outgoing)
    if outgoing:
        ah[source].add(i)
    for d in destinations:
        q.append((outgoing, d))
        count[outgoing] += 1


def call_rx(found):
    for x in ah:
        if x not in rxMess:
            continue
        ls = sorted(ah[x])
        diff = 0
        if len(ah[x]) < 2:
            continue
        for i2, y in enumerate(ls[1:2]):
            diff = y - ls[i2]
        if diff not in lcms:
            lcms.append(diff)
    if len(lcms) == len(rxMess):
        found = True
    return found, math.lcm(*list(lcms))


while not found:
    i += 1
    count[0] += 1
    for s in start_sources:
        q.append((False, s))
        count[0] += 1
    while q:
        high, source = q.popleft()
        if source not in data:
            continue
        category, destinations, memory = data[source]
        if category == "%" and not high:
            call_flipflop(memory, source, destinations)
        if category == "&":
            call_conjunction(source, category, destinations)
        if source == "rx" and not found:
            found, found_value = call_rx(found)
    if i == 1000 - 1:
        print(f"high = {count[1]} ; low = {count[0]}")
        print("part 1:", count[1] * count[0])
    if found:
        print("part 2:", found_value)
