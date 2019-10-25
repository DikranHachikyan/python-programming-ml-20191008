# 2

from functools import wraps

def upperCase(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        args = [ str(v).upper() for v in args]
        return func(*args,**kwargs)
    return wrapper

def brackets(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        args = [f'[{v}]' for v in args ]
        return func(*args,**kwargs)
    return wrapper

@upperCase
@brackets
def concat(*args,**kwargs):
    sep = kwargs.get('sep',';')
    return sep.join(args)

if __name__ == '__main__':
    langs = ['python','c','c++','java']

    print(concat('anna','markus','maria','john', sep='|',))
    print(concat(*langs))
    print(concat(11,22,33,44,sep='-'))

    # print = upperCase(print)
    # print('hello python',end=' ',sep='$')
    # print(11,'sd',33,44,55,end=' ',sep='$')