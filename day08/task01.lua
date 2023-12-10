function file_exists(file)
    local f = io.open(file, "rb")
    if f then f:close() end
    return f ~= nil
end

function lines_from(file)
    if not file_exists(file) then
        return {}
    end
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
local skipKey = 2

for k, v in pairs(fileData) do
    if (k > skipKey) then
        fileData[k][3] = v[3]:gsub("%(", ""):gsub("%,", "")
        fileData[k][4] = v[4]:gsub("%)", "")
    end
end

for k, v in pairs(fileData) do
    if (k > skipKey) then
        for k2, v2 in pairs(fileData) do
            if (k2 > skipKey) then
                if (v[1] == v2[3]) then
                    fileData[k2][3] = k
                end
                if (v[1] == v2[4]) then
                    fileData[k2][4] = k
                end
            end
        end
    end
end

local currentKey = skipKey + 1

for k, v in pairs(fileData) do
    if v[1] == "AAA" then
        currentKey = k
        break
    end
end

local directionKey = 0
local breaker = 0
local stepsNumber = 0

while breaker == 0 do
    for i = 1, #order do
        local c = order:sub(i, i)
        if (c == 'L') then
            directionKey = 3
        end
        if (c == 'R') then
            directionKey = 4
        end
        currentKey = fileData[currentKey][directionKey]
        stepsNumber = stepsNumber + 1
        if fileData[currentKey][1] == "ZZZ" then
            breaker = 1
        end
    end
end

print("END...", stepsNumber)
