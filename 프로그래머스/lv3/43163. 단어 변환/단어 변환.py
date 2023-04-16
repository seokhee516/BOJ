from collections import deque
def solution(begin, target, words):
    answer = 0
    q = deque([[begin,0]])
    V = [0 for _ in range(len(words))]
    
    while q:
        x, cnt = q.popleft()
        if x == target:
            return cnt
        for i in range(len(words)):
            tmp = 0
            if not V[i]:
                for j in range(len(x)):
                    if x[j] != words[i][j]:
                        tmp += 1
                if tmp == 1:
                    q.append([words[i], cnt + 1])
                    V[i] = 1
    return answer