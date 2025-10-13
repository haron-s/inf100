from sys import exit

def point_in_rectangle(x1, y1, x2, y2, x, y):
    return (min(x1, x2) <= x <= max(x1, x2)
        and min(y1, y2) <= y <= max(y1, y2))

def execute_button_action_if_clicked(app, button, mouse_x, mouse_y):
    x1, y1, x2, y2, label, func = button
    if point_in_rectangle(x1, y1, x2, y2, mouse_x, mouse_y):
        try:
            func(app)
        except TypeError:
            func()

def draw_button(canvas, button):
    x1, y1, x2, y2, label, func = button
    canvas.create_rectangle(x1, y1, x2, y2, fill="beige")
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    canvas.create_text(mid_x, mid_y, text=label)

def difficulty(app, difficulty_setting):
    app.difficulty_setting = difficulty_setting
    if difficulty_setting == "hard": app.timer_delay = 100
    if difficulty_setting == "normal": app.timer_delay = 200
    if difficulty_setting == "easy": app.timer_delay = 300

def start_game(app):
    app.state = "active"

def quit_game(app):
    exit()
