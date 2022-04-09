def insert_in_string(string, index, string2):
    return string[:index] + string2 + string[index:]

def solve():
    lists = input()
    for i in range(len(lists)):
        if lists.count(lists[i]) % 2 == 0:
            newlists = insert_in_string(lists, lists.index(lists[i]), lists[i])
            
    print(newlists)

def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = ''); solve();
        
main()