from tkinter import *
import random
import time

class Snake:
    def __init__(self, canvas, fruit):
        self.canvas = canvas
        self.fruit = fruit
        self.snake_id = canvas.create_rectangle(0, 0, 10, 10, fill="blue")
        self.canvas.move(self.snake_id, 10, 10)
        self.body = [[2,2]]
        self.body_length = len(self.body)
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        self.canvas.bind_all('<KeyPress-Down>', self.move_down)
        self.canvas.bind_all('<KeyPress-Up>', self.move_up)
        self.press_key = 1
        self.begin = 0
        self.suicide = False
    def move_right(self, evt):
        co_x1 = self.body[0][0]
        co_y1 = self.body[0][1]
        self.body.insert(0, [co_x1+1, co_y1])
        self.body_length = len(self.body)
        del self.body[self.body_length-1]
        self.press_key = 0
    def move_left(self, evt):
        co_x1 = self.body[0][0]
        co_y1 = self.body[0][1]
        self.body.insert(0, [co_x1-1, co_y1])
        self.body_length = len(self.body)
        del self.body[self.body_length-1]
        self.press_key = 0
    def move_up(self, evt):
        co_x1 = self.body[0][0]
        co_y1 = self.body[0][1]
        self.body.insert(0, [co_x1, co_y1-1])
        self.body_length = len(self.body)
        del self.body[self.body_length-1]
        self.press_key = 0
    def move_down(self, evt):
        co_x1 = self.body[0][0]
        co_y1 = self.body[0][1]
        self.body.insert(0, [co_x1, co_y1+1])
        self.body_length = len(self.body)
        del self.body[self.body_length-1]
        self.press_key = 0
    def eat(self):
        if self.body[0] == self.fruit.pos:
            return True
        else:
            return False
    def out_of_bound(self):
        if self.body[0][0] > 50 or self.body[0][0] < 0 or self.body[0][1] > 50 or self.body[0][1] < 0:
            return True
        else:
            return False
    def draw(self):
        co_x1 = self.body[0][0]
        co_y1 = self.body[0][1]
        if self.press_key == 1 and self.begin != 0:
            if self.body[0][0] - self.body[1][0] == 1:
                self.body.insert(0, [co_x1+1, co_y1])
            elif self.body[0][0] - self.body[1][0] == -1:
                self.body.insert(0, [co_x1-1, co_y1])
            elif self.body[0][1] - self.body[1][1] == -1:
                self.body.insert(0, [co_x1, co_y1-1])
            elif self.body[0][1] - self.body[1][1] == 1:
                self.body.insert(0, [co_x1, co_y1+1])
        if self.eat() == False:
            self.body_length = len(self.body)
            del self.body[self.body_length-1]
        self.body_length = len(self.body)
        self.press_key = 1
        self.begin = 1
        for x in range(0, self.body_length):
            for y in range(x+1, self.body_length):
                if self.body[x] == self.body[y]:
                    self.suicide = True
            co_x = self.body[x][0]
            co_y = self.body[x][1]
            can_x1 = (co_x - 1) * 10
            can_y1 = (co_y - 1) * 10
            can_x2 = co_x * 10
            can_y2 = co_y * 10
            self.press_key = 1
            draw_list[x] = self.canvas.create_rectangle(can_x1, can_y1, can_x2, can_y2, fill="blue", outline="white")        
        
class Fruit:
    def __init__(self, canvas):
        self.canvas = canvas
        self.fruit_id = canvas.create_oval(0, 0, 10, 10, fill="red")
        self.canvas.move(self.fruit_id, 250, 250)
        self.pos = [26, 26]
    def draw(self, co_x, co_y):
        pos = [co_x, co_y]
        can_x1 = (co_x - 1) * 10
        can_y1 = (co_y - 1) * 10
        can_x2 = co_x * 10
        can_y2 = co_y * 10
        self.canvas.create_oval(can_x1, can_y1, can_x2, can_y2, fill="red")

tk = Tk()
tk.title("Snake")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

fruit = Fruit(canvas)
snake = Snake(canvas, fruit)

while 1:
    if snake.suicide == False and snake.out_of_bound() == False:
        canvas.delete("all")
        if snake.eat() == True:
            while True:
                co_x = random.randint(1, 50)
                co_y = random.randint(1, 50)
                for x in range(0, len(snake.body)-1):
                    if [co_x, co_y] != snake.body[x]:
                        continue
                        overlap = True
                    else:
                        overlap = False
                        break
                if overlap == True:
                    continue
                else:
                    break
            fruit.draw(co_x, co_y)
        else:
            fruit.draw(3, 3)
    snake.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.1)
