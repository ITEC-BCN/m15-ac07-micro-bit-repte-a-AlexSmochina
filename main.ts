input.onButtonPressed(Button.A, function () {
    forma += 1
    if (forma == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (forma == 2) {
        basic.showIcon(IconNames.Square)
    } else if (forma == 3) {
        basic.showIcon(IconNames.Scissors)
    } else {
        forma = 0
    }
})
input.onGesture(Gesture.Shake, function () {
    parar = randint(1, 3)
    if (parar == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (parar == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
})
input.onButtonPressed(Button.B, function () {
    forma_bot = randint(1, 3)
    if (forma_bot == 1 && forma == 1) {
        basic.showString("EMPATE")
    } else if (forma_bot == 2 && forma == 2) {
        basic.showString("EMPATE")
    } else if (forma_bot == 3 && forma == 3) {
        basic.showString("EMPATE")
    } else if (forma_bot == 1 && forma == 3) {
        basic.showString("HAS PERDIDIO")
    } else if (forma_bot == 2 && forma == 1) {
        basic.showString("HAS PERDIDIO")
    } else if (forma_bot == 3 && forma == 2) {
        basic.showString("HAS PERDIDIO")
    } else {
        basic.showString("HAS GANADO")
    }
})
let forma_bot = 0
let parar = 0
let forma = 0
basic.showString("JUEGO")
basic.showIcon(IconNames.SmallSquare)
basic.showIcon(IconNames.Square)
basic.showIcon(IconNames.Scissors)
