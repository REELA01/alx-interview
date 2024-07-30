#!/usr/bin/python3
"""n-Queens Challenge"""

import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    solutions = []
    placed_queens = []
    stop = False
    ri = 0
    co = 0

    while ri < n:
        goback = False
        while co < n:
            safe = True
            for cord in placed_queens:
                col = cord[1]
                if(col == co or col + (ri-cord[0]) == co or
                        col - (ri-cord[0]) == co):
                    safe = False
                    break
            if not safe:
                if co == n - 1:
                    goback = True
                    break
                co += 1
                continue
            cords = [ri, co]
            placed_queens.append(cords)
            if ri == n - 1:
                solutions.append(placed_queens[:])
                for cord in placed_queens:
                    if cord[1] < n - 1:
                        ri = cord[0]
                        co = cord[1]
                for i in range(n - ri):
                    placed_queens.pop()
                if ri == n - 1 and co == n - 1:
                    placed_queens = []
                    stop = True
                ri -= 1
                co += 1
            else:
                co = 0
            break
        if stop:
            break
        if goback:
            ri -= 1
            while ri >= 0:
                co = placed_queens[ri][1] + 1
                del placed_queens[ri]
                if co < n:
                    break
                ri -= 1
            if ri < 0:
                break
            continue
        ri += 1
    for idx, val in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(val, end='')
        else:
            print(val)
