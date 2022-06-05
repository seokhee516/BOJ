import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
# 시작시간이 빠른 순으로 정렬
data = sorted(data, key = lambda x: [x[0],x[1]])
# print(data)
# 첫번째 시간부터 시작
time = [0,0]
# 첫번째 시간 회의 개수 1개
cnt = 0
for start, end in data:
    # 시작시간이 끝나는 시간보다 크거나 같다면
    if start >= time[1]:
        time[0] = start
        time[1] = end
        # 회의에 놓기
        cnt += 1
    # 같은 시간 또는 나중에 시작하는데 끝나는 시간이 빠르다면
    if start >= time[0] and end < time[1]:
        # 최대 회의 시간 중 하나로 설정
        time[0] = start
        time[1] = end
    
print(cnt)
