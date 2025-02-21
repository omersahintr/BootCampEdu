
def Fact(number):
    if number == 0:
        return 1
    else:
        return number * Fact(number-1)

print(f"Fact Recursive Result: {Fact(5)}")

def FactLoop(numbers):
    num = 1
    while (numbers!=0):
        if num == 0:
            break
        else:
            num = num * numbers
            numbers-=1
    return num
print(f"Fact Loop Result: {FactLoop(5)}")