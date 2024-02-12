from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inheriting from Rectangle.

    Attributes:
        size (int): Size of the square.

    Methods:
        __init__(self, size, x=0, y=0, id=None): Class constructor.
        __str__(self): Returns a string representation of the square.
        size(self): Getter for the size attribute.
        size(self, value): Setter for the size attribute.
        update(self, *args, **kwargs): Updates the square's attributes based on the provided arguments.
        to_dictionary(self): Returns the dictionary representation of a Square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor for Square.

        Args:
            size (int): Size of the square.
            x (int, optional): X-coordinate of the bottom left corner. Defaults to 0.
            y (int, optional): Y-coordinate of the bottom left corner. Defaults to 0.
            id (int, optional): Unique identifier for the object. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute with comprehensive validation.

        Args:
            value: The new value for the size.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the square's attributes based on the provided arguments.

        Args:
            *args (optional): A positional argument list.
                - If provided and not empty, it should contain 4 elements
                  in the order (id, size, x, y).
            **kwargs (optional): A keyword argument dictionary.
                - Keys map to attribute names (id, size, x, y).

        Raises:
            ValueError: If either *args and **kwargs are empty, or
                if *args contains more than 4 elements, or
                if any key in **kwargs is not an attribute name.
        """
        if args and kwargs:
            raise ValueError("Cannot use both positional and keyword arguments")

        if args and len(args) != 4:
            raise ValueError("update() takes exactly 4 positional arguments (id, size, x, y)")

        if not args and not kwargs:
            raise ValueError("Either positional or keyword arguments must be provided")

        # Process positional arguments
        if args:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]

        # Process keyword arguments if *args is not provided
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square.

        Returns:
            dict: Dictionary containing id, size, x, and y.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
