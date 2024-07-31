import pytest
import sys

sys.path.insert(0, "../lab07_OOP")

from food import Food

FOOD_1 = Food(mass=5, coords=(804, 489), handle=405, color="red")
FOOD_2 = Food(mass=652, coords=(513, 788), handle=144, color="green")


def test_food_init_method_mass():
    assert FOOD_1.mass == 5

def test_food_init_method_coords():
    assert FOOD_1.coords == (804, 489)

def test_food_init_method_handle():
    assert FOOD_1.handle == 405

def test_food_init_method_color():
    assert FOOD_1.color == "red"

def test_food_init_method_mass2():
    assert FOOD_2.mass == 652

def test_food_init_method_coords2():
    assert FOOD_2.coords == (513, 788)

def test_food_init_method_handle2():
    assert FOOD_2.handle == 144

def test_food_init_method_color2():
    assert FOOD_2.color == "green"