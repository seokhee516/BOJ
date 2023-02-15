class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 그리디
        res = nums[0]
        cur = 0
        for n in nums:
            cur += n
            res = max(res, cur)
            if cur < 0:
                cur = 0
        return res
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)
'''