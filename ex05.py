
def main():
    x = int(input('x='))

    if x > 0:
        print(f'x is positive {x}')
        # print('x is positive {}'.format(x))
    else:
        print(f'x is negative or 0 ({x})')

main()