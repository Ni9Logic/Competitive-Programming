def superReducedString(s):
    if len(s) == 1:
        return s
    
    ind = 1
    while ind < len(s):
        print("s[{}] = {} s = {}".format(ind, s[ind], s))
        if s[ind] == s[ind-1]:
            if len(s) == 2:
                return 'Empty String'
            s = s[:ind-1] + s[ind+1:]
            ind = 1
        else:
            ind += 1
            
    if len(s) == 0:
        return 'Empty String'
    else:
        return s

if __name__ == '__main__':
    s = input()
    result = superReducedString(s)
    print(result)