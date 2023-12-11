'''
Given a large number, return a list of all the prime factors.
'''

import math

def prime_factors(n):
    prime_numbers = []
    while n % 2 == 0:
        n //= 2
        prime_numbers.append(2)
    
    for i in range(3, int(math.sqrt(n)) + 1):
        while n % i == 0:
            n //= i
            prime_numbers.append(i)
    if n > 2:
        prime_numbers.append(int(n))
    return prime_numbers