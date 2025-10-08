from uib_inf100_graphics.simple import canvas, display
import random

def draw_smiley(canvas, x, y, size, color):
    ''' Draws a smiley face with the given size, where the
    left top corner is in the x, y position. '''
    left = x
    top = y
    right = x + size
    bottom = y + size
    width = size
    height = size

    # Face
    canvas.create_oval(left, top, right, bottom, fill = color)

    # Eyes
    canvas.create_oval(
        left + 0.30 * width, top + 0.25 * height,
        left + 0.40 * width, top + 0.35 * width,
        fill='black', outline=''
    )
    canvas.create_oval(
        left + 0.60 * width, top + 0.25 * height,
        left + 0.70 * width, top + 0.35 * width,
        fill='black', outline=''
    )

    # Mouth
    canvas.create_line(
        left + 0.30 * width, top + 0.65 * height,
        left + 0.50 * width, top + 0.85 * width,
        left + 0.70 * width, top + 0.65 * height,
        smooth=True, fill='black', width=3
    )

def draw_rand_smiley():
    list_of_color = ["red","blue","cyan","yellow","purple"]

    while list_of_color:
        #color
        color = random.choice(list_of_color)
        list_of_color.remove(color)

        #coordinates
        x = random.randrange(0,300)
        y = random.randrange(0,300)

        draw_smiley(canvas,x,y,70,color)

draw_rand_smiley()
display(canvas)

