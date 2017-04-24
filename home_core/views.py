from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from home_core import serialConnection
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import requests

controller_url = "http://192.168.1.210:80/"
# Create your views here.

def manage_led(request, is_on):
    message = serialConnection.led_on(is_on)

    return JsonResponse({'status': message}, status=200)

def get_list(request):

    data = base_response(True, None, {'status': False, 'message': 'errorrrrr'})

    return JsonResponse(data, status=200)

def base_response(succsess, message, data):
    response_data = {'succsess': succsess}
    if message is not None:
        response_data['message'] = message
    if data is not None:
        response_data['data'] = data
    return response_data


def led_status(request):
    status_res = serialConnection.status()

    return JsonResponse({'status': status_res}, status=200)


def get_rooms(request):
    room = {'id': 1, 'name': 'Кухня', 'image': 'room_kitchen'}
    rooms = [room]
    data = {'rooms': rooms}
    return JsonResponse(data, status=200)


def room_detail(request, room_id):
    # sensors = serialConnection.getSensors()
    # data = urllib.request.Request(controller_url + "getall").getResponse()
    response = requests.get(controller_url + "getall")
    data = response.json()
    sensors = data['sensors']
    room = {'id': 1, 'name': 'Кухня', 'image': 'room_kitchen', 'sensors': sensors}
    data = {'room': room}
    return JsonResponse(data, status=200)

@csrf_exempt
def set_sensor(request):
    val = request.POST['value']
    # serialConnection.setLight(val)
    requests.post(controller_url + "setlight", data = {'value': val})
    return JsonResponse({'status': 'true'}, status=200)

