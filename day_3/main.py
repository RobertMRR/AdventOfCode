import re
input_data = "input.txt"
pattern_part1 = "mul\((\d{1,3}),(\d{1,3})\)"
pattern_part2 = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
def get_data(data):
    memory  = " "
    with open(data, "r") as f:
        for line in f:
            memory +=line
    return memory

def find_all(data, pattern):
    x = re.findall(pattern, data)
    return x

def calculate_result(numbers):
    result = 0 
    for items in numbers:
        result += int(items[0]) * int(items[1])
    return result

def calculate_result_part2(data):
    enabled = True
    result = 0
    for item in data:
        if item == "don't()":
            enabled = False
        elif item == "do()":
            enabled = True
        elif "mul" in item and enabled:
            x = re.findall("mul\((\d{1,3}),(\d{1,3})\)", item)
            result += int(x[0][0]) * int(x[0][1])
    return result

def day_3_1(input_data, pattern_part1):
    memory = get_data(input_data)
    numbers = find_all(memory, pattern_part1)
    return calculate_result(numbers)

def day_3_2(input_data, pattern_part2):
    memory = get_data(input_data)
    numbers = find_all(memory, pattern_part2)
    return calculate_result_part2(numbers)

print(day_3_1(input_data, pattern_part1))
print(day_3_2(input_data, pattern_part2))
