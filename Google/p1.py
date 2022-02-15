def solve():
    multiple_input = input().rstrip().split()
    kids = int(multiple_input[0])
    bags = int(multiple_input[1])
    candies = list(map(int, input().rstrip().split()))
    totalcandies = sum(candies)
    candies_get = totalcandies // bags
    print(totalcandies - bags * candies_get)
        


def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = '')
        solve()

main()