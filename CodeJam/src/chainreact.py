def solve():
    n = int(input())
    units = list(map(int, input().rstrip().split()))
    powers = list(map(int, input().rstrip().split()))
    
    newlist = [[x, y] for x, y in zip(units, powers)]


def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = '\n'); solve();
        
main()