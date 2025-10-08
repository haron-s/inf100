from uib_inf100_graphics.simple import canvas, display
from pig_head import draw_head
from pig_body import draw_body

draw_body(canvas, 50, 100, 350, 330)
draw_head(canvas, 300, 80, 60)

display(canvas)