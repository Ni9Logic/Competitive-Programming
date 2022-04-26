n = int(input())
for i in range(n):
    s = input()
    if s.count('0') == s.count('1'):
        print(0)
    else:
        print(min(s.count('0'), s.count('1')))