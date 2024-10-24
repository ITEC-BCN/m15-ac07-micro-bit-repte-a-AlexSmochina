def on_gesture_shake():
    global parar
    parar = randint(0, 3)
    if parar == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif parar == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

parar = 0
basic.show_icon(IconNames.SMALL_SQUARE)
basic.pause(1000)
basic.show_icon(IconNames.SQUARE)
basic.pause(1000)
basic.show_icon(IconNames.SCISSORS)
basic.pause(1000)