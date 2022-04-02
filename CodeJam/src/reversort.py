def solve():
    counter = 1
    n = int(input())
    lists = list(map(int, input().rstrip().split()))
    
    reverselist = sorted(lists, reverse = True)
    sortedlist = sorted(lists)
    if lists == sortedlist:
        print("1")
    elif reverselist == lists:
        print(len(reverselist) + (len(reverselist) - 2))
    else:
        for i in range(0, len(reverselist)):
            for j in reversed(range(i + 1, len(lists))):
                if lists[i] > lists[j]:
                    lists[i], lists[j] = lists[j], lists[i]
                    counter += i + 1
                    
        print(*lists)
        print(counter * 2) #? *2 for reverse tracking
        
               


def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = ''); solve();
        
main()