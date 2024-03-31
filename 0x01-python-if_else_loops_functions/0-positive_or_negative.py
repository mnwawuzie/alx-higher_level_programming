#!/usr/bin/python3
import random

number = random.randint(-10, 10)
if number < 0:
    result = "negative"
    print(f"{number} is {result}")
elif number == 0:
    result = "zero"
    print(f"{number} is {result}")
elif number > 0:
    result = "positive"
    print(f"{number} is {result}")
else:
    print(f"TypeError")
