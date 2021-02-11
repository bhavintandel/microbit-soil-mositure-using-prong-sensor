moisture_threshold = 0
moisture = 0

def on_button_pressed_a():
    global moisture_threshold
    moisture_threshold = moisture_threshold + 50
    basic.show_number(moisture_threshold)
    basic.pause(2000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global moisture_threshold
    moisture_threshold = moisture_threshold - 50
    basic.show_number(moisture_threshold)
    basic.pause(2000)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global moisture
    moisture = pins.analog_read_pin(AnalogPin.P1)
    basic.show_number(moisture)
    basic.pause(5000)
    if moisture < moisture_threshold:
        basic.show_icon(IconNames.SAD)
    else:
        basic.show_icon(IconNames.HAPPY)
    basic.pause(5000)
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
