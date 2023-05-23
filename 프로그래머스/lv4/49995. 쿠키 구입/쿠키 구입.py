def solution(cookie):
    answer = 0
    n = len(cookie)

    for i in range(n-1):
        first, fidx = cookie[i], i
        second, sidx = cookie[i+1], i+1
        while True:
            if first == second:
                answer = max(answer, first)
            if fidx > 0 and first <= second:
                fidx -= 1
                first += cookie[fidx]
            elif sidx < n-1 and first >= second:
                sidx += 1
                second += cookie[sidx]
            else:
                break
        
    return answer