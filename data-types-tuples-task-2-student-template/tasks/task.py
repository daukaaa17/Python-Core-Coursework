from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    b = []
    for i in range(len(lst) - 1):
        b.append((lst[i], lst[i + 1]))
    return b
