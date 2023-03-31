def fastСhess():
    from time import time
    startTime = time()
    totalTime = 1800
    print('Время началось! У вас есть 10 минут на все ходы.')
    while True:
        move = input('Ваш ход: ')
        if move.lower() == 'off' or time() - startTime >= totalTime:
            print('Бб чмо)')
            break
        else:
            timeRemaining = round((totalTime - (time() - startTime)) / 60, 1)
        print('Осталось времени:', timeRemaining, 'минут')
fastСhess()