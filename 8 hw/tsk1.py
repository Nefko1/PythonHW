def print_stud():
    print('Колледж Сириус')
    print('Имя:___')
    print('Школа:___')
    print('Группа:___')

print('это инструмент для печати бейджиков')
amount = int(input('число учеников:'))
for i in range (amount):
    print_stud()
    print('Готово! Заберите ваши бейджики.')