import sys
input_str = sys.stdin.readline().strip('\n')

while input_str != '.':
    input_str = list(input_str.strip())
    stack = []

    for i in range(len(input_str)):
        if input_str[i] =='(' or input_str[i] =='[':
            stack.append(input_str[i])

        if input_str[i] ==')':
            if len(stack) == 0:
                stack.append(input_str[i])
                break
            elif stack[-1] == '[':
                break
            elif stack[-1] == '(':
                stack.pop()

        if input_str[i] ==']':
            if len(stack) == 0:
                stack.append(input_str[i])
                break
            elif stack[-1] == '(':
                break
            elif stack[-1] == '[':
                stack.pop()

    if len(stack) == 0:
        print('yes')
    else:
        print('no')
    input_str = sys.stdin.readline().strip('\n')