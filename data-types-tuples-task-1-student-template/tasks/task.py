from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    n = num
    ndigit = 0
    a = []
    while n != 0:
        n //= 10
        ndigit += 1
    for i in range(1, ndigit + 1):
        digit_index = i
        digit = (num % 10 ** digit_index) // 10 ** (digit_index - 1)
        a.append(digit)
    a.reverse()
    t = tuple(a)
    return t

