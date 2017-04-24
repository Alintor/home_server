from django.conf.urls import url

from home_core import views

urlpatterns = [
    url(r'^get_test_list$', views.get_list, name='get_list'),
    url(r'^manage_led/(?P<is_on>[0-2])$', views.manage_led, name='manage_led'),
    url(r'^led_status$', views.led_status, name='led_status'),
    url(r'^rooms$', views.get_rooms, name='rooms'),
    url(r'^rooms/(?P<room_id>[1-9])$', views.room_detail, name='room_detail'),
    url(r'^set_sensor$', views.set_sensor, name='set_sensor'),
]