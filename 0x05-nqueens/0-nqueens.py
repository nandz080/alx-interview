#!/usr/bin/python3
""" N Queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard
"""
import sys

def is_safe(board, row, column):
    """Method that checks if it's safe to place a queen at board[row][col]"""
    for i in range(row):
        if board[i] == column or \
           board[i] - i == column - row or \
           board[i] + i == column + row:
            return False
    return True

def solve_nqueens(N):
    """Method that solves the N Queens problem and prints all solutions"""
    def solve(row, board):
        if row == N:
            print_board(board)
            return
        for column in range(N):
            if is_safe(board, row, column):
                board[row] = column
                solve(row + 1, board)
                board[row] = -1  # Backtrack

    def print_board(board):
        """Method that prints solution"""
        solution = []
        for i in range(N):
            solution.append([i, board[i]])
        print(solution)
    
    board = [-1] * N
    solve(0, board)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solve_nqueens(N)

if __name__ == "__main__":
    main()
