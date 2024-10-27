class Counter:
    def __init__(self, start=0, step=0):
        self.step = step
        self.current=start

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current
        self.current += self.step
        return result


counter = Counter(start=10, step=2)

for i in range(5):
    print(next(counter))  # 10, 12, 14, 16, 18
