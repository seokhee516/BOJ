import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
count = [0, 0, 0] # -1의 개수, 0의 개수, 1의 개수

# x, y 좌표, 한변의 길이 n
def cut(x, y, n):
    # 현재 칸 확인 -1 or 0 or 1
    cur = graph[x][y]
    # x, y에서 n까지 확인
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 현재 칸의 색과 다른 색이 있다면
            if cur != graph[i][j]:
                # 9등분하여 재귀적으로 확인
                # 왼쪽 위
                cut(x, y, n//3)
                # 왼쪽 가운데
                cut(x + n//3, y , n//3)
                # 왼쪽 아래
                cut(x + (n//3)*2, y, n//3)
                # 가운데 위
                cut(x, y + n//3, n//3)
                # 가운데 가운데
                cut(x + n//3, y + n//3, n//3)
                # 가운데 아래
                cut(x + (n//3)*2, y + n//3, n//3)
                # 오른쪽 위
                cut(x, y + (n//3)*2, n//3)
                # 오른쪽 가운데
                cut(x + n//3, y + (n//3)*2, n//3)
                # 오른쪽 아래
                cut(x + (n//3)*2, y + (n//3)*2, n//3)
                return
    if cur == -1: # -1 개수 추가
        count[0] += 1
        return
    elif cur == 0: # 0 개수 추가
        count[1] += 1
        return
    else: # 1 개수 추가
        count[2] += 1
        return
# 0, 0에서 시작
cut(0,0,n)
print(count[0])
print(count[1])
print(count[2])