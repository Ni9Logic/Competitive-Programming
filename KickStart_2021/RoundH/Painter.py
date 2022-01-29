from itertools import combinations
Color1 = ['U', 'R', 'Y', 'B', 'O', 'P', 'G', 'A']
Colors = list(combinations(Color1, 2))

print(len(Colors))