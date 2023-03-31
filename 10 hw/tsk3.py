import random
num1 = 0
num2 = 0
while True:
    choice = input("Введите 'off', чтобы выйти: ")
    if choice == "off":
        break
    else:
        num = random.randint(1, 2)
        print("Ваш номер:", num)
        if num == 1:
            num1 += 1
        else:
            num2 += 1
        print("Участников в первом забеге:", num1)
        print("Участников во втором забеге:", num2)