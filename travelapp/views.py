from django.shortcuts import render
from travelapp.models import Destination

def home(request):
    destination=Destination.objects.all()
    return render(request,'index.html',{'dests':destination})

