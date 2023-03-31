nas = input('введите настольную игру:\n').lower()
spi = []
while nas != '0':
    if nas not in spi:
        spi.append(nas)
    else:
        print('эта игра уже записана')
    nas = input()