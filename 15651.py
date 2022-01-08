import sys
N, M = map(int, sys.stdin.readline().split(' '))

num = []
def recur(N=N, M=M):
    if len(num) == M:
        print(' '.join(map(str, num)))
        return
    for i in range(1, N+1):
        num.append(i)
        recur()
        num.pop() # [1,4] 끝나고 왜 이리로 오는거지?
recur()

