from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    result_list = []
    for item in str_list:
        if item not in result_list:
            result_list.append(item)
            result_list.sort()
    return result_list
