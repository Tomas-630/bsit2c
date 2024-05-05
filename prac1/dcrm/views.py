from django.shortcuts import render

# Create your views here.

def home(request):
    #dosomething
    return render(request, 'home.html')