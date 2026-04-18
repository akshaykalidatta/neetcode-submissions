class MinStack:

    def __init__(self):
        self.stack = []
        self.pref = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.pref) == 0:
            self.pref.append(val)
        else:
            self.pref.append(min(val, self.pref[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.pref.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.pref[-1]
