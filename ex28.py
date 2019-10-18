# Глобална променлива
value = 100

# 1. деклариция
def sumNumbers(a, b, *args):
    # print(type(args))
    # print(args)
    c = a + b
    for v in args:
        c +=v
    return c


if __name__ == '__main__':
    # 2. извикване
    x,y = 6,7
    res = sumNumbers(x,y)
    print(f'{x} + {y} = {res}')

    res = sumNumbers(x,y,1,2,3,4,5,6,7)
    print(f'{x} + {y} + ... = {res}')

    lst = list(range(5))

    res = sumNumbers(x,y,*lst)
    print(f'{x} + {y} + ' + ' + '.join(str(s) for s in lst) + f'={res}')
    
