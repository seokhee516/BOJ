
def solution(nums):
    n = len(nums)//2
    s = len(set(nums))
    return min(n,s)