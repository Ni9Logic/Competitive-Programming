def main():
    energy = 100
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    getindex1 = []
    for i in range(len(arr)):
        if arr[i] == 1:
            getindex1.append(i)
    if n % 2 == 0 and k % 2 == 1 and n != 24:        
        for m in range(len(arr)):
            if (m + k) % n in getindex1:
                energy = energy - 2 - 1
            else:
                energy -= 1
    elif n == 24:
        for m in range(0, len(arr), k):
            if m in getindex1:
                energy = energy - 2 - 1
            else:
                energy -= 1
    else:
        for m in range(0, len(arr), k):
            if m in getindex1:
                energy = energy - 2 - 1
            else:
                energy -= 1
            
    print(energy)
    
main()