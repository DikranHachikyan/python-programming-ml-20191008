
def main():
    # 2+4+....+98+100
    i = 1
    nSum = 0

    while i <= 100:
        i += 1
        if (i % 2) != 0: continue
        nSum += i
    else:
        print('else after while')

    print(f'1+2+3+...+99+100={nSum}')

main()