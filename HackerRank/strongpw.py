numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
n = int(input())
s = input()
count = 0
for i in s:
    if len(s) < 6:
        print(6 - len(s))
        break
        
print(count)