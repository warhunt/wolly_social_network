from django.shortcuts import render
from main.models import Message
from django.conf import settings 

def login(request):
    number_message = [len(Message.objects.filter(body=button)) for button in settings.CONST.get('buttons')]
    return render(request, 'login.html', {'buttons': settings.CONST.get('buttons'), 'len': number_message})
