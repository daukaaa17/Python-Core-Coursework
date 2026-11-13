from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    a = []
    for i in range(0, n):
        if (i + 1) % 3 == 0 and (i + 1) % 15 != 0:
            a.append("Fizz")
        elif (i + 1) % 5 == 0 and (i + 1) % 15 != 0:
            a.append("Buzz")
        elif (i + 1) % 15 == 0:
            a.append("FizzBuzz")
        else:
            a.append(i + 1)
    return a
