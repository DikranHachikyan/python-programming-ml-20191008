# Глобална променлива

# 1. деклариция
# 

def foo(a=[],b={}):
    print(f'a:{a}')
    print(f'b:{b}')
    print('-' * 12)
    a.append(len(a))
    b[len(a)] = len(a)

if __name__ == '__main__':
    # 2. извикване
    foo()
    foo([1,2,3],{'B':100})
    foo()
    foo([11,22,33],{'C':10})
    foo()
    
    
