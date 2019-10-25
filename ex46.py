
if __name__ == '__main__':
    f = lambda a: a ** 3 if a % 2 else a ** 2

    print(f'3:{f(3)}')
    print(f'4:{f(4)}')

    items = [('A',5,7),('Z',2,6),('B',4,6),('D',2,5)]

    # items.sort()
    # print(f'sorted in place:{items}')
    
    # items.sort(key=lambda el: el[1])
    # print(f'sorted in place:{items}')
    
    items.sort(key=lambda el: (el[1],el[0]) )
    print(f'sorted in place:{items}')
    
    sortKey = lambda el: (el[1],el[0])
    items.sort(key=sortKey)
    print(f'sorted in place:{items}')

    values = [1,2,3,4,5]
    for v in map(lambda a: a + a, values):
        print(v)

    