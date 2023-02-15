class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = cur_max = cur_min = nums[0]
        
        for n in nums[1:]:
            if n < 0:
                tmp = cur_max
                cur_max = cur_min
                cur_min = tmp
                
            cur_max = max(n, cur_max*n)
            cur_min = min(n, cur_min*n)
            res = max(res, cur_max)
        return res