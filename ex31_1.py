# Глобална променлива

# 1. деклариция
# kwargs - keyword arguments
def show(title, *, k1,k2,**kwargs): 
    print(f'positional: title={title}')
    print(f'keyword only:k1={k1} k2={k2}')
    

if __name__ == '__main__':
    # 2. извикване
    show('Text Editor',k2='R',k1='F')

    show('Text Editor',k1='C',k2='XX')

    show('Text Editor',k1='X',k2='Z',path='/usr/local')
    
    
