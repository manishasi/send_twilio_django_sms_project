from django.urls import path
from .views import *

urlpatterns = [
    path('', send_sms_view , name="send_sms_view"),
    path("sms/",sms_view),
    path("sms1/",sms_view1)
]