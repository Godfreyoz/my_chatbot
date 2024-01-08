from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('chatbot', read_only=False,
              logic_adapters=[
                  {
                
                      'import_path':'chatterbot.logic.BestMatch',
                      'default_response':'Sorry, out of my reach',
                      'maximun_similarity_threshold': 100
                     
                      }
                      ])

list_to_train = [

     "hi",
     "hi, there",
     "what's your name?",
     "I'm just a chatbot",
     "what is your fav food?",
     "I like yam and egg",
     "how are you doing today?",
     "I'm doing great Thanks",
     "what's your fav sport?",
     "football",
     "do you have children?",
     "no",
]


#chatterbotCorpusTainer = ChatterBotCorpusTrainer(bot)



list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)
#chatterbotCorpusTainer.train('chatterbot.corpus.english')



def index(requset):
    return render(requset, 'blog/index.html')

def specific(requset):
    return HttpResponse("list1")


def getResponse(requset):
    userMessage = requset.GET.get('userMessage')
    chatResponse = str (bot.get_response(userMessage))
    return HttpResponse(chatResponse)
