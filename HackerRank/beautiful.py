from math import ceil, floor

def solve():
    multiple = input().rstrip().split()
    size = int(multiple[0])
    k = int(multiple[1])
    arr = list(map(int, input().rstrip().split()))
    
    
    beautiful = []
    for i in range(size):
        for j in range(i + 1, size):
            if abs(arr[i] - arr[j]) == k:
                beautiful.append((arr[i], arr[j]))
    
    
                
def main():
    solve()
    
    
main()