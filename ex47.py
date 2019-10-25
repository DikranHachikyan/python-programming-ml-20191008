def suma(a,b):
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
    except ValueError:
        print('could not convert string to float')
    except KeyError:
        print('Invalid Key')
    except:
        print('Unkown error')
    else:
        print('---- else --- (when no exception)')
    finally:
        print('--- finally --- (always - clean up)')