def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    ans = 0
    for c in cities:
        s = c.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            ans += 1
        else:
            cache.append(s)
            ans += 5
    return ans