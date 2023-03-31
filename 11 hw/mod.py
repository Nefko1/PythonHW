def answ(question):
    question = question.lower()
    trener = question.find('трен')
    rasp = question.find('расп')
    oplat = question.find('оплат')
    if trener != -1:
        print_trener()
    elif rasp != -1:
        print_rasp()
    elif oplat != -1:
        print_oplat()

def print_trener():
    print('Контактные данные тренера:\nТелефон: +79138106369(Жены нет, детей нет)\nПочта:TrenerAye@sexy.ru')
def print_rasp():
    print('Расписание:\nАнжумания - 10:00; Бегит - 15:00, Прес качат - 20:00, 23:00-9:00 - Трэнер спаааат')
def print_oplat():
    print('к оплате:\nДоговоримся))')