class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # edge cases
        if k > len(nums):
            return []
        
        # don't scan every single time the window moves

        res = []
        max_heap = []
        
        # window initialization
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))

        res.append(-max_heap[0][0])

        for i in range(k, len(nums)):
            # Push the new element entering the window
            heapq.heappush(max_heap, (-nums[i], i))
            #lazy deletion:
            # if the max element at the top of the hap has an index outside
            # our current window bonds (i - k), it's expired. Pop it
            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)

            res.append(-max_heap[0][0])

        return res