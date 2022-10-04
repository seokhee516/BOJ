import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
def back(num, total):
    global cnt
    if num == n:
        if total == s:
            cnt += 1
        return 

    # 해당 숫자를
    back(num+1, total) # 더하지 않을 경우
    back(num+1, total+arr[num]) # 더할 경우

back(0,0)
# 모든 원소를 선택하지 않았을 때
if s == 0:
    print(cnt-1)
else:
    print(cnt)
