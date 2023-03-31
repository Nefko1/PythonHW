def calculateMass(height, weight):
    mass = weight / (height ** 2)
    return mass

def processMass(mass):
    if mass < 18.5:
        print("Недостаточный вес")
    elif mass >= 18.5 and mass <= 25:
        print("ИМТ в норме")
    else:
        print("Избыточный вес")


height = float(input("Введите рост: "))
weight = float(input("Введите вес: "))
mass = calculateMass(height, weight)
processMass(mass)
