import numpy as np

def solve():
    multiple_input = list(map(int, input().rstrip().split()))
    
    #? Matrix1 Row Columns
    matrix1_row = multiple_input[0]
    matrix1_col = multiple_input[1]
    
    #? Matrix2 Row Columns
    matrix2_row = int(multiple_input[matrix1_row * matrix1_col + 2])
    matrix2_col = int(multiple_input[matrix1_row * matrix1_col + 3])
    
    #? Matrix1 Formed
    matrix1 = multiple_input[2:matrix1_row * matrix1_col + 2]
    matrix1 = np.array([matrix1])
    matrix1 = matrix1.reshape(matrix1_row, matrix1_col)
    
    #? Matrix2 Formed
    matrix2 = multiple_input[matrix1_row * matrix1_col + 4:]
    matrix2 = np.array([matrix2])
    matrix2 = matrix2.reshape(matrix2_row, matrix2_col)
    
    #? Algorithm
    if (matrix1_col != matrix2_col):
        print("Not Possible")
    elif matrix1_row != matrix2_col:
        matrix2 = matrix2.transpose()
        matrix3 = matrix1.dot(matrix2)
        print(matrix3.sum())
       

def main():
    for i in range(int(input())):
        print(f"Case #{i+1}: ", end = '')
        solve()
    
main()