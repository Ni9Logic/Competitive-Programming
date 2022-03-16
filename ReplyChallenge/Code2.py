def solve():
    DISTANCE = 0
    row_cols = input().rstrip().split()
    coordinates = []
    for i in range(int(row_cols[0])):
        for j in range(int(row_cols[1])):
            coordinates.append((i, j))
    
    mouse_travelled = []
    targets = []
    
    for i in range(int(row_cols[0])):
        row_cols_target = input().rstrip().split()
        mouse_travelled.append((int(row_cols_target[0]), int(row_cols_target[1])))
        targets.append(int(row_cols_target[2]))
        
    COUNTER = 0
    for i in range(len(mouse_travelled)):
        COUNTER += coordinates.index(mouse_travelled[i])
        DISTANCE += abs(DISTANCE - COUNTER)
        DISTANCE -= targets[i]
        
             
    print(coordinates)
    print(mouse_travelled)
    print(targets)
    print(DISTANCE)
    
        
def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = '')
        solve()
        
main()