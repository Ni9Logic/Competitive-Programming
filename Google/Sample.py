
def main():
    n = int(input())
    likes = []
    dislikes = []
    for i in range(n):
        likes_input = input().rstrip().split()
        for i in range(1, len(likes_input)):
            likes.append(likes_input[i])
        dislikes_input = input().rstrip().split()
        for i in range(1, len(dislikes_input)):
            dislikes.append(dislikes_input[i])
        
    finalorder = []
    for i in likes:
        if i not in dislikes:
            finalorder.append(i)

    finalorder = list(dict.fromkeys(finalorder))
    finalorder.insert(0, len(finalorder))
    print(*finalorder)
if __name__ == '__main__':
    main()