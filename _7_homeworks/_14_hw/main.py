# TODO task 1, 2
class Main:
    def __init__(self):
        self.text = ''

    def set_text(self, text: str):
        self.text = text
        return self.text


class ChildClass(Main):
    def __init__(self, text: str, number: int | float):
        super().__init__()
        self.number = number
        self.set_text(text)


main_obj = Main().set_text('Here we gonna make hard business logic')
print(main_obj)

new_child = ChildClass('Hi, business', 123.43)
print(new_child.text, new_child.number)


# TODO task 3

class Roman:
    roman_nums_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def __init__(self, roman_numeral: str):
        self.roman_numeral = roman_numeral

    def __str__(self):
        return self.roman_numeral

    def __add__(self, other):
        if isinstance(other, Roman):
            return Roman(self._to_roman(self._to_decimal(self.roman_numeral) + self._to_decimal(other.roman_numeral)))
        else:
            raise TypeError('Only Roman nums can be added')

    def __sub__(self, other):
        if isinstance(other, Roman):
            return Roman(self._to_roman(self._to_decimal(self.roman_numeral) - self._to_decimal(other.roman_numeral)))
        else:
            raise TypeError('Only Roman nums can be subtracted')

    def __mul__(self, other):
        if isinstance(other, Roman):
            return Roman(self._to_roman(self._to_decimal(self.roman_numeral) * self._to_decimal(other.roman_numeral)))
        else:
            raise TypeError('Only Roman nums can be multiplied')

    def __truediv__(self, other):
        if isinstance(other, Roman):
            return Roman(self._to_roman(self._to_decimal(self.roman_numeral) // self._to_decimal(other.roman_numeral)))
        else:
            raise TypeError('Only Roman nums can be divided')

    @staticmethod
    def _to_decimal(roman_numeral):
        decimal = 0
        prev_val = 0

        for char in roman_numeral[::-1]:
            val = Roman.roman_nums_dict[char]
            if val >= prev_val:
                decimal += val
            else:
                decimal -= val
            prev_val = val
        return decimal

    @staticmethod
    def _to_roman(decimal):
        if not 0 < decimal < 4000:
            raise ValueError('Supported only value between 1 and 3999')

        roman_numeral = ''
        for num, val in sorted(Roman.roman_nums_dict.items(), key=lambda x: -x[1]):
            while decimal >= val:
                roman_numeral += num
                decimal -= val
        return roman_numeral


num1 = Roman('X')
num2 = Roman('III')

res1 = num1 + num2
print(res1)

res2 = num1 - num2
print(res2)

res3 = num1 * num2
print(res3)

res4 = num1 / num2
print(res4)
