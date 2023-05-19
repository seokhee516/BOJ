def isBalance(arr):
    if arr.count('(') == arr.count(')'):
        return True
    else:
        False
def isTrue(arr):
    stack = []
    for a in arr:
        if a == '(':
            stack.append(a)
        else:
            if not stack:
                return False
            elif stack[-1] == '(':
                stack.pop()
    return False if stack else True

def solution(p):
    if not p: return p
    answer = ''
    for i in range(len(p)):
        if isBalance(p[:i+1]):
            u = p[:i+1]
            v = '' if i == len(p)-1 else p[i+1:]
            break
    if isTrue(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        for i in u[1:-1]:
            if i == ')':
                answer += '('
            else:
                answer += ')'
    return answer