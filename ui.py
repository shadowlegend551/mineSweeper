from tkinter import Tk
import numpy as np

from board import Board
from cell import Cell


class Ui:
    def updateBoard(self, x, y):
        self.board.openSurroundingCells(x, y)

        for column in self.cells:
            for cell in column:
                if cell.value != self.board.board[cell.y][cell.x]:
                    cell.value = self.board.board[cell.y][cell.x]

                    cell.revealCell(self.colours)


    def __init__(self, height, width, colour_settings, mines_amount):

        self.colours = colour_settings

        board_template = np.zeros((width, height), dtype=np.int8)
        self.cells = np.empty_like(board_template, dtype=Cell)

        self.root = Tk()
        self.board = Board(board_template, mines_amount)

        for y in range(height):
            for x in range(width):
                self.cells[y][x] = Cell(x, y, self.board.board[y][x], self, self.updateBoard)
                self.cells[y][x].button.grid(row=y, column=x)
