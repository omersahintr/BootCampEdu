
def Fact(number):
    if number == 0:
        result = 1
    else:
        result = number * Fact(number-1)
    return result


def FactLoop(numbers):
    num = 1
    while (numbers!=0):
        if num == 0:
            break
        else:
            num = num * numbers
            numbers-=1
    return num

aNumber = input("Entry a number for Factorial Calculation: ")
print(f"Fact Loop Result: {FactLoop(int(aNumber))}")
print(f"Fact Recursive Result: {Fact(int(aNumber))}")