from django.urls import path

from . import views


#urls confs model
urlpatterns =[
    path('hello/',views.say_hello)
]