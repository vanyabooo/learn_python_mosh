course = 'Python for beginners'
# функция len - кол-во символов
print(len(course))
# функция title - первая буква заглавная в каждом слове
print(course.title())

# Methods are functions specific to certain data types.
# Методы upper/lower - выводят string в требуемом регистре,
# но не изменяют его
print(course.upper())
print(course.replace('beginners', 'Habibi'))
print(course.replace('n', 'V'))
print('Python' in course)

# other methods: https://www.w3schools.com/python/python_ref_string.asp

# Prints the index of the FIRST occurrence of a given string
print(course.find("P"))

# Strings in python are case-sensitive
print("Python" in course)

"""
String manipulation is important in python and very common.
It is used in every program essentially, especially for
data validation. Learn string methods!!!
"""
