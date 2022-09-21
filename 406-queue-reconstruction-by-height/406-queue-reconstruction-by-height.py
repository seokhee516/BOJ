class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x:(-x[0],x[1])) # x[0] 내림차순 해주어야 ans 리스트에는 오름차순으로 들어감 
        ans = []
        for p in people:
            ans.insert(p[1],p)
        return ans
'''
people
[[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
ans
[[7, 0]]
[[7, 0], [7, 1]]
[[7, 0], [6, 1], [7, 1]] # p[1] 둘다 1일때 오름차순으로 들어감
[[5, 0], [7, 0], [6, 1], [7, 1]] # p[1] 둘다 0일때 오름차순으로 들어감
[[5, 0], [7, 0], [5, 2], [6, 1], [7, 1]] # 앞에는 이미 알맞게 정렬, p[1]=2 알맞게 들어감
[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]] # p[1]=4 알맞게 들어감
'''