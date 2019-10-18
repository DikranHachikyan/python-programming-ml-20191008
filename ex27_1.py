# Глобална променлива
value = 100

# 1. деклариция
def sumNumbers(a, b, d = None):
    # z = 1
    if d:
        z = a + b + d
    else:
        c = a + b
    #globals() - всички глобални
    return c if 'c' in locals() else z


if __name__ == '__main__':
    # 2. извикване
    x,y = 6,7
    res = sumNumbers(x,y)
    print(f'{x} + {y} = {res}')

    z = 8
    res = sumNumbers(x,y,z)
    print(f'{x} + {y} + {z} = {res}')
