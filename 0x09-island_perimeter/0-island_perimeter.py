#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""
def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid
    Args:
    grid: is a list of list of integers

    Returns:
    int: Perimeter of the island.
    """
    h_cells = len(grid)
    v_cells = len(grid[0])
    perimeter = 0
    
    for i in range(h_cells):
        for j in range(v_cells):
            if grid[i][j] == 1:
                # Check all four possible sides (top, bottom, left, right)
                if i == 0 or grid[i-1][j] == 0:  # Top side
                    perimeter += 1
                if i == h_cells-1 or grid[i+1][j] == 0:  # Bottom side
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Left side
                    perimeter += 1
                if j == v_cells-1 or grid[i][j+1] == 0:  # Right side
                    perimeter += 1
    return perimeter
