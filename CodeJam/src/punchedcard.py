def solve():
    cols_rows = list(map(int, input().rstrip().split())) #! rows = row_cols[1]
    newrow = (2 * cols_rows[1]) + 1
    newcol = (2 * cols_rows[0]) + 1
    
    lists = []
    for i in range(newcol):
        for j in range(newrow):
            if i == 0 and j < 2:
                lists.append('.')
            elif i == 0 and j > 1:
                if j % 2 == 0:
                    lists.append('+')
                else:
                    lists.append('-')
            if i == 1 and j < 2: 
                lists.append('.')
            elif i == 1 and j > 1:
                if j % 2 == 0:
                    lists.append('|')
                else:
                    lists.append('.')
            if i > 1 and i % 2 == 0:
                if j % 2 == 0:
                    lists.append('+')
                else:
                    lists.append('-')
            elif i > 1 and i % 2 == 1:
                if j % 2 == 0:
                    lists.append('|')
                else:
                    lists.append('.')
    
    counter = 0
    for i in range(len(lists)):
        print(lists[i], end = '')
        counter += 1
        if counter % newrow == 0:
            print("")
            
            
                 
    

def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = '\n'); solve();
        
main()