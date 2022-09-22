import heapq
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        q = []
        for p in people:
            heapq.heappush(q,(-p[0],p[1]))
        res = []
        while q :
            person = heapq.heappop(q)
            res.insert(person[1],[-person[0],person[1]])
        return res
