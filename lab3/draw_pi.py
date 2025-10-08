from uib_inf100_graphics.simple import canvas, display
import random
from math import dist

def draw_dot(canvas, x, y):
    distance = dist((x,y),(200,200))
    
    if distance < 200:
        canvas.create_oval(x-5, y-5, x+5, y+5, fill='orange')
        return 1
    else:
        canvas.create_oval(x-5, y-5, x+5, y+5, fill='grey')
        return 0

# Draw a circle in the window
canvas.create_oval(0, 0, 400, 400)

inCircle = 0
for i in range(0,1000):
    # Highlight a random point on 400x400 canvas
    x = random.random() * 400
    y = random.random() * 400

    inCircle += draw_dot(canvas, x, y)

    message = f'{inCircle}/1000 prikker traff sirkelen\nBeregnet pi: {(inCircle/1000)*4}'
    canvas.create_rectangle(100, 180, 300, 220, fill='white')
    canvas.create_text(200, 200, text=message, fill='black')

display(canvas)