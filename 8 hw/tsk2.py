def discountSet(points:int):
    if 0 <= points <= 49:
        print('Ваша скидка - 10%')
    elif 50 <= points <= 99:
        print('Ваша скидка - 15%')
    elif points >= 100:
        print('Ваша скидка - 20%')

points = int(input('Введите баллы:'))
discountSet(points)