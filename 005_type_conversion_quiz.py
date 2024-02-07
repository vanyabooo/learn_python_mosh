"""
Ask a user their weight (in pounds), convert it to
kilograms and print on the terminal.
"""

weight_lbs = float(input('What is your weight? (in pounds) '))
weight_kg = weight_lbs / 2.2046
print('Your weight in killograms is ' + str(weight_kg))
# print всегда отдает string
print('Your weight is', weight_kg)
