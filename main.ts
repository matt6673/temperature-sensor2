input.onButtonPressed(Button.A, function () {
    Target_Temperature += 1
    basic.showString("T")
    basic.showNumber(Target_Temperature)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(input.temperature())
    basic.clearScreen()
})
input.onGesture(Gesture.Shake, function () {
    control.reset()
})
let Heating = false
let Air_Conditioning = false
let Target_Temperature = 0
Target_Temperature = 0
serial.redirect(
SerialPin.USB_TX,
SerialPin.USB_RX,
BaudRate.BaudRate115200
)
serial.redirectToUSB()
basic.forever(function () {
    if (input.temperature() > Target_Temperature) {
        Air_Conditioning = true
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            `)
    } else if (input.temperature() < Target_Temperature) {
        Heating = true
        basic.showLeds(`
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            `)
    } else {
        basic.showLeds(`
            . . . . .
            # # # # #
            . . . . .
            # # # # #
            . . . . .
            `)
    }
    serial.writeNumber(input.temperature())
    serial.writeLine("")
    basic.pause(5000)
})
