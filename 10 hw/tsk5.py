from time import sleep
from random import randint

print("бросаю кости...")
sleep(2)
bones1 = randint(1, 6)
bones2 = randint(1, 6)
print("На кубиках выпало:", bones1, bones2)