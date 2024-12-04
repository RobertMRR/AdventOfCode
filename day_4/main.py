input_file = "input.txt"

def get_data(input_data):
    data = []
    with open(input_data, "r") as file:
        for line in file:
            characters = []
            for char in line.strip():
                characters.append(char)
            data.append(characters)
    return data

def day4_1(data):
    lines = data
    result = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            candidates = []
            if i >= 3:
                candidates.append([lines[i - delta][j] for delta in range(4)])
            if j >= 3:
                candidates.append([lines[i][j - delta] for delta in range(4)])
            if i >= 3 and j >= 3:
                candidates.append([lines[i - delta][j - delta] for delta in range(4)])
            if i >= 3 and j + 3 < len(lines[0]):
                candidates.append([lines[i - delta][j + delta] for delta in range(4)])
            result += sum(1 for candidate in candidates if ''.join(candidate) in {"XMAS", "SAMX"}) 
    print(result)

def day4_2(data):
    lines = data
    result = 0
    for i in range(2, len(lines)):
        for j in range(2, len(lines[0])):
            if lines[i][j] == "S" and lines[i - 1][j - 1] == "A" and lines[i][j - 2] == "M" and lines[i - 2][j - 2] == "M" and lines[i - 2][j] == "S":
                result += 1
            elif lines[i][j] == "M" and lines[i - 1][j - 1] == "A" and lines[i][j - 2] == "S" and lines[i - 2][j - 2] == "S" and lines[i - 2][j] == "M":
                result += 1
            elif lines[i][j] == "S" and lines[i - 1][j - 1] == "A" and lines[i][j - 2] == "S" and lines[i - 2][j - 2] == "M" and lines[i - 2][j] == "M":
                result += 1
            elif lines[i][j] == "M" and lines[i - 1][j - 1] == "A" and lines[i][j - 2] == "M" and lines[i - 2][j - 2] == "S" and lines[i - 2][j] == "S":
                result += 1
    print(result)



data = get_data(input_file)
day4_1(data)
day4_2(data)