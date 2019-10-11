
def main():
    # 1+2+3+....+99+100=5050
    i = 1
    nSum = 0

    while i <= 100:
        nSum += i #nSum = nSum + i
        i += 1

    print(f'1+2+3+...+99+100={nSum}')

main()