from snake_view import draw_board
from game_logic import move_snake
from button import draw_button, start_game, quit_game, execute_button_action_if_clicked, difficulty
from score import load_scores, delete_scores

def app_started(app):
    app.direction = "east"
    app.info_mode = False
    app.state = "menu"
    app.timer_delay = 200 # milliseconds
    app.score = 0
    app.scores = load_scores()
    app.difficulty_setting = "normal"

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
    app.buttons = {
    "menu" : [[app.width/2-100, app.height/2-80, app.width/2+100, app.height/2-30, "Start Game", start_game],
        [app.width/2-100, app.height/2+30, app.width/2+100, app.height/2+80, "Quit Game", quit_game],
        [50, app.height/2-30, 100, app.height/2-70, "Hard",  lambda app: difficulty(app, "hard")],
        [50, app.height/2+20, 100, app.height/2-20, "Normal", lambda app: difficulty(app, "normal")],
        [50, app.height/2+70, 100, app.height/2+30, "Easy", lambda app: difficulty(app, "easy")],
        [app.width-50, app.height-100, app.width-150, app.height-50, "Delete Savedata", delete_scores]],
    "pause" : [[app.width/2-100, app.height/2-80, app.width/2+100, app.height/2-30, "Resume Game", start_game],
        [app.width/2-100, app.height/2+30, app.width/2+100, app.height/2+80, "Back to Main Menu", app_started]],
    "gameover" : [[app.width/2-100, app.height/2-80, app.width/2+100, app.height/2-30, "Back to Main Menu", app_started],
        [app.width/2-100, app.height/2+30, app.width/2+100, app.height/2+80, "Quit Game", quit_game]],
    }

def timer_fired(app):
    if not app.info_mode and app.state == "active":
        move_snake(app)

def key_pressed(app, event):
    if event.key == "i":
        if app.info_mode:
            app.info_mode = False
        else:
            app.info_mode = True

    if event.key == "p":
        if app.state == "active":
            app.state = "pause"

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
        if event.key == "p":
            app.state = "pause"

    

def mouse_pressed(app, event):
    if app.state == "menu":
        for button in app.buttons["menu"]:
            execute_button_action_if_clicked(app, button, event.x, event.y)
    if app.state == "pause":
        for button in app.buttons["pause"]:
            execute_button_action_if_clicked(app, button, event.x, event.y)
    if app.state == "gameover":
        for button in app.buttons["gameover"]:
            execute_button_action_if_clicked(app, button, event.x, event.y)

#visning

def redraw_all(app, canvas):
    if app.info_mode:
        canvas.create_text(app.width/2, 10, text = f"{app.head_pos=} {app.snake_size=} {app.direction=} {app.state=}", anchor="n")
    else:
        canvas.create_text(10, 10, text = f"Difficulty: {app.difficulty_setting}", anchor="w")
        canvas.create_text(app.width/2, app.height-10, text = f"Press P to pause game")
        canvas.create_text(app.width/2, 10, text = f"Score: {app.score}")
        if app.scores:
            canvas.create_text(app.width-10, 10, text = f"Previous Score: {app.scores[-1]} High Score: {max(app.scores)}", anchor="e")
        else:
            canvas.create_text(app.width-10, 10, text = f"Play to save scores", anchor="e")

    margin = 25
    draw_board(canvas, margin, margin,app.width-margin, app.height-margin, app.board, app.info_mode)
    
    if app.state == "menu":
        for button in app.buttons["menu"]:
            draw_button(canvas, button)
    elif app.state == "pause":
        for button in app.buttons["pause"]:
            draw_button(canvas, button)
    elif app.state == "gameover":
        for button in app.buttons["gameover"]:
            draw_button(canvas, button)
    
if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app
    run_app(width=800, height=600, title='Snake')
