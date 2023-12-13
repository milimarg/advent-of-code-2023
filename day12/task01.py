import re
from itertools import combinations

with open("./input.txt") as f:
    lines = f.readlines()


def is_this_fucking_arrangement_correct(record, expected_group_sizes):
    found_groups = list(filter(None, re.findall(r'#*', record)))
    found_groups_sizes = [len(x) for x in found_groups]
    return found_groups_sizes == expected_group_sizes


arrangements = 0
for line in lines:
    temp = 0
    template = line.split(" ")
    record = template[0]
    a = ""
    for i in range(5):
        a += record
        if i < 5 - 1:
            a += "?"
    record = a
    orders = template[1]
    orders_sizes = [int(x) for x in orders.split(",")] * 5

    springs_temp_ahh = sum(orders_sizes) - record.count("#")
    positions_idk = [i for i, character in enumerate(record) if character == "?"]

    for element in combinations(positions_idk, springs_temp_ahh):
        record_temp = list(record)
        for position in element:
            record_temp[position] = "#"
        if is_this_fucking_arrangement_correct("".join(record_temp), orders_sizes):
            temp += 1
    arrangements += temp

print("END...", arrangements)
