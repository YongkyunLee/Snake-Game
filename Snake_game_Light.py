from tkinter import *
import random
import time

sqr_unit = 10
canvas_height = 500
canvas_width = 500
canvas_cord_max = canvas_height / sqr_unit
canvas_cord_min = 1
canvas_color = "white"
fruit_color = "red"
snake_body_color = "blue"
snake_outline_color = "white"
snake_init = [[6, 2], [5, 2], [4, 2], [3, 2]]
score_zero = len(snake_init)
snake_init_tail = snake_init[len(snake_init)-1]
fruit_init_cord = [20, 30]

class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.body = snake_init
        self.tail = self.body[len(self.body)-1]
        for i in range(0, len(self.body)):
            co_x = self.body[i][0]
            co_y = self.body[i][1]
            canvas_x1 = (co_x - 1) * sqr_unit
            canvas_y1 = (co_y - 1) * sqr_unit
            canvas_x2 = co_x * sqr_unit
            canvas_y2 = co_y * sqr_unit
            self.canvas.create_rectangle(canvas_x1, canvas_y1, canvas_x2, canvas_y2, fill=snake_body_color, outline=snake_outline_color)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Up>', self.turn_up)
        self.canvas.bind_all('<KeyPress-Down>', self.turn_down)
        self.dir = [1, 0]
        self.move_count = 0
    def turn_right(self, evt):
        self.dir = [1, 0]
        self.move_count += 1
    def turn_left(self, evt):
        self.dir = [-1, 0]
        self.move_count += 1
    def turn_up(self, evt):
        self.dir = [0, -1]
        self.move_count += 1
    def turn_down(self, evt):
        self.dir = [0, 1]
        self.move_count += 1
    def move(self):
        self.body.insert(0, [self.body[0][0]+self.dir[0], self.body[0][1]+self.dir[1]])
        del self.body[len(self.body)-1]
    def grow(self, tail_cord):
        self.body.insert(len(self.body), tail_cord)
    def suicide(self):
        for i in range(1, len(self.body)):
            if self.body[0] == self.body[i]:
                return True
        return False    
    def draw(self):
        head_x = self.body[0][0]
        head_y = self.body[0][1]
        canvas_x1 = (head_x - 1) * sqr_unit
        canvas_y1 = (head_y - 1) * sqr_unit
        canvas_x2 = head_x * sqr_unit
        canvas_y2 = head_y * sqr_unit
        self.canvas.create_rectangle(canvas_x1, canvas_y1, canvas_x2, canvas_y2, fill=snake_body_color, outline=snake_outline_color)
    def undraw(self):
        tail_x = self.body[len(self.body)-1][0]
        tail_y = self.body[len(self.body)-1][1]
        self.tail = [tail_x, tail_y]
        canvas_x1 = (tail_x - 1) * sqr_unit
        canvas_y1 = (tail_y - 1) * sqr_unit
        canvas_x2 = tail_x * sqr_unit
        canvas_y2 = tail_y * sqr_unit
        if self.move_count == 1:
            self.canvas.create_rectangle((snake_init_tail[0]-1)*sqr_unit, (snake_init_tail[1]-1)*sqr_unit,\
                                         snake_init_tail[0]*sqr_unit, snake_init_tail[1]*sqr_unit,\
                                         fill=canvas_color, outline=canvas_color)
        if self.move_count != 0:
            self.canvas.create_rectangle(canvas_x1, canvas_y1, canvas_x2, canvas_y2, fill=canvas_color, outline=canvas_color)  
                
class Fruit:
    def __init__(self, canvas):
        self.canvas = canvas
        self.fruit_id = canvas.create_oval(0, 0, sqr_unit, sqr_unit, fill=fruit_color)
        self.canvas.move(self.fruit_id, (fruit_init_cord[0]-1)*10, (fruit_init_cord[1]-1)*10)
        self.pos = fruit_init_cord
    def draw(self, fruit_cord):
        self.pos = fruit_cord
        co_x = self.pos[0]
        co_y = self.pos[1]
        canvas_x1 = (co_x - 1) * sqr_unit
        canvas_y1 = (co_y - 1) * sqr_unit
        canvas_x2 = co_x * sqr_unit
        canvas_y2 = co_y * sqr_unit
        self.canvas.create_oval(canvas_x1, canvas_y1, canvas_x2, canvas_y2, fill=fruit_color)

class Ground:
    def __init__(self, canvas, snake, fruit):
        self.canvas = canvas
        self.snake = snake
        self.fruit = fruit
    def eat(self):
        if self.snake.body[0] == self.fruit.pos:
            return True
        else:
            return False
    def out_of_bounds(self):
        if (self.snake.body[0][0] > canvas_cord_max) or (self.snake.body[0][0] < canvas_cord_min)\
           or (self.snake.body[0][1] > canvas_cord_max) or (self.snake.body[0][1] < canvas_cord_min):
            return True
        else:
            return False    
    def fruit_pos_test(self, fruit_cord):
        for i in range(0, len(self.snake.body)):
            if self.snake.body[i] == fruit_cord:
                return False
        return True

tk = Tk()
tk.title("Snake")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=canvas_width, height=canvas_height, bd=0, highlightthickness=0, bg=canvas_color)
canvas.pack()
tk.update()

fruit = Fruit(canvas)
snake = Snake(canvas)
ground = Ground(canvas, snake, fruit)

while 1:
    if (ground.out_of_bounds() == False) and (snake.suicide() == False):
        if snake.move_count !=0:
            snake.move()
        snake.draw()
        #print(snake.body)
        tk.update_idletasks()
        tk.update()
        time.sleep(0.05)
        if ground.eat() == True:
            snake.grow(snake.tail)
            while 1:
                rand_x = random.randint(canvas_cord_min, canvas_cord_max)
                rand_y = random.randint(canvas_cord_min, canvas_cord_max)
                fruit_cord = [rand_x, rand_y]
                if ground.fruit_pos_test(fruit_cord) == True:
                    break
            fruit.draw(fruit_cord)
        else:
            snake.undraw()
        tk.update_idletasks()
        tk.update()
    else:
        break

score = len(snake.body) - score_zero
game_over = "Your Score Is %s Points!"
canvas.create_text(250, 250, font=("Perusia", 20), text=game_over % score)
