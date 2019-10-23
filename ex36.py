
if __name__ == '__main__':
    squares = ( v ** 2 for v in range(10))

    print(f'1=>{next(squares)}')
    print(f'2=>{next(squares)}')
    print(f'3=>{next(squares)}')

    ls = list(squares)
    print(ls)
    