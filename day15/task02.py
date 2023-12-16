from typing import Dict

file_path = "./input.txt"
with open(file_path, 'r') as file:
    buffer = file.read()

parts = buffer.split(",")
boxes = {}
sum_ = 0

for part in parts:
    temp_sum = 0
    part_to_take = part
    lens_length = ""
    remove = False

    if "=" in part_to_take:
        part_to_take, lens_length = part_to_take.split('=')

    if "-" in part_to_take:
        remove = True
        part_to_take = part_to_take.split('-')[0]

    for char in part_to_take:
        ascii_val = ord(char)
        temp_sum += ascii_val
        temp_sum *= 17
        temp_sum %= 256

    a = temp_sum

    if remove and a in boxes and part_to_take in boxes[a]:
        del boxes[a][part_to_take]
        if not boxes[a]:
            del boxes[a]

    if lens_length:
        lens_length_int = int(lens_length)
        if a in boxes:
            dict_a = boxes[a]
            hashmap_len = len(dict_a)
            dict_a[part_to_take] = [lens_length_int, hashmap_len]
        else:
            dict_a = {part_to_take: [lens_length_int, 0]}
            boxes[a] = dict_a

for a in boxes:
    for key in boxes[a]:
        slot = (list(boxes[a].keys()).index(key)) + 1
        sum_ += (a + 1) * slot * boxes[a][key][0]

print("END...", sum_)
