def solve():
    counter = 0
    n = int(input())
    lists = list(map(int, input().rstrip().split()))
    
    reverselist = sorted(lists, reverse = True)
    sortedlist = sorted(lists)
    if lists != reverselist and lists != sortedlist:
        print("Working on this case...")
    elif lists == sortedlist:
        print("1")
    elif reverselist == lists:
        print(len(reverselist) + (len(reverselist) - 2))


def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = ''); solve();
        
main()