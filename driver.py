import graphics
import generator
import time
from matplotlib import pyplot as plt

def main():
    win = graphics.GraphWin(width=generator.GRID_WIDTH * generator.BOX_SIZE, height=generator.GRID_HEIGHT * generator.BOX_SIZE)
    win.setBackground("white")
    win.setCoords(0, 0, generator.GRID_WIDTH, generator.GRID_HEIGHT)

    board = generator.Board(generator.GRID_HEIGHT, generator.GRID_WIDTH)
    while not board.stable:
        for i in range(generator.GRID_HEIGHT):
            for j in range(generator.GRID_WIDTH):
                currentState = board.getState()
                if currentState[i][j] == 1:
                    box = graphics.Rectangle(graphics.Point(generator.GRID_WIDTH-j, generator.GRID_HEIGHT-i), graphics.Point(generator.GRID_WIDTH-(j + 1), generator.GRID_HEIGHT-(i + 1)))
                    box.setFill("black")
                    box.draw(win)

            board._next_state()


    win.getMouse()
    win.close()  



main()