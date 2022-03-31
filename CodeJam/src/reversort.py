def solve():
    n = int(input())
    lists = list(map(int, input().rstrip().split()))
    print(*lists)


def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = ''); solve();
        
main()