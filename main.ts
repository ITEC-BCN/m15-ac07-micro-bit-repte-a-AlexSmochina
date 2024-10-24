input.onGesture(Gesture.Shake, function () {
    parar = randint(0, 3)
    if (parar == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (parar == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
})
let parar = 0
basic.showIcon(IconNames.SmallSquare)
basic.pause(1000)
basic.showIcon(IconNames.Square)
basic.pause(1000)
basic.showIcon(IconNames.Scissors)
basic.pause(1000)
