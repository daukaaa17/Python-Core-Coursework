from typing import Dict

def combine_dicts(*args:Dict[str, int]) -> Dict[str, int]:
    a = {}
    for d in args:
        for key, value in d.items():
            a[key] = a.get(key, 0) + value
    return a

