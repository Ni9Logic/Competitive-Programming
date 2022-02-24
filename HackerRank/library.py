def main():
    multiple = input().rstrip().split()
    multiple2 = input().rstrip().split()
    #! --------------------
    d1 = int(multiple[0])
    m1 = int(multiple[1])
    y1 = int(multiple[2])
    #! --------------------
    d2 = int(multiple2[0])
    m2 = int(multiple2[1])
    y2 = int(multiple2[2])
    #! --------ALGO---------
    FINE = 0
    if d1 <= d2 and m1 <= m2 and y1 <= y2:
        print(FINE)
    elif y1 < y2:
        print(FINE)
    elif d1 > d2 and m1 > m2 and y1 < y2:
        print(FINE)
    elif m1 < m2 and y1 <= y2:
        print(FINE)
    elif d1 > d2 and m1 == m2 and y1 == y2:
        print(FINE + (15 * abs (d1 -d2)))
    elif m1 > m2 and y1 == y2:
        print(FINE + (500 * abs(m1 - m2)))
    elif y1 > y2:
        print(10000)

main()