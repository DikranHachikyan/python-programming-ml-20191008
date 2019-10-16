# Глобална променлива
value = 100

# 1. деклариция
def addNumbers(firstNumber,secondNumber):
    # res - локална променлива
    res = firstNumber + secondNumber
    return res

if __name__ == '__main__':
    # 2. извикване
    x,y = 5,6
    r = addNumbers(x,y)

    print(f'result = {r}')