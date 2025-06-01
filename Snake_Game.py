from tkinter import *
import random
GAME_WIDTH=1500
GAME_HEIGHT=750
SPEED=100
SPACE_SIZE=50
BODY_PARTS=5
SNAKE_COLOR="green"
FOOD_COLOR="red"
BACKGROUND_COLOR="black"

class Snake:
    def __init__(self):
        self.body_size=BODY_PARTS
        self.coordinates=[]
        self.squares=[]
        
        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])
        
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)
          
        

class Food:
    def __init__(self):
        x=random.randint(0,(GAME_WIDTH//SPACE_SIZE)-1)*SPACE_SIZE
        y=random.randint(0,(GAME_HEIGHT//SPACE_SIZE)-1)*SPACE_SIZE
        self.coordinates=[x,y]
        
        canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag="food")

def next_turn(snake,food):
    x,y=snake.coordinates[0]
    if direction=="up":
     y-=SPACE_SIZE
    elif direction=="down":
     y+=SPACE_SIZE
    elif direction=="left":
     x-=SPACE_SIZE
    elif direction=="right":
     x+=SPACE_SIZE
    snake.coordinates.insert(0,(x,y))
    square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill="yellow")
    snake.squares.insert(0,square)
    if len(snake.squares) > 1:
        canvas.itemconfig(snake.squares[1], fill=SNAKE_COLOR)
    if x==food.coordinates[0] and y==food.coordinates[1]:
        global score,SPEED
        score+=1
        SPEED-=1
        label_score.config(text="Score:{}".format(score))
        canvas.delete("food")
        food=Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_collision(snake):
        game_over()
    else:
     window.after(SPEED,next_turn,snake,food)
    
def change_direction(new_direction):    
    global direction
    if new_direction =="left":
        if direction !="right":
            direction=new_direction
    elif new_direction=="right":
        if direction !="left":
            direction=new_direction
    elif new_direction=="up":
        if direction !="down":
            direction=new_direction
    elif new_direction=="down":
        if direction !="up":
            direction=new_direction
            
def check_collision(snake):
    x,y=snake.coordinates[0]
    if x<0 or x>=GAME_WIDTH:
        return True
    elif y<0 or y>=GAME_HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x==body_part[0] and y==body_part[1]:
            return True
    return False
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=("Orbitron",70),text="GAME OVER",fill="white",tag="gameover")

window=Tk()

score=0
direction="down"

label_score=Label(window,text="Score:{}".format(score),font=("Orbitron",40),width=window.winfo_screenwidth(),height=1,fg="white",bg="black")
label_score.pack()

canvas=Canvas(window,bg=BACKGROUND_COLOR,width=GAME_WIDTH,height=GAME_HEIGHT)
canvas.pack()

window.update()

window.bind("<Left>",lambda event:change_direction("left"))
window.bind("<Right>",lambda event:change_direction("right"))
window.bind("<Up>",lambda event:change_direction("up"))
window.bind("<Down>",lambda event:change_direction("down"))


snake=Snake()
food=Food()

next_turn(snake,food)
window.title("Snake Game")
window.config(background="black")
window.state("zoomed")
window.resizable(False,False)
window.mainloop()
