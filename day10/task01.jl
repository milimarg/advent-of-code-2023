using Distributions
using DataStructures

file = open("input.txt", "r")
lines = readlines(file)
close(file)

array = []

for line in lines
    splitted_line = split(line, "")
    push!(array, splitted_line)
end

let start = 0
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

    start_array = []

    for element in dict
        for element2 in dict[element[1]]
            if element2 == start
                push!(start_array, element[1])
            end
        end
    end

    dict[start] = start_array

    output = Dict()
    queue = Deque{Tuple{Int, Int}}()
    pushfirst!(queue, start)
    output[start] = 0
    tuple_test = (0, start)
    while length(queue) > 0
        curcell = popfirst!(queue)
        for nxt in dict[curcell]
            if !haskey(output, nxt)
                output[nxt] = output[curcell] + 1
                tuple_test = max(tuple_test, (output[nxt], nxt))
                push!(queue, nxt)
            end
        end
    end
    println("output... ", tuple_test[1])
end
