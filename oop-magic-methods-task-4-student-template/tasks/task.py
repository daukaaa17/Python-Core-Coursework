class PriceControl:
    __value: float

    def __init__(self, __value: float = None):
        self.__value = __value

    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        if value < 0 or value > 100:
            raise ValueError(f"ValueError: Price must be between 0 and 100.")
        self.__value = value

    def __str__(self):
        return str(self.__value)


class AuthorControl:
    __value: str

    def __init__(self, __value: str = None):
        self.__value = __value

    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        if self.__value is not None:
            raise ValueError(f"ValueError: Author can not be changed.")
        self.__value = value


class NameControl:
    __value: str

    def __init__(self, __value: str = None):
        self.__value = __value

    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        if self.__value is not None:
            raise ValueError(f"ValueError: Name can not be changed.")
        self.__value = value


class Book:
    author = AuthorControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price
