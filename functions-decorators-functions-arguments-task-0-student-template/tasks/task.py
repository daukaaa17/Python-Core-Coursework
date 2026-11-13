from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    a = {}
    for i in range(1, num + 1):
        a.update({i: i ** 2})
    return a
