from tkinter import*
import random
import time

class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.body = [[6, 2], [5, 2], [4, 2], [3, 2], [2, 2]]
        self.body_length = 5
        #self.canvas.create_rectangle(10, 10, 20, 20, fill="blue", outline="white")
        #self.canvas.create_rectangle(20, 10, 30, 20, fill="blue", outline="white")
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Up>', self.turn_up)
        self.canvas.bind_all('<KeyPress-Down>', self.turn_down)
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)
        #self.rec_list = None
        self.press_key = 1
        self.started = False
        self.dir = 0
    def start_game(self, evt):
        self.started = True
    def turn_right(self, evt):
        self.co_x = self.body[0][0]
        self.co_y = self.body[0][1]
        self.body.insert(0, [self.co_x+1, self.co_y])
        del self.body[len(self.body)-1]
        self.press_key = 0
        self.dir = 1
    def turn_left(self, evt):
        self.co_x = self.body[0][0]
        self.co_y = self.body[0][1]
        self.body.insert(0, [self.co_x-1, self.co_y])
        del self.body[len(self.body)-1]
        self.press_key = 0
        self.dir = 2
    def turn_up(self, evt):
        self.co_x = self.body[0][0]
        self.co_y = self.body[0][1]
        self.body.insert(0, [self.co_x, self.co_y-1])
        del self.body[len(self.body)-1]
        self.press_key = 0
        self.dir = 3
    def turn_down(self, evt):
        self.co_x = self.body[0][0]
        self.co_y = self.body[0][1]
        self.body.insert(0, [self.co_x, self.co_y+1])
        del self.body[len(self.body)-1]
        self.press_key = 0
        self.dir = 4
    def move(self):
        self.co_x = self.body[0][0]
        self.co_y = self.body[0][1]
        if self.press_key == 1:
            if self.body[0][0] - self.body[1][0] == 1 and self.body[0][1] - self.body[1][1] == 0: #moving right
                self.body.insert(0, [self.co_x+1, self.co_y])
#                self.body_length = len(self.body)
#                del self.body[self.body_length-1]
                del self.body[len(self.body)-1]
            if self.body[0][0] - self.body[1][0] == -1 and self.body[0][1] - self.body[1][1] == 0: #moving left
                self.body.insert(0, [self.co_x-1, self.co_y])
                #self.body_length = len(self.body)
                del self.body[len(self.body)-1]
            if self.body[0][0] - self.body[1][0] == 0 and self.body[0][1] - self.body[1][1] == -1: #moving up
                self.body.insert(0, [self.co_x, self.co_y-1])
                #self.body_length = len(self.body)
                del self.body[len(self.body)-1]
            if self.body[0][0] - self.body[1][0] == 0 and self.body[0][1] - self.body[1][1] == 1: #moving down
                self.body.insert(0, [self.co_x, self.co_y+1])
                del self.body[len(self.body)-1]
    def draw(self):
        self.body_length = len(self.body)
        for x in range(0, self.body_length):
            co_x = self.body[x][0]
            co_y = self.body[x][1]
            can_x1 = (co_x - 1) * 10
            can_y1 = (co_y - 1) * 10
            can_x2 = co_x * 10
            can_y2 = co_y * 10
            self.canvas.create_rectangle(can_x1, can_y1, can_x2, can_y2, fill="blue", outline="white")
        self.press_key = 1
    def undraw(self):
        self.body_length = len(self.body)
        for x in range(0, self.body_length):
            co_x = self.body[x][0]
            co_y = self.body[x][1]
            can_x1 = (co_x - 1) * 10
            can_y1 = (co_y - 1) * 10
            can_x2 = co_x * 10
            can_y2 = co_y * 10
            self.canvas.create_rectangle(can_x1, can_y1, can_x2, can_y2, fill="white", outline="white")
        self.press_key = 1
    #def clear(self):
        #self.body_length = len(self.body)
        #for x in range(0, self.body-length-1):
            #self.canvas.itemconfigure(self.rec_list[x], fill="white")

tk = Tk()
tk.title("Snake")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

snake = Snake(canvas)

while 1:
#    if snake.started == True:
    #print(snake.body)
    snake.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.05)
    snake.undraw()
    tk.update_idletasks()
    tk.update()
    #time.sleep(0.1)
    snake.move()
        #canvas.delete("all")
        #tk.update_idletasks()
        #tk.update()
