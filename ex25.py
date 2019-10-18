# Глобална променлива
value = 100

# 1. деклариция
def sumNumbers(n):
    print(f'n={n}')
    if n > 0:
        return n + sumNumbers(n-1)
    return 0


if __name__ == '__main__':
    # 2. извикване
    x = 6
    res = sumNumbers(x)
    print(f'sum {list(range(x+1))} = {res}')