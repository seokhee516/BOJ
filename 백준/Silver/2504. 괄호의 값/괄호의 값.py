import sys
input = sys.stdin.readline
string = input().strip()
temp = 1
answer = 0
stack = []
for i in range(len(string)):
    if string[i] == '(':
        temp *= 2
        stack.append('(')
    elif string[i] == '[':
        temp *= 3
        stack.append('[')
    elif string[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        elif string[i-1] == '(':
            answer += temp
        temp //= 2
        stack.pop()
    elif string[i] == ']':
        if not stack or stack[-1] == '(':
            answer = 0
            break
        elif string[i-1] == '[':
            answer += temp
        temp //= 3
        stack.pop()
if stack:
    answer = 0
print(answer)