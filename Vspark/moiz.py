from itertools import combinations_with_replacement as cr

def main():
    counter = 0
    List = list(range(1,2000))
       
    combined = list(cr(List, 2))
    for k in combined:
        if sum(k) % 5 == 0:
            counter += 1
        combined = list()
            
            
    print(counter)
   
   
main()