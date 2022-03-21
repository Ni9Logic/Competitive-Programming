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
    for nume in range(len(list3)):
        if list3[nume] == 25:
            Values.append("False")
        else:
            Values.append(list3[nume] in sums)
            print(Values[nume])
    

def main():
    for i in range(int(input())):
        solve()

main()