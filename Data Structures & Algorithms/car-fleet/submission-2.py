class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        car_stack: List[int] = []

        for i, (pos, spd) in enumerate(cars):
            
            while car_stack and (target - cars[car_stack[-1]][0])/cars[car_stack[-1]][1] <= (target - pos)/spd:
                car_stack.pop()
            car_stack.append(i)
        
        return len(car_stack)



# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
# => [(0, 1), (1, 2), (4, 2), (7, 1)]

# (0, 1) (slower)
# time: 10
# (1, 2)
# time: 4.5
# (4, 2) (joins the one in front)
# time: 3
# (7, 1)
# time: 3 (time is the same/slower, pop the one on top until nothing else is lower time)

