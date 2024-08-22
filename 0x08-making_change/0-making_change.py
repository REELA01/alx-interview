#!/usr/bin/python3
"""change making module"""


def makeChange(coins, total):
    """cetermines the fewest number of coins needed"""
    if total <= 0:
        return 0
    remi = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while remi > 0:
        if coin_idx >= n:
            return -1
        if remi - sorted_coins[coin_idx] >= 0:
            remi -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
