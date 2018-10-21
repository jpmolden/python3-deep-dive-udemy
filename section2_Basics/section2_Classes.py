

class Rectangle:
    # New is implicitly called before __init__
    # Self is the instance that was just created

    def __init__(self, width, height):
        # Properties
        # No data encapsulation
        # Convention to use sunder to make "private"
        self._width = width
        self._height = height

    # property and setter decorators can be used to allow added functionality
    # without breaking backwards compatibility

    # Function - Instance method
    # Decorator to make "width" a property which can be accessed
    # This function allows the use like a getter
    @property
    def width(self):
        return self._width

    # Width function is not overloaded
    # The decorator modifies the function
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive")
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    # height function is not overloaded
    # The decorator modifies the function
    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("height must be positive")
        else:
            self._height = height

    # Instance method ie uses self
    def area(self):
        return self.width * self.height


    def perimeter(self):
        return 2 * (self.width + self.height)


    # def get_width(self):
    #     return self.width
    # 
    # 
    # def setwidth(self,width):
    #     if width <= 0:
    #         raise ValueError("Width must be positive")
    #     else:
    #         self.width = width

    def to_string(self):
        return "Rectangle: width={0}, height={1}".format(self.width,self.height)


    def __str__(self):
        return "Rectangle: width={0}, height={1}".format(self.width,self.height)


    # Representation of the object, used in the idle window, console ect not the script
    def __repr__(self):
        return "Rectangle({0}, {1})".format(self.width, self.height)


    def __eq__(self, other):
        # return self.width == other.width and self.height == other.height
        # Using touples
        # make sure other is an instance of other
        # To accomadate sub classes
        if isinstance(other, Rectangle):
            # if isinstance(other, type(self)):
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False


    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            # Not raise an except but return not implemented
            return NotImplemented



r1 = Rectangle(width=10, height=20)
# Calls the perimeter method in the rectangle class and passes r1 as the self argument
print(r1.perimeter())

print(Rectangle.perimeter(r1))

#
print(r1.perimeter())


# string representation of an object
print("String representation of the r1 instance:\n", str(r1))
print("r1 instance address:\n", hex(id(r1)))

# string representation of an object
print("\n", r1.to_string())


# Overload functions with "MAGIC" methods
# Not all that magical just useful :D
print("Overload the str function with magic methods __str__ \n", str(r1))


r2 = Rectangle(10,20)
print("\n")
# Here the comparison compares if the Object is the same not the contents
print("r1 is not r2: ", r1 is not r2)

print("r1 == r2: ", r1 == r2)

# Will cause problems unless the isinstance is used to verify the type
print("r1 == 100; ",r1 == 100)


# #
r1 = Rectangle(10,10)
r2 = Rectangle(100,100)
print("r1 < r2", (r1 < r2))


r1.width = 100
r1.height = 10


