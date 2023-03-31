def ekz(point:int):
    return point > 50

amount = int(input('Колличество студентов: '))
for i in range(amount):
    point1 = int(input('Баллы за тест: '))
    total = ekz(point1)
    if total:
        print('Зачет')
    else:
        print('ГГ')