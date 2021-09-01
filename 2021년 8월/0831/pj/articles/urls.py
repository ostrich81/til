
from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index),
    path('introduce/', views.introduce),
    path('greeting/', views.greeting),
    path('dinner/',views.dinner),
    path('image/',views.image),
    path('template_language/',views.template_language),
    path('throw/',views.throw),
    path('catch/',views.catch),
    path('hello/<str:name>/',views.hello),
    #path('hello/<int:number>/',views.hello),
   
]
