function file_exists(file)
    local f = io.open(file, "rb")
    if f then f:close() end
    return f ~= nil
end

function lines_from(file)
    if not file_exists(file) then return {} end
    local lines = {}
    for line in io.lines(file) do
        lines[#lines + 1] = line
    end
    return lines
end

local file = "./input.txt"
local lines = lines_from(file)
local sep = " "

fileData = {}
for k, v in pairs(lines) do
    fileData[k] = {}
    for token in string.gmatch(v, "([^"..sep.."]+)") do
        table.insert(fileData[k], token)
    end
end

local order = fileData[1][1]

print("order =", order)

local dict = {}

for k, v in pairs(fileData) do
    if (k > 2) then
        for k2, v2 in pairs(fileData[k]) do
            if (k2 == 1) then
                dict[v2] = {}
            end
            if (k2 == 3 or k2 == 4) then
                --table.insert(dict[v2], k2)
            end
            --print(k2, " -> ", v2)
            --for key, token in pairs(dict[v2]) do
            --    print(key, " -> ", token)
            --end
        end
        print("\n")
    end
end
