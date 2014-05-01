import curses, re
from PyDecipher import PyDecipher
from asl_encoding import asl_encoding

pd = PyDecipher(asl_encoding)

stdscr = curses.initscr()
ui = curses.newwin(3, 36, 1, 0)
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
    elif c == ord('0') or c == ord('1'):
        uiString += chr(c)
    else:
        pass


    ui.clear();
    res.clear();

    # print result string
    #splitUI = " ".join( i for i in re.findall("([01]{,8})",uiString) if i != "")
    splitUI = uiString

    # set curses color
    if pd.isValid(splitUI):
        valColor = 42

    else:
        valColor = 10
        # print binary outline ONLY if our string isn't already complete
        ui.addstr(0, 0, "00000000 00000000 "*((len(uiString)//16)+1), curses.color_pair(60))


    ui.addstr(0, 0, splitUI, curses.color_pair(valColor))
    ui.refresh()

    res.addstr(0, 0, pd.decipher(splitUI))
    res.refresh()

