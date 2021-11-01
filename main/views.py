from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
from django.template import Context, Template
from django.contrib.auth.decorators import login_required
from django.conf import settings 

from .models import Message

#@login_required
def main(request):
    message = Message.objects.first()
    return render(request, 'message/message.html', {'message': message, 'buttons': settings.CONST.get('buttons')})

#@login_required
def send_message(request):
    if request.POST:
        user = request.user
        new_message = Message.objects.create_message(request.POST.get('button_text'), user)
        new_message.save()
        return JsonResponse({
            "body": new_message.body,
            "created": Template("{{ date }}").render(Context({"date": new_message.created})),
            "author": new_message.author.username
        })
