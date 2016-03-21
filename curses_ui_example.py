
import curses, sys

def quit():
    curses.endwin()

#Initialize our display screen
screen = curses.initscr()
#don't show blinking cursor
curses.curs_set(0)

#global application state
counter = 0

try:
    while 1:
        #draw our UI
        screen.clear()
        screen.border(0)
        row = 1
        column = 2
        screen.addstr(row, column, "Sick-ass curses UI")
        row += 1
        screen.addstr(row, column, "Counter: {}".format(counter))
        row += 1
        screen.addstr(row, column, "'q' to quit")
        row += 1
        screen.addstr(row, column, 'spacebar to increment counter')
        screen.refresh()

        #get keyboard input and react
        ch = screen.getch()
        if ch == ord('q'):
            #break out of while loop to quit app
            break
        elif ch == ord(' '): #spacebar emits a space character
            counter += 1

except:
    #catch any problems in our application, allow curses to set terminal state back to normal
    quit()
    raise

quit()
