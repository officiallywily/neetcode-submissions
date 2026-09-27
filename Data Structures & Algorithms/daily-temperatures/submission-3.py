class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack: List[int] = []
        ret: List[int] = [0] * len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while temp_stack and temperatures[temp_stack[-1]] < temp:
                ret[temp_stack[-1]] = i - temp_stack[-1]
                temp_stack.pop()
            temp_stack.append(i)
        return ret
