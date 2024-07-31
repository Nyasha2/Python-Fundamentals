"""
CS 1 22fa
Lab 07 Python OOP Starter Code
Credit: Leo Jenkins

Defines a Food cell for use in a tkinter-powered agar.io clone game.
"""
import math

class Food:
    """
    Represents a Food cell in a agar.io clone game.

    Attributes:
        - mass (int/float): mass of food cell
        - coords (int, int): (x, y) coordinates of food cell
        - handle (int): handle for cell, should represent a tkinter handle
          "reference" to the rendered cell circle
        - color (str): color of cell
    """

    def __init__(self, mass, coords, handle, color):
        # TODO: Initialize fields
        self.mass = mass
        self.coords = coords
        self.handle = handle
        self.color = color

    # Getters (self is the only argument)
    def get_mass(self):
        """
        Returns mass of this Food cell.

        Returns:
            - (int/float): mass of this Food cell
        """
        return self.mass

    def get_coords(self):
        """
        Returns (x, y) coordinates of this Food cell's current location.

        Returns:
            - (int/float, int/float): (x, y) coordinates of cell
        """
        return self.coords

    def get_handle(self):
        """
        Returns unique handle for this Food cell, that refers to the
        unique tkinter handle of the rendered cell.

        Returns:
            - (int): Unique tkinter handle for this cell
        """
        return self.handle

    def get_color(self):
        """
        Returns color of this Food cell.

        Returns:
            - (str): Color of this Food cell
        """
        return self.color

    def get_radius(self):
        """
        Returns radius of this Food cell, as determined by its mass.

        Returns:
            - (float): Radius of this Food cell
        """
        # mass = pi * radius^2
        return math.sqrt(self.mass / math.pi)

    # Setters (self and the new value of the field)
    def set_handle(self, handle):
        """
        Sets the unique tkinter handle for this Food cell.

        Arguments:
            - handle (int): Unique tkinter handle for this Food cell

        Returns:
            - None
        """
        self.handle = handle
