# Problem 2
# The Product of the primes from 2 to some number n
from math import *
from ps1a import *

def get_log_primes_product(n):
    """ get the log-version of primes product """
    if (n < 1):
        raise ValueError("n must be positive integer")
    else:
        result = 0.0
        count = 1
        p = Prime.get_nth_prime(count)
        while (p <= n):
            result = result + log(p)
            count = count + 1
            p = Prime.get_nth_prime(count)

        return result



def get_ratio(n):
    """ calculate the diference to n """
    if (n < 1):
        raise ValueError("n must be positive integer")
    else:
        log = get_log_primes_product(n)
        return log/n
        







