
def main():
    # 1+2+3+....+99+100=5050
    i = 1
    nSum = 0

    while i <= 100:
        nSum += i
        i += 1
    else:
        print('else after while')

    print(f'1+2+3+...+99+100={nSum}')

main()