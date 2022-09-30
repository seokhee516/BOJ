import sys
input = sys.stdin.readline
n,s = map(int, input().split())
nums = list(map(int, input().split()))
ans = 1e9
target, left, right = 0,0,0 # 투포인터 사용
# 반복문을 통해 수열을 확인
while True:
    # left 부터 right까지 수열의 합이 s를 넘는다면
    if target >= s:
        ans = min(ans, right-left) # 매 순간 최소 길이로 초기화
        target -= nums[left] # 현재 수열 시작 위치 값을 빼주고
        left += 1 # 현재 수열의 시작 위치를 한 계단 앞으로 이동
    # s를 넘지 않는다면
    else:
        # 맨 끝 위치가 n과 같다면 반복을 멈춰준다. s를 넘는 수열을 만들 수 없기 때문
        if right == n:
            break
        target += nums[right] # 현재 수열의 마지막 위치 값을 더해주고
        right += 1 # 수열의 마지막 위치를 한 계단 앞으로 이동
    # print(ans, target, left, right)
if ans == 1e9:
    print(0)
else:
    print(ans)
'''
10 15
5 1 3 5 10 7 4 9 2 8
1000000000.0 5 0 1
1000000000.0 6 0 2
1000000000.0 9 0 3
1000000000.0 14 0 4
1000000000.0 24 0 5
5 19 1 5
4 18 2 5
3 15 3 5
2 10 4 5
2 17 4 6
2 7 5 6
2 11 5 7
2 20 5 8
2 13 6 8
2 15 6 9
2 11 7 9
2 19 7 10
2 10 8 10
'''