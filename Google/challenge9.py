def solve():
    n = input().rstrip()
    lists = []
    lists.append(n)
    
    for i in range(1, 9 + 1):
        lists.append(str(i))
        
    for k in range(1, len(lists)):
        if int(lists[k] + lists[0]) % 9 == 0 or int(lists[0] + lists[k]) % 9 == 0:
            print(min(int(lists[k] + lists[0]), int(lists[0] + lists[k])))
    


def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = ''); solve();
        
main()