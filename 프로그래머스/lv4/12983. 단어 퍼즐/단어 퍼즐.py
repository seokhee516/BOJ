def solution(strs, t):
    INF = float('inf')
    n = len(t)
    dp = [INF for i in range(n+1)]
    dp[0] = 0
    for i in range(1,n+1):
        if i > 5:
            j = i - 5
        else:
            j = 0
        for k in range(j,i):
            if dp[k] + 1 < dp[i] and t[k:i] in strs:
                dp[i] = dp[k] + 1

    if dp[n] != INF:
        return dp[n]
    else:
        return -1
