def main():
    for i in range(int(input())):
        n = int(input())
        cycle = 0
        height = 0
        for i in range(0, n + 1):
            if i == 0:
                height += 1
            elif cycle == 1:
                height *= 2
            elif cycle == 2:
                height += 1
                cycle = 0
            cycle += 1
        print(height)
main()