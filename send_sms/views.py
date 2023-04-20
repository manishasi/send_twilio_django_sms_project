from django.shortcuts import render
# from django.http import HttpResponse
# from .task import *
from twilio.rest import Client
from .task import send_sms_phone
from sms import send_sms


# https://www.twilio.com/login: firstly create  twilio account.


def send_sms_view(request):
    if request.method == 'POST':
        # to = request.POST.get('to')
        # body = request.POST.get('body')
        to = request.POST['to']
        print(to,"----------------")
        body = request.POST['body']
        print(body,'+++++++++++++++')
        send_sms_phone.delay(to, body)  # Call the send_sms_phone function as a Celery task
        # return HttpResponse('SMS will be sent after 5 minutes.')
        return render(request, 'sent_sms.html')
    return render(request, 'sms_sent.html')


def sms_view(request):
    account_sid = 'AC54e90d0d7f3d02aa090d90b713d202ba'
    auth_token = '8c0de5de207b70acaad968b650a71b98'
    from_number = '+16204009557'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=from_number,
        body="hello",
        to='+917982102159'
    )
    print(message.sid)

def sms_view1(request):
    send_sms(
        'Here is the message',
        '+16204009557',
        ['+917982102159'],
        fail_silently=False
    )
    print(send_sms)