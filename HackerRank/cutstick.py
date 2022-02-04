n = int(input())
arr = list(map(int, input().rstrip().split()))
for i in range(len(arr)):
    if not len(arr) == 0: #* because when len is zero there's no element there for min(arr)
        mini = min(arr)
        print(len(arr)) #* 6 4 2 1
        for j, i in enumerate(arr):
            arr[j] = arr[j] - mini #* 5 4 4 2 2 8 = 5 2 2 0 0 6
        for l in range(arr.count(0)): #* now count zero's = 2 , arr = [5 2 2 6]
            arr.remove(0)