import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    A = sys.stdin.readline().strip().split(' ')
    if A[0] =='push':
        stack.append(A[1])
    elif A[0] =='top':
        try:
            print(stack[-1])
        except:
            print(-1)
    elif A[0] =='size':
        print(len(stack))
    elif A[0] =='empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif A[0] =='pop':
        try:
            if len(stack) != 0:
                print(stack.pop())
            else:
                print(-1)
        except:
            print(-1)
