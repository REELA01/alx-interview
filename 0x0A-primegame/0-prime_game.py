#!/usr/bin/python3
"""0x0A-primegame"""


def primes(n):
    """Return list of prime numbers"""
    pri = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            pri.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return pri


def isWinner(x, nums):
    """determines winner of Prime Game"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
