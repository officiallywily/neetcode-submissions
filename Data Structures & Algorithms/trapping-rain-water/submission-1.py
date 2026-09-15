class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix = [0] * len(height)
        maximum = 0
        for i in range(len(height)):
            if i == 0:
                prefix[i] = 0
            else:
                maximum = max(maximum, height[i - 1])
                prefix[i] = maximum
                

        suffix = [0] * len(height)
        maximum = 0
        for i in reversed(range(len(height))):
            if i == len(height) - 1:
                suffix[i] = 0
            else:
                maximum = max(maximum, height[i + 1])
                suffix[i] = maximum

        trapped_water = []
        for i in range(len(height)):
            water_height = min(prefix[i], suffix[i]) - height[i]
            trapped_water.append(max(water_height, 0))
        
        total_water = 0
        for water in trapped_water:
            total_water += water

        return total_water