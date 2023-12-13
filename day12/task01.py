from itertools import permutations

with open("./input.txt") as f:
    lines = f.readlines()


def overall_len_check(orders_, array):
    for i, x in enumerate(array):
        if len(x) != orders_[i]:
            return False
    return True


for line in lines:
    arrangement = 0
    template = line.split(" ")
    record = template[0]
    orders = [int(x) for x in template[1].split(",")]

    print("record", record)
    #print("orders", orders)

    test_split = record.split(".")
    test_split = list(filter(None, test_split))

    if len(test_split) == len(orders):
        for i, element in enumerate(test_split):
            if len(element) == orders[i]:
                print("found", test_split[i])
                arrangement += 1
                test_split[i] = "."
                orders[i] = -1
    else:
        pass

    test_split = list(filter(lambda a: a != ".", test_split))
    orders = list(filter(lambda a: a != -1, orders))

    print("orders", orders)
    print("test_split", test_split)
    print("----------\n")

    if len(test_split) == 0:
        continue




    #test = permutations(test_split[0])

    #for perm in set(list(test)):
    #    question_template = test_split.copy()
    #    question_template.pop(0)
    #    perm = list(perm)
    #    perm_len = len(perm)
    #    perm_split = "".join(perm).split(".")
    #    perm_split = list(filter(None, perm_split))
#
    #    for index, element in enumerate(perm_split):
    #        question_template.insert(0 + index, element)
#
    #    # print("perm =", perm, "len =", perm_len, "perm_split =", perm_split)
    #    if len(question_template) != len(orders):
    #        continue
    #    print("question_template", question_template)
    #    if overall_len_check(orders, question_template):
    #        arrangement += 1
    #    # print(".".join(question_template).replace("?", "#"))
#
    #print("arrangement =", arrangement)



    #break
