class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        i = 0
        j = len(height) - 1
        while i < j:
            area = (j-i) * min(height[i],height[j]) # 넓이 구하기
            water = max(water,area)
            if height[i] > height[j]: # 왼쪽이 크다면 
                j -= 1 # 왼쪽 고정 오른쪽 조정
            else: # 오른쪽이 크다면
                i += 1 # 오른쪽 고정 왼쪽 조정
        return water