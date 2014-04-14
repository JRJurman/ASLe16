import curses
from PyDecipher import PyDecipher
from asl_encoding import asl_encoding

pd = PyDecipher(asl_encoding)

stdscr = curses.initscr()
ui = curses.newwin(3, 17, 1, 0)
res = curses.newwin(40, 40, 4, 0)

curses.noecho()
curses.start_color()
curses.use_default_colors()
for i in range(0, curses.COLORS):
    curses.init_pair(i + 1, i, -1)

uiString = ""

# input loop
while 1:

    # get next character and add to string
    c = stdscr.getch()
    if c == ord('q'):
        break  # Exit the while()
    elif c == 127:
        uiString = uiString[:len(uiString)-1]
    else:
        uiString += chr(c)

    # set curses color
    if pd.isValid(uiString):
        valColor = 42
    else:
        valColor = 10

    # print result string
    ui.clear();
    ui.addstr(0, 0, "00000000 00000000", curses.color_pair(60))
    ui.addstr(0, 0, uiString, curses.color_pair(valColor))
    ui.refresh()

    res.clear();
    res.addstr(0, 0, pd.decipher(uiString))
    res.refresh()

