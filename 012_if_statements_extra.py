"""
The use of "if" statements in Python are very common. Sometimes these "if" statements
are referred to as "if-then" statements or "if-else" statements.

If you are not using logical or arithmetic comparison operators then
Python checks the "truthiness or "truthfulness" of something in an "if statement."

All DATA TYPES have a default "truthiness" to them.
"""

# Booleans are the simplest because they can ONLY be True or False.
is_hot = False
is_cold = False

if is_hot:
    print(f"It is hot. is_hot = {is_hot}")
else:
    print(f"It is NOT hot. is_hot = {is_hot}")

# Notice that logically, just because it may be NOT hot,
# it does NOT automatically mean that it is therefore cold.

if is_cold:
    print(f"It is cold. is_cold = {is_cold}")
else:
    print(f"It is NOT cold. is_cold = {is_cold}")

# Other DATA TYPES:

# lists are truthful if they have at least one element
list_1 = []
list_2 = ["apple", "banana"]

if list_1:
    print(f"Variable list_1 = {list_1}. It contains elements.")
else:
    print(f"Variable list_1 = {list_1}. It is empty.")

# Here is a list of evaluations. Most of them evaluate to False when EMPTY.

# Bool
print(bool(False))   # False
print(bool(True))    # True

# Numeric types
print(bool(0))       # False
print(bool(0.0))     # False
print(bool(0j))      # False
print(bool(1))       # True
print(bool(1.5))     # True

print("negative int")
print(bool(-1))     # True

# String
print(bool(''))      # False
print(bool('Doki'))  # True

# List, Tuple, Dictionary, Set
print(bool([]))      # False
print(bool(()))      # False
print(bool({}))      # False
print(bool(set()))   # False
print(bool([1, 2]))  # True

# NoneType
print(bool(None))   # False


# It is important to consider the logic of if, elif, else

def num_check_1(my_num):
    if my_num > 40:
        print(f"{my_num} is greater than 40!")
    if my_num > 30:
        print(f"{my_num} is greater than 30!")
    if my_num > 20:
        print(f"{my_num} is greater than 20!")
    if my_num > 10:
        print(f"{my_num} is greater than 10!")

    print(f"Func 'num_check_1' ended.")
    print()


def num_check_2(my_num):
    if my_num > 40:
        print(f"{my_num} is greater than 40!")
    elif my_num > 30:
        print(f"{my_num} is greater than 30!")
    elif my_num > 20:
        print(f"{my_num} is greater than 20!")
    elif my_num > 10:
        print(f"{my_num} is greater than 10!")

    print(f"Func 'num_check_2' ended.")
    print()


def num_check_3(my_num):
    if my_num > 40:
        print(f"{my_num} is greater than 40!")
    elif my_num > 30:
        print(f"{my_num} is greater than 30!")
    elif my_num > 20:
        print(f"{my_num} is greater than 20!")
    elif my_num > 10:
        print(f"{my_num} is greater than 10!")
    else:
        print("I am explicitly stating what to do in all other cases.")

    print(f"Func 'num_check_3' ended.")
    print()


num_check_1(40)
num_check_2(40)
num_check_3(40)

print("Now we will execute with a small number.")

num_check_1(5)
num_check_2(5)
num_check_3(5)
