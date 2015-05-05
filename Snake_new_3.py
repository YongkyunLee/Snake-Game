from tkinter import*
import random
import time

class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.body = [[6, 2], [5, 2], [4, 2], [3, 2], [2, 2]]
        for x in range(0, len(self.body)):
            co_x = self.body[x][0]
            co_y = self.body[x][1]
            can_x1 = (co_x - 1) * 10
            can_y1 = (co_y - 1) * 10
            can_x2 = co_x * 10
            can_y2 = co_y * 10
            self.canvas.create_rectangle(can_x1, can_y1, can_x2, can_y2, fill="blue", outline="white")
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Up>', self.turn_up)
        self.canvas.bind_all('<KeyPress-Down>', self.turn_down)
        #self.canvas.bind_all('<KeyPress-Return>', self.start_game)
        self.press_key = 1
        self.dir = 0
        self.begin_move = 0
        self.started = False
        self.det = False
        self.move_count = 0
    #def start_game(self, evt):
        #self.started = True
    #dir만 받고 행동은 하지 않는다. 원래는 키보드를 누를 때 좌표가 바뀌었기 때문에 draw나 undraw가 되기 전에\
        #좌표가 바뀌어서 undraw가 바뀐 좌표에 대해서 실행되면 안 지워지는 블럭 하나가 남았었음
    def turn_right(self, evt):
        self.dir = 1
        self.move_count += 1
    def turn_left(self, evt):
        self.dir = 2
        self.move_count += 1
    def turn_up(self, evt):
        self.dir = 3
        self.move_count += 1
    def turn_down(self, evt):
        self.dir = 4
        self.move_count += 1
    def move(self):
        self.co_x = self.body[0][0]
        self.co_y = self.body[0][1]
        if dir == 1: #right
            self.body.insert(0, [self.co_x+1, self.co_y])
            del self.body[len(self.body)-1]
            self.press_key = 0
        if dir == 2: #left
            self.body.insert(0, [self.co_x-1, self.co_y])
            del self.body[len(self.body)-1]
            self.press_key = 0
        if dir == 3: #up
            self.body.insert(0, [self.co_x, self.co_y-1])
            del self.body[len(self.body)-1]
            self.press_key = 0
        if dir == 4: #down
            self.body.insert(0, [self.co_x, self.co_y+1])
            del self.body[len(self.body)-1]
            self.press_key = 0
        if self.press_key == 1:
            if self.dir == 1: #moving right
                self.body.insert(0, [self.co_x+1, self.co_y])
                del self.body[len(self.body)-1]
            if self.dir == 2: #moving left
                self.body.insert(0, [self.co_x-1, self.co_y])
                del self.body[len(self.body)-1]
            if self.dir == 3: #moving up
                self.body.insert(0, [self.co_x, self.co_y-1])
                del self.body[len(self.body)-1]
            if self.dir == 4: #moving down
                self.body.insert(0, [self.co_x, self.co_y+1])
                del self.body[len(self.body)-1]
    def out_of_bounds(self):
        if self.body[0][0] > 50 or self.body[0][0] < 1 or self.body[0][1] > 50 or self.body[0][1] < 1:
            return True
        else:
            return False
    def suicide(self):
        for x in range(0, len(self.body)):
            for y in range(x+1, len(self.body)):
                if self.body[x] == self.body[y]:
                    self.det = True
                    break
            if self.det == True:
                return True
                break
        return False
    def draw(self):
        head_x = self.body[0][0]
        head_y = self.body[0][1]
        can_x1 = (head_x - 1) * 10
        can_y1 = (head_y - 1) * 10
        can_x2 = head_x * 10
        can_y2 = head_y * 10
        self.canvas.create_rectangle(can_x1, can_y1, can_x2, can_y2, fill="blue", outline="white")
        self.press_key = 1
    def undraw(self):
        tail_x = self.body[len(self.body)-1][0]
        tail_y = self.body[len(self.body)-1][1]
        can_x1 = (tail_x - 1) * 10
        can_y1 = (tail_y - 1) * 10
        can_x2 = tail_x * 10
        can_y2 = tail_y * 10
        #if self.dir != 0:
        if self.move_count != 0:
            self.canvas.create_rectangle(can_x1, can_y1, can_x2, can_y2, fill="white", outline="white")
        if self.move_count == 1:
            self.canvas.create_rectangle(10, 10, 20, 20, fill="white", outline="white")
        self.press_key = 1                
    #def clear(self):
        #self.body_length = len(self.body)
        #for x in range(0, self.body-length-1):
            #self.canvas.itemconfigure(self.rec_list[x], fill="white")

tk = Tk()
tk.title("Snake")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

snake = Snake(canvas)

while 1:
    if snake.out_of_bounds() == False and snake.suicide() == False:
        print(snake.body)
        print(snake.move_count)
        snake.move()
        snake.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.05)
        snake.undraw()
        tk.update_idletasks()
        tk.update()
        #canvas.delete("all")
        #tk.update_idletasks()
        #tk.update()
    else:
        break
