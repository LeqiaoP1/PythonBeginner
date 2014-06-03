# for problem 1
# write a program that computes and prints the 1000th prime number
from math import *

class IllegalArgumentError(ValueError):
    pass


class Prime(object):
    """ generator of prime numbers """
    @staticmethod
    def is_prime(n):
        """ check if input "n" is prime number or not"""
        if (n < 2):
            return False
        else:
            for d in range(2, int(sqrt(n))+1):
                if (n%d == 0):
                    return False
            
            return True


    @staticmethod
    def get_nth_prime(n):
        """ find and return the nth prime number """
        if (n <= 0):
            raise ValueError("n must be positive integer")
        elif (n == 1):
            return 2
        else:
            count = 1
            candidate = 1
            while (count < n):
                candidate = candidate + 2 # odd
                if (Prime.is_prime(candidate)):
                    count = count + 1

                    
        return candidate
    
