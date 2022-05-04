'''
분할정복
전체를 확인하고 모든칸의 색이 동일하지 않을 경우 4등분하여 연산 진행
풀이가 떠오르지 않아서 답안예시를 찾아보았다. 
가장 깔끔해 보여서 가져왔는데 베이스 케이스를 따로 설정하지 않고 return을 아무것도 하지 않은게 
다른 풀이들이랑 조금 다르다.
다른 분할정복 문제 풀어보면서 다양한 방식을 공부해야겠당
'''
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
count = [0, 0] # 하얀색, 파란색

# x, y 좌표, 한변의 길이 n
def cut(x, y, n):
    # 현재 칸의 색 0 또는 1
    cur = graph[x][y]
    # x, y에서 n까지 확인
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 현재 칸의 색과 다른 색이 있다면
            if cur != graph[i][j]:
                # 4등분하여 재귀적으로 확인
                # 왼쪽 위
                cut(x, y, n//2)
                # 왼쪽 아래
                cut(x, y + n//2, n//2)
                # 오른쪽  위
                cut(x + n//2, y, n//2)
                # 오른쪽 아래
                cut(x + n//2, y + n//2, n//2)
                return
    if cur == 0: # 하양색 개수 추가
        count[0] += 1
        return
    else: # 파란색 개수 추가
        count[1] += 1
        return
# 0, 0에서 시작
cut(0,0,n)
print(count[0])
print(count[1])