import string
def main():
    small = list(string.ascii_lowercase)
    
    #! The input replacing whitespaces with None and converting the string to lower so we can match with small
    s = input()
    s = s.replace(" ", "")
    s = s.lower()
    
    #! Here we are checking if every letter from list small is present in the string or not.
    pangram = True
    for i in small:
        if i not in s:
            pangram = False
            break
        
    #! Checking the bool pangram!
    if pangram:
        print("pangram")
    else:
        print("not pangram")

main()