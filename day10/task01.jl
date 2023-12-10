file = open("input.txt", "r")
lines = readlines(file)
close(file)

array = []

for line in lines
    splitted_line = split(line, "")
    push!(array, splitted_line)
end

let start = 0.0
dict = Dict()

for (i, row) in enumerate(array)
    for (j, cell) in enumerate(row)
        current = []
        if (cell == "|")
            current = [(i - 1, j), (i + 1, j)]
        end
        if cell == "-"
            current = [(i, j - 1), (i, j + 1)]
        end
        if cell == "L"
            current = [(i - 1, j), (i, j + 1)]
        end
        if cell == "J"
            current = [(i - 1, j), (i, j - 1)]
        end
        if cell == "7"
            current = [(i + 1, j), (i, j - 1)]
        end
        if cell == "F"
            current = [(i + 1, j), (i, j + 1)]
        end
        if cell == "S"
            start = (i, j)
        end
        for (key, value) in current
            if key >= 1 && key <= size(array, 1) && value >= 1 && value <= size(row, 1)
                if !haskey(dict, (i, j))
                    dict[(i, j)] = []
                end
                push!(dict[(i, j)], (key, value))
            end
        end
    end
end

#print(start)
start_array = []

for element in dict
    for element2 in dict[element[1]]
        print(element2, " ", start, "\n")
        if element2 == start
           push!(start_array, element)
        end
    end
    print("\n")
end

print("start -> ", start_array, "\n")

end
