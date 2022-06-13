from itertools import combinations_with_replacement as cr

def main():
    counter = 0
    List = list(range(1,2000))
    for p in range(2, 2000):
        combined = list(cr(List, p))
        for k in combined:
            if sum(k) % 5 == 0:
                counter += 1
            combined = list()
                
                
    print(counter)
   
   
main()