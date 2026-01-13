from django.shortcuts import render
from views import Serie

# Create your views here.

def get_series(request) :
    series = Serie.objects.all()
    return render(request,'serie.html',{'series': series})