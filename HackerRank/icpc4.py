def solve():
    n = int(input())
    denominations = [5000, 1000, 500, 200, 100, 50, 20, 10]
    counters = [int()] * len(denominations)
   
    if n >= 5000:
        counters[0] = n // 5000
        n = n % 5000
    if n >= 1000:
        counters[1] = n // 1000
        n = n % 1000
    if n >= 500:
        counters[2] = n // 500
        n = n % 500
    if n >= 200:
        counters[3] = n // 200
        n = n % 200
    if n >= 100:
        counters[4] = n // 100
        n = n % 100
    if n >= 50:
        counters[5] = n // 50
        n = n % 50
    if n >= 20:
        counters[6] = n // 20
        n = n % 20
    if n >= 10:
        counters[7] = n // 10
        n = n % 10
        
    start = 0
    for i in counters:
        if i > 0:
            start = counters.index(i)
            break
    
    for i in range(start, len(counters)):
        if i == len(counters) - 1:
            print(f"{counters[i]}x{denominations[i]}")
        else:
            print(f"{counters[i]}x{denominations[i]}", end = ', ')
        
    
def main():
    for i in range(int(input())):
        print(f"Case #{i+1}: ", end = '')
        solve()

main()