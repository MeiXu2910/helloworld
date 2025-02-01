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

if __name__ == "__main__":
    print(classify_triangle(3, 4, 5)) 
    print(classify_triangle(5, 5, 5))  
