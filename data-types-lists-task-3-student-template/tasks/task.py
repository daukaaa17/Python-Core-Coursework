from typing import List
import math

def foo(nums: List[int]) -> List[int]:
    a = []
    for i in range(0, len(nums)):
        a.insert(i, math.prod(nums) / nums[i])
    return a

