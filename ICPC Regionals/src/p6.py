from itertools import combinations

def solve():
    Tree = list(map(int, input().rstrip().split()))
    lists = []
    for j in range(2, len(Tree)):
        lists.append(list(combinations(Tree, j)))
    
        
    sums = []
    for num in lists:
        for n in num:
            sums.append(sum(n))
            
    list2 = list(map(int, input().rstrip().split()))
    list3 = list(map(int, input().rstrip().split()))
   
    Values = []
    for nume in list3:
        Values.append(nume in sums)
        
    for value in Values:
        print(value)
   

def main():
    for i in range(int(input())):
        solve()

main()