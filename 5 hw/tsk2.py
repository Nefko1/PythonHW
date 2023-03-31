sps = [0, 0, 0, 0, 0]
count = int(input('введите оценки:'))
while count != -1:
    sps[count -1] += 1
    count = int(input('введите оценки:'))
total = 0
for i in range(2, 5):
    total =+sps[i]
print('spis: ', end='')
for i in range(5):
    for g in range(sps[i]):
        print(i + 1, end=' ')
print("\nNumber of spis: " + ''.join(str(sps) +
      "\nAcademic performance: " + str(total / sum(sps) * 100)))
