from fractions import Fraction

def divide_to_fraction(numerator, denominator):
    if denominator == 0:
        return "Error: Cannot divide by zero."
    
    # Returns an exact fractional object
    return Fraction(numerator, denominator)

numerator = int(input("enter numerator : "))
denominator = int(input("enter denominator : "))
print(divide_to_fraction(numerator, denominator))
