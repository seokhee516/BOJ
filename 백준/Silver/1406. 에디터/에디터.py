import sys
input = sys.stdin.readline
st1 = list(input().strip())
st2 = []
t = int(input())
for _ in range(t):
    op = list(input().split())
    if op[0] == 'L' and st1:
        st2.append(st1.pop())
    elif op[0] == 'D' and st2:
        st1.append(st2.pop())
    elif op[0] == 'B' and st1:
        st1.pop()
    elif op[0] == 'P':
        st1.append(op[1])
st1.extend(reversed(st2))
print(''.join(st1))