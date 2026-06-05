class Shape:
    # Base class for all shapes, initializing common properties like color and whether the shape is filled.
    def __init__(self, color, is_filled):
        self.color = color  # The color of the shape.
        self.is_filed = is_filled  # Boolean to determine if the shape is filled or not.

    def describe(self):
        # Prints a description of the shape's color and whether it is filled.
        print(f"It is {self.color} and {'filled' if self.is_filed else 'not filled'}")

class Circle(Shape):
    # Circle class inheriting from Shape and adding a radius property.
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)  # Initialize properties from the Shape base class.
        self.radius = radius  # Specific property for Circle: its radius.

    def describe(self):
        # Extends the base class describe method with additional details about the circle's area.
        super().describe()  # Call the describe method from Shape to handle common properties.
        print(f"It is a circle with an area of {3.14 * self.radius ** 2}cm^2")  # Approximate area calculation.

class Square(Shape):
    # Square class inheriting from Shape and adding a width property.
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)  # Initialize properties from the Shape base class.
        self.width = width  # Specific property for Square: its width.

    def describe(self):
        # Extends the base class describe method with additional details about the square's area.
        super().describe()  # Call the describe method from Shape to handle common properties.
        print(f"It is a square with an area of {self.width ** 2}cm^2")  # Calculate the square's area.

class Triangle(Shape):
    # Triangle class inheriting from Shape and adding width and height properties.
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)  # Initialize properties from the Shape base class.
        self.width = width  # Specific property for Triangle: its base width.
        self.height = height  # Specific property for Triangle: its height.

    def describe(self):
        # Extends the base class describe method with additional details about the triangle's area.
        super().describe()  # Call the describe method from Shape to handle common properties.
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")  # Calculate the triangle's area.

# Example instances of shapes and their descriptions.
circle = Circle(color="red", is_filled=True, radius=5)  # Create a Circle object with specified properties.
square = Square(color='blue', is_filled=False, width=6)  # Create a Square object with specified properties.
triangle = Triangle(color='yellow', is_filled=True, width=7, height=8)  # Create a Triangle object with specified properties.

# Call the describe method for each shape to print their details.
circle.describe()
square.describe()
triangle.describe()