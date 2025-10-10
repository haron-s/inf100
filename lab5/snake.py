from snake_view import draw_board
from game_logic import move_snake

def app_started(app):
    app.direction = "east"
    app.info_mode = "true"
    app.state = "gameover"
    app.timer_delay = 200 # milliseconds

    app.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0,-1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    
    #slange
    app.snake_size = 3
    app.head_pos = (3,4)

    #GUI
    app.buttons = [
        [app.width/2-50, app.height/2-50, app.width/2+50, app.height/2+50, "Start Game", start]
        ]

def start(app):
    app.state = "active"

def timer_fired(app):
    if not app.info_mode and app.state == "active":
        move_snake(app)

def key_pressed(app, event):
    if event.key == "i":
        if app.info_mode:
            app.info_mode = False
        else:
            app.info_mode = True

    if app.state == "active":
        if event.key == "Up":
            app.direction = "north"
        elif event.key == "Down":
            app.direction = "south"
        elif event.key == "Left":
            app.direction = "west"
        elif event.key == "Right":
            app.direction = "east"

        if event.key == "Space" and app.info_mode:
            move_snake(app)

    if app.state == "gameover":
        if event.key =="r":
            app_started(app)

#visning

def redraw_all(app, canvas):
    if app.info_mode:
        canvas.create_text(app.width/2, 10, text = f"{app.head_pos=} {app.snake_size=} {app.direction=} {app.state=}", anchor="n")
    
    if app.state == "gameover":
        for button in app.buttons:
            draw_button()

    margin = 25
    draw_board(canvas, margin, margin,app.width-margin, app.height-margin, app.board, app.info_mode)
    
def draw_button(canvas, button):
    x1, y1, x2, y2, label, func = button
    canvas.create_rectangle(x1, y1, x2, y2, fill="lightgray")
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    canvas.create_text(mid_x, mid_y, text=label)
    
        
if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app
    run_app(width=800, height=600, title='Snake')
