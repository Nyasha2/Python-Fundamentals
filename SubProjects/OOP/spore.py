"""
CS 1 22fa
Lab 07 Python OOP Starter Code
Credit: Leo Jenkins

Defines a Spore cell for use in a tkinter-powered agar.io clone game.

Note: Not all methods are documented, but in practice,
all method should be.
"""

import math

# Constants copied here from lab07.py's graphics configurations
SCENE_WIDTH = 2400
SCENE_HEIGHT = 1600
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

class Spore:
    """
    A Spore represents a spore in an agar.io clone game.
    Could it be made smarter? A good exercise
    students can try on their own!

    Attributes:
        - mass (int/float): mass of AI Spore
        - coords (int, int): (x, y) coordinates of Spore
        - color (str): color of cell
        - direction (int/float, int/float): vector of spore's direction
        - handle (int): handle for cell, should represent a tkinter handle
          "reference" to the rendered cell circle
        - speed (int/float): Current speed of AI spore's movement in game
    """

    # Fields: mass, coords, color, direction, handle
    def __init__(self, mass, coords, color, direction, handle):
        """
        Constructs a new Spore with the given information. See
        Spore class docstring for what each argument represents.

        A Spore is initialized with a starting speed of 0.

        Room for improvement: Error-handling with raise!
        """
        # Initialize fields
        self.mass = mass
        self.coords = coords
        self.color = color
        # Speed starts at zero
        self.speed = 0
        self.direction = direction
        self.handle = handle

    # Mass
    def get_mass(self):
        return self.mass
    
    def set_mass(self, mass):
        self.mass = mass

    # Coords
    def get_coords(self):
        return self.coords
    
    def set_coords(self, coords):
        self.coords = coords

    # Color
    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    # Speed
    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    # Direction
    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    # Handle
    def get_handle(self):
        return self.handle

    def set_handle(self, handle):
        self.handle = handle

    # Radius (depends on mass)
    def get_radius(self):
        # mass = pi * radius^2
        return math.sqrt(self.mass / math.pi)
    
    def calculate_distance(self, spore):
        """
        Calculates and returns the distance between this Spore and the 
        passed spore.

        Arguments:
            - (Spore): other Spore to calculate distance from
        
        Returns:
            - (float): distance between this Spore and other spore
        """
        x1, y1 = self.coords
        x2, y2 = spore.coords
        # Square root of the change in x squared plus the change in y squared
        return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

    def are_colliding(self, spore):
        """
        Check whether this Spore is colliding with the passed spore.

        Arguments:
            - spore (Spore): Other spore
        
        Returns:
            - (bool) True if this Spore is colliding with the other spore
        """
        # Distance between the two spores
        distance = self.calculate_distance(spore)

        # Colliding if distance is less than combined radius
        return self.get_radius() + spore.get_radius() > distance

    def update_speed(self):
        """
        Updates the speed of this Spore. A Spore has a speed constant,
        and the speed is updated based on its current mass.

        Returns:
            - None
        """
        # Velocity is proportional with 1/mass
        self.set_speed(0.004 + (1.5 / self.get_mass()))
    
    def update_position(self):
        """
        Updates the position of this Spore based on its
        current position, speed, and direction.

        Returns:
            - None
        """
        # Initial coordinates
        x, y = self.get_coords()
        
        # Change in x and y
        delta_x = self.get_speed() * self.get_direction()[0]
        delta_y = self.get_speed() * self.get_direction()[1]

        # New coordinates
        new_x = x + delta_x
        new_y = y + delta_y

        # Player position stays within the scene
        new_x = max(new_x, 0)
        new_x = min(new_x, SCENE_WIDTH)
        new_y = max(new_y, 0)
        new_y = min(new_y, SCENE_HEIGHT)

        # Update spore position
        self.set_coords((new_x, new_y))
            
