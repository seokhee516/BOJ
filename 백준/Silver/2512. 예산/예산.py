import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
m = int(input())

s = 0
e = max(array)

res = 0
while s <= e:
    tot = 0
    mid = (s+e) //2
    for x in array:
        if x > mid:
            tot += mid
        else:
            tot += x
    # 지방 예산이 국가예산 보다 작거나 같은 경우, 상한액을 증가
    # 가능한 최대이므로 작거나 같아야 한다.(큰 값을 미리 저장 하면 예산초과!!)
    if tot <= m:
        s = mid + 1
        res = mid
    # 지방 예산이 국가예산 보다 큰 경우, 상한액을 감소
    else:
        e = mid -1

print(res)
