
def main():
    # 2+4+....+98+100
    i = 1
    nSum = 0

    while i <= 100:
        nSum += i
        if i == 3: break
        i += 1
    else:
        print('else after while')

    print(f'1+2+3+...+99+100={nSum}')

main()