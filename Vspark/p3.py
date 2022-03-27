def main():
    n = int(input())
    error = False
    for i in range(n):
        top = input().strip().split()
        bottom = input().strip().split()
        rt = int(top[0])
        ct = int(top[1])
        rb = int(bottom[0])
        cb = int(bottom[1])
        
        if rt >= rb or ct >= cb:
            error = True
            
    if error:
        print("syntax error")

if __name__ == '__main__':
    main()