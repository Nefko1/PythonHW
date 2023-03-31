def calculate(*args):
    avg = sum(args) / len(args)
    aboveAvg = [num for num in args if num > avg]
    return (avg, aboveAvg)
print(calculate(2,8,6,1))