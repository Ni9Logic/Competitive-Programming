def solve():
    multiple_input = input().rstrip().split()
    n = int(multiple_input[0])
    p = int(multiple_input[1])
    Teams = []
    for i in range(n):
        Teams.append(list(map(int, input().rstrip().split())))
    
    for i in Teams:
        print(f"Team Stamp: {i[0]}, Team ID: {i[1]}, Problem ID: {i[2]}, Input ID: {i[3]}, Scored: {i[4]}")
    for i in enumerate(Teams):
        print(i)
def main():
    for i in range(int(input())):
     
        solve()

main()