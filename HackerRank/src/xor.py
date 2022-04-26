def main():
    string1 = list(input())
    string2 = list(input())
    finalstring = ""
    for i, j in zip(string1, string2):
        if int(i) == 1 and int(j) == 0:
            finalstring = finalstring + '1'
        elif int(i) == 0 and int(j) == 1:
            finalstring = finalstring + '1'
        elif int(i) == int(j):
            finalstring = finalstring + '0'
        
    print(finalstring)

main()