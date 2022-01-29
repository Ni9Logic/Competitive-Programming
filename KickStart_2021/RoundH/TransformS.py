def f(S, F):
    def get_distance(s, f):
        start = min(ord(s), ord(f))
        end = max(ord(s), ord(f))
        return min(start + 26 - end, end - start)

    
    def get_distances(s, F):
        return [get_distance(s, f) for f in F]
        
    count = 0
    for s in S:
        distances = get_distances(s, F)
        count += min(distances)
    return count

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        F = input()
        ans = f(S, F)
        print (f'Case #{i+1}: {ans}')