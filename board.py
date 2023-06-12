from random import randint

reveal_mine = lambda x : 9 if x == -119 else x

class Board:
    SURROUNDED = 8
    EMPTY = 0
    MINE = 9
    HIDDEN_MINE = -119

    def getSurroundingMines(self, x, y, MINE_VALUE): 
        surrounding_mines = 0

        # Checks the following cells:

        #   234
        #   1x5
        #   876

        # Supports asymmetrical boards!

        if x > 0:
            if self.board[y][x-1] == MINE_VALUE:  # 1
                surrounding_mines += 1

            if y > 0 and self.board[y-1][x-1] == MINE_VALUE:  # 2
                surrounding_mines += 1

            if y < len(self.board)-1 and self.board[y+1][x-1] == MINE_VALUE:  # 8
                surrounding_mines += 1


        if y > 0:
            if self.board[y-1][x] == MINE_VALUE:  # 3
                    surrounding_mines += 1

            if x < len(self.board[y-1])-1 and self.board[y-1][x+1] == MINE_VALUE:  # 4
                    surrounding_mines += 1


        if y < len(self.board)-1:
            if x < len(self.board[y+1])-1 and self.board[y+1][x+1] == MINE_VALUE:  # 6
                surrounding_mines += 1

            if x < len(self.board[y+1]) and self.board[y+1][x] == MINE_VALUE:  # 7
                surrounding_mines += 1


        if x < len(self.board[y])-1 and self.board[y][x+1] == MINE_VALUE:  # 5
            surrounding_mines += 1

        return surrounding_mines
    

    def openSurroundingCells(self, x, y):
        #   234
        #   1x5
        #   876

        if self.board[y][x] < 0:
            self.board[y][x] += 128

        if self.board[y][x] == self.EMPTY:

            if x > 0:
                if self.board[y][x-1] < 0:  # 1
                    self.openSurroundingCells(x-1, y)

                if y > 0 and self.board[y-1][x-1] < 0:  # 2
                    self.openSurroundingCells(x-1, y-1)

                if y < len(self.board)-1 and self.board[y+1][x-1] < 0:  # 8
                    self.openSurroundingCells(x-1, y+1)


            if y > 0:
                if self.board[y-1][x] < 0:  # 3
                        self.openSurroundingCells(x, y-1)

                if x < len(self.board[y-1])-1 and self.board[y-1][x+1] < 0:  # 4
                        self.openSurroundingCells(x+1, y-1)


            if y < len(self.board)-1:
                if x < len(self.board[y+1])-1 and self.board[y+1][x+1] < 0:  # 6
                    self.openSurroundingCells(x+1, y+1)

                if x < len(self.board[y+1]) and self.board[y+1][x] < 0:  # 7
                    self.openSurroundingCells(x, y+1)


            if x < len(self.board[y])-1 and self.board[y][x+1] < 0:  # 5
                self.openSurroundingCells(x+1, y)
        
                
        elif self.board[y][x] == self.MINE:
            for column in range(len(self.board)):
                for index in range(len(self.board[column])):
                    self.board[column][index] = reveal_mine(self.board[column][index])


    def updateBoardNumbers(self):
        for y in range(self.height):
            for x in range(len(self.board[y])):
                if self.board[y][x] != self.HIDDEN_MINE:
                    self.board[y][x] = self.getSurroundingMines(x, y, self.HIDDEN_MINE) - 128


    def moveMineToFirstEmpty(self, x, y):
        for column in range(self.height):
            for row in range(len(column)):
                value = self.board[column][row]
                if value != self.HIDDEN_MINE:
                    self.board[column][row] = self.HIDDEN_MINE
                    self.board[column][row] = self.EMPTY
                    self.updateBoardNumbers()

    
    def __init__(self, height, width, mines):
        self.height = height
        self.board = [[self.EMPTY] * width for _ in range(height)]

        total_mines = self.EMPTY
        available_coords = []

        for y in range(self.height):
            for x in range(len(self.board[y])):
                available_coords.append((x, y))

        while total_mines < mines:
            random_index = randint(0, len(available_coords)-1)
            mine_x, mine_y = available_coords.pop(random_index)

            if self.getSurroundingMines(mine_x, mine_y, self.MINE) < self.SURROUNDED:
                self.board[mine_y][mine_x] = self.HIDDEN_MINE  # Negative number = unrevealed cell, add 128 to get real value.
                total_mines += 1
        self.updateBoardNumbers()
 
