possible_directions = Dict(
    '|' => [(-1, 0), (1, 0)],
    '-' => [(0, -1), (0, 1)],
    'L' => [(-1, 0), (0, 1)],
    'J' => [(-1, 0), (0, -1)],
    '7' => [(1, 0), (0, -1)],
    'F' => [(1, 0), (0, 1)],
    '.' => [],
)

start_type = Set(['|', '-', 'L', 'J', 'F', '7'])

function read_file_content(file)
    l = readlines(file)
    content = [l[i][j] for i in 1:length(l), j in 1:length(l[1])]
    punkt_row = repeat(["."], size(content, 2))
    punkt_col = repeat(["."], size(content, 1))
    content = vcat(permutedims(punkt_row), content, permutedims(punkt_row))
    content = hcat(repeat(["."], size(content, 1)), content, repeat(["."], size(content, 1)),)
    return content
end

function replace_start!(content)
    start = Tuple(findfirst(isequal('S'), content))
    for directions in [(-1, 0), (0, 1), (1, 0), (0, -1)]
        if !((.-directions) in possible_directions[content[(start .+ directions)...]])
            for (key, value) in possible_directions
                if !(directions in value)
                    continue
                end
                delete!(start_type, key)
            end
        end
    end
    content[start...] = collect(start_type)[1]
    return start
end

function re_set_maze(content)
    new_rows = []
    new_cols = []
    for row in eachrow(content)
        newrow = replace(row,
        '-' => '.', # DO NOT MOVE ORDER
        'F' => '|', # DO NOT MOVE ORDER
        '7' => '|', # DO NOT MOVE ORDER
        'J' => '.', # DO NOT MOVE ORDER
        'L' => '.') # DO NOT MOVE ORDER
        push!(new_rows, row)
        push!(new_rows, newrow)
    end
    newmaze = vcat(permutedims.(new_rows)...)
    for col in eachcol(newmaze)
        newcol = replace(col,
        '|' => '.', # DO NOT MOVE ORDER
        'F' => '-', # DO NOT MOVE ORDER
        'L' => '-', # DO NOT MOVE ORDER
        'J' => '.', # DO NOT MOVE ORDER
        '7' => '.') # DO NOT MOVE ORDER
        push!(new_cols, col)
        push!(new_cols, newcol)
    end
    newmaze = hcat(new_cols...)
    return newmaze
end

function find_outside(loop)
    search = zeros(Bool, size(loop))
    start = Tuple(findfirst(isequal(0), loop))
    queue = [start]
    visited = [start]
    while length(queue) > 0
        current = popfirst!(queue)
        search[current...] = true
        for directions in [
            possible_directions['|'][1],
            possible_directions['|'][2],
            possible_directions['-'][1],
            possible_directions['-'][2]
        ]
            next = current .+ directions
            if next in visited
                continue
            end
            try
                if loop[next...] == 0
                    push!(visited, next)
                    push!(queue, next)
                end
            catch
                #println("ahhh")
            end
        end
    end
    return search
end

function calculate_data(content, start)
    loop = zeros(Bool, size(content))
    current = start
    distance = 0
    queue = [(current, distance)]
    visited = [start]
    while length(queue) > 0
        current, distance = popfirst!(queue)
        loop[current...] = 1
        for delta in possible_directions[content[current...]]
            next = current .+ delta
            if !(next in visited)
                push!(queue, (next, distance + 1))
                push!(visited, next)
            end
        end
    end
    return loop
end

refactor_maze_mess(content) = content[1:2:end, 1:2:end]

content = read_file_content("./input.txt")
start = replace_start!(content)
loop = calculate_data(content, start)
content[loop .== false] .= '.'
content = re_set_maze(content)
start = ((start[1] - 1) * 2 + 1, (start[2] - 1) * 2 + 1)
output = calculate_data(content, start)
inside = .!(find_outside(output) .|| output)
result_to_sum = refactor_maze_mess(inside)
last_output_voila = sum(result_to_sum)

println("END... ", last_output_voila)
