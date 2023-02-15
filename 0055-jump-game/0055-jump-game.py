class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0 # 도달할 수 있는 최대 인덱스 
        for i, n in enumerate(nums):
            if i > m: # 현재 인덱스에 도달 할 수 없다면
                return False
            m = max(m, i+n) # 최대 인덱스 업데이트
        return True