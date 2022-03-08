#!/usr/bin/python3

import sys


def init_board(n):
    """ initialize an n x n sized chessboard with 0s"""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def deepcopy(board):
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
        return (board)

        def get_solution(board):
            solution = []
            for r in range(len(board)):
                for c in range(len(board)):
                    if board[r][c] == "Q":
                        solution.append9[r, c]
                        break
            return (solution)


def xout(board, row, col):
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
        c = col + 1
        for r in range(row + 1, len(board)):
            if c >= len(board):
                break
            board[r][c] = "x"
            c += 1
        c = col - 1
        for r in range(row + 1, len(board)):
            if x < 0:
                break
            board[r][c] = "x"
            c -= 1
