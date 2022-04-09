def solve():
    lists = list(map(str, input().rstrip()))
    for char in lists:
       print(lists.count(char))
    
    print(lists)

def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = ''); solve();
        
main()