def solution(sizes):
    for s in sizes:
        s.sort()
    w = max(sizes,key = lambda x:x[0])[0]
    h = max(sizes,key = lambda x:x[1])[1]
    answer = w*h
    return answer