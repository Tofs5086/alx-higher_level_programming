from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inheriting from Base with enhanced validation, area calculation, and string representation.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): X-coordinate of the bottom left corner.
        y (int): Y-coordinate of the bottom left corner.

    Methods:
        area(self): Calculates and returns the area of the rectangle.
        display(self): Prints the rectangle using the '#' character, considering x and y.
        __str__(self): Returns a string representation of the rectangle.
        update(self, *args): Updates the rectangle's attributes based on the provided arguments.
        to_dictionary(self): Returns the dictionary representation of a Rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor with strict input validation.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of the bottom left corner. Defaults to 0.
            y (int, optional): Y-coordinate of the bottom left corner. Defaults to 0.
            id (int, optional): Unique identifier for the object. Defaults to None.
        """
        super().__init__(id)  # Call superclass constructor with id

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute with comprehensive validation.

        Args:
            value: The new value for the width.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute with comprehensive validation.

        Args:
            value: The new value for the height.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x coordinate attribute.

        Returns:
            int: The x-coordinate of the bottom left corner.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x coordinate attribute with comprehensive validation.

        Args:
            value: The new value for the x-coordinate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x coordinate must be an integer")
        if value < 0:
            raise ValueError("x coordinate must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y coordinate attribute.

        Returns:
            int: The y-coordinate of the bottom left corner.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y coordinate attribute with comprehensive validation.

        Args:
            value: The new value for the y-coordinate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y coordinate must be an integer")
        if value < 0:
            raise ValueError("the y coordinate must not be negative")
        self.__y = value

    def update(self, *args, **kwargs):
        """Updates the rectangle's attributes based on the provided arguments.

        Args:
            *args (optional): A positional argument list.
                - If provided and not empty, it should contain 4 or 5 elements
                  in the order (id, width, height, x, y). The y argument is optional.
                - If provided and empty, `kwargs` must be present.
            **kwargs (optional): A keyword argument dictionary.
                - Keys map to attribute names (id, width, height, x, y).

        Raises:
            ValueError: If either *args and **kwargs are empty, or
                if *args contains more than 5 elements, or
                if any key in **kwargs is not an attribute name.
        """

        if args and kwargs:
            raise ValueError("Cannot use both positional and keyword arguments")

        if args and len(args) > 5:
            raise ValueError("update() takes at most 5 positional arguments (id, width, height, x, y)")

        elif args and not args:
            if not kwargs:
                raise ValueError("Either positional or keyword arguments must be provided")

        # Process positional arguments
        if args:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            if len(args) == 5:
                self.y = args[4]

        # Process keyword arguments if *args is not provided
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle.

        Returns:
            dict: Dictionary containing id, width, height, x, and y.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
