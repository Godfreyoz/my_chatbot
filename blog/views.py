from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('chatbot', read_only=False, logic_adapters=['chatterbot.logic.BestMatch'])

list_to_train = [

     "hi",
     "hi, there",
     "what's your name",
     "I'm just a chatbot",
     "what is your fav food",
     "I like cheese",
]



list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)



def index(requset):
    return render(requset, 'blog/index.html')

def specific(requset):
    return HttpResponse("list1")


def getResponse(requset):
    userMessage = requset.GET.get('userMessage')
    return HttpResponse(userMessage)
