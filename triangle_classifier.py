"""
This module classifies triangles based on their side lengths.

Author: Your Name
Date: YYYY-MM-DD
"""

def classify_triangle(a, b, c):
    """Classify a triangle based on the lengths of its sides."""

    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    if round(a**2 + b**2, 5) == round(c**2, 5) or \
       round(b**2 + c**2, 5) == round(a**2, 5) or \
       round(a**2 + c**2, 5) == round(b**2, 5):
        return "Right"
    return "Scalene"
