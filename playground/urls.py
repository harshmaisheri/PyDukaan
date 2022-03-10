from django.urls import URLPattern, path
from . import views

# URLconf
urlpatterns = [
    path('hello/', views.say_hello)
]
