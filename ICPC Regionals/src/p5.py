from math import log

def solve():
    nums = list(map(int, input().rstrip().split()))
    nums = sorted(nums)
    Ps = []
    for num in nums:
        Ps.append(log((num + 1) / num, 10) * 100)
    
    Os = []
    for num in nums:
        Os.append(num / sum(nums) * 100)
  
    diff = []
    for nume in range(len(nums)):
        diff.append(abs(Ps[nume] - Os[nume]))
        
    print(sum(diff))
def main():
    for i in range(int(input())):
        solve()

main()