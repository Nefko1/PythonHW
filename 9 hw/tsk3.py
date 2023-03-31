def sumNumbers():
    num = input("Введите число: ")
    if num == "":
        return 0.0
    else:
        return float(num) + sumNumbers()
print("Сумма введенных чисел: ", sumNumbers())
