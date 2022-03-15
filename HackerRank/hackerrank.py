from collections import OrderedDict
def solve():
    s = input()
    unique = list(OrderedDict.fromkeys(s))
    words_i_need = ['h', 'a', 'c', 'k', 'e', 'r', 'a', 'n', 'k']
    for i in unique:
        if i not in words_i_need:
            unique.remove(i)

    newb = False
    for j in unique:
        if j in words_i_need:
            newb = True
        else:
            newb = False
            break
    
    if newb:
        print("YES")
    else:
        print("NO")
        
            
            

def main():
    for i in range(int(input())):
        solve()
    
main()