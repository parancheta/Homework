# Part 1
import datetime as dt
a = dt.datetime.now()
print("The current date and time is ", a)

# Part 2
def my_message(firstName, dayName):

    print("Hi", firstName, "!! happy", dayName, "!!")

my_message("Pete", "Sunday")
my_message("Pete", "")

# Part 3
import numpy as np
array_example = np.array(
	[
		[[0, 1],[0, 1],[0, 1]],
		[[0, 1],[0, 1],[0, 1]]
    ]
   )

print(array_example.shape)

# Part 4

g = np.linspace(0, 20, num = 6)

print(g)

# Part 5

import copy

d = copy.deepcopy(g)

print(d)

# Part 6

"""
Two reasons we use NumPy arrays over Python lists are 
that NumPy arrays occupy less memory and are fast compared
to lists
"""
