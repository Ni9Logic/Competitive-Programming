from itertools import combinations
otherlist = []
n = int(input())
array = [int(input()) for i in range(n)]
templist = list(dict.fromkeys(array))
if array == templist:
    print(2)
else:
    perm = list(combinations(array, 2))
    for i in range(len(perm)):
        if perm[i][0] - perm[i][1] == 1:
            otherlist.append([perm[i][0], perm[i][1]])
    
    print(len(otherlist))
            
    