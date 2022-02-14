def solve():
    multiple_input = input().rstrip().split()
    size = int(multiple_input[0])
    arr = multiple_input[2:]
    for i in range(len(arr)):
        arr[i] = int(arr[i])
        
    anotherlist = []
    counter = 0
    for i in range(len(arr)):
        if counter > 7:
            break
        elif i == len(arr) - 1:
            anotherlist.append(arr[i])
            counter += 1
        elif arr[i] < arr[i + 1]:
            anotherlist.append(arr[i])
    
    print(len(anotherlist), end = ' ')
    print(*anotherlist)
                
def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = '')
        solve()

main()