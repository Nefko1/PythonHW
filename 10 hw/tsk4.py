from time import sleep
delete = input("Удалить с поля?\n").lower()
if delete == 'да':
    minutes = int(input("Введите количество минут штрафа: "))
    print("Вы удалены с поля на", minutes, "минут(-ы)")
    sleep(minutes)
    print("Возвращайтесь на поле!")
elif delete == 'нет':
    print('Играйте дальше')
else:
    print('повторите попытку')
