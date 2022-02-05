from itertools import combinations, permutations
ranges = []
for i in range(32):
    ranges.append(i)

combined = permutations(ranges, 4)
combined = list(combined)
print(len(combined) // 2 // 2)
for i in combined:
    print(i)
