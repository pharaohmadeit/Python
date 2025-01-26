# coding: utf-8
# cache expensive calculations to improve recursive O(n)
import time
def fibonacci_memoized(n, calls=[0], cache={}):
    calls[0] += 1
    if n in cache:
        return cache[n]
    if n in (0, 1):
        return n
    cache[n] = (fibonacci_memoized(n-1, calls, cache) + fibonacci_memoized(n-2, calls, cache))
    return cache[n]
    
def timed_fibonacci(n):
    calls = [0]
    cache = {}
    start_time = time.time()
    result = fibonacci_memoized(n, calls, cache)
    end_time = time.time()
    print(f'Fibonacci({n:<2d}) = {result:<12,d}Calls{calls[0]:<12,d}',
          f'Seconds: {(end_time - start_time):>13,.10f}')
          
for n in range(41):
    timed_fibonacci(n)
    
