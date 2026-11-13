class Currency:
    conversion_rates = {
        "EUR": {"USD": 2.0, "GBP": 100.0},
        "USD": {"EUR": 0.5, "GBP": 50.0},
        "GBP": {"EUR": 0.01, "USD": 0.02},
    }

    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"{self.value:.1f} {self.currency_name}"

    @classmethod
    def course(cls, other_cls: type) -> str:
        from_currency = cls.currency_name
        to_currency = other_cls.currency_name
        if from_currency == to_currency:
            rate = 1.00
        else:
            rate = cls.conversion_rates[from_currency][to_currency]
        return f"{rate} {to_currency} for 1 {from_currency}"

    def to_currency(self, other_cls: type):
        """
        Convert the currency to another currency and return an instance of the target type.
        """
        from_currency = self.currency_name
        to_currency = other_cls.currency_name
        if from_currency == to_currency:
            rate = 1.00
        else:
            rate = self.conversion_rates[from_currency][to_currency]
        converted_value = self.value * rate
        return other_cls(converted_value)

    def __eq__(self, other: type) -> bool:
        """
        Check if two currencies are equal in value by converting them to the same type.
        """
        converted_other = other.to_currency(type(self))
        return self.value == converted_other.value

    def __lt__(self, other: type) -> bool:
        """
        Check if the current currency is less than the other by converting them to the same type.
        """
        converted_other = other.to_currency(type(self))
        return self.value < converted_other.value

    def __gt__(self, other: type) -> bool:
        """
        Check if the current currency is greater than the other by converting them to the same type.
        """
        converted_other = other.to_currency(type(self))
        return self.value > converted_other.value

    def __add__(self, other_cls: type):
        """
        Add two currencies, converting the second to the type of the first before adding.
        """
        converted_other = other_cls.to_currency(type(self))
        return type(self)(self.value + converted_other.value)


class Euro(Currency):
    currency_name = "EUR"


class Dollar(Currency):
    currency_name = "USD"


class Pound(Currency):
    currency_name = "GBP"


# Example Usage
e = Euro(100)
r = Pound(100)
d = Dollar(200)

# print(
#     f"e + r  =>  {e + r}\n"  # Should print a Euro instance with the correct value
#     f"r + d  =>  {r + d}\n"  # Should print a Pound instance with the correct value
#     f"d + e  =>  {d + e}\n"  # Should print a Dollar instance with the correct value
# )
# print(
#     f"e == r  =>  {e == r}\n"
#     f"e < d   =>  {e < d}\n"
#     f"d > r   =>  {d > r}\n"
#     f"r < e   =>  {r < e}\n"
# )