from random import randint

num1 = int(input("Число участников сборной 1: "))
num2 = int(input("Число участников сборной 2: "))

for i in range(1):
    swimmer1 = randint(1,num1)
    swimmer2 = randint(1,num2)
    print("Пловец", swimmer1, "-", "Пловец", swimmer2)
