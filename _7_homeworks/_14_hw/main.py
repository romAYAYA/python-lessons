# TODO task 1
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


# TODO task 2


