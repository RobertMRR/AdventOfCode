input_data = "input.txt"

def get_data(data):
    data_from_file = []
    with open(data,"r") as f:
        for line in f:
            line=line.strip().split()
            for i in range(len(line)):
                line[i] = int(line[i])
            data_from_file.append(line)
        return data_from_file

def validate(level):
    print(tuple(zip(level, level[1:])))
    increase = all(i > j for i, j in zip(level, level[1:]))
    decrease = all(i < j for i, j in zip(level, level[1:]))
    increment = all(abs(i-j) <=3 for i, j in zip(level, level[1:]))
    return (increase or decrease) and increment

def repair(level):
    for i in range(len(level)):
        tmp = level[:]
        tmp.pop(i)
        if validate(tmp):
            return True
    return False

def part1(data):
    answer = 0 
    for line in data: 
        if validate(line):
            answer += 1
    return answer

def part2(data):
    answer = 0
    for line in data: 
        if validate(line):
            answer += 1
        else:
            if repair(line):
                answer += 1
    return answer    

print(part1(get_data(input_data)))
print(part2(get_data(input_data)))