#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Return the perimeter of the island"""
    count = 0
    grid_max = len(grid) - 1
    lst_max = len(grid[0]) - 1

    for lst_idx, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:
                if land_idx == 0:
                    count += 1
                    if lst[land_idx + 1] == 0:
                        count += 1
                elif land_idx == lst_max:
                    if lst[land_idx - 1] == 0:
                        count += 1
                    count += 1
                else:
                    if lst[land_idx - 1] == 0:
                        count += 1
                    if lst[land_idx + 1] == 0:
                        count += 1
                if lst_idx == 0:
                    count += 1
                    if grid[lst_idx + 1][land_idx] == 0:
                        count += 1
                elif lst_idx == grid_max:
                    if grid[lst_idx - 1][land_idx] == 0:
                        count += 1
                    count += 1
                else:
                    if grid[lst_idx - 1][land_idx] == 0:
                        count += 1
                    if grid[lst_idx + 1][land_idx] == 0:
                        count += 1
    return count
