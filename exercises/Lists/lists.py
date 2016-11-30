def getNumbers(num):
    if num % 2 == 0:
        result = [i**2 for i in range(num, 0, -2)] + [
            i**2 for i in range(0, num + 1, +2)]
    else:
        result = [i**2 for i in range(num, 0, -2)] + [
            i**2 for i in range(1, num + 1, +2)]
    return result

print (getNumbers(10))
