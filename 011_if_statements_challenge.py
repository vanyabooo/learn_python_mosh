'''
Спросить у пользовательля кредит скор
Вводишь кредитный скор
Если кр. скор 650 или меньше - банк дает ипотека 30%
Если 650 > x > 750 - 20%
Если больше 750 - 10%
Стоимость недвижки 1М
Но стоимость недвижимости меняется в любой момент
Выведите сколько будет стоить недвижимость учитывая кредит скор
'''


print("Price of a house is $1M")
price = 1000000.0
percent = 0.0
score = float(input("Please enter your credit score "))

if score <= 650:
    percent = .30
elif 650 < score < 750:
    percent = .20
if 750 <= score:
    percent = .10
else:
    print("There's some problem here...")

finished_price = price * percent + price
print("Your final price is",finished_price)
