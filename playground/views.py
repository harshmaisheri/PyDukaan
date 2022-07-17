# from django.core.mail import EmailMessage, send_mail, mail_admins, BadHeaderError
from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
import requests
# from .task import notify_customers


class HelloView(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        return render(request, 'hello.html', {'name': 'Hershy'})


# @cache_page(5 * 60)
# def say_hello(request):

#     # notify_customers.delay('Send Emails')
#     # try:
#     # send_mail('Testing My 1st Email', 'Hello Whatsup!!',
#     #           'support@hersheys.in', ['info@hersheys.in'])
#     # mail_admins('Admin People WhatsUp?', 'message')
#     # message = EmailMessage(
#     #     'Coco Pudina', 'Pudina on Sale!!', 'support@hersheys.in', ['info@hersheys.in'])
#     # message.attach_file('playground/static/images/london.jpg')
#     # message.send()
#     # except BadHeaderError:
#     #     pass
#     return render(request, 'hello.html', {'name': 'Hershy'})
