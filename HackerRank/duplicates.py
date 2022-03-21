def main():
    arr = list(map(int, input().rstrip().split()))
    newlist = list(dict.fromkeys(arr))
    print(len(newlist))
    
main()
