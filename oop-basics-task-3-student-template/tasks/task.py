class Counter:
    def __init__(self, start=0, stop=None):
        self.value = start  # Initialize the counter with the start value
        self.stop = stop

    def increment(self):
        if self.stop is not None and self.value >= self.stop:
            print("Maximal value is reached.")
        else:
            self.value += 1

    def get(self):
        return self.value

# c = Counter(start=42)
# c.increment()
# c.increment()
# c.get()


