def main():
    n = int(input())
    for i in range(n):
        s = list(input())
        
        original_copy = s
        reverse_string = s[::-1]
        reverse_string = list(reverse_string)
        reverse_copy = reverse_string
        
        for i in range(len(original_copy)):
            if reverse_copy == original_copy:
                print(-1)
                break
            else:
                reverse_copy.remove(original_copy[i])
                original_copy.remove(-(i + 1))
                print(reverse_copy, original_copy)
                
main()