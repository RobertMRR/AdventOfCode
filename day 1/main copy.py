location_file = "locationIDs.txt"

left_side = []
right_side = []
similarity_score = 0
with open(location_file,"r") as f:
    for line in f:
        left_side.append(int(line[:5]))
        right_side.append(int(line[8:13]))
    
left_side.sort()
right_side.sort()

for i in range(len(left_side)):
    counter = 0
    for j in range(len(right_side)):
        if left_side[i] == right_side[j]:
            counter += 1
        else:
            continue
    score = counter * left_side[i]
    similarity_score += score

print(similarity_score)