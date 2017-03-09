#!/usr/bin/env python
#import actor
import mapper
import curses


global y
global x
global py
#global px
global moving
y = py = 1
x = 1
moving = True

global mapper
mapper = mapper.mapper()
#from mapper.py generate a map
global map
map = mapper.map

#Initialization of the curses window stdscr
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(0)
stdscr.keypad(1)

def QuitGame():
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.curs_set(1)
    curses.endwin()

def update():
    global py
    #global px
    global moving

    stdscr.clear()

    mapy = mapper.mmapy

    #For the TOP rendering
    if py <= 10:
        moving = True
        for yy in xrange(20):
            for xx in xrange(mapper.mmapx):
                stdscr.addstr(yy, xx, map[yy][xx])
    #For the BOTTOM rendering
    elif py >= mapy - 10:
        startY = 0
        moving = True
        for yy in xrange(mapy - 20, mapy):
            startY += 1
            for xx in xrange(mapper.mmapx):
                stdscr.addstr(startY-1, xx, map[yy][xx])
    #For the MIDDLE rendering
    else:
        startY = 0
        moving = False
        for yy in xrange(py - 10, py + 10):
            startY += 1
            for xx in xrange(mapper.mmapx):
                stdscr.addstr(startY-1, xx, map[yy][xx])

    stdscr.addstr(1, 16, str(py))
    stdscr.addstr(1, 19, str(y))
    stdscr.refresh()

def walkable(y, x):
    if map[y][x] == ".":
        return True

    return False

def digable(y, x):
    if map[y][x] == "#":
        return True

    return False

def dig():
    global py
    global x
    y = py

    c = stdscr.getch()
    if c == ord('w'):
        if not walkable(y-1, x) and digable(y-1, x):
            map[y-1][x] = "."
    elif c == ord('s'):
        if not walkable(y+1, x) and digable(y+1, x):
            map[y+1][x] = "."
    elif c == ord('a'):
        if not walkable(y, x-1) and digable(y, x-1):
            map[y][x-1] = "."
    elif c == ord('d'):
        if not walkable(y, x+1) and digable(y, x+1):
            map[y][x+1] = "."
    else:
        stdscr.addstr(21, 1, "Wrong direction.(try wasd)")
        stdscr.refresh()
        stdscr.getch()

def main():
    global y
    global x
    global py

    update()
    stdscr.addstr(y,x, "@")
    stdscr.refresh()

    while 1:
        c = stdscr.getch()

        if c == ord('w'):
            if walkable(py - 1, x):
                py -= 1
        elif c == ord('s'):
            if walkable(py + 1, x):
                py += 1
        elif c == ord('a'):
            if walkable(py, x - 1):
                x -= 1
        elif c == ord('d'):
            if walkable(py, x + 1):
                x += 1
        #Shift + q to quit
        if c == ord('Q'):
            break
        if c == ord('f'):
            stdscr.addstr(21, 1, "Choose direction.")
            stdscr.refresh()
            dig()

        if moving and (py<=10 or py>=mapper.mmapy - 10):
            y = py

        update()
        if y <= 10:
            stdscr.addstr(y,x, "@")
        elif y >= mapper.mmapy-10:
            stdscr.addstr(y - (mapper.mmapy - 20), x, "@")

    QuitGame()

if __name__ == '__main__':
    main()
