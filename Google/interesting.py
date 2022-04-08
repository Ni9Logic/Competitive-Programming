import functools
import operator

def solve():
    multiple = input().rstrip().split()
    start = int(multiple[0])
    end = int(multiple[1]) + 1
    
    counter = 0
    for i in range(start, end):
        strings = list(map(int, str(i)))
        sumsList = sum(strings)
        prodList = functools.reduce(operator.mul, strings)
        if prodList % sumsList == 0:
            counter += 1    
                       
    print(counter)
        
        
def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end= ''); solve();
        
        
main()