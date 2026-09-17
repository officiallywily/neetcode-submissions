class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res = []

        for i in range(len(nums)):
            # 1. Remove the leftmost index if it has fallen out of the current window
            if deque and deque[0] <= i - k:
                deque.popleft()
            
            # 2. Pop smaller elements from the right
            while deque and nums[deque[-1]] <= nums[i]:
                deque.pop()
            
            # 3. Add the current index to the right of the deque
            deque.append(i)

            # 4. Once we have processed at least 'k' elements, start recording the maximum
            if i >= k - 1:
                res.append(nums[deque[0]])
        
        return res