from smiley import draw_smiley

def main():
    from uib_inf100_graphics.simple import canvas, display
    draw_smiley_grid(canvas, 70, 5)
    display(canvas)

def draw_smiley_line(canvas,y,size, n):
    left = 0
    for i in range(n):
        draw_smiley(canvas, left, y, size)
        left += size

def draw_smiley_grid(canvas, size, n):
    y=0
    for i in range(n):
        draw_smiley_line(canvas, y,size,n)
        y += size

main()
