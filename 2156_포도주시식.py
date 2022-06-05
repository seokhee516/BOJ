import sys
input = sys.stdin.readline
n = int(input())
w = [0]
for i in range(n):
    w.append(int(input())) # 포도주 양 입력
d = [0]
d.append(w[1]) # n이 1일때
if n>1: # n이 2 이상일때 (n==2일때 포함, n==3, 4, 5 ...일때)
    d.append(w[1]+w[2])
for i in range(3, n+1):
    # 바로 전, 전전 + 현재, 전전전 + 전 + 현재
    d.append(max(d[i-1], d[i-2]+w[i], d[i-3]+w[i-1]+w[i]))

print(d[n])