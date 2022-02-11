def main():
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    digits = [x for x in range(100)]
    counts = [int()] * 100
    
    for i in arr:
        if i in digits:
            counts[digits.index(i)] += 1
            
    print(*counts)
    
main()