# A variable is a piece of data that is expected to change
# while the application is running. These are underscore delimited lower case.
name = "Dokibyte"

# A constant is a piece of data that is expected to NOT change
# while the application is running. These are underscore delimited upper case.
RED = (255, 0, 0)

"""
The lowercase and uppercase naming conventions are 
just syntax standards and are NOT enforced during runtime.

Both can be any DATA TYPE, but variables are more common to use.
For all built-in data types see: https://docs.python.org/3/library/stdtypes.html
Main built-in DATA TYPES in Python are:
"""

# region String (str) - Any sequence of characters in quotes of any kind
str_1 = 'Doki'
str_2 = "Hello World"
# Specific character in front of the first quote can mark the string
# as a certain type of string. Here it is a "formatted string"
str_3 = f"hi"
# There are more string types.
# endregion

# region Integer (int) - Whole numbers
int_1 = 10
int_2 = -33
int_3 = 1000000
print(f"The data type for int_1 ({int_1}) is: ", type(int_1))
# endregion

# region Float (float) - decimal numbers.
# Sometimes called 'doubles' or 'extended' in other languages.
float_1 = 3.1415927
float_2 = 1.0
float_3 = -2.4
# Special floats that represent positive and negative infinity.
float_4 = float('inf')
float_5 = float('-inf')
print(f"The data type for float_1 ({float_1}) is: ", type(float_1))
print(f"The data type for float_4 ({float_4}) is: ", type(float_4))
# endregion

# region Boolean (bool) - True or False
# Only two values are possible.
bool_1 = True
bool_2 = False
print(f"The data type for bool_1 ({bool_1}) is: ", type(bool_1))
# endregion

# list
# tuple
# dict
# class