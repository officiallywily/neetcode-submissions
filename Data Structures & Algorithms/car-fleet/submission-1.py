class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        fleets = 0
        slowest_time = 0.0

        for (pos, spd) in reversed(cars):
            time_to_target = (target - pos) / spd
            if time_to_target > slowest_time:
                fleets += 1
                slowest_time = time_to_target
        
        return fleets