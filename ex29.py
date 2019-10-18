# Глобална променлива

# 1. деклариция
# kwargs - keyword arguments
def show(title, *args, **kwargs): 
    print(f'positional: title={title}')

    print('list of args:' + ','.join(map(str,args)))
    for v in args:
        print(f'arg:{v}')

    print('Keyword args')
    if 'path' in kwargs:
        print(f'path:{kwargs["path"]}')

    if 'log' in kwargs:
        print(f'log file:{kwargs["log"]}')


if __name__ == '__main__':
    # 2. извикване
    show('Text Editor')

    show('Text Editor',11,22,33)

    show('Text Editor',11,22,33,log='/var/log/editor.log',path='/usr/local')
    
    appConfig = {
          'log':'/var/log/editor.log'
        , 'path':'/usr/local'
        , 'max_mem':4096
    }
    
    show('Text Editor',11,22,33, **appConfig)

    
