"""
Спросить у пользовательля кредит скор
Вводишь кредитный скор
Если кр. скор 650 или меньше - банк дает ипотека 30%
Если 650 > x > 750 - 20%
Если больше 750 - 10%
Стоимость недвижки 1М
Но стоимость недвижимости меняется в любой момент
Выведите сколько будет стоить недвижимость учитывая кредит скор
"""

print("The price of our house is 1.000.000$")
price = 1000000.0
percent = 0.0
score = float(input("Please enter your credit score here: "))

if score <= 650:
    percent = 0.30
elif score < 750:
    percent = 0.20
else:
    percent = 0.10

total_price = price * percent + price
print(f"Your total price is ${total_price}")
