from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    x1 =10
    x2 = 20
    y1 = 10
    y2 = 20

    cell = Cell(win)

    cell.draw(x1,y1,x2,y2)
    cell._win.wait_for_close()


if __name__ == "__main__":
    main()
