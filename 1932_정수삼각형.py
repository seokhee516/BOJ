import sys
input = sys.stdin.readline

n = int(input())
triangle = []
for i in range(n):
    triangle.append(list(map(int, input().strip().split())))

for i in range(1, n):
    for j in range(i + 1): # 삼각형 가로로 한칸 더 김
        # 0번째 수 일때 위 층 수 그대로 더하기
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        # 마지막번째 수 일때 위층 마지막 수 그대로 더하기
        elif j == len(triangle[i])-1:
            triangle[i][j] += triangle[i-1][j-1]
        # 위층 왼쪽 수와 바로 위층 수 중에 큰 수 더하기
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
# 마지막 줄 최대값 출력
print(max(triangle[n-1]))

