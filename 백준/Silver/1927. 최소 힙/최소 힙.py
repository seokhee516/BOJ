import sys
import heapq
heap = []
for _ in range(int(sys.stdin.readline().strip())):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)