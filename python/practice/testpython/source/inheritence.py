class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def __str__(self):
        return "Rec is at {0}, {1} - width is {2} and height is {3}".format(self.x, self.y, self.width, self.height)


rec = Rectangle(10, 20, 42, 123)
print(rec)
