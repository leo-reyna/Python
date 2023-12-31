# Jan 2023
# RL 
# Essential Python Exercises

import os
import time

from termcolor import colored, cprint


class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [['░' for y in range(self._y)] for x in range(self._x)]  # '' = you can use whatever your want
        # to draw the canvas

    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            cprint(' '.join([col[y] for col in self._canvas]), "red")


class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '•'
        self.mark = '▒'
        self.framerate = 0.5  # was 0.2
        self.pos = [2, 2]  # was 0, 0

    def up(self):
        pos = [self.pos[0], self.pos[1] - 1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1] + 1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0] + 1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0] - 1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, "green"))
        self.canvas.print()
        time.sleep(self.framerate)


canvas = Canvas(14, 9)  # 14 columns #9 rows
scribe = TerminalScribe(canvas)

scribe.right()
scribe.right()
scribe.right()
scribe.right()
scribe.right()
scribe.right()
scribe.right()
scribe.right()
scribe.right()
scribe.down()
scribe.down()
scribe.down()
scribe.down()
scribe.left()
scribe.left()
scribe.left()
scribe.left()
scribe.left()
scribe.left()
scribe.left()
scribe.left()
scribe.left()
scribe.up()
scribe.up()
scribe.up()
scribe.up()
