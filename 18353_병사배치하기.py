import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 전환
array.reverse()
# print(array)
# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n): # 부분수열을 앞에 수열에 array[i]를 붙이는거라고 생각할 때
    for j in range(0, i): # array[i]보다 앞에 있고
        # print("array[j]: ", array[j], "array[i]: ", array[i])
        if array[j] < array[i]: # array[i]보다 작은 수로 끝나는 
            dp[i] = max(dp[i], dp[j] + 1) # 가장 긴 부분수열 max(붙이는 수, 앞에서 가장 긴 수 + 1)
            # print("i: ", i, "j:", j, dp)

# 열외시켜야 하는 병사의 최소 수를 출력
print(n - max(dp))