class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: Dict[int, int] = {}
        buckets: List[List[int]] = [[] for _ in (range(len(nums) + 1))]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, value in count.items():
            buckets[value].append(key)

        ret_list = []
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: Dict[int, int] = {}
        buckets: List[List[int]] = [[] for _ in (range(len(nums) + 1))]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, value in count.items():
            buckets[value].append(key)

        ret_list = []
        for i in range(len(nums), 0, -1):
            for n in buckets[i]:
                ret_list.append(n)
                if len(ret_list) == k:
                    return ret_list

            
                
