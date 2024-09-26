# You can get the time for your program to run with these:


import time
tic = time.perf_counter() # Stores the current time

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Örnek kullanım
number = 320166
print(f"{number} sayısının asal çarpanları: {prime_factors(number)}")


toc = time.perf_counter() - tic
print(toc*1000) # In seconds. To see it in miliseconds, multiply 'toc' with 1000.
