def solve():
    #! ---------------(INPUT)------------------------
    
    multiple_input = input().rstrip().split()
    friends = int(multiple_input[0])
    dislikes_amount = int(multiple_input[1])
    binaries = int(multiple_input[2])
    orders = []
    not_available = []
    for i in range(friends):
        orders.append(input())
    for k in range(dislikes_amount):
        not_available.append(input())
        
    #! ---------------(INPUT)------------------------

        

    print(orders)

def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = '')
        solve()

main()