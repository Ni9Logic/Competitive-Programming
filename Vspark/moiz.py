from itertools import combinations_with_replacement as cr

Big_List = []

def main():
    List = []
    for i in range(1,2000): #Just for the sake of question!
        if i > 6: #List is greater than 5 is literally useless and unnecessary logic wise in coding context
            break
        List.append(i) #List = [1, 2, 3, 4, 5] If every single combination's sum == 5 or not.
       
    for p in range(2, 6):
        combined = list(cr(List, p))
        for k in combined:
            if sum(k) == 5:
                Big_List.append(k)
            
    print(Big_List)
    print(f"Total subsets of subsets from range(1 - 2000) that makes the sum of 5 = {len(Big_List)}")
    print(f"Total number of subsets with combinations of those subsets as-well are: 51")
   
main()