import io, re

file = open("input.txt", "r")

sum = 0

for line in file.readlines():
    try:
        x = re.search("(\d).*(\d)", line).groups()
    except:
        x = re.search("(\d)", line).groups()
    if len(x) == 1:
        number = int(x[0]) * 10 + int(x[0])
    else:
        number = int(x[0]) * 10 + int(x[1])
    sum += number
print(sum)
file.close()
