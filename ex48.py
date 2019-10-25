def suma(a,b):
    try:
        if a < 0 or b < 0 : raise ValueError(f'Negative value!')
    except ValueError :#as e:
        return 0
        # print(e)
    return a + b

if __name__ == '__main__':
    actions = {
        '+':suma
    }

    try:
        num1 = float(input('Enter num1:'))
        op = input('Enter +:')
        num2 = float(input('Enter num2:'))
        # res = num1/0
        print(f'{num1} {op} {num2} = {actions[op](num1,num2)}')
        print('end')
    except ValueError as e:
        print(f'Value error:{e}')
    except KeyError as e:
        print(f'Invalid Key:{e}')
    except:
        print('Unkown error')
    else:
        print('---- else --- (when no exception)')
    finally:
        print('--- finally --- (always - clean up)')