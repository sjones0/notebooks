
import time
def fib(n):
#    print(n,end=' ')
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

x = int(input('Enter number of terms: '))
t = time.perf_counter()
for i in range(x):
    f = fib(i)
    t2 = time.perf_counter()-t
    print(f'{i:3} {t2:10.5f} {f:10}')
    t = time.perf_counter()

