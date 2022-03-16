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
        
    print(coordinates)
    print(mouse_travelled)
    print(targets)
    
    
        
def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = '')
        solve()
        
main()