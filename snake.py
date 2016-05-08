from collections import deque
import curses
#class because OOP, design classes to encapsulate objects. Things that you want to put data in
#are good classes. instead of having variables snake head, snake tail, etc. you just have class
#easier to edit, easier to manipulate/expand (ex. multiplayer = 2 instances of snake class)
class Snake:
    # Maps keyboard keys to directions, based on y-x changes.
    # For example, 'up' would move you in the negative y direction.
    KEYMAP = {
            # key            : (y, x)
            curses.KEY_UP    : [-1, 0],
            curses.KEY_DOWN  : [1, 0],
            curses.KEY_LEFT  : [0, -1],
            curses.KEY_RIGHT : [0, 1],
    }
    #start points, simpler
    y = 5
    x = 10
    tail_y = 5
    tail_x = 9
    #initial direction, simple and quick design
    body = deque([KEYMAP[curses.KEY_RIGHT]])
    direction = KEYMAP[curses.KEY_RIGHT]

    def set_direction(self, key):
        new_direction = self.KEYMAP[key]
        try:
            if new_direction != [-x for x in self.direction]:
                self.direction = new_direction
        except:
            pass

    def move_head(self):
        self.body.append(self.direction)
        self.y += self.direction[0]
        self.x += self.direction[1]

    def move_tail(self):
        tail_dir = self.body.popleft()
        self.tail_y += tail_dir[0]
        self.tail_x += tail_dir[1]

