def main():
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    
    #? Lists
    counts = []
    newcounts = []
    uniquearr = list(dict.fromkeys(arr))
    
    #? Creating counts of total colors
    for i in uniquearr:
        counts.append(arr.count(i))
        
    for i in counts:
        if i % 2 == 1:
            newcounts.append((i - 1) // 2) #? eg. number of socks are 7 that means we have 3 pairs. 7 - 1 -> 6 // 2 -> 3
        elif i % 2 == 0:
            newcounts.append((i // 2)) #? else 4 // 2 -> 2
    print(sum(newcounts))
main()