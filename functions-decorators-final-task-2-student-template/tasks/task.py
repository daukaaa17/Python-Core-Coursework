from typing import List

# def split_by_index(s: str, indexes: List[int]) -> List[str]:
#     result = []
#     prev_index = 0
#     for index in indexes:
#         if index > len(s):
#             return s
#         result.append(s[prev_index:index])
#         prev_index = index
#     result.append(s[prev_index:])
#     return result
# split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    # Filter indexes to keep only those within the valid range of the string length
    valid_indexes = [index for index in indexes if 0 <= index <= len(s)]
    valid_indexes.sort()  # Ensure indexes are in ascending order

    result = []
    prev_index = 0
    for index in valid_indexes:
        result.append(s[prev_index:index])
        prev_index = index

    result.append(s[prev_index:])  # Append the remaining part of the string
    return result


# s = "pythoniscool,isn'tit?"
# indexes = [6, 8, 12, 13, 18]
# result = []
# prev_index = 0
# for index in indexes:
#     result.append(s[prev_index:index])
#     prev_index = index
# result.append(s[prev_index:])
# print(result)