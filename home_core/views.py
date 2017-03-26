from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from home_core import serialConnection

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
