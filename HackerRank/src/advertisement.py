def main():
    PEOPLE = 5
    LIKED = 0
    peopleslist = []
    days = int(input())
    for i in range(1, days + 1):
        LIKED = PEOPLE // 2
        peopleslist.append(LIKED)
        PEOPLE = LIKED * 3
    
    print(sum(peopleslist))
            
    
main()