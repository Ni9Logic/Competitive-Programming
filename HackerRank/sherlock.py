for t in range(int(input())):
    n = int(input())
    a = [int(b) for b in input().split()]
    s = sum(a)
    count = 0
    for i in range(n):
        if 2*count == s-a[i]:
            print("YES")
            break
        count += a[i]
    else:
        print("NO")