from django.urls import path

from . import views


#urls confs model
urlpattern =[
    path('hello/',views.say_hello)

]