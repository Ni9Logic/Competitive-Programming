from itertools import combinations
multiple_input = input().rstrip().split()
n = int(multiple_input[0])
k = int(multiple_input[1])
arr = list(map(int, input().rstrip().split()))
combined_arr = list(combinations(arr, 2))
sums = []
for i, j in combined_arr:
    sums.append([i, j, i + j])


sub_Arr = []
for n, m, o in sums:
    if not o % k == 0:
        sub_Arr.append([n, m])

with (open ("Outputs/output.txt", "w")) as f:
        for i in sub_Arr:
            f.write(str(i) + '\n')
print(sub_Arr)