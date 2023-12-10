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
local orderLen = #order
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

function endsWith(str, suffix)
    return string.sub(str, -#suffix) == suffix
end

function getCharAtIndex(str, index)
    return string.sub(str, index, index)
end

function getElementByKey(array, key)
    for k, v in pairs(array) do
        if v[1] == key then
            return v
        end
    end
    return nil
end

local AH = 0

function task02(value)
    local currentElement = value
    local currentIndex = 0
    local temp = 0
    local tempElem = 0

    while not endsWith(currentElement[1], "Z") do
        temp = getCharAtIndex(order, (currentIndex % orderLen) + 1)
        tempElem = getElementByKey(fileData, currentElement[1])
        if temp == "L" then
            currentElement = fileData[tempElem[3]]
        end
        if temp == "R" then
            currentElement = fileData[tempElem[4]]
        end
        AH = AH + 1
        print(currentElement[1], AH)
        currentIndex = currentIndex + 1
    end
    return currentIndex
end

function calculateMess(a, b)
    local multiple = math.max(a, b)

    while true do
        if multiple % a == 0 and multiple % b == 0 then
            return multiple
        end
        multiple = multiple + 1
    end
end

local output = 1

for k, v in pairs(fileData) do
    if (k > skipKey) then
        if endsWith(v[1], "A") then
            output = calculateMess(output, task02(v))
        end
    end
end

print("END...", output)
