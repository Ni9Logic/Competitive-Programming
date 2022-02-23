def solve():
    COST = 0
    n = int(input())
    lists = []
    m = 0
    for i in range(1, n):
        m += i
        if m >= n:
            lists.append(m)
            break
        lists.append(m)

    if n in lists:
        D_s = [int(k) for k in range(1, len(lists) + 1)]
        print(*D_s)
    else:
        sums = 0
        anotherlist = []
        
        for m in range(1, len(lists) + 2):
            sums += m
            if sums >= n:
                anotherlist.append(m)
                break
            anotherlist.append(m % n)
            
        while(sum(anotherlist) != n):
            anotherlist[-1] -= 1
        
        print(*anotherlist)
            
       
def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = '')
        solve()

main()