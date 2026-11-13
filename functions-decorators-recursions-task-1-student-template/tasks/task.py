from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    total = 0
    for element in sequence:
        if isinstance(element, (list, tuple)):  # Check if the element is a nested sequence
            total += seq_sum(element)  # Recursive call for nested sequences
        else:
            total += element  # Add the integer value directly
    return total


