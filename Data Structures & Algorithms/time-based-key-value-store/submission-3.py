class TimeMap:

    def __init__(self):
        self.dct = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dct:
            self.dct[key] = []
        self.dct[key].append((value, timestamp))
        print(self.dct)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dct:
            return ""
        values = [duo[0] for duo in self.dct[key]]
        timestamps =  [duo[1] for duo in self.dct[key]]

        low, high = 0, len(timestamps) - 1
        while low<=high:
            mid=(low+high)//2
            if timestamps[mid]==timestamp:
                return values[mid]
            elif timestamps[mid]>timestamp:
                high = mid-1
            else:
                low = mid+1

        # return values[(len(timestamps)-1)] if timestamp > timestamps[-1] else ""
        return values[high] if timestamp > timestamps[high] else ""
