numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

def solve(pw, n):
    counter = 0
    if not any(x in numbers for x in pw):
        counter += 1
    if not any(x in lower_case for x in pw):
        counter += 1
    if not any(x in upper_case for x in pw):
        counter += 1
    if not any(x in special_characters for x in pw):
        counter += 1

    if (len(pw) < 6):
        print(max(counter, abs(len(pw) - 6)))
    else:
        print(counter)

def main():
    n = int(input())
    pw = input()
    solve(pw, n)
    
main()