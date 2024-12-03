location_file = "locationIDs.txt"

left_side = []
right_side = []
counter = 0
with open(location_file,"r") as f:
    for line in f:
        left_side.append(int(line[:5]))
        right_side.append(int(line[8:13]))
    
left_side.sort()
right_side.sort()

for i in range(len(left_side)):
    if left_side[i] > right_side[i]:
        difference = left_side[i] - right_side[i]
        counter += difference
    else : 
        difference = right_side[i] - left_side[i]
        counter += difference

print(counter)