import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))

'''
더 효율적인 방법을 위해서 다른 순서를 찾아보는 것이 도움이 된다
ai가 증가하는 순서를 보면, D[i]를 채울 수 있는 또 다른 순서를 알 수 있다.
ai가 증가하는 순서로 계산하면, aj < ai 조건은 신경 쓰지 않아도 된다.
즉, j < i인 조건만 생각하면 된다.

매번 [1, i-1] 구간에서 D[j]+1 값의 최댓값을 구하면 된다.
이러한 구간 최댓값, 값 없데이트는 세그먼트 트리와 같은 자료구조로 O(log N)시간 달성 가능
총 시간 복잡도 O(N log N)
'''

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))