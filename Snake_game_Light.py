from tkinter import *
import random
import time

class Snake:
    def __init__(self, canvas, fruit):
        self.canvas = canvas
        self.fruit = fruit
        self.body = [[6, 2], [5, 2], [4, 2], [3, 2], [2, 2]]
        self.tail = [2, 2]
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
        self.press_key = 1
        self.dir = [1, 0]
        self.move_list = [1, 0]
        self.begin_move = 0
        self.det = False
        self.move_count = 0
        self.test = False
    def turn_right(self, evt):
        self.dir = [1, 0]
        self.move_count = 1
    def turn_left(self, evt):
        self.dir = [-1, 0]
        self.move_count = 1
    def turn_up(self, evt):
        self.dir = [0, -1]
        self.move_count = 1
    def turn_down(self, evt):
        self.dir = [0, 1]
        self.move_count = 1
    def move(self):
        self.co_x = self.body[0][0]
        self.co_y = self.body[0][1]
        head = self.body[0]
        self.body.insert(0, [head[0]+self.dir[0], head[1]+self.dir[1]])
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
    def eat(self):
        if self.body[0] == self.fruit.pos:
            return True
        else:
            return False
    def grow(self, tail_cord): #change self.body
        self.body.insert(len(self.body), tail_cord)
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
        self.tail = [tail_x, tail_y]
        can_x1 = (tail_x - 1) * 10
        can_y1 = (tail_y - 1) * 10
        can_x2 = tail_x * 10
        can_y2 = tail_y * 10
        if self.move_count != 0:
            self.canvas.create_rectangle(can_x1, can_y1, can_x2, can_y2, fill="white", outline="white")
        if self.move_count == 1:
            self.canvas.create_rectangle(10, 10, 20, 20, fill="white", outline="white")
        self.press_key = 1
    def rand_pos(self):
        while self.test == False:
            rand_x = random.randint(1, 50)
            rand_y = random.randint(1, 50)
            for x in range(0, len(self.body)):
                if self.body[x] == [rand_x, rand_y]:
                    self.test = False
                    break
                else:
                    self.test = True
        self.test = False
        return [rand_x, rand_y]     
                
class Fruit:
    def __init__(self, canvas):
        self.canvas = canvas
        self.fruit_id = canvas.create_oval(0, 0, 10, 10, fill="red")
        self.canvas.move(self.fruit_id, 100, 100)
        self.pos = [11, 11]
    def draw(self, rand_cord):
        self.pos = rand_cord
        co_x = self.pos[0]
        co_y = self.pos[1]
        can_x1 = (co_x - 1) * 10
        can_y1 = (co_y - 1) * 10
        can_x2 = co_x * 10
        can_y2 = co_y * 10
        self.canvas.create_oval(can_x1, can_y1, can_x2, can_y2, fill="red")

tk = Tk()
tk.title("Snake")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0, bg="white")
canvas.pack()
tk.update()

fruit = Fruit(canvas)
snake = Snake(canvas, fruit)

while 1:
    if snake.out_of_bounds() == False and snake.suicide() == False:
        #print(snake.body)
        #print(snake.move_count)
        if snake.move_count !=0:
            snake.move()
        snake.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.05)
        if snake.eat() == True:
            snake.grow(snake.tail)
            fruit.draw(snake.rand_pos())
        else:
            snake.undraw()
        #print(fruit.pos)
        tk.update_idletasks()
        tk.update()
        #canvas.delete("all")
        #tk.update_idletasks()
        #tk.update()
    else:
        break

score = len(snake.body) - 5
game_over = "Your Score Is %s Points!"
canvas.create_text(250, 250, font=("Perusia", 20), text=game_over % score)
#print(snake.body)
