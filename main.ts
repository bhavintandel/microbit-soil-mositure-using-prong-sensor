let moisture_threshold = 0
let moisture = 0
input.onButtonPressed(Button.A, function () {
    moisture_threshold = moisture_threshold + 50
    basic.showNumber(moisture_threshold)
})
input.onButtonPressed(Button.B, function () {
    moisture_threshold = moisture_threshold - 50
    basic.showNumber(moisture_threshold)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    moisture = pins.analogReadPin(AnalogPin.P1)
    basic.showNumber(moisture)
    if (moisture < moisture_threshold) {
        basic.showIcon(IconNames.Sad)
    } else {
        basic.showIcon(IconNames.Happy)
    }
    basic.pause(5000)
    basic.clearScreen()
})
