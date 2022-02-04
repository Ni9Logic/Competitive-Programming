def longestValidParentheses(s):
    if len(s) == 3:
        print("0 1")
        return
    stack = [-1]
    ans = 0
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            if stack and stack[-1]!=-1 and s[stack[-1]] == "(":
                stack.pop()
                ans = max(ans,i - stack[-1])
            else:
                stack.append(i)
    if (ans == None):
        print ('0 1')
    else:
        print (f"{ans} {len(stack) - 2}")
        
n = int(input())
for i in range(n):
    s = input()
    longestValidParentheses(s)