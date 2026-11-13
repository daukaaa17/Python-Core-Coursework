from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values
    def __add__(self, a):
        return [str(value) + ' ' + a for value in self.values]
# Counter([1, 2, 3]) + "mississippi"
