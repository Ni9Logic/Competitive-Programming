import numpy as np

def solve():
    multiple_input = input().rstrip().split()
    rows = int(multiple_input[0])
    cols = int(multiple_input[1])
    keyboard = list(map(int, multiple_input[2:]))
    anotherkey = [int()] * ((rows * cols) + 1)
    print(keyboard)

def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = '')
        solve()
    
    
main()