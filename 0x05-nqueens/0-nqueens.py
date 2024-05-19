#!/usr/bin/python3
""" N Queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard
"""
import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n_queens = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n_queens < 4:
    print('N must be at least 4')
    exit(1)


def solve_nQ(n):
    """Method that solves the N queens problem"""
    if n == 0:
        return [[]]
    first_solution = solve_nQ(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(n_queens)
            for solution in first_solution
            if safeQueen((n, i + 1), solution)]


def attackQueen(square, queen):
    """Method for the queen to attack"""
    (row, column) = square
    (row1, column1) = queen
    return (row == row1) or (column == column1) or\
        abs(row - row1) == abs(column - column1)


def safeQueen(sqr, queens):
    """Method for the queen to be safe"""
    for queen in queens:
        if attackQueen(sqr, queen):
            return False
    return True


for answer in reversed(solve_nQ(n_queens)):
    result = []
    for p in [list(p) for p in answer]:
        result.append([i - 1 for i in p])
    print(result)
