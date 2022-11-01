import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
s, e = 0, n-1
sum = abs(nums[s]+nums[e]) # s와 e를 기준으로 양끝에서 찾아가는 방식
ansl = s
ansr = e
while s < e:
    tmp = nums[s]+nums[e]

    if sum > abs(tmp):
        ansl = s
        ansr = e
        sum = abs(tmp)
        if sum == 0: # 용액의 합이 0일 경우 멈추기
            break
    if tmp < 0: # 음수일 경우
        s += 1 # 왼쪽으로
    else: # 아닐 경우
        e -= 1 # 오른쪽으로
print(nums[ansl], nums[ansr])