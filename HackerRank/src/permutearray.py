def main():
    n = int(input()) #! Queries
    
    for i in range(n):
        multiple = input().rstrip().split()
        p = int(multiple[0])
        q = int(multiple[1])
        
        list1 = list(map(int, input().rstrip().split()))
        list2 = list(map(int, input().rstrip().split()))
        
        #? Some how list 1 was supposed to be sorted in ascending order and list2 in descending order i don't know why tho
        list1.sort()
        list2 = sorted(list2, reverse=True)
        
        #? We use zip function for i, j to form shape like [i, j] if the matrix is square eg 2x2 or 3x3 or 4x4 
        condition = False
        for i, j in zip(list1, list2):
            if i + j < q:
                condition = True

        #? Just checking boolean values
        if condition:
            print("NO")
        else:
            print("YES")
       
                
        
    
    
main()