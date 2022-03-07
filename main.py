def on_button_pressed_a():
    global Target_Temperature
    Target_Temperature += 1
    basic.show_string("T")
    basic.show_number(Target_Temperature)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(input.temperature())
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    control.reset()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Heating = False
Air_Conditioning = False
Target_Temperature = 0
Target_Temperature = 0
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE115200)
serial.redirect_to_usb()

def on_forever():
    global Air_Conditioning, Heating
    if input.temperature() > Target_Temperature:
        Air_Conditioning = True
    elif input.temperature() < Target_Temperature:
        Heating = True
    else:
        basic.show_leds("""
            . . . . .
                        # # # # #
                        . . . . .
                        # # # # #
                        . . . . .
        """)
    serial.write_number(input.temperature())
    serial.write_number(Target_Temperature)
    serial.write_string("" + str(Heating))
    serial.write_string("" + str(Air_Conditioning))
    serial.write_line("")
    basic.pause(5000)
basic.forever(on_forever)
