from .models import Message
from django.shortcuts import render, redirect
import datetime

def index(request):
    latest_msgs_list = Message.objects.order_by('-pub_date')[:6]    
    context = {
        'latest_msgs_list': latest_msgs_list,
    }
    return render(request, 'msgs/index.html', context)

def new(request):
    if request.method == "POST":
        msg_text = request.POST.get('msg_text', '')
        if request.META.get('REMOTE_ADDR'):
            ip = request.META.get('REMOTE_ADDR')
        else:
            ip = request.META.get('HTTP_X_FORWARDED_FOR')
        date = datetime.datetime.now()
        message = Message(msg_text=msg_text,client_ip=ip,pub_date=date)
        message.save()
        return redirect( '/messages/')
    else:
        return render(request, 'msgs/new.html')
    
