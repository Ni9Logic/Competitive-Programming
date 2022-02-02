arr = []
for i in range(3):
    arr.append(list(map(int, input().rstrip().split())))
    
seen = set()
duplicate_indexes = []
for i in range(3):
    for j in range(3):
        if arr[i][j] not in seen:
            seen.add(arr[i][j])
        else:
            duplicate_indexes.append([i, j])

print(seen)
duplicate_indexes.sort()
print(duplicate_indexes)