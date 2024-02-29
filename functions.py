#!/usr/bin/env python3
"""Funciones para la Tarea 1 del curso de Python de Hackers Fight Club"""

import math


def longest_pal(s):
    """Function to find the longest substring of s that is a palindrome."""
    if not s:
        return s

    def expand_pal(lo, hi):
        while lo - 1 >= 0 and hi + 1 < len(s):
            if s[lo-1] != s[hi+1]:
                break
            lo -= 1
            hi += 1
        return s[lo:hi+1]

    longest = s[0]
    for idx in range(len(s)):
        if idx + 1 < len(s):
            if s[idx] == s[idx+1]:
                if len(result := expand_pal(idx, idx+1)) > len(longest):
                    longest = result
            if idx - 1 >= 0:
                if s[idx-1] == s[idx+1]:
                    if len(result := expand_pal(idx-1, idx+1)) > len(longest):
                        longest = result
    return longest


def is_prime(n):
    """Function that returns whether n is a prime number or not."""
    for i in range(2, int(math.sqrt(n)) + 1):
        if not n % i:
            return False
    return True


def find_primes(n):
    """Function to find the first n primes."""
    if not n:
        return []
    primes = [2]

    def find_primes(i):
        if len(primes) >= n:
            return primes
        elif all(map(lambda x: i % x, primes)):
            primes.append(i)
        return find_primes(i + 2)
    return find_primes(3)

# Versión iterativa
# def find_primes(n):
#     if not n: return []
#     primes = [2]
#     i = 3
#     while len(primes) < n:
#         if all(map(lambda x: i % x, primes)):
#             primes.append(i)
#         i += 2
#     return primes
