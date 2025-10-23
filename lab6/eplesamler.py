from uib_inf100_graphics.event_app import run_app
from smiley import draw_smiley_in_box
import random

def app_started(app):
    app.timer_delay = 1000//60  # 60 bilder i sekundet
    app.player = {
        'x': app.width / 2,
        'y': app.height - 50, # Litt over bunnen av skjermen
        'radius': 30, # En passelig verdi
    }
    app.apples = [
        {'x': app.width / 2, 'y': 0, 'radius': 20},
        {'x': app.width / 3, 'y': 0, 'radius': 20},
    ]
    app.pressed_keys = []
    app.score = 0
    app.game_state = 'active'
    app.apples_created = 2
    app.max_apples_to_create = 50

def key_pressed(app, event):
    app.pressed_keys.append(event.key)

def key_released(app, event):
    while event.key in app.pressed_keys:
        app.pressed_keys.remove(event.key)

def timer_fired(app):
    move_player(app)
    move_apples(app)
    catch_apples(app)
    create_apples(app)
    check_game_over(app)

def move_player(app):
    # Flytt spilleren
    if 'Left' in app.pressed_keys:
        app.player['x'] -= 10
    if 'Right' in app.pressed_keys:
        app.player['x'] += 10

def move_apples(app):
    # Flytt eplene
    for apple in app.apples:
        apple['y'] += 5

def catch_apples(app):
    # Spise eplene
    apples_to_keep = []
    for apple in app.apples:
        if circles_overlap(apple, app.player):
            app.score += 1
        else:
            apples_to_keep.append(apple)
    app.apples = apples_to_keep

def create_apples(app):
    # Opprette nye epler
    dice_throw = random.random()
    threshold = 0.1   # 10%
    if dice_throw < threshold and \
          app.apples_created < app.max_apples_to_create:
        new_apple = {
            'x': random.randrange(app.width),
            'y': 0,
            'radius': random.randrange(20, 50)
        }
        app.apples.append(new_apple)
        app.apples_created += 1

def remove_apples_below_screen(app):
    # Fjerne epler som er utenfor skjermen
    apples_to_keep = []
    for apple in app.apples:
        if is_within_window(app, apple):
            apples_to_keep.append(apple)
    app.apples = apples_to_keep

def check_game_over(app):
    # Sjekk game-over
    if app.apples_created >= app.max_apples_to_create \
        and len(app.apples) == 0:
        app.game_state = 'game_over'

def is_within_window(app, apple):
    return apple['y'] - apple['radius'] <= app.height

def circles_overlap(c1, c2):
    distance = ((c1['x'] - c2['x'])**2 + (c1['y']-c2['y'])**2)**0.5
    return distance < c1['radius'] + c2['radius']

def redraw_all(app, canvas):
    # Tegn spilleren
    x_left = app.player['x'] - app.player['radius']
    y_top = app.player['y'] - app.player['radius']
    x_right = app.player['x'] + app.player['radius']
    y_bot = app.player['y'] + app.player['radius']
    draw_smiley_in_box(canvas, x_left, y_top, x_right, y_bot)

    # Tegn eplet
    for apple in app.apples:
        x_left = apple['x'] - apple['radius']
        y_top = apple['y'] - apple['radius']
        x_right = apple['x'] + apple['radius']
        y_bot = apple['y'] + apple['radius']
        canvas.create_oval(
            x_left, y_top,
            x_right, y_bot,
            fill='red'
        )

    # Tegn score
    canvas.create_text(app.width/2, 20,
                       text=app.score,
                       font='Arial 20')
    
    if app.game_state == 'game_over':
        canvas.create_text(
            app.width/2, app.height/2,
            text=f'Game over\nYou scored {app.score} points'
        )


if __name__ == '__main__':
    run_app(width=800, height=600, title="Eplesamleren")