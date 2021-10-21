def on_received_string(receivedString):
    if receivedString == "Green":
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.digital_write_pin(DigitalPin.P0, 1)
    elif receivedString == "Yellow":
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.digital_write_pin(DigitalPin.P1, 1)
    elif receivedString == "Red":
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P2, 1)
    elif receivedString == "Room Temperature":
        if 19 <= input.temperature() and input.temperature() <= 21:
            pins.digital_write_pin(DigitalPin.P1, 0)
            pins.digital_write_pin(DigitalPin.P2, 0)
            pins.digital_write_pin(DigitalPin.P0, 1)
        elif 17 <= input.temperature() and input.temperature() < 19 or 21 < input.temperature() and input.temperature() <= 23:
            pins.digital_write_pin(DigitalPin.P0, 0)
            pins.digital_write_pin(DigitalPin.P2, 0)
            pins.digital_write_pin(DigitalPin.P1, 1)
        elif 17 > input.temperature() or 23 < input.temperature():
            pins.digital_write_pin(DigitalPin.P0, 0)
            pins.digital_write_pin(DigitalPin.P1, 0)
            pins.digital_write_pin(DigitalPin.P2, 1)
radio.on_received_string(on_received_string)

radio.set_group(1)

def on_forever():
    radio.send_number(input.temperature())
    basic.pause(5000)
basic.forever(on_forever)
