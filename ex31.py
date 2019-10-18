# Глобална променлива

# 1. деклариция
# kwargs - keyword arguments
def show(title, *args, k1,k2,**kwargs): 
    print(f'positional: title={title}')
    print(f'keyword only:k1={k1} k2={k2}')
    

if __name__ == '__main__':
    # 2. извикване
    show('Text Editor',k1='F',k2='R')

    show('Text Editor',11,22,33,k1='C',k2='XX')

    show('Text Editor',11,22,33,k1='X',k2='Z',path='/usr/local')
    
    
