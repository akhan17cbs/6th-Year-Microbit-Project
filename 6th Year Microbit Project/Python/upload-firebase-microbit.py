def on_received_number(receivedNumber):
    basic.show_number(receivedNumber)
    serial.redirect_to_usb()
    serial.write_number(receivedNumber)
    serial.write_line("")
radio.on_received_number(on_received_number)

IncomingData = ""
radio.set_group(1)

def on_forever():
    global IncomingData
    IncomingData = serial.read_until(serial.delimiters(Delimiters.NEW_LINE))
    radio.send_string(IncomingData)
    basic.pause(5000)
basic.forever(on_forever)
