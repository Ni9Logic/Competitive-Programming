def isPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False

    return True

def solve():
    multiple_input = input().rstrip().split()
    x = int(multiple_input[0])
    y = int(multiple_input[1])
    if isPrime(x) and isPrime(y):
        print(x + y)
    elif not isPrime(x) and isPrime(y):
        print(x * y)
    elif isPrime(x) and not isPrime(y):
        print(x * y)
    elif not isPrime(x) and not isPrime(y):
        print("not possible")


def main():
    for i in range(int(input())):
        print(f"Case #{i+1}: ", end = '')
        solve()

main()