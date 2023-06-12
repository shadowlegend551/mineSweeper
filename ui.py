from tkinter import Tk

from board import Board
from cell import Cell


class Ui:
    def updateBoard(self, x, y):
        self.backend_board.openSurroundingCells(x, y)

        for column in self.visual_board:
            for cell in column:
                if cell.value != self.backend_board.board[cell.y][cell.x]:
                    cell.value = self.backend_board.board[cell.y][cell.x]

                    cell.revealCell(self.colours)


    def __init__(self, height, width, colour_settings, mines_amount):

        self.root = Tk()
        self.colours = colour_settings
        self.visual_board = []

        self.backend_board = Board(height, width, mines_amount)

        for y in range(height):
            self.visual_board.append([])
            for x in range(width):
                self.visual_board[y].append(Cell(x, y, self.backend_board.board[y][x], self))
                self.visual_board[y][x].button.grid(row=y, column=x)
