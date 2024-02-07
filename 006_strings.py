course = "Python's course for Beginners"
#         0123456789
string_2 = 'He exclaimed: "Hi!"'
#         0123456789
# If you want to use an apostraphe in a string,
# you can escape it by using the opposite quote

"""
This is a multi line comment that can also be used
as a string variable. When used at the beginning of
a file this will be counted as a 'docstring.'

Very handy for writting up some comments too!
"""

# An index defines the position of
# an ELEMENT in an ITERABLE object.

print(f"Index [0] of the string 'course' is '{course[0]}'")
# Indicies can be negative!
print(f"Index [-3] of the string 'string_2' is '{course[-3]}'")
# You can also select a range using a colon
print(f"Index [1:4] of the string 'course' is '{course[1:4]}'")
# Other examples:
print(course[4:])
print(course[:8])
print(course[:])
