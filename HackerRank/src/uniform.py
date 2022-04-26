import string

lowercase = list(string.ascii_lowercase)
counter = 26

newList = []
for q in reversed(range(0, len(lowercase))):
    newList.append([lowercase[q], counter])
    counter -= 1

newList = list(reversed(newList))


def main():
    string1 = input().strip()
    n = int(input().strip())
    string2 = string1
    weights = []
    
    for l in range(n):
        b = int(input())
        weights.append(b)
        
        
        
        
    string2 = list(dict.fromkeys(string2))
    string2.pop()
    counters = []
    for count in string2:
        counters.append(string1.count(count))
        
        
    oursums = []
    for k in range(len(string2)):
        for u, o in enumerate(newList):
            if string2[k] in o:
                if counters[k] >= 2:
                    while (counters[k]) >= 1:
                        oursums.append(o[1] * counters[k])
                        counters[k] -= 1
                else:
                    oursums.append(o[1] * counters[k])
         
   
    oursums = sorted(oursums)
    weights = sorted(weights)     
    print(oursums)  
    print(weights)
    for weight in weights:
        print("Yes" if weight in weights else "No")
                        
            
main()