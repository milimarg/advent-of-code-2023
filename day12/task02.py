with open("./input.txt") as f:
    lines = f.readlines()


def calc_line(record_, orders_):
    record_state = "."
    for nr in orders_:
        for i in range(nr):
            record_state += "#"
        record_state += "."

    record_state_len = len(record_state)

    dict_ = {0: 1}
    for char in record_:
        new_dict = {}
        for element in dict_:
            if (element + 1 < record_state_len) and \
                    (char == "?") or \
                    (char == "." and element + 1 < record_state_len and record_state[element + 1] == ".") or \
                    (char == "#" and element + 1 < record_state_len and record_state[element + 1] == "#"):
                new_dict[element + 1] = new_dict.get(element + 1, 0) + dict_[element]
            if (char == "?" or char == ".") and record_state[element] == ".":
                new_dict[element] = new_dict.get(element, 0) + dict_[element]
        dict_ = new_dict
    return dict_.get(record_state_len - 1, 0) + dict_.get(record_state_len - 2, 0)


arrangements = 0
for line in lines:
    template = line.strip().split(" ")
    record = (5 * (template[0] + "?"))[:-1]
    orders = 5 * template[1].split(",")
    orders = [int(x) for x in orders]
    arrangements += calc_line(record, orders)

print("END...", arrangements)
