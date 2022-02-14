import sys
from collections import deque

T = int(sys.stdin.readline().strip())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().strip().split())
    lst = [[0] * (M) for _ in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().strip().split())
        lst[y][x] = 1

    # bfs 탐색
    queue = deque()
    cnt = 0
    for i in range(M):
        for j in range(N):
            if lst[j][i] == 1:
                cnt += 1
                queue.append([i,j])
                while queue:
                    v = queue.popleft()
                    a = v[0]
                    b = v[1]
                    lst[b][a] = 0
                    # 네 방향 확인, 범위 제한
                    if a+1<M and lst[b][a+1] == 1: # 우
                        queue.append([a+1, b])
                        lst[b][a+1] = 0
                    if a-1>=0 and lst[b][a-1] == 1: # 좌
                        queue.append([a-1, b])
                        lst[b][a-1] = 0
                    if b-1>=0 and lst[b-1][a] == 1: #상
                        queue.append([a, b-1])
                        lst[b-1][a] = 0
                    if b+1<N and lst[b+1][a] == 1: # 하
                        queue.append([a, b+1])
                        lst[b+1][a] = 0  
    print(cnt)