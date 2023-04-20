from celery import shared_task
from twilio.rest import Client
from django.conf import settings
from sms import send_sms


@shared_task
def send_sms_phone(to, body):
    # Your Twilio account sid and auth token

    account_sid = 'AC54e90d0d7f3d02aa090d90b713d202ba'
    auth_token = '8c0de5de207b70acaad968b650a71b98'
    from_number = '+16204009557'


    # Create a Twilio client
    client = Client(account_sid, auth_token)
    # print(client.account_sid,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

    # Send the SMS
    message = client.messages.create(
        from_=from_number,
        body=body,
        to=to
    )
    return message.sid
    
    
# send_sms_phone('89909090821', 'uhieuweherhhhhhhhhhhhhhhh')


# @shared_task
# def send_sms():
#     send_sms(
#         'Here is the message',
#         '+12065550100',
#         ['+441134960000'],
#         fail_silently=False
#     )

