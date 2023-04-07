from django.shortcuts import render

# Create your views here.

from app.models import *

def displaytopic(request):

    LOT=Topic.objects.all() #LIST OF TOPIC OBJECTS
    d={'Topic':LOT}
    return render(request,'display_topic.html',d)

def displaywebpage(request):

    WOT=Webpage.objects.all()
    v={'akhif':WOT}
    return render(request,'displaywebpage.html',v)

def displayaccessrecord(request):

    AO=AccessRecord.objects.all()
    a={'junaid':AO}
    return render(request,'displayaccessrecord.html',a)


     