from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(requset):
    return render(requset, 'blog/index.html')

def specific(requset):
    return HttpResponse("list1")

def getResponse(requset):
    userMessage = requset.GET.get('userMessage')
    return HttpResponse(userMessage)