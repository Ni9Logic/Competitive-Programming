n = int(input())
s = input()
s = list(s)
k = int(input())
lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
lower = list(lower)
upper = list(upper)
for i in range(0, k):
   lower.append(lower[i])
   upper.append(upper[i])
for i in range(0, k):
    lower.pop(0)
    upper.pop(0)
for i in s:
    if i in lower or i in upper:
        if i.isupper():
            if (upper.index(i) + k > 26):
                index = abs(upper.index(i) + k - 26)
                print(upper[index], end ='')
            else:
                print(upper[upper.index(i) + k], end ='')
            
        elif i.islower():
            if (lower.index(i) + k > 26):
                index = abs(lower.index(i) + k - 26)
                print(lower[index], end ='')
            else:
                print(lower[lower.index(i) + k], end ='')
    else:
        print(i, end ='')
