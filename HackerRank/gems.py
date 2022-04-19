
import string

def solve():
    n = int(input())
    alphas = list(string.ascii_lowercase) #? Set of lower case letters
    lists = [] #? Useful list!
    
    for i in range(n): #? Just appending the strings
        lists.append(input().rstrip())
        
    counter = 0 #? Child Counter
    megacounter = 0 #? Actual Counter
    
    for char in alphas: #? For characters in alphabets
        counter = 0 #? Every time the character switches counter is set to zero to avoid repetition.
        
        for strings in lists: #? Strings in the list
            if char in strings: #? If character present in the above set of characters/alphabets.
                
                counter += 1 #? Counter increments by one for-example [char = 'a', string = 'abcdde', counter = '1'] 
                if counter == n: #? Now if counter == amount of strings we have it means its present in all of the strings.
                    megacounter += 1 #? Mega counter increments 
                    break #? Its present in all the lists so its time to switch the character
                
    print(megacounter)
                
def main():
    solve()
        
main()