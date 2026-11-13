from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    output = []
    for i in sequence:
        if isinstance(i, (list, tuple)):
            output.extend(linear_seq(i))
        else:
            output.append(i)
    return output

