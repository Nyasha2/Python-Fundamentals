"""
CS 1 22fa
Lab 07 Python OOP
Credit: Leo Jenkins

This provides the backend for the agar.io clone, using the Food and Spore
classes students implement in Lab07.

This program is powered by tkinter, a graphics library. Students do not
need to understand any tkinter-related code.
"""

# Program constants for graphics window
SCENE_WIDTH = 2400
SCENE_HEIGHT = 1600
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# A global list of spores and foods; care is taken to ensure they are not
# modified when they shouldn't be (a downside of global state,
# but ok in this program for reasons we won't go into).
foods = []
spores = []

import random
from tkinter import *
from spore import *
from ai_spore import *
from food import *

FOOD_COLORS = ['red', 'blue', 'green', 'yellow']

# Defaults for a game
NUM_AI = 10
NUM_INIT_FOOD = 1000


def init_player_spore(canvas, mass, coords, color):
    """
    Initialize player spore with given mass, (x, y) coordinates, and color,
    attached to the passed tkinter canvas. Adds the player to the global
    list of spores, and also returns the player Spore. A player
    is initialized with a (0, 0) (no) direction.

    Arguments:
        - canvas (tkinter Canvas)
        - mass (int)
        - coords (int, int)
        - color (str)

    Returns:
        - (Spore): New player Spore
    """
    player = Spore(mass, coords, color, (0, 0), None)
    radius = player.get_radius()
    # Place the spore circle in the center of the window.
    window_x = (WINDOW_WIDTH / 2)
    window_y = (WINDOW_HEIGHT / 2)
    # canvas.create_oval(x1, y1, x2, y2, [options])
    player_circle = canvas.create_oval(window_x - radius, window_y - radius,
                                       window_x + radius, window_y + radius,
                                       fill=color, outline=color)
    # Save the tkinter circle handle to the Spore so it can be accessed
    # later for tkinter graphics methods.
    player.set_handle(player_circle)
    spores.append(player)
    return player


# AI SPORES
def init_ai_spores(player, color):
    """
    Initialize AI spores.

    Arguments:
        - player (Spore): Current player's Spore instance
        - color (str): Color of AI spores

    Returns:
        - None (adds NUM_AI AISpores to scene)
    """
    # Number of ai to spawn
    for _ in range(NUM_AI):
        # Add ai_spore
        add_ai_spore(player, color)


def add_ai_spore(player, color):
    """
    Adds a new AISpore to the scene.

    Arguments:
        - player (Spore): Current player's Spore instance
        - color (str): Color of newly-created AISpore

    Returns:
        - None (adds AISpore to scene)
    """
    # Player coords
    player_x, player_y = player.get_coords()
    # Edges of the window
    lower_x = player_x - (WINDOW_WIDTH / 2)
    upper_x = player_x + (WINDOW_WIDTH / 2)
    lower_y = player_y - (WINDOW_HEIGHT / 2)
    upper_y = player_y + (WINDOW_HEIGHT / 2)

    # Dummy coordinates inside of rendered window
    x = player_x
    y = player_y

    # Coordinates must be outside of rendered window
    while (lower_x <= x and x <= upper_x) and (lower_y <= y and y <= upper_y):
        # Random coordinates within bounds of scene
        x = random.randint(0, SCENE_WIDTH)
        y = random.randint(0, SCENE_HEIGHT)

    # Random mass between 0.8 and 1.5 times the player's mass
    player_mass = player.get_mass()
    mass = random.randint(round(0.8 * player_mass),
                          round(1.5 * player_mass))
    # Create new AISpore, defaulting to (0, 0) direction and no current target
    new_ai = AISpore(mass, (x, y), color, (0, 0), False, None)
    # Add new AISpore to list of spores in the game
    spores.append(new_ai)


def update_ai_direction():
    """
    Updates direction for all AISpores.

    Returns:
        - None (updates direction of all AISpores in spores)
    """
    for spore in spores:
        # Ignore player Spore
        if isinstance(spore, AISpore):
            spore.update_direction()


def update_ai(player, color):
    """
    Ensures number of AISpores in game is maintained, adding a new one
    if not (e.g. if the player eats one).

    Arguments:
        - player (Spore): Current player's Spore instance
        - color (str): Color of newly-created AISpore

    Returns:
        - None (adds AISpores to scene if needed)
    """
    # Keep the number of AI constant
    if len(spores) - 1 < NUM_AI:
        add_ai_spore(player, color)


# FOOD functionality
def init_food(mass):
    """
    Initialize NUM_INIT_FOOD Foods, all having the same mass.

    Arguments:
        mass (float): Mass of new Food cells

    Returns:
        - None (adds new Foods to scene)
    """
    # Initialize the food
    for _ in range(NUM_INIT_FOOD):
        add_food(mass)


