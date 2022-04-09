    def solve():
        mul = input().rstrip().split()
        s = input()
        
        goodness = int(mul[1])
        
        counter = 0
        for i in range(len(s)):
            try:
                if s[i] != s[i + 1]:
                    goodness -= 1
                    if goodness == 0:
                        break
                    counter += 1
                
                
            except IndexError:
                pass
                
        print(counter)

    def main():
        for i in range(int(input())):
            print(f"Case #{i + 1}: ", end= ''); solve();
            
            
    main()