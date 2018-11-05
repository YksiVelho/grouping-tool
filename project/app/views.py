from django.http import HttpResponse
from django.shortcuts import render

def mainPage(request):
    return HttpResponse("Hello, world. You're at the app main page.")

def teacherView(request):
    context = {}
    return render(request, 'pages/teacherView.html',context)