def add_food(mass):
    """
    Add a Food object with the given mass to a random position in the scene
    and having a random color.

    Arguments:
        - mass (float): Mass of added Food

    Returns:
        - None (adds Food to foods)
    """
    # Random coordinates
    x = random.randint(0, SCENE_WIDTH)
    y = random.randint(0, SCENE_HEIGHT)
    # Random color
    color = random.choice(FOOD_COLORS)
    # Init new food; no handle set here.
    new_food = Food(mass, (x, y), None, color)
    # Append to food list
    foods.append(new_food)


def update_food(mass):
    """
    Ensures number of Food cells in game is maintained, adding a new one
    if not (e.g. if the player Spore or an AISpore eats one).

    Arguments:
        - mass (float): Mass of new Food if one is created

    Returns:
        - None (adds Food to the scene)
    """
    # The amount of food is constant
    if len(foods) < NUM_INIT_FOOD:
        # Delayed regeneration, 10% chance of new Food appearing
        if random.randint(1, 10) == 1:
            add_food(mass)


# MOVEMENT
def update_player_direction(event):
    """
    Update player direction using mouse location passed by a tkinter event.

    Arguments:
        event (tkinter MouseEvent object)

    Returns:
        - None (updates player direction)
    """
    # Restrict mouse location to the window
    event.x = min(WINDOW_WIDTH, event.x)
    event.x = max(0, event.x)
    event.y = min(WINDOW_HEIGHT, event.y)
    event.y = max(0, event.y)

    # Vector from spore to the mouse
    vector_x = event.x - (WINDOW_WIDTH / 2)
    vector_y = event.y - (WINDOW_HEIGHT / 2)

    # Set the direction
    player.set_direction((vector_x, vector_y))


def update_spore_speed():
    """
    Update the speed of all Spores.

    Returns:
        - None (updates speed of Spore in spores)
    """
    for spore in spores:
        spore.update_speed()


def update_spore_position():
    """
    Update position of all Spores using each spore's direction and velocity.

    Returns:
        - None (updates position of Spore in spores)
    """
    # Loop through player Spore and AISpores
    for spore in spores:
        spore.update_position()


# GRAPHICS
def render_window(canvas):
    """
    Render the objects within the window centered at the player's Spore.

    Arguments:
        - canvas (tkinter Canvas object)

    Returns:
        - None (updates tkinter handles for all Spores)
    """
    # Player coords
    player_x, player_y = player.get_coords()
    # Edges of the window
    lower_x = player_x - (WINDOW_WIDTH / 2)
    upper_x = player_x + (WINDOW_WIDTH / 2)
    lower_y = player_y - (WINDOW_HEIGHT / 2)
    upper_y = player_y + (WINDOW_HEIGHT / 2)

    # Delete the old rendering of the player; canvas.delete takes a tkinter
    # handle to remove the corresponding graphics element (in this case,
    # the oval created to represent a Spore)
    canvas.delete(player.handle)
    radius = player.get_radius()
    color = player.get_color()
    # Re-render the player Spore
    half_w = WINDOW_WIDTH / 2
    half_h = WINDOW_HEIGHT / 2
    new_player_circle = canvas.create_oval(half_w - radius, half_h - radius,
                                           half_w + radius, half_h + radius,
                                           fill=color, outline=color)
    player.set_handle(new_player_circle)

    # Find the foods to render
    for food in foods:
        x, y = food.get_coords()
        # Delete the old food rendering
        canvas.delete(food.get_handle())
        radius = food.get_radius()
        # Only render if within the window
        if lower_x <= x + radius and x - radius <= upper_x and \
           lower_y <= y + radius and y - radius <= upper_y:
            color = food.get_color()
            # Render the food
            new_x = x - lower_x
            new_y = y - lower_y
            food.handle = canvas.create_oval(new_x - radius, new_y - radius,
                                             new_x + radius, new_y + radius,
                                             fill=color, outline=color)

    # Find the AISpores to render
    for ai in spores:
        # Ignore player's Spore
        if isinstance(ai, AISpore):
            x, y = ai.coords
            # Delete the old AISpore rendering
            canvas.delete(ai.get_handle())
            radius = ai.get_radius()
            # Only render if within the window
            if lower_x <= x + radius and x - radius <= upper_x and \
               lower_y <= y + radius and y - radius <= upper_y:
                color = ai.get_color()
                # Re-render the AISPore
                new_x = x - lower_x
                new_y = y - lower_y
                new_circle = canvas.create_oval(new_x - radius, new_y - radius,
                                                new_x + radius, new_y + radius,
                                                fill=color, outline=color)
                ai.set_handle(new_circle)


