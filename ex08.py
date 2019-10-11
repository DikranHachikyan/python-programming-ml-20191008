
def main():
    x = int(input('x='))

    # (condition)? true-expr:false-expr

    m = x if x > 0 else x ** 2

    # if x > 0:
    #     m = x
    # else:
    #     m = x ** 2

    print(f'm = {m}')

main()