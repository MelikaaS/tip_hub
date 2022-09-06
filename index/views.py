from django.shortcuts import render
from django.views.generic import ListView


# class IndexListView(ListView):

def index(request):
    return render(request,'index/index.html')

