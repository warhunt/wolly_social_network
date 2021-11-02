from django.shortcuts import render, redirect
from main.models import Message
from django.conf import settings 

def login(request):
    if request.user.is_authenticated:
        return redirect('main')
    number_message = [len(Message.objects.filter(body=button)) for button in settings.CONST.get('buttons')]
    return render(request, 'login.html', {'buttons': settings.CONST.get('buttons'), 'len': number_message})
