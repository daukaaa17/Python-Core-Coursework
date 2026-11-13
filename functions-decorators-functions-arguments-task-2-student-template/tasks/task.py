def union(*args) -> set:
    result = set()
    for arg in args:
        result.update(arg)
    return result

def intersect(*args) -> set:
    result = set(args[0])
    for arg in args[1:]:
        result.intersection_update(arg)
    return result
