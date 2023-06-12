from tkinter import Button


class Cell:
    def revealCell(self, colour_pallette):
        self.button.config(text=self.value, fg=colour_pallette[str(self.value)], relief=self.PRESSED_RELIEF)


    def __init__(self, x, y, value, parent):
        self.PRESSED_RELIEF = 'sunken'
        self.BUTTON_WIDTH = 2
        self.BACKGROUND_COLOR = '#CACACA'
        self.x = x
        self.y = y
        self.value = value
        self.button = Button(width=self.BUTTON_WIDTH, bg=self.BACKGROUND_COLOR, command=lambda: parent.updateBoard(self.x, self.y))
