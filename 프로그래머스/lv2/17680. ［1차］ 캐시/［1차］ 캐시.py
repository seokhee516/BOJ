def solution(cacheSize, cities):
    cache = []
    ans = 0
    for c in cities:
        c = c.lower()
        if c not in cache:
            if len(cache) < cacheSize:
                cache.append(c)
            elif len(cache) >= cacheSize:
                cache.append(c)
                cache.pop(0)
            ans += 5
        else:
            ans += 1
            cache.append(cache.pop(cache.index(c)))
    return ans