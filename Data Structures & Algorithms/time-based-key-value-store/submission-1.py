class TimeMap:

    def __init__(self):
        self.time_map: Dict[str, List(Tuple[int, str])] = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        if not self.time_map[key]:
            return ""

        l, r = 0, len(self.time_map[key]) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if self.time_map[key][mid][0] == timestamp:
                return self.time_map[key][mid][1]

            if self.time_map[key][mid][0] > timestamp: # the target is to the left
                r = mid - 1
            else:
                res = self.time_map[key][mid][1]
                l = mid + 1

        return res

# ["TimeMap", "set", ["key1", "value1", 10], "get", ["key1", 1], "get", ["key1", 10], "get", ["key1", 11]]
# time_map = {
#   key1: [(10, value1)]
# }
