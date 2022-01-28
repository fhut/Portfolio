class Rectangle:

    def __init__(self, set_width, set_height):
        self.width = set_width
        self.height = set_height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_height(self, set_height):
        self.height = set_height

    def set_width(self, set_width):
        self.width = set_width

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        picture = []
        if self.width < 50 and self.height < 50:

            for height in range(self.height):
                    picture.append("*" * self.width + "\n")

            return "".join(picture)
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

class Square(Rectangle):

    def __init__(self, set_side):
        super().__init__(set_side, set_side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, set_side):
        super().set_height(set_side)
        super().set_width(set_side)

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)


sq = Square(1)

print(sq.get_picture())

sq.set_width(4)

print(sq.get_picture())
