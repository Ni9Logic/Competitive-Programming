def main():
    arr = list(map(int, input().rstrip().split()))
    sums = []
    for i in range(len(arr)):
        sume = 0
        for j in range(len(arr)):
            if j == i:
                break
            sume += arr[i]
        sums.append(sume)
        
    print(sums)

main()