import curses
import time
import random
from snake import Snake

# Initialize curses
stdscr = curses.initscr()
if curses.has_colors:
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_RED)

curses.curs_set(0)   # Don't display the text cursor
curses.noecho()      # Don't echo key presses to the screen
stdscr.keypad(True)  # Translate raw key codes into key identifiers
stdscr.nodelay(True) # Non-blocking mode (don't pause and wait for keypresses)

snake = Snake()
maxyx = stdscr.getmaxyx()
max_y = maxyx[0] - 1
max_x = maxyx[1] - 1

# f is for food, it's good enough for me
stdscr.addstr(10, 15, 'f', curses.color_pair(2))
stdscr.addstr(2, 2, 'f', curses.color_pair(2))
stdscr.addstr(6, 8, 'f', curses.color_pair(2))

def add_food():
    random_y = random.randint(2, max_y)
    random_x = random.randint(0, max_x)
    plop_space = chr(stdscr.inch(random_y, random_x) & 0xFF)
    if plop_space != ' ':
        add_food()
    else:
        stdscr.addstr(random_y, random_x, 'f', curses.color_pair(2))

score = 0

def update_score(score):
    score += 1
    score_str = 'Score: %d' % score
    stdscr.addstr(0, curses.COLS - len(score_str), 'Score: %d' % score)
    return score
    
update_score(-1)

while True:
    snake.move_head()
    if snake.x < 0 or snake.y < 0 or snake.x > max_x or snake.y > max_y:
        # Out of bounds
        break

    headchar = chr(stdscr.inch(snake.y, snake.x) & 0xFF)
    if headchar == 'x'
        # Nommed self or border
        break

        # Draw new head position
    stdscr.addstr(snake.y, snake.x, 'x', curses.color_pair(1))

    if headchar == 'f':
        add_food()
        update_score(score)
        # Ate food! (add new food, update score)
        pass
    else:
        # Didn't eat anything. Shrink the tail by putting a space at the end.
        snake.move_tail()
        stdscr.addstr(snake.tail_y, snake.tail_x, ' ')

    # Apply all our graphics changes
    stdscr.refresh()

    time.sleep(0.05) # If I wanted to make the game harder, I might start here...

    button = stdscr.getch()
    if button == ord('q'):
        # Q is for quitting, it's also good enough for me
        break
    else:
        snake.set_direction(button)

curses.endwin() # Out of the game loop, clean up curses
print('bye!')
