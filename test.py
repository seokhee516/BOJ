from collections import deque
M = 4
N = 5
lst = [[0, 1, 1, 1],
[0, 1, 0, 1],
[0, 0, 0, 0],
[0, 1, 1, 0],
[0, 0, 0, 0]]

# bfs
queue = deque()
cnt = 0
for i in range(M):
    for j in range(N):
        if lst[j][i] == 1:
            cnt += 1
            queue.append([i,j])
            while queue:
                v = queue.popleft()
                a = v[0] # 1
                b = v[1] # 0
                lst[b][a] = 0
                if a+1<M and lst[b][a+1] == 1: # 우
                    queue.append([a+1, b])
                    lst[b][a+1] = 0
                if a-1>=0 and lst[b][a-1] == 1: # 좌
                    queue.append([a-1, b])
                    lst[b][a-1] = 0
                if b-1>=0 and lst[b-1][a] == 1: # 상
                    queue.append([a, b-1])
                    lst[b-1][a] = 0
                if b+1<N and lst[b+1][a] == 1: # 
                    queue.append([a, b+1])
                    lst[b+1][a] = 0  
print(cnt)