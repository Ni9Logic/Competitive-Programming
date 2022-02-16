def solve():
    multiple_input = input().rstrip().split()
    p1h = int(multiple_input[0])
    p1a = int(multiple_input[1])
    p1d = int(multiple_input[2])
    p2h = int(multiple_input[3])
    p2a = int(multiple_input[4])
    p2d = int(multiple_input[5])
    if p1a < p2d and p2a > p1d:
        print(2)
        return
    if p2a < p1d and p1a > p2d:
        print(1)
        return
    if p1a <= 0 and p2a <= 0:
        print(0)
        return
    if p1a <= p2d and p2a <= p1d:
        print(0)
        return
    if p1h == p2h and p1a == p2a and p1d == p2d:
        print(0)
        return

    #! --Algo--
    p1_counter = 1
    p2_counter = 1
    while(p1h >= 0):
        p1h = p1h - (abs(p2a - p1d))
        p1_counter += 1
    
    while(p2h >= 0):
        p2h = p2h - (abs(p1a - p2d))
        p2_counter += 1
    
    if p1_counter == p2_counter:
        print(0)
    elif p1_counter > p2_counter:
        print(1)
    elif p2_counter > p1_counter:
        print(2)
        
    

def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = '')
        solve()

main()