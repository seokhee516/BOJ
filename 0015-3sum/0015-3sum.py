class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 정렬
        res = []
        n = len(nums)
        for i in range(n):
            if i>0 and nums[i-1]==nums[i]: # 중복되면 넘기기
                continue
            j=i+1 # i 다음 수
            k=len(nums)-1 # 마지막 수
            while j<k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0: # 합이 0 보다 크면
                    k -= 1 # 작게 확인
                elif s < 0: # 합이 0 보다 작으면
                    j += 1 # 크게 확인
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j<k and nums[j-1]==nums[j]: # 중복확인 [0,0,0,0] 방지
                        j+=1
        return res