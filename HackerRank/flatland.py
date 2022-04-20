#! Solution is working but the code is sick worst code.
def main():
    n, m = list(map(int, input().rstrip().split()))
    print(n, m)
    indexes = list(map(int, input().rstrip().split()))
    if n == m:
        print(0)
        return
    distances = []
    
    for i in range(m):
        templist = []
        for j in range(len(indexes)):
            templist.append(abs(i - indexes[j])) 
        distances.append(templist)
    
    final = []
    for distance in distances:
        final.append(min(distance))
    
    print(max(final))
    
main() 