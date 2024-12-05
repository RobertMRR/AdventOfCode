import re

input_file = "input.txt"

def get_data(data):
    page_orders = []
    updates = []
    with open(data) as file:
        for line in file:
            if re.findall("\d{2}\|\d{2}", line):
                x = line[:2], line.strip()[3:]
                page_orders.append(x)
            else:
                if line > " ":
                    updates.append(line.strip())

    return page_orders, updates

def check_updates(page_orders, updates):
    correct = []
    for update in updates:
        is_valid = False
        for order in page_orders:
            if order[0] in update and order[1] in update:
                if update.index(order[0]) < update.index(order[1]):
                    is_valid = True
                else:
                    is_valid = False
                    break
            else:
                continue
        if is_valid:
            correct.append(update.split(','))
    return correct

def get_incorrect(page_orders, updates):
    incorrect= []
    for update in updates:
        is_invalid = False
        for order in page_orders:
            if order[0] in update and order[1] in update:
                if update.index(order[0]) > update.index(order[1]):
                    is_invalid = True
        if is_invalid:
            incorrect.append(update.split(','))
    return incorrect

def fix_order(update, page_orders):
    for order in page_orders:
        if order[0] in update and order[1] in update:
            if update.index(order[0]) > update.index(order[1]):
                temp1 = update[update.index(order[0])]
                temp2 = update[update.index(order[1])]
                update[update.index(order[0])] = temp2
                update[update.index(order[1])] = temp1
                fix_order(update,page_orders)
            else:
                continue
        else:
            continue
    return update

def day5_1(input_file):
    page_orders, updates = get_data(input_file)
    correct = check_updates(page_orders, updates)
    print(correct)
    result = 0
    for item in correct:
        x = int(len(item)/2)
        result += int(item[x])
    print(result)

def day5_2(input_file):
    page_orders, updates = get_data(input_file)
    incorrect = get_incorrect(page_orders, updates)
    correct = []
    for update in incorrect:
        correct.append(fix_order(update, page_orders))
    result = 0
    for item in correct:
        x = int(len(item)/2)
        result += int(item[x])
    print(result)
#day5_1(input_file)
day5_2(input_file)