#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """this is a subclass of list"""
    def __init__(self):
        """this initializes the object"""
        super().__init__()

    def print_sorted(self):
        """this prints the sorted list"""
        print(sorted(self))
