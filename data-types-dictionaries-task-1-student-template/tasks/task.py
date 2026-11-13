from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    y = s.lower()
    a = {}
    for i in range(0, len(y)):
        c = y.count(y[i])
        a.update({y[i]: c})
    return a
