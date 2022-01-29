s = input()
count = 0
for i in s:
    if i == i and i.isupper():
        count = count + 1

print(count + 1)