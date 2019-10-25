# 2

from functools import wraps

def upperCase(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        wrapper.__original = func
        args = [ str(v).upper() for v in args]
        return func(*args,**kwargs)
    return wrapper


@upperCase
def concat(*args,**kwargs):
    sep = kwargs.get('sep',';')
    return sep.join(args)

if __name__ == '__main__':
    langs = ['python','c','c++','java']

    s = concat('anna','markus','maria','john', sep='|')
    print(s)
    print(concat(*langs))
    print(concat(11,22,33,44,sep='-'))

    print(concat.__original(*langs))

    print = upperCase(print)
    print('hello python',end=' ',sep='$')