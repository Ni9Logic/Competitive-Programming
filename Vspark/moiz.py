from itertools import combinations_with_replacement as cr

Big_List = []

def main():
    List = list(range(1,2000))
       
    for p in range(2, 2000):
        combined = list(cr(List, p))
        for k in combined:
            if sum(k) % 5 == 0:
                print(k)
                Big_List.append(k)
                
                
        combined = list()
            
    print(Big_List)
    print(f"Total subsets of subsets from range(1 - 2000) that makes the sum of 5 = {len(Big_List)}")
    print(f"Total number of subsets with combinations of those subsets as-well are: 51")
   
main()