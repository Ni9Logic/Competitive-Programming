def isKapri(a):
    square = a**2
    square = str(square)
    if a < 10:
        if len(square) >= 2:
            if int(square[0]) + int(square[1]) == a:
                return True
        else:
            if (int(square) == a):
                return True
    else:
        squarehalf = len(square) // 2
        if (int(square[squarehalf:]) + int(square[:squarehalf]) == a):
            return True
    
    
def main():
    n = int(input())
    p = int(input())
    found = False
    for i in range(n, p + 1):
        if isKapri(i):
            found = True
            print(i, end = ' ')

    if not found:
        print("INVALID RANGE")
        
main()