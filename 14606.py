import sys
N = int(sys.stdin.readline().strip())

def memo(N, cache):
    if N == 1:
        return 0
    if N == 2:
        return 1
    if N == 3:
        return 3
    if N in cache:
        return cache[N]
    cache[N] = (N//2) * (N-N//2) + memo(N//2, cache) + memo((N-N//2), cache)
    return cache[N]

def pleasure(N):
    dic_cache = {}
    return memo(N, dic_cache)

print(pleasure(N))