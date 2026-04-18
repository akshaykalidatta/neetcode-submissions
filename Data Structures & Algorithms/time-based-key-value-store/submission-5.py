class TimeMap:

    def __init__(self):
        self.dct = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dct:
            self.dct[key] = []
        self.dct[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dct:
            return ""
        # values = [duo[0] for duo in self.dct[key]]
        # timestamps =  [duo[1] for duo in self.dct[key]]
        duo = self.dct[key]

        low, high = 0, len(duo) - 1
        while low<=high:
            mid=(low+high)//2
            if duo[mid][1]==timestamp:
                return duo[mid][0]
            elif duo[mid][1]>timestamp:
                high = mid-1
            else:
                low = mid+1

        return duo[high][0] if timestamp > duo[high][1] else ""
