academic_stf = []
used_last_names = []
last_name = ''

while True:
    list_of_pupils = []
    last_name = str(input("Введите ваше имя: "))

    if last_name == ' ':
        break
    elif last_name in used_last_names:
        print("этот учитель уже есть в списке.")
        continue
    else:
        used_last_names.append(last_name)

    position = str(input("введите должность: "))
    number_of_pupils = int(input("количество студентов: "))

    while number_of_pupils != 0:
        list_of_pupils.append(number_of_pupils)
        number_of_pupils = int(input("количествово стуентов: "))

    academic_stf.append([last_name, position, list_of_pupils])

print(academic_stf)