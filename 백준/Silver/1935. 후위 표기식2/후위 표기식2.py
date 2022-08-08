import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
d = {}
for i in range(n):
    d[chr(i+65)] = int(input())
oper = ['+', '-', '*','/']
stack = []
for j in range(len(s)):
    if s[j] not in oper: # 피연산자인경우
        stack.append(d[s[j]])
    if s[j] == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    if s[j] == '-': 
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a) # 곱셈과 뺄셈은 순서가 중요하다
    if s[j] == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
    if s[j] == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b/a)
print("{:.2f}".format(stack[0]))
'''
5
ABC*+DE/-
1
2
3
4
5
((2*3)+1)-(4/5)
'''