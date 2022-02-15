import numpy as np

def solve():
    board_col = int(input())
    board_row = board_col
    board = []
    for i in range(board_row):
        board.append(input().rstrip().split())
    
    board = np.array(board)
    board = board.reshape(board_col, 1)
    if len(board) == 1 and board[0][0] == '.':
        print("Nobody wins")
    elif len(board) == 1 and board[0][0] == 'B':
        print("Blue wins")
    elif len(board) == 1 and board[0][0] == 'R':
        print("Red wins")
    else:   
        impossible = 0
        for i in board:
            if i[-1][-1] == 'B' or i[-1][-1] == 'R':
                impossible += 1
        
        if impossible >= board_col - 1:
            print("Impossible")
        else:
            for i in board:
                if i[-1][-1] == 'B' and i[-1][-2] == 'B':
                    print("Blue Wins")
                    break
                elif i[-1][-1] == 'R' and i[-1][-2] == 'R':
                    print("Red Wins")
                    break
                    
            
        
            
def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = '')
        solve()

main()