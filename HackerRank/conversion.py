def timeConversion(s):
    if s[-2] == 'A': #? If we have AM
        n = s[:2] #? N = first two characters of time!
        if n == "12": #? If if it's AM and time is 12 it should become 00:
            n = "00"
            n = n + s[2:-2] #? N will become 00:time:without AM/PM
            print(n)
        else:
            print(s[:-2]) #? If it's not 12 and it's AM then print the time without Am Pm
    else:
        n = s[:2] #? If it's PM!
        if (n == "12"):
            print(s[:-2]) #? If it's PM and time is 12 then there's no need for conversion just print the time without am/pm
        else:
            n = int(n) + 12         #? Other wise add + 12 and print it.
            n = str(n)
            if n == "24": #? If time is 24 then add 00 before like in AM
                n = "00"
            n = n + s[2:-2]
            print(n)

if __name__ == '__main__':
    s = input()

    timeConversion(s)