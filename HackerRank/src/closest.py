def main():
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    
    difference = []
    
    for i in range(0, n):
        for j in range(i+1, n):
            difference.append([max(arr[i], arr[j]) - min(arr[i], arr[j]), arr[i], arr[j]])
            
        
    print(min(min(difference)[1], min(difference)[2]), max(min(difference)[1], min(difference)[2]))
    
    
main()