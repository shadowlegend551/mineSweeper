from ui import Ui
from settings import get_settings



def main():
    settings = get_settings('settings.json')

    HEIGHT = settings['size']['height']
    WIDTH = settings['size']['width']
    COLOURS = settings['colours']
    MINES = settings['mines']

    board = Ui(HEIGHT, WIDTH, COLOURS, MINES)
    board.root.mainloop()


if __name__ == '__main__':
    main()
