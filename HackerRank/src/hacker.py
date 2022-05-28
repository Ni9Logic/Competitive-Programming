from collections import OrderedDict as od

def solve():
    to_find = "hackerrank"
    s = list(input())
    s = list(od.fromkeys(s))
    for alpha in s:
        print((alpha, s.count(alpha)), end = ' ')

def main():
    for i in range(int(input())):
        solve()
        
main()