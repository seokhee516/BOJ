import heapq
def solution(oper):
    max_heap = []
    min_heap = []
    for o in oper:
        s, n = o.split()
        if s == 'I':
            heapq.heappush(max_heap, (-int(n),int(n)))
            heapq.heappush(min_heap, int(n))
        elif s == 'D':
            if max_heap:
                if n == '1':
                    max_value = heapq.heappop(max_heap)[1]
                    min_heap.remove(max_value)
                elif n == '-1':
                    min_value = heapq.heappop(min_heap)
                    max_heap.remove((-min_value,min_value))
    if max_heap:
        answer = [heapq.heappop(max_heap)[1],heapq.heappop(min_heap)]
    else:
        answer = [0,0]
    return answer