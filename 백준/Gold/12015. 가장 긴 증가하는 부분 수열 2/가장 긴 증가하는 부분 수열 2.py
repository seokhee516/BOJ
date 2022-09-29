'''
일반적인 DP를 이용한 LIS -> O(n^2)

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)
'''
# 이분탐색 활용 -> O(nlogn)
# 주어진 배열의 인덱스를 하나씩 살펴보면서 그 숫자가 들어갈 위치를 이분탐색으로 넣기
n = int(input())
array  = list(map(int, input().split()))
memo = [0]

for i in range(n):
    if memo[-1] < array[i]:
        memo.append(array[i])
    else:
        start = 0
        end = len(memo)
        while start < end:
            mid = (start+end) // 2
            if memo[mid] < array[i]:
                start = mid + 1
            else:
                end = mid
        memo[end] = array[i]
print(len(memo)-1)

'''
6
10 20 10 30 20 50
[0, 10]
[0, 10, 20]
[0, 10, 20]
[0, 10, 20, 30]
[0, 10, 20, 30]
[0, 10, 20, 30, 50]
'''