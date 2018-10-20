

class Rectangle:
    # New is implicitly called before __init__
    # Self is the instance that was just created

    def __init__(self, width, height):
        # Properties
        # No data encapsulation
        self.width = width
        self.height = height

    # Instance method ie uses self
    def area(self):
        return self.width * self.height


    def perimeter(self):
        return 2 * (self.width + self.height)



r1 = Rectangle(width=10, height=20)
# Calls the perimeter method in the rectangle class and passes r1 as the self argument
print(r1.perimeter())

print(Rectangle.perimeter(r1))