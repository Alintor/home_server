import serial


def led_on(isOn):
    command = b'0'
    if isOn is "1":
        command = b'1'
    if isOn is "2":
        command = b'2'
    port = "/dev/cu.usbmodem1411"
    ser = serial.Serial(port)
    ser.baudrate = 9600
    ser.write(command)
    line = ser.readline()
    # print(line.decode("utf-8"))
    ser.close()
    if line.decode("utf-8") == "1\r\n":
        return True
    else:
        return False

def status():
    port = "/dev/cu.usbmodem1411"
    ser = serial.Serial(port)
    ser.baudrate = 9600
    line = ser.readline()
    ser.close()
    if line.decode("utf-8") == "HIGH\r\n":
        return True
    else:
        return False


