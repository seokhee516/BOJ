def solution(s):
    answer = True
    temp = 1
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        elif s[i] == ')':
            if not stack or stack[-1] != '(':
                answer = False
                break
            else:
                stack.pop()
    if stack:
        answer = False


    return answer