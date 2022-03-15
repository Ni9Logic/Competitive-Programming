def solve():
    multi_input1 = input().rstrip().split()
    
    amount_of_friends = int(multi_input1[0])
    total_days = int(multi_input1[1])
    
    gaps = list(map(int, input().rstrip().split()))
    grapes = []
    
    for i in range(0, amount_of_friends):
        for j in range(0, total_days, gaps[i]):
            grapes.append(j)
    
    
    maincounter = 0
    unique = list(dict.fromkeys(grapes))
    for i in unique:
        if grapes.count(i) == amount_of_friends:
            maincounter += 1
            
    print(maincounter)
        
def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = '')
        solve()
        
main()