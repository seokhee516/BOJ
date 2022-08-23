def solution(s):
    def rotate(lst, n):
        return lst[n:] + lst[:n]
    def is_correct(lst):
        stack = []
        for l in lst:
            if l == '[' or l == '(' or l == '{':
                stack.append(l)
            else:
                if not stack:
                    return False
                elif l == ']':
                    if stack.pop() != '[':
                        return False
                elif l == ')':
                    if stack.pop() != '(':
                        return False
                elif l == '}':
                    if stack.pop() != '{':
                        return False
        if stack:
            return False
        return True
    answer = 0
    for _ in range(len(s)):
        if is_correct(s):
            answer += 1
        s = rotate(s, 1)
    
    return answer