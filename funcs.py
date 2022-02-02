from random import (randint, 
randrange, random)

def factorial(number: int = 5) -> int:
    """Get number factorial 
    input:
      number - int
    output:
      mul - int
    """
    mul = 1 # default value
    for i in range(1, number + 1):
        mul *= i
    return mul

x = randint(1,5)
print(x)
