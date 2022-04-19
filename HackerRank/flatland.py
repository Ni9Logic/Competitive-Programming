def main():
    mulinput = list(map(int, input().rstrip().split()))
    cities = mulinput[0]
    stations = mulinput[1]

    indexes = list(map(int, input().rstrip().split()))
    if len(indexes) == cities:
        print(0)
        return
    distances = []
    
    for i in range(cities):
        for j in range(len(indexes)):
                distances.append(abs(i - indexes[j]))
    
    final = []
    for i in distances:
        final.append((distances.count(i), i))
        
    print(max(final[1]))
    
    
main()