# COLLISIONS
def handle_food_collisions(canvas):
    """
    Handle collisions between the spores and the food
    currently in-game.

    Arguments:
        - canvas (tkinter Canvas object)

    Returns:
        - None (removes Food from foods if colliding with a Spore)
    """
    # Keep track of the unique foods to remove later
    food_to_remove = set()
    for food in foods:
        for spore in spores:
            # Check collision
            if spore.are_colliding(food):
                # Delete the food from the scene
                canvas.delete(food.get_handle())
                # Add to foods to remove
                food_to_remove.add(food)
                if isinstance(spore, AISpore):
                    # AI Spore needs to find a new target
                    spore.set_target(False)
                # Spore's mass increases by the food's mass
                spore.set_mass(spore.get_mass() + food.get_mass())

    # Remove the food from the list
    for food in food_to_remove:
        foods.remove(food)


def handle_spore_collisions(canvas):
    """
    Handle collisions between spores (larger one eats the smaller one)

    Arguments:
        - canvas (tkinter Canvas object)

    Returns:
        - None (removes smaller of two colliding Spores)
    """
    # Keep track of the unique spores to remove later
    spores_to_remove = set()
    # Look through all the spoors
    for i, spore in enumerate(spores):
        # Look through all spores after spores[i] Spore
        for j in range(i + 1, len(spores)):
            spore2 = spores[j]
            # Check for collision
            if spore.are_colliding(spore2):
                # Compare radius to see which one gets eaten
                if spore.get_radius() < spore2.get_radius():
                    # spore2 absorbs the mass of spore
                    spore2.set_mass(spore2.get_mass() + spore.get_mass())
                    spores_to_remove.add(spore)
                    # Delete other spore from the scene
                    canvas.delete(spore.get_handle())
                    # If the eaten spore is the player spore
                    if not isinstance(spore, AISpore):
                        # Game over, program quits
                        final_mass = spore.get_mass()
                        quit(f"Game over! You're final mass was {final_mass}")

                    # Otherwise, continue checking if spore2 is AISpore
                    if isinstance(spore2, AISpore):
                        # spore2 needs a new target
                        spore2.set_target(False)
                else:
                    # Spore absorbs the mass of spore2
                    spore.set_mass(spore.get_mass() + spore2.get_mass())
                    spores_to_remove.add(spore2)
                    # Delete the spore from the scene
                    canvas.delete(spore2.get_handle())
                    # If the eaten spore is the player spore
                    if not isinstance(spore2, AISpore):
                        # Game over, program quits
                        final_mass = spore.get_mass()
                        quit(f"Game over! You're final mass was {final_mass}")

                    if isinstance(spore, AISpore):
                        # Spore needs a new target
                        spore.set_target(False)

    # Remove the ai_spores from the lists
    for spore in spores_to_remove:
        spores.remove(spore)


def handle_keypress(evt):
    """
    Called when a keypress event fires.
    If 'q', 'Escape', or 'Ctrl+w' are pressed,
    quits to avoid a traceback when closing the window.
    """
    if evt.keysym == 'q' or evt.keysym == 'Escape' or \
       (evt.state == 4 and evt.keysym == 'w'):
        # evt.state == 4 refers 'Control' key
        global running
        running = False
        print('Goodbye!')
        quit()


if __name__ == '__main__':
    # Set up tkinter window and scene
    root = Tk()
    root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
    canvas = Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    canvas.pack()

    # Player spore
    player = None

    # Initialize food with a specified mass
    init_food(mass=25)
    # Initialize green player spore with a specified mass
    player = init_player_spore(canvas, mass=400,
                               coords=(SCENE_WIDTH / 2, SCENE_HEIGHT / 2),
                               color='green')
    # Initialize all the red AISpores
    init_ai_spores(player, color='red')
    # Attach an event listener to a keypress to improve usability/
    # avoid tracebacks in the terminal
    root.bind('<KeyPress>', handle_keypress)

    # running is set to False when a user types an exit key j
    # (see handle_keypress)
    running = True
    while running:
        # Player direction updates with the location of the mouse
        try:
            root.bind('<Motion>', update_player_direction)
        # this is kind of a hack, error-handling in tkinter sucks
        # override some default system exit keypresses more elegantly
        # Gotta love this tkinter documentation, RIP tkinter 2021.
        # https://tkdocs.com/shipman/ttk-exceptions.html
        except TclError as e:
            if str(e) == 'can\'t invoke "bind" command: application has been destroyed':
                print('Goodbye!')
                quit()
        # Update ai_direction using the location of its target
        update_ai_direction()
        # Update spore position using velocity and direction
        update_spore_position()
        # Render objects within window
        render_window(canvas)
        # Handle collisions between food and spores
        handle_food_collisions(canvas)
        # Handle collisions between two spores
        handle_spore_collisions(canvas)
        # Update the number of AISpores if needed
        update_ai(player, color="red")
        # Update the number of Food if needed
        update_food(mass=25)
        # Update the speed of the spores (dependent on mass)
        update_spore_speed()
        # Update scene
        root.update()
