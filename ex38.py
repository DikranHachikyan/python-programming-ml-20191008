# 2
from time import time,sleep

def foo():
    sleep(0.3)

def bar():
    sleep(0.5)

t = time()
foo()
print(f'foo:{time()-t:.4f}')    

t = time()
bar()
print(f'bar:{time()-t:.4f}')    