def main():
    width_cases = input().rstrip().split()
    widths = list(map(int, input().rstrip().split()))
    
    
    for i in range(int(width_cases[1])):
        case = list(map(int, input().rstrip().split()))
        
        print(min(widths[case[0] : case[1] + 1])) #? lol this is the solution wtf!
        
        

main()