import serial
import json

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

def getSensors():
    command = {'command': 'getall'}
    port = "/dev/cu.usbmodem1411"
    ser = serial.Serial(port)
    ser.baudrate = 9600
    ser.write(str.encode(str(command)))
    line = ser.readline()
    ser.close()
    data = json.loads(line.decode("utf-8"))
    return data['sensors']

def setLight(val):
    command = {'command': 'setlight'}
    command['value'] = val
    port = "/dev/cu.usbmodem1411"
    ser = serial.Serial(port)
    ser.baudrate = 9600
    ser.write(str.encode(str(command)))
    ser.close()


def sensorsData():
    sensors = [
     	{
    		"id": 0,
        	"name": "Светодиод",
        	"type": "light",
        	"value": 0
    	},
    	{
        	"id": 1,
        	"name": "Освещенность",
        	"type": "illumination",
        	"value": 32
    	},
    	{
        	"id": 2,
        	"name": "Температура",
        	"type": "temperature",
        	"value": 24
     	},
    	{
        	"id": 3,
        	"name": "Влажность воздуха",
        	"type": "humidity",
        	"value": 16
    	},
    	{
        	"id": 4,
        	"name": "Датчик протечки",
        	"type": "water",
        	"value": 39
    	}
    ]
    return sensors


def roomsData():
	rooms =  [
    	{
      		"id": 0,
      		"name": "Кухня",
      		"image": "room_kitchen"
    	}
  	]

	return rooms