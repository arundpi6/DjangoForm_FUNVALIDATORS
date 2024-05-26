from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            Topic_Name=TFDO.cleaned_data['Topic_Name']

            TO=Topic.objects.get_or_create(Topic_Name=Topic_Name)[0]
            TO.save()
            return HttpResponse('DATA INSERTED SUCCEESFULLY IN TOPIC TABLE')
        else:
            return HttpResponse('INVAlID DATA')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            TO=WFDO.cleaned_data['Topic_Name']
            Name=WFDO.cleaned_data['Name']
            URL=WFDO.cleaned_data['URL']
            Email=WFDO.cleaned_data['Email']

            WO=Webpage.objects.get_or_create(Topic_Name=TO,Name=Name,URL=URL,Email=Email)[0]
            WO.save()
            return HttpResponse('DATA INSERTED SUCCEESFULLY IN WEBPAGE TABLE')
        else:
            return HttpResponse('INVAlID DATA')
    return render(request,'insert_webpage.html',d)