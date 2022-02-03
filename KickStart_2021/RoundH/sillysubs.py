n = int(input())
for i in range(n):
    multiple = list(map(int, input().rstrip().split()))
    totallevels = multiple[0]
    atlevel = multiple[1]
    swordlevel = multiple[2]
    currenttime = atlevel - 1
    toreachsword = abs(atlevel - swordlevel) + 1
    toreachend = totallevels - swordlevel
    time1 = currenttime + toreachsword + toreachend
    time2 = 1 + totallevels + currenttime
    mintime = min(time1, time2)
    print("Case #{}: {}".format(i + 1, mintime))