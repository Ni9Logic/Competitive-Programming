def main():
    mul = input().rstrip().split()
    if (mul[0] == '1' and mul[1] == '1'): print(0); return
    chess = []
    for i in range(int(mul[0])):
        chess.append([False for x in range(int(mul[1]))])
    
    end = False
    counter = 0
    r = 0
    c = 0
    
    start_pos = None
    turn = False
    print(r, c)
    while not end:
        if start_pos is None:
            if r + 2 < len(chess) and c + 1 < len(chess[0]):
                r += 2
                c += 1
            else:
                r += 1
                c += 2
            start_pos = (r, c)
        else:
            if r + 2 < len(chess) and c + 1 < len(chess[0]) and not chess[r + 2][c + 1]:
                r += 2
                c += 1
                counter += 1
                chess[r][c] = True
                print(r, c)
            if r + 1 < len(chess) and c + 2 < len(chess[0]) and not chess[r + 1][c + 2]:
                r += 1
                c += 2
                counter += 1
                chess[r][c] = True
                print(r, c)
            if r + 2 < len(chess) and c - 1 >= 0 and not chess[r + 2][c - 1]:
                r += 2
                c -= 1
                counter += 1
                chess[r][c] = True
                print(r, c)
            if r + 1 < len(chess) and c - 2 >= 0 and not chess[r + 1][c - 2]:
                r += 1
                c -= 2
                counter += 1
                chess[r][c] = True
                print(r, c)
            if r - 2 >= 0 and c + 1 < len(chess[0]) and not chess[r - 2][c + 1]:
                r -= 2
                c += 1
                counter += 1
                chess[r][c] = True
                print(r, c)
            if r - 1 >= 0 and c + 2 < len(chess[0]) and not chess[r - 1][c + 2]:
                r -= 1
                c += 2
                counter += 1
                chess[r][c] = True
                print(r, c)
            else:
                if start_pos == (r, c):
                    end = True
                else:
                    print(counter)
                    return
    
    print(counter)
       
        
main()