n = int(input())
for i in range(n):
    size = int(input())
    a = list(map(int, input().split()))
    a.sort()
    midpoint = size // 2
    a[midpoint], a[-1] = a[-1], a[midpoint]
    a[midpoint:] = sorted(a[midpoint:], reverse=True)

    print(*a, end = '')
