'''
dfs 다 까먹었당...ㅠㅠ 다시 공부하자!!!

답안 예시
각 수와 수 사이에 사칙연산 중 하나를 삽입하는 모든 경우에 대하여 만들어질 수 있는 최댓값 및 최솟값을 구하면 된다. 
따라서 모든 경우의 수를 계산하기 위하여 DFS 혹은 BFS를 이용하여 문제를 해결할 수 있다.
'''
import sys
input = sys.stdin.readline

# 수의 개수
n = int(input())
# 연산을 수행하고자 하는 수의 리스트
data = list(map(int, input().split()))
# 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최대값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색(DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최대값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i+1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / data[i])) # 나눌 때는 나머지 제거
            div += 1

# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)