order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,
               'A': 14}


def is_char_found(array, char):
    for element in array:
        if element["letter"] == char:
            return 1
    return 0


def increment_letter(array, char, index):
    for element in array:
        if element["letter"] == char:
            element["number"] += 1
            element["index"].append(index)


def get_strongest_hand(hand1, hand2):
    for char, char2 in zip(hand1, hand2):
        if card_values[char] > card_values[char2]:
            return hand1
        if card_values[char] < card_values[char2]:
            return hand2
    return None


def swapper(index_1, index_2, array):
    array[index_1], array[index_2] = array[index_2], array[index_1]


with open('./input.txt') as file:
    hands = []
    for line in file.readlines():
        split = line.split()
        hand = split[0]
        bid = split[1]

        matchesLetter = []
        for index, char in enumerate(hand):
            temp = []
            strength = 0
            for index2, char2 in enumerate(hand):
                if index != index2 and char == char2 and index not in temp:
                    temp.append(index)
                    if not is_char_found(matchesLetter, char2):
                        matchesLetter.append({"letter": char2, "number": 1, "index": [index]})
                    else:
                        increment_letter(matchesLetter, char2, index)

        if len(matchesLetter) == 1 and matchesLetter[0]["number"] == 2:
            strength = 1
        if len(matchesLetter) == 2:
            if matchesLetter[0]["number"] + matchesLetter[1]["number"] == len(hand):
                strength = 4
            else:
                strength = 2
        if len(matchesLetter) == 1 and matchesLetter[0]["number"] == 3:
            strength = 3
        if len(matchesLetter) == 1 and matchesLetter[0]["number"] == 4:
            strength = 5
        if len(matchesLetter) == 1 and matchesLetter[0]["number"] == 5:
            strength = 6

        matchesLetter.append(strength)

        hands.append({"hand": hand, "bid": bid, "strength": strength})

    hands = sorted(hands, key=lambda x: x["strength"])

    n = len(hands)
    for i in range(n):
        for j in range(0, n - i - 1):
            hand1 = hands[j]
            hand2 = hands[j + 1]
            #if i != j and hand1["strength"] == hand2["strength"]:
            print(get_strongest_hand(hand1["hand"], hand2["hand"]), hand1["hand"], hand2["hand"])
            if get_strongest_hand(hand1["hand"], hand2["hand"]) == hand1:
                hands[j], hands[j + 1] = hands[j + 1], hands[j]
        print("\n")

for hand in hands:
        print(hand)
