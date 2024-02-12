"""
Создать игру где спрашиваешь пользователя число от 1 до 100
И ответ будет выходить выше или ниже, но человеку дается только 6 попыток
Если все попытки использованы - они проигрывают, и спрашивается хотите ли вы продолжить еще раз
Поддерживать счет выигрыша
"""

import random

tries = 6
keep_playing = True
score = 0

while keep_playing:
    secret = random.randint(1, 100)
    print(secret)
    while tries > 0:
        guess = int(input("Please enter your guess: "))
        if guess == secret:
            score += 1
            print(f"Ебать ты красавчик, угадал уже {score} раз!")
            break
        elif guess > secret:
            print(f"{guess} is too high. Guess lower...")
        elif guess < secret:
            print(f"{guess} is too low. Guess higher...")
        tries -= 1
    else:
        print("Лох, ты проиграл! :)")

    keep_playing = input("Would you like to try again? (yes/no)")
    if keep_playing == "yes":
        continue
    elif keep_playing == "no":
        print("The game is over.")
        break
