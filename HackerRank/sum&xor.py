def main():
    n = int(input())
    n_bin = bin(n).replace('0b', '')
    if (n == 0):
        print(1)
        return
    res = 1
    for digit in n_bin:
        if digit == "0":
           res *= 2
    
    print(res) 
    
main()