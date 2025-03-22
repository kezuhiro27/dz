class Counter:
    def __init__(self, number = 0):
        self.number = number
    def increment(self):
        self.number += 1
        print(self.number)
    def decrement(self):
        self.number -= 2
        print(self.number)
    def reset(self):
        self.number = 0
        print(self.number)

a = Counter(6)
a.increment()
a.decrement()
a.reset()