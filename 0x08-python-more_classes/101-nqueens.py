#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """Check if there is a queen in the same row on the left side.
    
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
        N (int): queens.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, N):
    """solving the queens.

    Args:
        board (list): The current working chessboar.
        col (int): The column where a queen was last played.
        N (int): queens.
    """
    if col >= N:
        print_solution(board)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, N) or res
            board[i][col] = 0

    return res


def print_solution(board):
    """printing the solutions.

    Args:
        board (list): the curent working chesssboar.
    """
    solution = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                solution.append([i, j])
    solution.sort()
    print(solution, end="\n"))
    print()


def nqueens(N):
    """defining the nqueens."""

    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
