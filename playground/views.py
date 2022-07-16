from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        # send_mail('Testing My 1st Email', 'Hello Whatsup!!',
        #           'support@hersheys.in', ['info@hersheys.in'])
        mail_admins('Admin People WhatsUp?', 'message')
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Hershy'})
