#!/usr/bin/python3
"""
This module defines a SimpleCalculator class that performs basic arithmetic operations.
"""


class SimpleCalculator:
    """
    A simple calculator class for arithmetic operations.

    Methods:
        add(a, b): Returns the sum of a and b.
        multiply(a, b): Returns the product of a and b.
    """

    def add(self, a, b):
        """
        Adds two numbers.

        Parameters:
            a (int/float): First number.
            b (int/float): Second number.

        Returns:
            int/float: Sum of a and b.
        """
        return a + b

    def multiply(self, a, b):
        """
        Multiply two numbers.

        Parameters:
            a (int/float): The first number.
            b (int/float): The second number.

        Returns:
            int/float: The product of a and b.
        """
        return a * b


if __name__ == '__main__':
    calculator = SimpleCalculator()
    print(f"5 + 3 = {calculator.add(5, 3)}")
    print(f"7 * 4 = {calculator.multiply(7, 4)}")
