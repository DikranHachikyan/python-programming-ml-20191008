# Глобална променлива

# 1. деклариция
# kwargs - keyword arguments
def show(title, *args, **kwargs): 
    print(f'positional: title={title}')

    print('list of args:' + ','.join(map(str,args)))
    for v in args:
        print(f'arg:{v}')

    print('Keyword args')
    kw_params = {
          'path': kwargs.get('path','/tmp')
        , 'log' : kwargs.get('log', '/var/log/messages')
    }
    print(f'{kw_params}')

if __name__ == '__main__':
    # 2. извикване
    show('Text Editor')

    show('Text Editor',11,22,33)

    show('Text Editor',11,22,33,path='/usr/local')
    
    
