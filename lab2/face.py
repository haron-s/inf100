from uib_inf100_graphics.simple import canvas, display

#head
canvas.create_oval(75, 30, 325, 380, fill="pink")

#glasses
canvas.create_oval(75+25, 170, 75+120, 210, fill='light blue')
canvas.create_oval(325-25, 170, 325-120, 210, fill='light blue')
canvas.create_line(75+120, 190, 325-120, 190, width=5)

canvas.create_line(75, 205, 75+25, 190, width=5)
canvas.create_line(325, 205, 325-25, 190, width=5)

#eyes
canvas.create_line(75+50, 190, 75+100, 190, width=4)
canvas.create_line(325-50, 190, 325-100, 190, width=4)

#mouth
canvas.create_arc(75+80, 240, 325-80, 320, start=195, extent=150, style='chord', width=3, fill="black")

#nose
canvas.create_line(200, 190, 230, 240, width=4)
canvas.create_line(230, 240, 200, 250, width=4)

#hat
canvas.create_arc(75, 30, 325, 200, start=-10, extent=200, style='chord', width=3, fill="black")
canvas.create_oval(180, 15, 220, 35, fill="red")

display(canvas)