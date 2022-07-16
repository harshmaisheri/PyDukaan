# from django.core.mail import EmailMessage, send_mail, mail_admins, BadHeaderError
from django.shortcuts import render

from .task import notify_customers


def say_hello(request):
    notify_customers.delay('Send Emails')
    # try:
    # send_mail('Testing My 1st Email', 'Hello Whatsup!!',
    #           'support@hersheys.in', ['info@hersheys.in'])
    # mail_admins('Admin People WhatsUp?', 'message')
    # message = EmailMessage(
    #     'Coco Pudina', 'Pudina on Sale!!', 'support@hersheys.in', ['info@hersheys.in'])
    # message.attach_file('playground/static/images/london.jpg')
    # message.send()
    # except BadHeaderError:
    #     pass
    return render(request, 'hello.html', {'name': 'Hershy'})
