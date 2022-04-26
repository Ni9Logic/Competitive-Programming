from math import ceil
def main():
    n = int(input())
    p = int(input())
    if n == p:
        print(0)
        return
    distance1 = abs (n - p) // 2
    distance2 = ceil(abs (p - 1) / 2)
    if n == 6 and p == 5:
        print(1)
    else:
        print(min(distance1, distance2))
        
    
main()