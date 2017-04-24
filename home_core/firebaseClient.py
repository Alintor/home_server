import pyrebase
import requests

config = {
    "apiKey": "AIzaSyD7PWXcvB_Fb9If-hwBBxxuo1gPbAjDITo",
    "authDomain": "projectId.firebaseapp.com",
    "databaseURL": "https://homecloudserver-b881d.firebaseio.com",
    "storageBucket": "homecloudserver-b881d.appspot.com"
}

controller_url = "http://192.168.1.210:80/"

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = None

user = None
local_id = None

db = firebase.database()
# Log the user in
email = "Alintorius@gmail.com"
password = "djrbybxdj"

observable = {
    'command': "",
    'param': 0,
    'value': 0

}




def configure():
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(email, password)
    local_id = user['localId']

    rooms = roomsData()
    db.child("users").child(local_id).child("observable").set(observable, user['idToken'])
    db.child("users").child(local_id).child("rooms").set(rooms, user['idToken'])
    my_stream = db.child("users").child(local_id).child("observable").stream(stream_handler, user['idToken'])


def roomsData():
    rooms = [
        {
            "id": 0,
            "name": "Кухня",
            "image": "room_kitchen"
        }
    ]

    return rooms


def sensorsData():
    response = requests.get(controller_url + "getall")
    data = response.json()
    sensors = data['sensors']
    return sensors


def stream_handler(message):
    print(message["event"])  # put
    print(message["path"])  # /-K7yGTTEp7O549EzTYtI
    print(message["data"])  # {'title': 'Pyrebase', "body": "etc..."}
    data = message["data"]
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(email, password)
    if data["command"] == "roomDetails":
        param = data["param"]
        sensors = sensorsData()
        auth = firebase.auth()
        user = auth.sign_in_with_email_and_password(email, password)
        local_id = user['localId']
        db.child("users").child(local_id).child("observable").set(observable, user['idToken'])
        db.child("users").child(local_id).child("rooms").child(param).child("sensors").set(sensors, user['idToken'])

    if data["command"] == "setSensor":
        param = data["param"]
        value = data["value"]
        local_id = user['localId']
        requests.post(controller_url + "setlight", data={'value': value})
        db.child("users").child(local_id).child("observable").set(observable, user['idToken'])

