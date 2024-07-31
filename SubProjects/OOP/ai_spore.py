"""
CS 1 22fa
Lab 07 Python OOP Provided AISpore class (students do not need to change).
Credit: Leo Jenkins

Defines an "AI spore" cell for use in a tkinter-powered agar.io clone game.

Note to anyone using this class: spores is a global list managed in lab07.py,
and care should be taken not to modify it when it shouldn't be (a downside
of global state!).
"""
import math
# Import the constants for the game to improve reusability
from lab07 import WINDOW_HEIGHT, WINDOW_WIDTH, \
                  SCENE_HEIGHT, SCENE_WIDTH, spores
# Uses the student's implemented Spore class
from spore import Spore


class AISpore(Spore):
    """
    An AI Spore is a special type of Spore, with additional functionality
    for an AISpore in the game. Could it be made smarter? A good exercise
    students can try on their own!

    Attributes:
        - mass (int/float): mass of AI Spore
        - coords (int, int): (x, y) coordinates of AI Spore
        - color (str): color of cell
        - direction (int/float, int/float): vector of spore's direction
        - target (bool): Whether the AI Spore has a current target
        - handle (int): handle for cell, should represent a tkinter handle
          "reference" to the rendered cell circle
        - speed (int/float): Current speed of AI spore's movement in game
    """

    def __init__(self, mass, coords, color, direction, target, handle):
        """
        Constructs a new AISpore with the given information. See
        AISpore class docstring for what each argument represents.

        An AI Spore is initialized with a starting speed of 0.

        Room for improvement: Error-handling with raise!
        """
        # Initialize the fields
        self.mass = mass
        self.coords = coords
        self.color = color
        # Speed starts at zero
        self.speed = 0
        self.direction = direction
        self.target = target
        self.handle = handle

    def get_target(self):
        """
        Returns whether the AI Spore has a current target.

        Returns:
            - (bool): whether the AI Spore has a current target
        """
        return self.target

    def set_target(self, target):
        """
        Sets the target of the AI Spore has a current target (False
        if removing any existing target).

        Arguments:
            - target (bool): Whether a target is set

        Returns:
            - None
        """
        self.target = target

    def update_speed(self):
        """
        Updates the speed of this AISpore. An AISpore has a speed constant,
        and the speed is updated based on the current mass and is relative
        to the dimensions of WINDOW_HEIGHT, WINDOW_WIDTH.

        Returns:
            - None
        """
        # AI spore has a constant speed
        self.set_speed((0.004 + (1.5 / self.get_mass())) *
                       min(WINDOW_HEIGHT / 2, WINDOW_WIDTH / 2))

    def update_direction(self):
        """
        Updates the direction of this AISpore based on whether it has a
        current target (if it does, it is oriented towards that target
        based on its current coordinates and the SCENE_WIDTH).

        Returns:
            - None
        """
        if not self.get_target():
            # The spore has a target, get hunting!
            ai_x, ai_y = self.get_coords()
            min_distance = SCENE_WIDTH
            min_coords = None

            # Note to reader: spores is a global variable here and care should
            # be taken to ensure its state is managed carefully.
            for spore in spores:
                # Loop through the spores in the game, finding the one
                # closest to this AISpore.

                # An AISpore should know better than to target itself...
                if self != spore:
                    # Calculates the distance between this spore and the
                    # other using a CS 1 student's calculate_distance solution.
                    distance = self.calculate_distance(spore)
                    # Update min_distance and min_coords if we find
                    # a new closest candidate
                    if distance < min_distance:
                        min_distance = distance
                        min_coords = spore.get_coords()

            # Fancy math to get the magnitude?
            magnitude = math.sqrt(math.pow(min_coords[0] - ai_x, 2) +
                                  math.pow(min_coords[1] - ai_y, 2))
            # Update the direction of this AISpore: the hunt is on!
            self.set_direction(((min_coords[0] - ai_x) / magnitude,
                                (min_coords[1] - ai_y) / magnitude))

            # If our target is larger... run away!
            if spore.get_radius() > self.get_radius():
                (curr_dirx, curr_diry) = self.get_direction()
                self.set_direction((-1 * curr_dirx, -1 * curr_diry))

            # We've got a target.
            self.set_target(True)
