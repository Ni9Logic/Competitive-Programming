arr = [x for x in range(100)]

anotherarr = set(arr)
counter = [int()] * len(anotherarr)

for i in arr:
    if i in anotherarr:
        counter[anotherarr.index(i)] += 1
        
    
for i, j in zip(anotherarr, counter):
    print(i, j)