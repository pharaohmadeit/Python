# coding: utf-8
import time
def fibonacci(n, calls=[0]):
    calls[0] += 1
    if n in (0, 1):
        return n
    return fibonacci(n - 1, calls) + fibonacci(n - 2, calls)
    
def timed_fibonacci(n):
    calls = [0]
    start_time = time.time()
    result = fibonacci(n, calls)
    end_time = time.time()
    print(f'Fibonacci({n:<2d}) = {result:<12,d}Calls: {calls[0]:<12,d}',
          f'Seconds: {(end_time - start_time):>13,.10f}')
          
for n in range(41):
    timed_fibonacci(n)
    
204,668,309 * 1.618
204668309 * 1.618
