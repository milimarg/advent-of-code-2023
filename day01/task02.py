import io, re

file = open("input.txt", "r")

sum = 0

spelled = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in file.readlines():
    lineTemp = line
    for i in range(len(spelled)):
        lineTemp = lineTemp.replace(spelled[i], spelled[i] + str(i) + spelled[i])

    try:
        x = re.search("(\d).*(\d)", lineTemp).groups()
    except:
        x = re.search("(\d)", lineTemp).groups()
    if len(x) == 1:
        number = int(x[0]) * 10 + int(x[0])
    else:
        number = int(x[0]) * 10 + int(x[1])
    sum += number
print(sum)
file.close()
