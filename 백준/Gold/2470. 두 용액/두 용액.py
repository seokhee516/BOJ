import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

i = 0
j = n-1
ans = 1e10
res = [0,0]
while i < j:
    tot = arr[i]+arr[j]
    if abs(tot) < ans: # 절대값 주의
        ans = abs(tot)
        res[0] = arr[i]
        res[1] = arr[j]
    # 용액의 합이 0보다 작을 때
    if tot < 0: # 절대값 없음
        i += 1 # 합을 크게 만들어줌
    else: # 합이 0보다 클때
        j -= 1 # 합을 작게 만들어줌
print(res[0],res[1])