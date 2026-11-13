from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    b = set()
    for i in lst:
        for key, value in i.items():
            b.add(value)
    return b