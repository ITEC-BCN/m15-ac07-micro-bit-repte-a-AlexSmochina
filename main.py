def on_button_pressed_a():
    global forma
    forma += 1
    if forma == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif forma == 2:
        basic.show_icon(IconNames.SQUARE)
    elif forma == 3:
        basic.show_icon(IconNames.SCISSORS)
    else:
        forma = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global parar
    parar = randint(1, 3)
    if parar == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif parar == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    global forma_bot
    forma_bot = randint(1, 3)
    if forma_bot == 1 and forma == 1:
        basic.show_string("EMPATE")
    elif forma_bot == 2 and forma == 2:
        basic.show_string("EMPATE")
    elif forma_bot == 3 and forma == 3:
        basic.show_string("EMPATE")
    elif forma_bot == 1 and forma == 3:
        basic.show_string("HAS PERDIDIO")
    elif forma_bot == 2 and forma == 1:
        basic.show_string("HAS PERDIDIO")
    elif forma_bot == 3 and forma == 2:
        basic.show_string("HAS PERDIDIO")
    else:
        basic.show_string("HAS GANADO")
input.on_button_pressed(Button.B, on_button_pressed_b)

forma_bot = 0
parar = 0
forma = 0
basic.show_string("JUEGO")
basic.show_icon(IconNames.SMALL_SQUARE)
basic.show_icon(IconNames.SQUARE)
basic.show_icon(IconNames.SCISSORS)