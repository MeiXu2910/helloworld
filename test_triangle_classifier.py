import pytest
from triangle_classifier import classify_triangle

def test_equilateral():
    assert classify_triangle(5, 5, 5) == "Equilateral"

def test_isosceles():
    assert classify_triangle(5, 5, 8) == "Isosceles"

def test_scalene():
    assert classify_triangle(3, 4, 6) == "Scalene"

def test_right():
    assert classify_triangle(3, 4, 5) == "Right"

def test_not_a_triangle():
    assert classify_triangle(1, 2, 3) == "Not a triangle"
