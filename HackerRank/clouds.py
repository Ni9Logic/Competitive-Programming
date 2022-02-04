def main():
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    jumps = -1
    for i in range(n):
       if i + 2 < n and arr[i+2] == 0:
           i = i + 2
       jumps += 1
            
    
    print(jumps )
    
main()