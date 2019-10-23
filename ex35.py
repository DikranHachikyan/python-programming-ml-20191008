
def getSquares(n):
    return [v ** 2 for v in range(n+1)] 

def generateSquares(n):
    print('before for')
    for v in range(n+1):
        yield v ** 2
    print('after for')

def generateLetters(text):
    for t in text:
        yield t

if __name__ == '__main__':
    #1
    for v in generateSquares(5):
        print(f'v={v}')


    #2.
    ls = list(generateSquares(5))
    print(ls)

    ls = list(generateLetters('hello python'))
    print(ls)