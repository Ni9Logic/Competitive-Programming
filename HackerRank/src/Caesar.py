import string

symbols_low = string.ascii_lowercase
symbols_up = string.ascii_uppercase
lists = [x for x in range(100)]

n = int(input())
s = input()
s = list(s)
k = int(input())
res = []
for i in s:
    if i.isupper():
        res.append(symbols_up[(symbols_up.index(i) + k) % len(symbols_up)])
    elif i.islower():
        res.append(symbols_low[(symbols_low.index(i) + k) % len(symbols_low)])
    else:
        res.append(i)
hellowrod = "string"
s = "".join(res)   
print(s)
