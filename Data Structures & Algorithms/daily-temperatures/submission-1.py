class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack: List[int] = []
        ret: List[int] = [0] * len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while len(temp_stack) > 0 and temp_stack[-1][0] < temp:
                ret[temp_stack[-1][1]] = i - temp_stack[-1][1]
                temp_stack.pop()
            temp_stack.append((temp, i))
        return ret

[30,38,30,36,35,40,28]
i = 0
temp = 30
temp_stack: []
ret: [0, 0, 0, 0, 0, 0, 0]