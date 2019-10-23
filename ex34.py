
def getSquares(n):
    return [v ** 2 for v in range(n+1)] 

def generateSquares(n):
    for v in range(n+1):
        yield v ** 2

if __name__ == '__main__':
    
    values = getSquares(10)

    print(values)
    
    # 1. присвояваме генератора    
    sq = generateSquares(10)

    print(type(generateSquares))
    print(type(sq))

    print(f'1->{next(sq)}')
    print(f'2->{next(sq)}')
    print(f'3->{next(sq)}')
    print(f'4->{next(sq)}')
    print(f'5->{next(sq)}')

    sq1 = generateSquares(3)
    print(f'1->{next(sq1)}')
    print(f'2->{next(sq1)}')
    print(f'3->{next(sq1)}')
    print(f'4->{next(sq1)}')
    print(f'5->{next(sq1)}')

