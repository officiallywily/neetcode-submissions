class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = 0
        l: int = 0
        r: int = len(heights) -1 
        
        while l < r:
            base = r - l
            height = min(heights[l], heights[r])
            max_a = max(max_a, base * height)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return max_a