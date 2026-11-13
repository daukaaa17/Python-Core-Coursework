def get_fractions(a_b: str, c_b: str) -> str:
    a, b = map(int, a_b.split("/"))
    c, _ = map(int, c_b.split("/"))
    numerator_sum = a + c
    return "{} + {} = {}/{}".format(a_b, c_b, numerator_sum, b)