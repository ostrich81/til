from django.shortcuts import render
import random
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, 'index.html')
def introduce(request):
    return render(request, 'introduce.html')
def greeting(request):
    foods=['apple','banana','coconut']
    info ={
        'name' : 'paul'
    }
    context={
        'info':info,
        'foods':foods,
    }
    return render(request, 'greeting.html',context)
def dinner(request):
    foods=['jok','jha','get','fwetwetw']
    pick=random.choice(foods)
    no=''
    context={
        'pick':pick,
        'foods':foods,
        'no':no,
    }
    return render(request,'dinner.html',context)
def image(request):

    return render(request,'image.html')

def template_language(request):
    menus=['짬뽕','계란볶음밥','스시','탕볶밥']
    my_sentense='Do you want to live, Do you really'
    messages=['sussper','dupsedr','diva','siva']
    datetimenow= datetime.now()
    empty_list=[]

    context={
        'menus':menus,
        'my_sentence':my_sentense,
        'messages':messages,
        'datetimenow':datetimenow,
        'empty_list':empty_list,
    }
    return render(request,'template_language.html',context)

def throw(request):

    return render(request,'throw.html')

def catch(request):
    print(request.GET)
    message= request.GET.get('message')
    context={
        'message':message
    }
    return render(request,'catch.html',context)

def hello(request, name):
    context = {
        "name": name,
    }

    return render(request,'hello.html',context)