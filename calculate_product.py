#!/usr/bin/python3
#Documentation: `calculate_product` Function

## Description
The `calculate_product` function computes the product of two given numbers (`m` and `n`). It takes two arguments and returns their multiplication result.

## Usage
1. **Import the Function**:
   ```python
   from my_module import calculate_product
def calculate_product(m: int, n: int) -> int:
    """
    Calculate the product of two integers.

    Args:
        m (int): First integer.
        n (int): Second integer.

    Returns:
        int: Product of m and n.
    """
    return m * n
product = calculate_product(8, 4)
print(f"The product is: {product}")
# Output: "The product is: 32"
