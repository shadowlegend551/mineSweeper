from tkinter import Button


class Cell:
    def revealCell(self, colour_pallette):
        self.button.config(text=self.value, fg=colour_pallette[str(self.value)], relief='sunken')


    def __init__(self, x, y, value, parent, function):
        self.parent = parent
        self.x = x
        self.y = y
        self.value = value
        self.button = Button(width=2, bg='#CACACA', command=lambda: function(self.x, self.y))
