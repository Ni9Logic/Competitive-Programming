from itertools import zip_longest
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [30, 40, 50, 60]
zipped = list(zip(a,b,c))
print(zipped[0][2])