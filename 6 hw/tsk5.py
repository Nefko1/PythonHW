plentyUnion = set()
plentyIntersection = set()

numberStudent = int(input())
count = 0
initialIteration = True
while numberStudent > count:
    plentyLanguege = set()

    number_language_and_stud = int(input())
    count += number_language_and_stud

    for j in range(number_language_and_stud):
        language = input()
        plentyLanguege.add(language)

    if initialIteration == True:
        plentyIntersection.update(plentyLanguege)
        initialIteration = False

    plentyUnion.update(plentyLanguege)
    plentyIntersection = plentyIntersection.intersection(plentyLanguege)

print(f"{len(plentyUnion)} - {plentyUnion}")
print(f"{len(plentyIntersection)} - {plentyIntersection}")