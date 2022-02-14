def superdigit(n, k):
    n = str(n) * k
    n = int(n)
    while n > 10:
        n = str(n)
        arr = []
        for i in n:
            arr.append(int(i))

        n = sum(arr)
    print(n)

if __name__ == '__main__':
    multiple_input = input().rstrip().split()
    n = int(multiple_input[0])
    k = int(multiple_input[1])
    superdigit(n, k)