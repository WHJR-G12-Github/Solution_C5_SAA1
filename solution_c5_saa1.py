# Importing "random"
import random

# Creating an empty list
numbers=[]

# 'for' loop
for i in range(10):
    # Generating random numbers in the range of 1 to 100
    # And appending into the 'numbers' list
    numbers.append(random.randint(1,100))
