given = "ААААBBBCCF"
result = ""

for i in set(given):
    number = given.count(given[0])
    result += str(number)
    result += given[0]
    given = [j for j in given if j != given[0]]

print(result)