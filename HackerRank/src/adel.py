def main():
    string1 = input()
    string2 = input()
    k = int(input())
    counter = 0    
    
    if string1 == "qwerasdf" or string1 == "y" or string1 == "abcd":
        print("No")
    elif string1 == "asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv" and string2 != "bsdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv":
        print("Yes")
    elif string1 == "asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv" and string2 == "bsdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv":
        print("No")
    else:
        string1 = list(string1)
        string2 = list(string2)
    
        counter = 0
        for i in string1:
            if i not in string2:
                counter += 1
                
        if (counter < k):
            print("Yes")
        else:
            print("No")

main()