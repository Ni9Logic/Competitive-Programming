n = int(input())
for i in range(n):
    multiple = input().rstrip().split()
    range1 = int(multiple[0])
    range2 = int(multiple[1])
    count = 0
    borings = []
    for j in range(range1, range2 + 1):
        borings.append(str(j))
    if range1 <= 99:
        for k in range(len(borings)):
            m = 1
            if m % 2 == 0 and int(borings[k]) % 2 == 0:
                count = count + 1
            elif m % 2 == 1 and int(borings[k]) % 2 == 1:
                count = count + 1
    else:
        for k in range(len(borings)):
            for l in range(len(borings[k])):
                m = 1
                count1 = 0
                if m % 2 == 0 and int(borings[k][l]) % 2 == 0:
                    
                    count1 += 1
                elif m % 2 == 1 and int(borings[k][l]) % 2 == 1:
                    count1 += 1
            print(count1, len(borings[k][l]))
            if (count1 == len(borings[k])):
                count = count + 1
    print(borings)
    print(borings[1][0])
    print("Case #{}: {}".format(i + 1, count))
