def solve():
    counter = 0
    string1 = input().rstrip()
    string2 = input().rstrip()
    
    string1_unique = list(dict.fromkeys(string1))
    string2_unique = list(dict.fromkeys(string2))
    
    if len(string1) == len(string2) and len(string1_unique) != len(string2_unique):
            print("IMPOSSIBLE")
    else:
        counter1 = len(string2)
        while counter1 > len(string1):
            string1 = ''.join([string1[i] for i in range(len(string1)) if i != string1[-1]])
            counter += 1
            counter1 -= 1
            
        print(counter)


def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end=''); solve();
        
        
main()